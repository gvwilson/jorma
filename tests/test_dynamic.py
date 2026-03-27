"""Tests for dynamic role detection (phase and follower) in roles.py."""

import pytest
from conftest import dynamic_role_of

from jorma import FOLLOWER, GENERATOR_STATE, PHASE, SNAPSHOT


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
            prev = current
            current = val

    assert dynamic_role_of(run, name="prev") == FOLLOWER


def test_follower_linked_list_style():
    def run():
        a = 10
        b = 0
        for v in [20, 30, 40, 50]:
            b = a
            a = v

    assert dynamic_role_of(run, name="b") == FOLLOWER


def test_follower_not_detected_for_independent():
    # x and y are independent — y should NOT be follower of x.
    def run():
        x = 1
        y = 100
        for i in range(4):
            x = i
            y = i * 10

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
        backup = data
        data.append(4)

    assert dynamic_role_of(run, name="backup") == SNAPSHOT


def test_snapshot_saves_for_comparison():
    # saved captures the current value of original before it is overwritten.
    def run():
        original = "hello"
        saved = original
        original = "goodbye"

    assert dynamic_role_of(run, name="saved") == SNAPSHOT


def test_snapshot_not_detected_for_follower():
    # prev is a classic follower (tracks previous value of current);
    # it should NOT be classified as snapshot.
    def run():
        current = 1
        prev = None
        for val in [2, 3, 4, 5]:
            prev = current
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
        result = list(gen)

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
