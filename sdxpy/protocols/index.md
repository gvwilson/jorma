# protocols

## better_iterator.py

### Static analysis

| Scope                          | Variable | Role        | Location |
| :------------------------------| :--------| :-----------| :--------|
| module.BetterCursor.__init__   | self     | fixed value | line 10  |
| module.BetterCursor.__init__   | text     | fixed value | line 10  |
| module.BetterCursor.__next__   | self     | fixed value | line 15  |
| module.BetterCursor._advance   | self     | fixed value | line 21  |
| module.BetterIterator.__init__ | self     | fixed value | line 2   |
| module.BetterIterator.__init__ | text     | fixed value | line 2   |
| module.BetterIterator.__iter__ | self     | fixed value | line 5   |

## callable.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | add_3    | fixed value | line 9   |
| module                | result   | fixed value | line 10  |
| module.Adder.__call__ | arg      | fixed value | line 5   |
| module.Adder.__call__ | self     | fixed value | line 5   |
| module.Adder.__init__ | self     | fixed value | line 2   |
| module.Adder.__init__ | value    | fixed value | line 2   |

## decorator_param.py

### Static analysis

| Scope                        | Variable | Role        | Location |
| :----------------------------| :--------| :-----------| :--------|
| module.original              | message  | fixed value | line 14  |
| module.wrap                  | label    | fixed value | line 1   |
| module.wrap._decorate        | func     | fixed value | line 2   |
| module.wrap._decorate._inner | args     | fixed value | line 3   |

## decorator_simple.py

### Static analysis

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.original    | message  | fixed value | line 11  |
| module.wrap        | func     | fixed value | line 1   |
| module.wrap._inner | args     | fixed value | line 2   |

## mock_context.py

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
| module.subber                   | a             | fixed value | line 21  |
| module.subber                   | b             | fixed value | line 21  |

## mock_object.py

### Static analysis

| Scope                          | Variable | Role        | Location |
| :------------------------------| :--------| :-----------| :--------|
| module.Fake.__call__           | args     | fixed value | line 10  |
| module.Fake.__call__           | kwargs   | fixed value | line 10  |
| module.Fake.__call__           | self     | fixed value | line 10  |
| module.Fake.__init__           | func     | fixed value | line 5   |
| module.Fake.__init__           | self     | fixed value | line 5   |
| module.Fake.__init__           | value    | fixed value | line 5   |
| module.adder                   | a        | fixed value | line 24  |
| module.adder                   | b        | fixed value | line 24  |
| module.fakeit                  | func     | fixed value | line 17  |
| module.fakeit                  | name     | fixed value | line 17  |
| module.fakeit                  | value    | fixed value | line 17  |
| module.fakeit                  | fake     | fixed value | line 19  |
| module.test_fake_records_calls | fake     | fixed value | line 38  |

## mock_time.py

### Static analysis

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module.elapsed | since    | fixed value | line 4   |

## naive_iterator.py

### Static analysis

| Scope                         | Variable | Role        | Location |
| :-----------------------------| :--------| :-----------| :--------|
| module.NaiveIterator.__init__ | self     | fixed value | line 2   |
| module.NaiveIterator.__init__ | text     | fixed value | line 2   |
| module.NaiveIterator.__iter__ | self     | fixed value | line 5   |
| module.NaiveIterator.__next__ | self     | fixed value | line 9   |
| module.NaiveIterator._advance | self     | fixed value | line 15  |

## test_better_iterator.py

### Static analysis

| Scope                                | Variable | Role        | Location |
| :------------------------------------| :--------| :-----------| :--------|
| module.gather                        | buffer   | fixed value | line 4   |
| module.gather                        | result   | gatherer    | line 5   |
| module.gather                        | char     | stepper     | line 6   |
| module.test_naive_buffer             | buffer   | fixed value | line 12  |
| module.test_naive_buffer_nested_loop | buffer   | fixed value | line 17  |
| module.test_naive_buffer_nested_loop | result   | gatherer    | line 18  |
| module.test_naive_buffer_nested_loop | _        | stepper     | line 19  |
| module.test_naive_buffer_nested_loop | inner    | stepper     | line 20  |

## test_naive_iterator.py

### Static analysis

| Scope                                 | Variable | Role        | Location |
| :-------------------------------------| :--------| :-----------| :--------|
| module.gather                         | buffer   | fixed value | line 5   |
| module.gather                         | result   | gatherer    | line 6   |
| module.gather                         | char     | stepper     | line 7   |
| module.test_naive_buffer              | buffer   | fixed value | line 13  |
| module.test_naive_buffer_empty_string | buffer   | fixed value | line 18  |
| module.test_naive_buffer_nested_loop  | buffer   | fixed value | line 24  |
| module.test_naive_buffer_nested_loop  | result   | gatherer    | line 25  |
| module.test_naive_buffer_nested_loop  | outer    | stepper     | line 26  |
| module.test_naive_buffer_nested_loop  | inner    | stepper     | line 27  |

## util.py

### Static analysis

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.run_tests | prefix   | fixed value | line 1   |
| module.run_tests | whence   | fixed value | line 1   |
| module.run_tests | results  | fixed value | line 2   |
| module.run_tests | name     | stepper     | line 3   |
| module.run_tests | test     | stepper     | line 3   |

## wrap_capture.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | original | unknown     | line 14  |
| module.logging        | func     | fixed value | line 5   |
| module.logging._inner | value    | fixed value | line 6   |
| module.original       | value    | fixed value | line 1   |

## wrap_param.py

### Static analysis

| Scope                 | Variable | Role        | Location |
| :---------------------| :--------| :-----------| :--------|
| module                | original | unknown     | line 14  |
| module.logging        | func     | fixed value | line 5   |
| module.logging        | label    | fixed value | line 5   |
| module.logging._inner | value    | fixed value | line 6   |
| module.original       | value    | fixed value | line 1   |

