"""Tests for static role classifiers in roles.py."""

import pytest
from conftest import role_of

from jorma import (
    CONTAINER,
    FIXED_VALUE,
    GATHERER,
    LAZY_VALUE,
    LOG,
    MOST_RECENT,
    MOST_WANTED,
    ONE_WAY_FLAG,
    ORGANIZER,
    STEPPER,
    TEMPORARY,
    TOGGLE,
    UNKNOWN,
)


# ---------------------------------------------------------------------------
# Fixed value
# ---------------------------------------------------------------------------


def test_fixed_value_simple():
    src = "x = 42"
    assert role_of(src, "x") == FIXED_VALUE


def test_fixed_value_string():
    src = 'greeting = "hello"'
    assert role_of(src, "greeting") == FIXED_VALUE


def test_fixed_value_constant_in_function():
    src = """
def f():
    pi = 3.14159
"""
    assert role_of(src, "pi", "module.f") == FIXED_VALUE


# ---------------------------------------------------------------------------
# Stepper
# ---------------------------------------------------------------------------


def test_stepper_for_loop_target():
    src = """
for i in range(10):
    pass
"""
    assert role_of(src, "i") == STEPPER


def test_stepper_aug_assign_const_in_loop():
    src = """
i = 0
while i < 10:
    i += 1
"""
    assert role_of(src, "i") == STEPPER


def test_stepper_self_ref_const_in_loop():
    src = """
n = 1
while n < 100:
    n = n * 2
"""
    assert role_of(src, "n") == STEPPER


# ---------------------------------------------------------------------------
# Gatherer
# ---------------------------------------------------------------------------


def test_gatherer_aug_var_in_loop():
    src = """
total = 0
for x in data:
    total += x
"""
    assert role_of(src, "total") == GATHERER


def test_gatherer_self_ref_var_in_loop():
    src = """
result = 0
for x in data:
    result = result + x
"""
    assert role_of(src, "result") == GATHERER


# ---------------------------------------------------------------------------
# Most-recent holder
# ---------------------------------------------------------------------------


def test_most_recent_unconditional_loop():
    src = """
last = None
for item in items:
    last = item
"""
    assert role_of(src, "last") == MOST_RECENT


# ---------------------------------------------------------------------------
# Most-wanted holder
# ---------------------------------------------------------------------------


def test_most_wanted_conditional_loop():
    src = """
best = None
for x in data:
    if x > threshold:
        best = x
"""
    assert role_of(src, "best") == MOST_WANTED


def test_most_wanted_max_pattern():
    src = """
maximum = data[0]
for x in data:
    if x > maximum:
        maximum = x
"""
    assert role_of(src, "maximum") == MOST_WANTED


# ---------------------------------------------------------------------------
# One-way flag
# ---------------------------------------------------------------------------


def test_one_way_flag_false_to_true():
    src = """
found = False
for item in items:
    if item == target:
        found = True
"""
    assert role_of(src, "found") == ONE_WAY_FLAG


def test_one_way_flag_true_to_false():
    src = """
ok = True
for item in items:
    if item < 0:
        ok = False
"""
    assert role_of(src, "ok") == ONE_WAY_FLAG


# ---------------------------------------------------------------------------
# Temporary
# ---------------------------------------------------------------------------


def test_temporary_swap():
    src = "a, b = b, a"
    assert role_of(src, "a") == TEMPORARY
    assert role_of(src, "b") == TEMPORARY


def test_temporary_swap_in_function():
    src = """
def sort_two(a, b):
    a, b = b, a
    return a, b
"""
    assert role_of(src, "a", "module.sort_two") == TEMPORARY


# ---------------------------------------------------------------------------
# Organizer
# ---------------------------------------------------------------------------


def test_organizer_sort():
    src = """
items = [3, 1, 2]
items.sort()
"""
    assert role_of(src, "items") == ORGANIZER


def test_organizer_reverse():
    src = """
nums = [1, 2, 3]
nums.reverse()
"""
    assert role_of(src, "nums") == ORGANIZER


# ---------------------------------------------------------------------------
# Container
# ---------------------------------------------------------------------------


def test_container_append_and_remove():
    src = """
bag = []
bag.append(1)
bag.remove(1)
"""
    assert role_of(src, "bag") == CONTAINER


def test_container_add_to_set():
    src = """
seen = set()
seen.add(x)
seen.discard(y)
"""
    assert role_of(src, "seen") == CONTAINER


# ---------------------------------------------------------------------------
# Toggle
# ---------------------------------------------------------------------------


def test_toggle_not():
    src = """
flag = True
flag = not flag
"""
    assert role_of(src, "flag") == TOGGLE


def test_toggle_subtract():
    src = """
side = 0
side = 1 - side
"""
    assert role_of(src, "side") == TOGGLE


def test_toggle_xor():
    src = """
bit = 0
bit ^= 1
"""
    assert role_of(src, "bit") == TOGGLE


# ---------------------------------------------------------------------------
# Log
# ---------------------------------------------------------------------------


def test_log_append_only():
    src = """
history = []
for item in stream:
    history.append(item)
"""
    assert role_of(src, "history") == LOG


def test_log_extend_only():
    src = """
log = []
log.extend(batch)
"""
    assert role_of(src, "log") == LOG


def test_log_not_when_removal():
    src = """
buf = []
buf.append(x)
buf.pop()
"""
    assert role_of(src, "buf") == CONTAINER


# ---------------------------------------------------------------------------
# Lazy value
# ---------------------------------------------------------------------------


def test_lazy_value_none_sentinel():
    src = """
cached = None
if condition:
    cached = compute()
"""
    assert role_of(src, "cached") == LAZY_VALUE


def test_lazy_value_neg_one_sentinel():
    src = """
index = -1
if found:
    index = pos
"""
    assert role_of(src, "index") == LAZY_VALUE


def test_lazy_value_empty_string_sentinel():
    src = """
name = ""
if data:
    name = data["name"]
"""
    assert role_of(src, "name") == LAZY_VALUE


# ---------------------------------------------------------------------------
# Unknown
# ---------------------------------------------------------------------------


def test_unknown_self_ref_outside_loop():
    # x references itself in the RHS but there is no loop — not stepper or
    # gatherer (those require loop context) and not fixed value.
    src = """
x = 0
x = x + y
"""
    assert role_of(src, "x") == UNKNOWN
