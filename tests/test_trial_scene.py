import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pygame

from mxbiflow.trial import SemanticEvent, State, Trial, TrialScene, track_touch


class _Region:
    def contains(self, position: tuple[int, int]) -> bool:
        return position == (20, 10)


class _TrialScene(TrialScene):
    pass


class TrialSceneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.session = Mock()
        self.aplayer = Mock()
        self.mxbiflow = SimpleNamespace(
            session=self.session,
            mxbi=SimpleNamespace(
                aplayer=self.aplayer,
                screen_size=SimpleNamespace(width=100, height=50),
            ),
        )

    def test_scene_adds_one_trial_and_finishes_runtime(self) -> None:
        finished: list[bool] = []
        state = State("iti")
        state.duration = 10
        _TrialScene.trial_factory = staticmethod(
            lambda context: Trial(
                initial_state="iti",
                states=[state],
                finish_callbacks=[finished.append],
            )
        )

        with patch("mxbiflow.trial.scene.get_mxbiflow", return_value=self.mxbiflow):
            scene = _TrialScene()
            scene.start()
            scene.update(0.010)

        self.session.add_trial.assert_called_once_with()
        self.assertFalse(scene.running)
        self.assertEqual(finished, [True])
        self.aplayer.cancel_all.assert_called_once_with()

    def test_mouse_and_finger_input_become_semantic_events(self) -> None:
        target = track_touch(_Region(), "target")
        background = SemanticEvent("backgroundTouched")
        touches: list[object] = []
        waiting = State("waiting")
        waiting.duration = None
        waiting.wait_events = [target.touched, background]
        waiting.next_state_after_event = {
            target.touched: "target",
            background: "background",
        }
        target_state = State("target")
        target_state.duration = None
        background_state = State("background")
        background_state.duration = None

        def build(context: object) -> Trial:
            return Trial(
                initial_state="waiting",
                states=[waiting, target_state, background_state],
                touch_trackers=[target.tracker],
                unclaimed_touch_event=background,
                touch_observers=[touches.append],
            )

        _TrialScene.trial_factory = staticmethod(build)
        with patch("mxbiflow.trial.scene.get_mxbiflow", return_value=self.mxbiflow):
            scene = _TrialScene()
            scene.start()
            scene.handle_event(pygame.event.Event(pygame.FINGERDOWN, x=0.2, y=0.2))
            scene.update(0)

        runtime = scene.runtime
        self.assertIsNotNone(runtime)
        assert runtime is not None
        self.assertEqual(runtime.current_state, target_state)
        self.assertEqual(len(touches), 1)


if __name__ == "__main__":
    unittest.main()
