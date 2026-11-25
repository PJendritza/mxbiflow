"""MX Eye events carry the stage level and keep task metadata."""

import unittest
from unittest.mock import Mock, PropertyMock, patch

from mxbiflow.core.context import MXBIFlow


class EyeEventMetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        session, mxbi = Mock(), Mock()
        session.mxbi_config.mxbi_id = "test-rig"
        session.session_id = 1
        session.current_animal.current_stage_name = "fixation"
        session.current_animal.current_stage.level = 3
        session.current_animal.trial_id = 7
        mxbi.screen_size.width, mxbi.screen_size.height = 1024, 600
        self.sender = Mock()
        self.context = MXBIFlow(session, mxbi)
        self.animal = session.current_animal
        patcher = patch.object(self.context, "_event_sender", return_value=self.sender)
        patcher.start()
        self.addCleanup(patcher.stop)

    def sent(self):
        return self.sender.send.call_args.args[0]

    def test_every_event_carries_the_stage_and_its_level(self) -> None:
        self.context._send_eye_event("animal_entered")
        event = self.sent()
        self.assertEqual(event.stage, "fixation")
        self.assertEqual(event.metadata, {"stage_level": 3})

    def test_stimulus_metadata_is_kept_beside_the_level(self) -> None:
        tolerance = {"radius": 80, "unit": "px"}
        self.context.stimulus_event("stimulus_shown", "target-1",
                                    metadata={"tolerance_area": tolerance})
        self.context.eye_display_presented()
        self.assertEqual(self.sent().metadata,
                         {"tolerance_area": tolerance, "stage_level": 3})

    def test_a_level_set_by_the_task_is_not_replaced(self) -> None:
        self.context._send_eye_event("stimulus_changed", stimulus_id="t",
                                     metadata={"stage_level": 9})
        self.assertEqual(self.sent().metadata, {"stage_level": 9})

    def test_unknown_stage_or_no_animal_sends_no_level(self) -> None:
        type(self.animal).current_stage = PropertyMock(side_effect=ValueError("Unknown stage"))
        self.context._send_eye_event("animal_left")
        self.assertEqual(self.sent().metadata, {})
        self.context._session.current_animal = None
        self.context._send_eye_event("run_ended")
        self.assertEqual(self.sent().metadata, {})


if __name__ == "__main__":
    unittest.main()
