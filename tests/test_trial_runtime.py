import unittest

from mxbiflow.trial import Call, SemanticEvent, State, Trial, TrialRuntime


class TrialRuntimeTests(unittest.TestCase):
    def test_initial_state_entry_runs_once(self) -> None:
        entries: list[str] = []
        waiting = State("waiting")
        waiting.duration = None
        waiting.on_entry = [Call(entries.append, "waiting")]
        runtime = TrialRuntime(Trial(initial_state="waiting", states=[waiting]))

        runtime.start()
        runtime.update(1.0)

        self.assertEqual(entries, ["waiting"])
        self.assertEqual(runtime.current_state, waiting)

    def test_timeout_transition_runs_exit_and_entry_once(self) -> None:
        calls: list[str] = []
        waiting = State("waiting")
        waiting.duration = 10
        waiting.on_exit = [Call(calls.append, "exit")]
        waiting.next_state_after_timeout = "done"
        done = State("done")
        done.duration = None
        done.on_entry = [Call(calls.append, "entry")]
        runtime = TrialRuntime(Trial(initial_state="waiting", states=[waiting, done]))

        runtime.start()
        runtime.update(0.009)
        runtime.update(0.001)

        self.assertEqual(calls, ["exit", "entry"])
        self.assertEqual(runtime.current_state, done)

    def test_matching_event_has_priority_over_timeout(self) -> None:
        target_touched = SemanticEvent("targetTouched")
        waiting = State("waiting")
        waiting.duration = 10
        waiting.wait_events = [target_touched]
        waiting.next_state_after_event = {target_touched: "correct"}
        waiting.next_state_after_timeout = "timeout"
        correct = State("correct")
        correct.duration = None
        timeout = State("timeout")
        timeout.duration = None
        runtime = TrialRuntime(
            Trial(
                initial_state="waiting",
                states=[waiting, correct, timeout],
            )
        )

        runtime.start()
        runtime.emit(target_touched)
        runtime.update(0.010)

        self.assertEqual(runtime.current_state, correct)

    def test_irrelevant_events_are_discarded(self) -> None:
        target_touched = SemanticEvent("targetTouched")
        other = SemanticEvent("other")
        waiting = State("waiting")
        waiting.duration = None
        waiting.wait_events = [target_touched]
        waiting.next_state_after_event = {target_touched: "correct"}
        correct = State("correct")
        correct.duration = None
        runtime = TrialRuntime(
            Trial(initial_state="waiting", states=[waiting, correct])
        )

        runtime.start()
        runtime.emit(other)
        runtime.update(0)

        self.assertEqual(runtime.current_state, waiting)
        self.assertEqual(len(runtime.events), 0)

    def test_zero_duration_chain_completes_during_start(self) -> None:
        calls: list[str] = []
        first = State("first")
        first.on_entry = [Call(calls.append, "first")]
        first.next_state_after_timeout = "second"
        second = State("second")
        second.on_entry = [Call(calls.append, "second")]
        runtime = TrialRuntime(Trial(initial_state="first", states=[first, second]))

        runtime.start()

        self.assertTrue(runtime.completed)
        self.assertEqual(calls, ["first", "second"])

    def test_zero_duration_cycle_is_rejected(self) -> None:
        first = State("first")
        first.next_state_after_timeout = "second"
        second = State("second")
        second.next_state_after_timeout = "first"
        runtime = TrialRuntime(
            Trial(initial_state="first", states=[first, second]),
            max_immediate_transitions=4,
        )

        with self.assertRaisesRegex(RuntimeError, "immediate transition limit"):
            runtime.start()

    def test_unknown_next_state_fails_during_trial_validation(self) -> None:
        state = State("state")
        state.next_state_after_timeout = "missing"

        with self.assertRaisesRegex(ValueError, "unknown state 'missing'"):
            Trial(initial_state="state", states=[state])

    def test_final_state_runs_exit_once(self) -> None:
        exits: list[str] = []
        final = State("final")
        final.on_exit = [Call(exits.append, "exit")]
        runtime = TrialRuntime(Trial(initial_state="final", states=[final]))

        runtime.start()
        runtime.stop()

        self.assertTrue(runtime.completed)
        self.assertEqual(exits, ["exit"])


if __name__ == "__main__":
    unittest.main()
