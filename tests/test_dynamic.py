"""Tests for dynamic role detection (phase and follower) in roles.py."""

import pytest
from conftest import dynamic_role_of

from roles import FOLLOWER, PHASE


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
    from roles import trace_function

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
    from roles import trace_function

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

    from roles import trace_function

    result = trace_function(run)
    for (name, _scope), role in result.items():
        if name == "y":
            assert role != FOLLOWER
