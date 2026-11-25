# pyright: reportPrivateUsage=false

import unittest
from unittest.mock import Mock, patch

from mxbiflow.core.context import MXBIFlow
from mxbiflow.driver.detector.detector import DetectionResult, DetectorEvent
from mxbiflow.driver.detector.fusion_continuous_detector import FusionContinuousDetector
from mxbiflow.driver.peripheral.rfid.dorset_lid665v42 import Result
from mxbiflow.gameloop.detector_bridge import DetectorBridge


class DetectorBridgeTests(unittest.TestCase):
    def test_fusion_visit_reaches_mx_eye_before_rfid(self) -> None:
        for tag_time, tag_id, leave_time in (
            (101.0, "tag-A", 120.0),  # Identity arrives within the window.
            (115.0, "tag-A", 120.0),  # Identity arrives after the timeout.
            (101.0, "unmapped", 120.0),
            (None, None, 120.0),  # No identity ever arrives.
            (None, None, 102.0),  # Leaves before the timeout.
        ):
            with self.subTest(tag_time=tag_time, tag_id=tag_id, leave_time=leave_time):
                self._check_fusion_eye_visit(tag_time, tag_id, leave_time)

    def _check_fusion_eye_visit(
        self, tag_time: float | None, tag_id: str | None, leave_time: float
    ) -> None:
        reader, beam = Mock(), Mock()
        detector = FusionContinuousDetector(reader, beam, rfid_timeout=10)
        bridge = DetectorBridge(detector, {"tag-A": "animal-A"})
        with patch.object(detector, "begin"):
            bridge.start()

        session, mxbi, sender = Mock(), Mock(), Mock()
        session.current_animal = None
        session.mxbi_config.mxbi_id = "test-rig"
        session.session_id = 1
        mxbi.screen_size.width, mxbi.screen_size.height = 1024, 600
        mxbi.eyetracker.record_on_animal = True
        context = MXBIFlow(session, mxbi)

        def poll(now: float, *, present: bool = True, tag: Result | None = None) -> None:
            beam.read.return_value = present
            reader.read.return_value = tag
            with patch("mxbiflow.driver.detector.fusion_continuous_detector.time", return_value=now):
                detector._poll_once()
            bridge.emit_pygame_event()

        with (
            patch.object(context, "_event_sender", return_value=sender),
            patch("mxbiflow.gameloop.detector_bridge.event.post",
                  side_effect=lambda event: context.eye_detector_event(event.msg)),
        ):
            poll(100.0)
            entry = sender.send.call_args.args[0]
            self.assertEqual(entry.kind, "animal_entered")
            self.assertEqual(entry.timestamp_ns, 100_000_000_000)
            self.assertIsNone(entry.rfid_id)
            self.assertIsNone(entry.animal)
            self.assertTrue(entry.control_recording)
            self.assertTrue(entry.visit_id)
            if leave_time > 111.0 and (tag_time is None or tag_time > 111.0):
                poll(111.0)
                sender.send.assert_called_once()
            if tag_time is not None:
                assert tag_id is not None
                poll(tag_time, tag=Result(tag_time - 0.1, tag_id))
                identity = sender.send.call_args.args[0]
                self.assertEqual(identity.kind, "animal_identified")
                self.assertEqual(identity.rfid_id, tag_id)
                self.assertEqual(identity.animal, "animal-A" if tag_id == "tag-A" else None)
            poll(leave_time, present=False)
            events = [call.args[0] for call in sender.send.call_args_list]
            expected = ["animal_entered"]
            if tag_time is not None:
                expected.append("animal_identified")
            self.assertEqual([event.kind for event in events], [*expected, "animal_left"])
            self.assertTrue(all(event.visit_id == entry.visit_id for event in events))
            poll(leave_time + 1)
            self.assertNotEqual(sender.send.call_args.args[0].visit_id, entry.visit_id)

    def test_subscribes_before_begin_and_maps_identification(self) -> None:
        detector = Mock()
        callbacks = {}
        detector.register_event.side_effect = lambda event, callback: callbacks.update(
            {event: callback}
        )
        detector.begin.side_effect = lambda: callbacks[DetectorEvent.ANIMAL_IDENTIFIED](
            DetectionResult(animal_id="tag-A")
        )
        bridge = DetectorBridge(detector, {"tag-A": "animal-A"})
        bridge.start()
        with patch("mxbiflow.gameloop.detector_bridge.event.post") as post:
            bridge.emit_pygame_event()
            messages = [call.args[0].msg for call in post.call_args_list]
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].kind, DetectorEvent.ANIMAL_IDENTIFIED)
        self.assertEqual(messages[0].animal, "animal-A")

    def test_unmapped_identification_does_not_switch_task(self) -> None:
        detector = Mock()
        callbacks = {}
        detector.register_event.side_effect = lambda event, callback: callbacks.update(
            {event: callback}
        )
        bridge = DetectorBridge(detector, {})
        bridge.start()
        with self.assertLogs("mxbiflow.rfid", level="WARNING"):
            callbacks[DetectorEvent.ANIMAL_IDENTIFIED](
                DetectionResult(animal_id="missing")
            )
        with patch("mxbiflow.gameloop.detector_bridge.event.post") as post:
            bridge.emit_pygame_event()
        # Keep the raw RFID for the eye event log, but no mapped identity is
        # supplied to the scheduler, so this cannot select another task.
        self.assertIsNone(post.call_args.args[0].msg.animal)
        self.assertEqual(post.call_args.args[0].msg.rfid_id, "missing")
