"""Tests for dynamic role detection (phase and follower) in roles.py."""

import pytest
from unittest.mock import MagicMock

from conftest import dynamic_role_of

from jorma import FOLLOWER, GENERATOR_STATE, PHASE, SNAPSHOT
from jorma.dynamic import DynamicTracer, run_as_main, run_dynamic


# ---------------------------------------------------------------------------
# Phase
# ---------------------------------------------------------------------------


def test_phase_traffic_light():
    def run():
        state = "red"
        for _ in range(6):
            if state == "red":
                state = "green"
            elif state == "green":
                state = "yellow"
            else:
                state = "red"

    assert dynamic_role_of(run, name="state") == PHASE


def test_phase_numeric_states():
    # States 1, 2, 3 cycle via conditional branches — not a follower of any
    # other variable because the next state is computed from the current state,
    # not copied from a peer.
    def run():
        state = 1
        for _ in range(7):
            if state == 1:
                state = 2
            elif state == 2:
                state = 3
            else:
                state = 1

    assert dynamic_role_of(run, name="state") == PHASE


def test_phase_not_detected_for_boolean():
    # Boolean toggling should NOT be classified as phase.
    def run():
        flag = True
        for _ in range(4):
            flag = not flag

    result = {}
    from jorma import trace_function

    result = trace_function(run)
    for (name, _scope), role in result.items():
        if name == "flag":
            assert role != PHASE


def test_phase_not_detected_for_stepper():
    # A simple counter that never revisits a value should NOT be phase.
    def run():
        state = 0
        for _ in range(5):
            state += 1

    result = {}
    from jorma import trace_function

    result = trace_function(run)
    for (name, _scope), role in result.items():
        if name == "state":
            assert role != PHASE


# ---------------------------------------------------------------------------
# Follower
# ---------------------------------------------------------------------------


def test_follower_classic_prev_current():
    def run():
        current = 1
        prev = None
        for val in [2, 3, 4, 5]:
            prev = current  # noqa: F841
            current = val

    assert dynamic_role_of(run, name="prev") == FOLLOWER


def test_follower_linked_list_style():
    def run():
        a = 10
        b = 0  # noqa: F841
        for v in [20, 30, 40, 50]:
            b = a  # noqa: F841
            a = v

    assert dynamic_role_of(run, name="b") == FOLLOWER


def test_follower_not_detected_for_independent():
    # x and y are independent — y should NOT be follower of x.
    def run():
        x = 1
        y = 100
        for i in range(4):
            x = i  # noqa: F841
            y = i * 10  # noqa: F841

    from jorma import trace_function

    result = trace_function(run)
    for (name, _scope), role in result.items():
        if name == "y":
            assert role != FOLLOWER


# ---------------------------------------------------------------------------
# Snapshot
# ---------------------------------------------------------------------------


def test_snapshot_one_time_copy():
    # backup copies data once; data is not reassigned, so this is a snapshot
    # not a follower (follower requires multiple updates).
    def run():
        data = [1, 2, 3]
        backup = data  # noqa: F841
        data.append(4)

    assert dynamic_role_of(run, name="backup") == SNAPSHOT


def test_snapshot_saves_for_comparison():
    # saved captures the current value of original before it is overwritten.
    def run():
        original = "hello"
        saved = original  # noqa: F841
        original = "goodbye"

    assert dynamic_role_of(run, name="saved") == SNAPSHOT


def test_snapshot_not_detected_for_follower():
    # prev is a classic follower (tracks previous value of current);
    # it should NOT be classified as snapshot.
    def run():
        current = 1
        prev = None
        for val in [2, 3, 4, 5]:
            prev = current  # noqa: F841
            current = val

    assert dynamic_role_of(run, name="prev") == FOLLOWER


# ---------------------------------------------------------------------------
# Generator state
# ---------------------------------------------------------------------------


def test_generator_state_iterator():
    def run():
        it = iter([1, 2, 3, 4, 5])
        total = 0
        for x in it:
            total += x

    assert dynamic_role_of(run, name="it") == GENERATOR_STATE


def test_generator_state_generator_expression():
    def run():
        gen = (x * 2 for x in range(5))
        result = list(gen)  # noqa: F841

    assert dynamic_role_of(run, name="gen") == GENERATOR_STATE


def test_generator_state_not_for_list():
    # A plain list is not a generator state.
    def run():
        items = [1, 2, 3]
        total = 0
        for x in items:
            total += x

    from jorma import trace_function

    result = trace_function(run)
    for (name, _scope), role in result.items():
        if name == "items":
            assert role != GENERATOR_STATE


# ---------------------------------------------------------------------------
# tracer() matching and non-matching directory branches
# ---------------------------------------------------------------------------


def test_tracer_matching_directory(tmp_path):
    # tracer() should return _line_tracer for frames in the target directory.
    script = tmp_path / "script.py"
    script.write_text("x = 1\n")
    tracer = DynamicTracer(str(script))
    frame = MagicMock()
    frame.f_code.co_filename = str(script)
    result = tracer.tracer(frame, "call", None)
    assert result == tracer._line_tracer


def test_tracer_non_matching_directory(tmp_path):
    # tracer() should return None for frames outside the target directory.
    script = tmp_path / "script.py"
    script.write_text("x = 1\n")
    tracer = DynamicTracer(str(script))
    frame = MagicMock()
    frame.f_code.co_filename = "/some/other/directory/other.py"
    result = tracer.tracer(frame, "call", None)
    assert result is None


# ---------------------------------------------------------------------------
# _line_tracer() via run_as_main
# ---------------------------------------------------------------------------


def test_line_tracer_via_run_as_main(tmp_path):
    # run_as_main exercises _line_tracer through sys.settrace.
    script = tmp_path / "counter.py"
    script.write_text(
        "total = 0\n"
        "for i in range(5):\n"
        "    total += i\n"
    )
    roles = run_as_main(script)
    assert isinstance(roles, dict)


# ---------------------------------------------------------------------------
# _check_phase with unhashable values
# ---------------------------------------------------------------------------


def test_check_phase_unhashable_values():
    # A variable that holds lists cannot be hashed; _check_phase must not raise.
    from jorma import trace_function

    def run():
        data = [1]  # noqa: F841
        data = [1, 2]  # noqa: F841
        data = [1]  # noqa: F841
        data = [1, 2]  # noqa: F841

    # Should complete without raising; unhashable values are silently skipped.
    result = trace_function(run)
    for (_name, _scope), role in result.items():
        assert role != PHASE  # lists can never be phase


# ---------------------------------------------------------------------------
# run_dynamic
# ---------------------------------------------------------------------------


def test_run_dynamic_happy_path(tmp_path):
    script = tmp_path / "funcs.py"
    script.write_text(
        "def count_up():\n"
        "    x = 0\n"
        "    for i in range(5):\n"
        "        x += i\n"
    )
    roles = run_dynamic(script, "count_up", [])
    assert isinstance(roles, dict)


def test_run_dynamic_missing_function(tmp_path):
    script = tmp_path / "funcs.py"
    script.write_text("def real_func(): pass\n")
    with pytest.raises(AttributeError):
        run_dynamic(script, "no_such_func", [])


def test_run_dynamic_unloadable_path(tmp_path):
    missing = tmp_path / "nonexistent.py"
    with pytest.raises((ImportError, FileNotFoundError, OSError)):
        run_dynamic(missing, "f", [])


def test_run_dynamic_suppress(tmp_path):
    script = tmp_path / "noisy.py"
    script.write_text(
        "def greet():\n"
        "    msg = 'hello'\n"
        "    print(msg)\n"
    )
    # suppress=True should discard the print output without raising.
    roles = run_dynamic(script, "greet", [], suppress=True)
    assert isinstance(roles, dict)


# ---------------------------------------------------------------------------
# run_as_main
# ---------------------------------------------------------------------------


def test_run_as_main_happy_path(tmp_path):
    script = tmp_path / "main.py"
    script.write_text(
        "if __name__ == '__main__':\n"
        "    total = 0\n"
        "    for i in range(3):\n"
        "        total += i\n"
    )
    roles = run_as_main(script)
    assert isinstance(roles, dict)


def test_run_as_main_sys_exit(tmp_path):
    script = tmp_path / "exits.py"
    script.write_text(
        "import sys\n"
        "x = 1\n"
        "sys.exit(0)\n"
    )
    # sys.exit() must be caught; run_as_main should return normally.
    roles = run_as_main(script)
    assert isinstance(roles, dict)


def test_run_as_main_suppress(tmp_path):
    script = tmp_path / "noisy.py"
    script.write_text("print('hello')\n")
    roles = run_as_main(script, suppress=True)
    assert isinstance(roles, dict)


def test_run_as_main_unloadable_path(tmp_path):
    missing = tmp_path / "nonexistent.py"
    with pytest.raises((ImportError, FileNotFoundError, OSError)):
        run_as_main(missing)
