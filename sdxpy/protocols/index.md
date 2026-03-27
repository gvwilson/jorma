# Variable Role Analysis: protocols

## alternative_design.py

Error during dynamic analysis (TypeError): decorator() missing 1 required positional argument: 'label'
### Static analysis

| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module.decorator        | func     | fixed value | line 1   |
| module.decorator        | label    | fixed value | line 1   |
| module.decorator._inner | arg      | fixed value | line 2   |
| module.double           | x        | fixed value | line 8   |

## better_iterator.py

### Static analysis

| Scope                          | Variable | Role        | Location |
| :------------------------------| :--------| :-----------| :--------|
| module.BetterCursor.__init__   | self     | fixed value | line 12  |
| module.BetterCursor.__init__   | text     | fixed value | line 12  |
| module.BetterCursor.__next__   | self     | fixed value | line 17  |
| module.BetterCursor._advance   | self     | fixed value | line 24  |
| module.BetterIterator.__init__ | self     | fixed value | line 3   |
| module.BetterIterator.__init__ | text     | fixed value | line 3   |
| module.BetterIterator.__iter__ | self     | fixed value | line 6   |

## callable.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | add_3    | fixed value | line 8   |
| module                | result   | fixed value | line 9   |
| module.Adder.__call__ | arg      | fixed value | line 5   |
| module.Adder.__call__ | self     | fixed value | line 5   |
| module.Adder.__init__ | self     | fixed value | line 2   |
| module.Adder.__init__ | value    | fixed value | line 2   |
add_3(8): 11

## decorator_param.py

### Static analysis

| Scope                        | Variable | Role        | Location |
| :----------------------------| :--------| :-----------| :--------|
| module.original              | message  | fixed value | line 11  |
| module.wrap                  | label    | fixed value | line 1   |
| module.wrap._decorate        | func     | fixed value | line 2   |
| module.wrap._decorate._inner | args     | fixed value | line 3   |
++ wrapping
original: example
-- wrapping

## decorator_simple.py

### Static analysis

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.original    | message  | fixed value | line 9   |
| module.wrap        | func     | fixed value | line 1   |
| module.wrap._inner | args     | fixed value | line 2   |
before call
original: example
after call

## ex_timer.py

Error during dynamic analysis (NameError): name 'Timer' is not defined
### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | start    | fixed value | line 3   |

## ex_with.py

Syntax error in '/Users/gvwilson/jorma/sdxpy/protocols/ex_with.py': invalid character '…' (U+2026) (<unknown>, line 1)

## mock_context.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'mock_object'
### Static analysis

| Scope                           | Variable      | Role        | Location |
| :-------------------------------| :-------------| :-----------| :--------|
| module.ContextFake.__enter__    | self          | fixed value | line 11  |
| module.ContextFake.__exit__     | exc_traceback | fixed value | line 17  |
| module.ContextFake.__exit__     | exc_type      | fixed value | line 17  |
| module.ContextFake.__exit__     | exc_value     | fixed value | line 17  |
| module.ContextFake.__exit__     | self          | fixed value | line 17  |
| module.ContextFake.__init__     | func          | fixed value | line 6   |
| module.ContextFake.__init__     | name          | fixed value | line 6   |
| module.ContextFake.__init__     | self          | fixed value | line 6   |
| module.ContextFake.__init__     | value         | fixed value | line 6   |
| module.check_no_lasting_effects | fake          | fixed value | line 27  |
| module.subber                   | a             | fixed value | line 22  |
| module.subber                   | b             | fixed value | line 22  |

## mock_object.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'util'
### Static analysis

| Scope                          | Variable | Role        | Location |
| :------------------------------| :--------| :-----------| :--------|
| module.Fake.__call__           | args     | fixed value | line 10  |
| module.Fake.__call__           | kwargs   | fixed value | line 10  |
| module.Fake.__call__           | self     | fixed value | line 10  |
| module.Fake.__init__           | func     | fixed value | line 5   |
| module.Fake.__init__           | self     | fixed value | line 5   |
| module.Fake.__init__           | value    | fixed value | line 5   |
| module.adder                   | a        | fixed value | line 26  |
| module.adder                   | b        | fixed value | line 26  |
| module.fakeit                  | func     | fixed value | line 18  |
| module.fakeit                  | name     | fixed value | line 18  |
| module.fakeit                  | value    | fixed value | line 18  |
| module.fakeit                  | fake     | fixed value | line 20  |
| module.test_fake_records_calls | fake     | fixed value | line 41  |

## mock_time.py

### Static analysis

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module.elapsed | since    | fixed value | line 3   |

## naive_iterator.py

### Static analysis

| Scope                         | Variable | Role        | Location |
| :-----------------------------| :--------| :-----------| :--------|
| module.NaiveIterator.__init__ | self     | fixed value | line 3   |
| module.NaiveIterator.__init__ | text     | fixed value | line 3   |
| module.NaiveIterator.__iter__ | self     | fixed value | line 6   |
| module.NaiveIterator.__next__ | self     | fixed value | line 10  |
| module.NaiveIterator._advance | self     | fixed value | line 18  |

## test_naive_iterator.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'naive_iterator'
### Static analysis

| Scope                                 | Variable | Role        | Location |
| :-------------------------------------| :--------| :-----------| :--------|
| module.gather                         | buffer   | fixed value | line 5   |
| module.gather                         | result   | gatherer    | line 6   |
| module.gather                         | char     | stepper     | line 7   |
| module.test_naive_buffer              | buffer   | fixed value | line 13  |
| module.test_naive_buffer_empty_string | buffer   | fixed value | line 19  |
| module.test_naive_buffer_nested_loop  | buffer   | fixed value | line 26  |
| module.test_naive_buffer_nested_loop  | result   | gatherer    | line 27  |
| module.test_naive_buffer_nested_loop  | outer    | stepper     | line 28  |
| module.test_naive_buffer_nested_loop  | inner    | stepper     | line 29  |

## wrap_capture.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | original | unknown     | line 11  |
| module.logging        | func     | fixed value | line 4   |
| module.logging._inner | value    | fixed value | line 5   |
| module.original       | value    | fixed value | line 1   |
before call
original: example
after call

## wrap_infinite.py

### Static analysis

| Scope           | Variable | Role        | Location |
| :---------------| :--------| :-----------| :--------|
| module          | original | fixed value | line 9   |
| module.logging  | value    | fixed value | line 4   |
| module.original | value    | fixed value | line 1   |
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before callError during dynamic analysis (RecursionError): maximum recursion depth exceeded

before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call
before call

## wrap_param.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | original | unknown     | line 11  |
| module.logging        | func     | fixed value | line 4   |
| module.logging        | label    | fixed value | line 4   |
| module.logging._inner | value    | fixed value | line 5   |
| module.original       | value    | fixed value | line 1   |
++ call
original: example
-- call

