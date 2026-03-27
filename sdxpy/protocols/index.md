# Protocols

## mock_time.py

| Variable | Scope | Role |
|---|---|---|
| since | module.elapsed | fixed value |

## callable.py

| Variable | Scope | Role |
|---|---|---|
| add_3 | module | fixed value |
| result | module | fixed value |
| arg | module.Adder.__call__ | fixed value |
| self | module.Adder.__call__ | fixed value |
| self | module.Adder.__init__ | fixed value |
| value | module.Adder.__init__ | fixed value |

## mock_object.py

| Variable | Scope | Role |
|---|---|---|
| args | module.Fake.__call__ | fixed value |
| kwargs | module.Fake.__call__ | fixed value |
| self | module.Fake.__call__ | fixed value |
| func | module.Fake.__init__ | fixed value |
| self | module.Fake.__init__ | fixed value |
| value | module.Fake.__init__ | fixed value |
| a | module.adder | fixed value |
| b | module.adder | fixed value |
| func | module.fakeit | fixed value |
| name | module.fakeit | fixed value |
| value | module.fakeit | fixed value |
| fake | module.fakeit | fixed value |
| fake | module.test_fake_records_calls | fixed value |

## ex_with.py

*No output from jorma (possible syntax error or empty file).*

## mock_context.py

| Variable | Scope | Role |
|---|---|---|
| self | module.ContextFake.__enter__ | fixed value |
| exc_traceback | module.ContextFake.__exit__ | fixed value |
| exc_type | module.ContextFake.__exit__ | fixed value |
| exc_value | module.ContextFake.__exit__ | fixed value |
| self | module.ContextFake.__exit__ | fixed value |
| func | module.ContextFake.__init__ | fixed value |
| name | module.ContextFake.__init__ | fixed value |
| self | module.ContextFake.__init__ | fixed value |
| value | module.ContextFake.__init__ | fixed value |
| fake | module.check_no_lasting_effects | fixed value |
| a | module.subber | fixed value |
| b | module.subber | fixed value |

## wrap_infinite.py

| Variable | Scope | Role |
|---|---|---|
| original | module | fixed value |
| value | module.logging | fixed value |
| value | module.original | fixed value |

## wrap_capture.py

| Variable | Scope | Role |
|---|---|---|
| original | module | unknown |
| func | module.logging | fixed value |
| value | module.logging._inner | fixed value |
| value | module.original | fixed value |

## wrap_param.py

| Variable | Scope | Role |
|---|---|---|
| original | module | unknown |
| func | module.logging | fixed value |
| label | module.logging | fixed value |
| value | module.logging._inner | fixed value |
| value | module.original | fixed value |

## decorator_simple.py

| Variable | Scope | Role |
|---|---|---|
| message | module.original | fixed value |
| func | module.wrap | fixed value |
| args | module.wrap._inner | fixed value |

## decorator_param.py

| Variable | Scope | Role |
|---|---|---|
| message | module.original | fixed value |
| label | module.wrap | fixed value |
| func | module.wrap._decorate | fixed value |
| args | module.wrap._decorate._inner | fixed value |

## alternative_design.py

| Variable | Scope | Role |
|---|---|---|
| func | module.decorator | fixed value |
| label | module.decorator | fixed value |
| arg | module.decorator._inner | fixed value |
| x | module.double | fixed value |

## naive_iterator.py

| Variable | Scope | Role |
|---|---|---|
| self | module.NaiveIterator.__init__ | fixed value |
| text | module.NaiveIterator.__init__ | fixed value |
| self | module.NaiveIterator.__iter__ | fixed value |
| self | module.NaiveIterator.__next__ | fixed value |
| self | module.NaiveIterator._advance | fixed value |

## test_naive_iterator.py

| Variable | Scope | Role |
|---|---|---|
| buffer | module.gather | fixed value |
| result | module.gather | gatherer |
| char | module.gather | stepper |
| buffer | module.test_naive_buffer | fixed value |
| buffer | module.test_naive_buffer_empty_string | fixed value |
| buffer | module.test_naive_buffer_nested_loop | fixed value |
| result | module.test_naive_buffer_nested_loop | gatherer |
| outer | module.test_naive_buffer_nested_loop | stepper |
| inner | module.test_naive_buffer_nested_loop | stepper |

## better_iterator.py

| Variable | Scope | Role |
|---|---|---|
| self | module.BetterCursor.__init__ | fixed value |
| text | module.BetterCursor.__init__ | fixed value |
| self | module.BetterCursor.__next__ | fixed value |
| self | module.BetterCursor._advance | fixed value |
| self | module.BetterIterator.__init__ | fixed value |
| text | module.BetterIterator.__init__ | fixed value |
| self | module.BetterIterator.__iter__ | fixed value |

## ex_timer.py

| Variable | Scope | Role |
|---|---|---|
| start | module | fixed value |

