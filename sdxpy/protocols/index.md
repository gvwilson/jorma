# Variable Role Analysis: protocols

## alternative_design.py

```

[module.decorator]
  func                     fixed value             (line 1)
  label                    fixed value             (line 1)

[module.decorator._inner]
  arg                      fixed value             (line 2)

[module.double]
  x                        fixed value             (line 8)
```

## better_iterator.py

```

[module.BetterCursor.__init__]
  self                     fixed value             (line 12)
  text                     fixed value             (line 12)

[module.BetterCursor.__next__]
  self                     fixed value             (line 17)

[module.BetterCursor._advance]
  self                     fixed value             (line 24)

[module.BetterIterator.__init__]
  self                     fixed value             (line 3)
  text                     fixed value             (line 3)

[module.BetterIterator.__iter__]
  self                     fixed value             (line 6)
```

## callable.py

```

[module]
  add_3                    fixed value             (line 8)
  result                   fixed value             (line 9)

[module.Adder.__call__]
  arg                      fixed value             (line 5)
  self                     fixed value             (line 5)

[module.Adder.__init__]
  self                     fixed value             (line 2)
  value                    fixed value             (line 2)
```

## decorator_param.py

```

[module.original]
  message                  fixed value             (line 11)

[module.wrap]
  label                    fixed value             (line 1)

[module.wrap._decorate]
  func                     fixed value             (line 2)

[module.wrap._decorate._inner]
  args                     fixed value             (line 3)
```

## decorator_simple.py

```

[module.original]
  message                  fixed value             (line 9)

[module.wrap]
  func                     fixed value             (line 1)

[module.wrap._inner]
  args                     fixed value             (line 2)
```

## ex_timer.py

```

[module]
  start                    fixed value             (line 3)
```

## ex_with.py

```
Syntax error in '/Users/gvwilson/jorma/sdxpy/protocols/ex_with.py': invalid character '…' (U+2026) (<unknown>, line 1)
```

## mock_context.py

```

[module.ContextFake.__enter__]
  self                     fixed value             (line 11)

[module.ContextFake.__exit__]
  exc_traceback            fixed value             (line 17)
  exc_type                 fixed value             (line 17)
  exc_value                fixed value             (line 17)
  self                     fixed value             (line 17)

[module.ContextFake.__init__]
  func                     fixed value             (line 6)
  name                     fixed value             (line 6)
  self                     fixed value             (line 6)
  value                    fixed value             (line 6)

[module.check_no_lasting_effects]
  fake                     fixed value             (line 27)

[module.subber]
  a                        fixed value             (line 22)
  b                        fixed value             (line 22)
```

## mock_object.py

```

[module.Fake.__call__]
  args                     fixed value             (line 10)
  kwargs                   fixed value             (line 10)
  self                     fixed value             (line 10)

[module.Fake.__init__]
  func                     fixed value             (line 5)
  self                     fixed value             (line 5)
  value                    fixed value             (line 5)

[module.adder]
  a                        fixed value             (line 26)
  b                        fixed value             (line 26)

[module.fakeit]
  func                     fixed value             (line 18)
  name                     fixed value             (line 18)
  value                    fixed value             (line 18)
  fake                     fixed value             (line 20)

[module.test_fake_records_calls]
  fake                     fixed value             (line 41)
```

## mock_time.py

```

[module.elapsed]
  since                    fixed value             (line 3)
```

## naive_iterator.py

```

[module.NaiveIterator.__init__]
  self                     fixed value             (line 3)
  text                     fixed value             (line 3)

[module.NaiveIterator.__iter__]
  self                     fixed value             (line 6)

[module.NaiveIterator.__next__]
  self                     fixed value             (line 10)

[module.NaiveIterator._advance]
  self                     fixed value             (line 18)
```

## test_naive_iterator.py

```

[module.gather]
  buffer                   fixed value             (line 5)
  result                   gatherer                (line 6)
  char                     stepper                 (line 7)

[module.test_naive_buffer]
  buffer                   fixed value             (line 13)

[module.test_naive_buffer_empty_string]
  buffer                   fixed value             (line 19)

[module.test_naive_buffer_nested_loop]
  buffer                   fixed value             (line 26)
  result                   gatherer                (line 27)
  outer                    stepper                 (line 28)
  inner                    stepper                 (line 29)
```

## wrap_capture.py

```

[module]
  original                 unknown                 (line 11)

[module.logging]
  func                     fixed value             (line 4)

[module.logging._inner]
  value                    fixed value             (line 5)

[module.original]
  value                    fixed value             (line 1)
```

## wrap_infinite.py

```

[module]
  original                 fixed value             (line 9)

[module.logging]
  value                    fixed value             (line 4)

[module.original]
  value                    fixed value             (line 1)
```

## wrap_param.py

```

[module]
  original                 unknown                 (line 11)

[module.logging]
  func                     fixed value             (line 4)
  label                    fixed value             (line 4)

[module.logging._inner]
  value                    fixed value             (line 5)

[module.original]
  value                    fixed value             (line 1)
```

