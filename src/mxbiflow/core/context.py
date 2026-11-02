from pathlib import Path
import time
from uuid import uuid4

from mxbiflow.driver import MXBI
from mxbiflow.driver.eyetracker.eyetracker import EyeSample

from ..infra.timer import FrameTimer
from ..models.session import Session
from .path import get_data_dir_path


class MXBIFlow:
    def __init__(self, session: Session, mxbi: MXBI) -> None:
        self._session = session
        self._timer = FrameTimer()
        self._mxbi = mxbi
        self._eye_events = None
        self._run_id = str(uuid4())
        self._visit_id = None
        self._eye_animal = None
        self._eye_rfid = None
        self._pending_stimuli = []

    def _event_sender(self):
        from ..driver.eyetracker import MxEyeEyetracker
        from ..infra.eye_events import EyeEventSender

        tracker = self._mxbi.eyetracker
        if not isinstance(tracker, MxEyeEyetracker) or tracker.event_client is None:
            return None
        if self._eye_events is None:
            self._eye_events = EyeEventSender(
                tracker.event_client, self.data_dir / "eye_events" / f"{self._run_id}.jsonl"
            )
        return self._eye_events

    def _send_eye_event(self, kind, timestamp_ns=None, **fields):
        from py_mx_eye import ExperimentEvent

        sender = self._event_sender()
        if sender is None:
            return
        animal = self._session.current_animal
        tracker = self._mxbi.eyetracker
        sender.send(ExperimentEvent(
            kind=kind, timestamp_ns=timestamp_ns or time.time_ns(),
            run_id=self._run_id, visit_id=self._visit_id,
            rig_id=self._session.mxbi_config.mxbi_id,
            session_id=self._session.session_id,
            animal=self._eye_animal, rfid_id=self._eye_rfid,
            stage=animal.current_stage_name if animal else None,
            trial_id=animal.trial_id if animal else None,
            screen_dimensions=(self._mxbi.screen_size.width, self._mxbi.screen_size.height),
            control_recording=bool(getattr(tracker, "record_on_animal", False)),
            **fields,
        ))

    def eye_detector_event(self, msg):
        """Forward detector transitions, preserving raw RFID and detection time."""
        kind = str(msg.kind)
        if kind in ("animal_entered", "unknown_animal_entered"):
            if self._visit_id is not None:
                self._send_eye_event("animal_left", msg.timestamp_ns)
            self._visit_id = str(uuid4())
            self._eye_animal = msg.animal if kind == "animal_entered" else None
            self._eye_rfid = msg.rfid_id
            kind = "animal_entered"
        elif kind == "animal_identified":
            self._eye_animal, self._eye_rfid = msg.animal, msg.rfid_id
        elif kind == "fault_detected":
            kind = "detector_fault"
        elif kind != "animal_left":
            return
        self._send_eye_event(kind, msg.timestamp_ns)
        if kind in ("animal_left", "detector_fault"):
            self._visit_id = self._eye_animal = self._eye_rfid = None

    def stimulus_event(self, kind: str, stimulus_id: str, **details) -> None:
        """Call when changing what draw() presents, not on every frame.

        kind: stimulus_shown, stimulus_changed or stimulus_hidden. Position and
        size use Pygame screen pixels. Game stamps/sends after the next flip.
        """
        if kind not in ("stimulus_shown", "stimulus_changed", "stimulus_hidden"):
            raise ValueError("Unknown stimulus event kind")
        self._pending_stimuli.append((kind, stimulus_id, details))

    def eye_display_presented(self) -> None:
        timestamp = time.time_ns()
        pending, self._pending_stimuli = self._pending_stimuli, []
        for kind, stimulus_id, details in pending:
            self._send_eye_event(kind, timestamp, stimulus_id=stimulus_id, **details)

    def close_eye_events(self) -> None:
        if self._eye_events is not None:
            self._send_eye_event("run_ended")
            self._eye_events.close()

    @property
    def session(self) -> Session:
        return self._session

    @property
    def timer(self) -> FrameTimer:
        return self._timer

    @property
    def mxbi(self) -> MXBI:
        return self._mxbi

    @property
    def eye_sample(self) -> EyeSample | None:
        """Return the eye-tracking sample available for this frame.

        ``None`` when no eyetracker is configured, or when no usable sample is
        available: none measured yet, aged out, or the sample stream stopped.

        Scenes read this from ``update(dt_s)``, so gaze is consumed once per
        frame without blocking the game loop. See ``docs/eyetracking.md``.
        """
        eyetracker = self._mxbi.eyetracker
        return None if eyetracker is None else eyetracker.sample()

    @property
    def data_dir(self) -> Path:
        return get_data_dir_path()

    def update(self) -> None:
        self._timer.update()


_current_mxbiflow: MXBIFlow | None = None


def get_mxbiflow() -> MXBIFlow:
    if _current_mxbiflow is None:
        raise RuntimeError("MXBIFlow not initialized")
    return _current_mxbiflow


def set_mxbiflow(mxbiflow: MXBIFlow) -> None:
    global _current_mxbiflow
    if _current_mxbiflow is not None:
        raise RuntimeError("MXBIFlow already initialized")
    _current_mxbiflow = mxbiflow
