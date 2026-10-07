import unittest

from mxbiflow.trial import Call, Set


class _Target:
    def __init__(self) -> None:
        self.visible = False
        self.position = (0, 0)


class SetTests(unittest.TestCase):
    def test_set_is_deferred_until_execute(self) -> None:
        target = _Target()

        action = Set(target, visible=True)

        self.assertFalse(target.visible)
        action.execute(None)
        self.assertTrue(target.visible)

    def test_set_changes_multiple_properties(self) -> None:
        target = _Target()

        Set(target, visible=True, position=(10, 20)).execute(None)

        self.assertTrue(target.visible)
        self.assertEqual(target.position, (10, 20))

    def test_set_rejects_unknown_property(self) -> None:
        with self.assertRaisesRegex(AttributeError, "unknown"):
            Set(_Target(), unknown=True)


class CallTests(unittest.TestCase):
    def test_call_is_deferred(self) -> None:
        values: list[int] = []
        action = Call(values.append, 3)

        self.assertEqual(values, [])
        action.execute(None)
        self.assertEqual(values, [3])


if __name__ == "__main__":
    unittest.main()
