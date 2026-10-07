import unittest

from mxbiflow.trial import EventQueue, SemanticEvent, track_touch


class _Region:
    def contains(self, position: tuple[int, int]) -> bool:
        return 0 <= position[0] < 10 and 0 <= position[1] < 10


class EventQueueTests(unittest.TestCase):
    def test_events_are_emitted_and_drained_in_order(self) -> None:
        queue = EventQueue()
        first = SemanticEvent("first")
        second = SemanticEvent("second")

        queue.emit(first, 1)
        queue.emit(second, 2)
        records = queue.drain()

        self.assertEqual([record.event for record in records], [first, second])
        self.assertEqual([record.payload for record in records], [1, 2])
        self.assertEqual(len(queue), 0)


class TouchTrackerTests(unittest.TestCase):
    def test_hit_testing_produces_semantic_touch_event(self) -> None:
        events = track_touch(_Region(), "target")

        self.assertEqual(events.touched.name, "targetTouched")
        self.assertIs(events.tracker.event_at((5, 5)), events.touched)
        self.assertIsNone(events.tracker.event_at((15, 5)))


if __name__ == "__main__":
    unittest.main()
