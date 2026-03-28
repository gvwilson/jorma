"""Tests for static role classifiers in roles.py."""

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


# ---------------------------------------------------------------------------
# AST node coverage: visit_ClassDef
# ---------------------------------------------------------------------------


def test_class_def_variable_inside_class():
    src = """
class Foo:
    x = 1
"""
    assert role_of(src, "x", "module.Foo") == FIXED_VALUE


# ---------------------------------------------------------------------------
# AST node coverage: for-loop tuple unpacking target
# ---------------------------------------------------------------------------


def test_for_tuple_unpack_target():
    src = """
pairs = [(1, 2), (3, 4)]
for a, b in pairs:
    pass
"""
    assert role_of(src, "a") == STEPPER
    assert role_of(src, "b") == STEPPER


# ---------------------------------------------------------------------------
# AST node coverage: starred assignment target
# ---------------------------------------------------------------------------


def test_starred_assignment_target():
    src = """
items = [1, 2, 3, 4]
first, *rest = items
"""
    assert role_of(src, "first") == FIXED_VALUE
    assert role_of(src, "rest") == FIXED_VALUE


# ---------------------------------------------------------------------------
# AST node coverage: visit_AugAssign first_line and cond tracking
# ---------------------------------------------------------------------------


def test_aug_assign_no_prior_assignment():
    # x += 1 with no prior assignment: first_line must still be recorded.
    src = """
x = 0
x += 1
"""
    from jorma import analyze
    results = {v.name: v for v, _ in analyze(src)}
    assert results["x"].first_line > 0


def test_aug_assign_inside_if_inside_loop():
    # "+=" inside an if inside a loop exercises cond_depth tracking.
    src = """
total = 0
for x in range(10):
    if x % 2 == 0:
        total += x
"""
    assert role_of(src, "total") == GATHERER


def test_aug_assign_inside_if_outside_loop():
    # "+=" inside an if outside a loop exercises any_cond_depth tracking.
    # x += 1 sets aug_assigns, so it is not fixed value and falls through to unknown.
    src = """
x = 0
flag = True
if flag:
    x += 1
"""
    assert role_of(src, "x") == UNKNOWN


# ---------------------------------------------------------------------------
# AST node coverage: visit_AnnAssign
# ---------------------------------------------------------------------------


def test_annotated_assignment():
    src = "x: int = 5"
    assert role_of(src, "x") == FIXED_VALUE


# ---------------------------------------------------------------------------
# AST node coverage: visit_NamedExpr (walrus operator)
# ---------------------------------------------------------------------------


def test_walrus_operator():
    src = """
items = [1, 2, 3]
if (n := len(items)) > 0:
    pass
"""
    assert role_of(src, "n") == FIXED_VALUE


# ---------------------------------------------------------------------------
# AST node coverage: visit_With
# ---------------------------------------------------------------------------


def test_with_statement_bound_variable():
    src = """
with open("f") as fh:
    pass
"""
    from jorma import analyze
    results = {v.name: v for v, _ in analyze(src)}
    assert "fh" in results


# ---------------------------------------------------------------------------
# AST node coverage: visit_ExceptHandler
# ---------------------------------------------------------------------------


def test_except_handler_bound_variable():
    src = """
try:
    pass
except ValueError as e:
    pass
"""
    from jorma import analyze
    results = {v.name: v for v, _ in analyze(src)}
    assert "e" in results
