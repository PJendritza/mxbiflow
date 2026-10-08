import unittest
from dataclasses import dataclass
from unittest.mock import patch

from pygame import Surface

from mxbiflow.trial import PositionTrail


@dataclass(frozen=True)
class _Sample:
    timestamp_ns: int
    x: float
    y: float


class PositionTrailTests(unittest.TestCase):
    def test_draws_fading_history_and_current_position(self) -> None:
        sample = _Sample(timestamp_ns=1, x=20.4, y=30.6)
        trail = PositionTrail(lambda: sample)
        screen = Surface((100, 100))

        with patch(
            "mxbiflow.trial.stimuli.monotonic",
            side_effect=[1.0, 1.2],
        ):
            trail.update(1 / 60)
            trail.draw(screen)

        color = screen.get_at((20, 31))
        self.assertGreater(color.r, color.g)
        self.assertGreater(color.r, color.b)

    def test_deduplicates_samples_and_expires_old_history(self) -> None:
        sample: _Sample | None = _Sample(timestamp_ns=1, x=20, y=30)
        trail = PositionTrail(lambda: sample)

        with patch(
            "mxbiflow.trial.stimuli.monotonic",
            side_effect=[1.0, 1.1, 1.5],
        ):
            trail.update(0)
            trail.update(0)
            sample = None
            trail.update(0)

        screen = Surface((100, 100))
        trail.draw(screen)
        self.assertEqual(screen.get_at((20, 30)), (0, 0, 0, 255))

    def test_rejects_invalid_visual_parameters(self) -> None:
        with self.assertRaisesRegex(ValueError, "history_ms"):
            PositionTrail(lambda: None, history_ms=0)
        with self.assertRaisesRegex(ValueError, "alpha"):
            PositionTrail(lambda: None, trail_min_alpha=200, trail_max_alpha=100)


if __name__ == "__main__":
    unittest.main()
