# Variable Roles

Static (and eventually dynamic) analysis of variable roles in Python programs,
based on Sajaniemi's theory of roles of variables.

## Bibliography

```
@article{inproceedings,
  author = {Sajaniemi, Jorma},
  year = {2002},
  month = {07},
  title = {Visualizing roles of variables to novice programmers},
  booktitle = {Proc. PPIG 14},
  file = {Sajaniemi2002-visualizing-roles-novice-programmers.pdf}
}

@inproceedings{Sajaniemi2005,
  author = {Sajaniemi, Jorma and Navarro-Prieto, Raquel},
  year = {2005},
  month = {1},
  title = {Roles of variables in experts' programming knowledge},
  booktitle = {Proc. PPIG 17},
  file = {Sajaniemi2005-roles-experts-programming-knowledge.pdf}
}

@article{Sajaniemi2006,
  title = {Roles of variables in three programming paradigms},
  author = {Sajaniemi, J. and Ben-Ari, M. and Byckling, P. and Gerdt, P. and Kulikova, Y.},
  journal = {Computer Science Education},
  volume = {16},
  number = {4},
  year = {2006},
  month = {12},
  doi = {10.1080/08993400600874584},
  file = {Sajaniemi2006-roles-three-paradigms.pdf}
}
```

## Usage

```
python roles.py target.py                      # static analysis only
python roles.py target.py func_name [arg …]    # static + dynamic
```

When a function name is supplied, `roles.py` will run static analysis, then
import `target.py` and call `func_name` with the given arguments (all passed as
strings) so that dynamic analysis can observe actual value sequences at runtime.
Dynamic analysis is not yet implemented.

## Sajaniemi's Roles

Jorma Sajaniemi identified a small set of stereotypical patterns that describe
how variables behave — specifically, how a variable's value changes over time
relative to other variables. Ten roles cover 99 % of variables in novice-level
procedural programs. The roles are a cognitive concept: they describe what a
variable *does*, not how it is declared.

| Role | Description |
|---|---|
| Fixed value | Initialized once and not changed thereafter. |
| Stepper | Steps through a systematic, predictable succession of values (e.g. a loop counter). |
| Walker | Traverses a data structure element by element, where each new value depends on the previous position. |
| Follower | Always receives the previous value of some other variable (e.g. `prev = current` before `current` is updated). |
| Most-recent holder | Holds the latest value encountered in an unpredictable series, typically successive inputs. |
| Most-wanted holder | Holds the best value found so far (maximum, minimum, closest match). |
| Gatherer | Accumulates the combined effect of individual values (running sum, product, count). |
| One-way flag | A two-valued variable that, once changed from its initial value, never reverts (e.g. an error sentinel set to `True` and never reset). |
| Temporary | Holds a value for a very short time only, most commonly in a swap operation. |
| Organizer | A collection used only to rearrange its elements (e.g. sorted in place), never to add or remove them. |
| Container | A collection whose elements are added and/or removed during the computation. |

## Additional Roles

The following six roles extend Sajaniemi's list to cover patterns that are
common in modern Python but absent from his original taxonomy.

| Role | Description |
|---|---|
| Toggle | Alternates between two values on successive updates (e.g. `side = not side`, `turn = 1 - turn`), distinct from a one-way flag (which never reverts) and a stepper (which advances monotonically). |
| Phase | Holds one of a small enumerated set of named states representing stages of an algorithm or process (a state-machine variable), with defined legal transitions between states. |
| Snapshot | Holds the value of another variable frozen at a specific earlier point in time, for comparison or rollback, distinct from a follower (which continuously tracks). |
| Log | An append-only, growing sequence of every value encountered in order, preserving full history rather than reducing it (unlike a gatherer) or allowing removal (unlike a container). |
| Lazy value | Initialized to a sentinel (e.g. `None`, `-1`, `""`) and set to its true value exactly once on first access; thereafter immutable, like a fixed value but with deliberately deferred initialization. |
| Generator state | Holds the internal state of a sequence-producing algorithm (random-number generator, UUID generator), updated in a deterministic but deliberately opaque way. |

## Static vs Dynamic Analysis

Static analysis (inspecting source code without running it) can detect patterns
in assignment structure but cannot observe actual runtime values. Dynamic
analysis (tracing execution) sees real value sequences but only for the inputs
provided.

| Role | Static | Dynamic | Notes |
|---|---|---|---|
| Fixed Value | ✓ | | Single assignment, no loops |
| Stepper | ✓ | | For-loop target; or `+= constant` in loop |
| Walker | | ✓ | Requires type info to recognise `.next` / pointer arithmetic |
| Follower | | ✓ | Requires data-flow to see one var receives another's previous value |
| Most-Recent Holder | ✓ | | Unconditional assignment inside a loop |
| Most-Wanted Holder | ✓ | | Conditional assignment inside a loop |
| Gatherer | ✓ | | `+= variable` in loop; or `x = x + y` in loop |
| One-Way Flag | ✓ | | Boolean initialised one way, only flipped the other way in a loop |
| Temporary | ✓ | | Tuple-swap pattern `a, b = b, a` |
| Organizer | ✓ | | Only `.sort()` / `.reverse()` called, no element removal |
| Container | ✓ | | Mutating collection methods called (add/remove) |
| Toggle | ✓ | | `x = not x`, `x = C - x`, `x ^= 1` |
| Log | ✓ | | Append-only container methods; no removal methods |
| Lazy Value | partial | ✓ | Sentinel assignment + later conditional set; dynamic confirms single-set |
| Phase | | ✓ | Requires recognising state-machine transitions at runtime |
| Snapshot | | ✓ | Requires data-flow to confirm value is frozen from another variable |
| Generator State | | ✓ | Requires recognising RNG / hash update patterns at runtime |

## Implementation Notes

### Static detection heuristics

`roles.py` walks the AST with `ast.NodeVisitor` and records per-variable
counters for each scope (module, function, class). Role determination applies
heuristics in priority order:

1. Temporary — appears in a tuple-swap (`a, b = b, a`)
2. Toggle — all self-referential assignments match `not x`, `C - x`, or `x ^= 1`
3. Log — container methods called, but only additive ones (no removal)
4. Container — any mutating collection method called
5. Organizer — only `.sort()` / `.reverse()` called
6. Stepper — for-loop target; or `+=` constant in loop; or `x = x + constant` in loop
7. Gatherer — `+=` variable in loop; or `x = x + y` in loop
8. One-Way Flag — boolean initialised outside loop, only flipped inside
9. Most-Wanted Holder — all loop assignments are inside an `if`
10. Most-Recent Holder — at least one unconditional assignment inside a loop
11. Lazy Value — sentinel (None / -1 / "") assigned outside loop; later assigned inside a conditional outside a loop
12. Fixed Value — no loop assignments, no augmented assignments, no self-references
13. Unknown — does not match any detectable pattern

### Roles not yet detected statically

Walker, Follower, Phase, Snapshot, and Generator State require either type
information (to recognise pointer/linked-list traversal) or runtime value
sequences (to observe state-machine transitions and data-flow dependencies).
These are reserved for the dynamic analysis phase.

## Project History

1. Literature review: Read three papers by Sajaniemi et al. (PPIG 2002,
   PPIG 2005, 2006) describing the roles of variables and their application
   across procedural, object-oriented, and functional programming paradigms.

2. Tool survey: Identified Python tools suitable for static analysis
   (`ast`, `astroid`, `libcst`) and dynamic analysis (`sys.settrace`, `snoop`,
   `viztracer`, `hunter`) of variable roles.

3. Initial implementation: Wrote `roles.py` using Python's `ast` module
   to detect the eleven Sajaniemi roles via static analysis.

4. Role extension: Proposed ten additional roles beyond Sajaniemi's
   taxonomy and surveyed programming languages that make role-like
   concepts explicit in their type systems (Rust, Kotlin, Dafny,
   Eiffel, LiquidHaskell, Clean, Plaid).

5. Role refinement: Added static detection of Toggle, Log, and Lazy
   Value; added Phase, Snapshot, and Generator State as named roles;
   extended CLI to accept an optional function name and arguments.

6. Dynamic analysis: Implemented `DynamicTracer` in `roles.py` using
   `sys.settrace` to detect Phase and Follower roles at runtime.
   The tracer snapshots `frame.f_locals` on every line and return event,
   records value sequences and pre-change context for each variable, then
   applies two detectors:
   - **Follower**: every update (not initialization) to variable A gives A
     the value that some consistent other variable B held just before the
     change.  Initial sentinel assignments (e.g. `prev = None`) are excluded
     from the check so they do not break detection.
   - **Phase**: variable holds 2–6 distinct non-boolean scalar values and
     revisits at least one state (total observations exceed distinct count).
   One subtle issue fixed during implementation: Python's `sys.settrace`
   fires a `"line"` event *before* the line executes, so the pre-change
   snapshot must be taken on the previous event and compared on the current
   one.  A second non-obvious issue: `-1` in Python's AST is
   `UnaryOp(USub, Constant(1))`, not `Constant(-1)`, requiring a special
   case in `_is_sentinel`.

7. Test suite: Created `tests/test_static.py` (29 tests covering all 13
   static classifiers) and `tests/test_dynamic.py` (7 tests for Phase and
   Follower detection).  Tests are run with `uv run pytest tests/`.
   A `conftest.py` provides `role_of` and `dynamic_role_of` helpers.
   One design note: a test case initially used `mode = t` (direct copy from
   loop variable) to exercise numeric phase states; this correctly classified
   as Follower rather than Phase, so the test was rewritten to use
   if-else transitions where the next state is computed from the current one.
