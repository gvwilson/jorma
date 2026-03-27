# Variable Role Analysis: func

## closure.py

```

[module]
  has_secret               fixed value             (line 6)

[module.make_hidden]
  thing                    fixed value             (line 1)
```

## counter_fail.py

```

[module]
  c                        fixed value             (line 8)
  i                        stepper                 (line 9)

[module.make_counter]
  value                    fixed value             (line 2)

[module.make_counter._inner]
  value                    unknown                 (line 4)
```

## counter_succeed.py

```

[module]
  c                        fixed value             (line 8)
  i                        stepper                 (line 9)

[module.make_counter]
  value                    fixed value             (line 2)
```

## ex_dict_zip.py

```
Warning: no variables found.
```

## example_def.py

```

[module]
  double                   fixed value             (line 15)

[module.same]
  num                      fixed value             (line 2)
```

## func.py

```

[module]
  OPERATIONS               fixed value             (line 100)

[module.do]
  env                      fixed value             (line 106)
  instruction              fixed value             (line 106)
  args                     fixed value             (line 109)
  op                       fixed value             (line 109)

[module.do_add]
  args                     fixed value             (line 4)
  env                      fixed value             (line 4)
  left                     fixed value             (line 6)
  right                    fixed value             (line 7)

[module.do_call]
  args                     fixed value             (line 11)
  env                      container               (line 11)
  name                     fixed value             (line 14)
  values                   fixed value             (line 15)
  func                     fixed value             (line 18)
  body                     fixed value             (line 20)
  params                   fixed value             (line 20)
  result                   fixed value             (line 25)

[module.do_comment]
  args                     fixed value             (line 32)
  env                      fixed value             (line 32)

[module.do_func]
  args                     fixed value             (line 36)
  env                      fixed value             (line 36)
  params                   fixed value             (line 38)
  body                     fixed value             (line 39)

[module.do_get]
  args                     fixed value             (line 43)
  env                      fixed value             (line 43)

[module.do_gt]
  args                     fixed value             (line 47)
  env                      fixed value             (line 47)

[module.do_if]
  args                     fixed value             (line 51)
  env                      fixed value             (line 51)
  cond                     fixed value             (line 53)
  choice                   fixed value             (line 54)

[module.do_leq]
  args                     fixed value             (line 57)
  env                      fixed value             (line 57)

[module.do_neg]
  args                     fixed value             (line 61)
  env                      fixed value             (line 61)

[module.do_not]
  args                     fixed value             (line 65)
  env                      fixed value             (line 65)

[module.do_or]
  args                     fixed value             (line 69)
  env                      fixed value             (line 69)
  temp                     fixed value             (line 71)

[module.do_print]
  args                     unknown                 (line 75)
  env                      fixed value             (line 75)

[module.do_repeat]
  args                     fixed value             (line 80)
  env                      fixed value             (line 80)
  count                    fixed value             (line 82)
  i                        stepper                 (line 83)
  result                   most-recent holder      (line 84)

[module.do_seq]
  args                     fixed value             (line 87)
  env                      fixed value             (line 87)
  a                        stepper                 (line 88)
  result                   most-recent holder      (line 89)

[module.do_set]
  args                     fixed value             (line 92)
  env                      fixed value             (line 92)
  name                     fixed value             (line 94)
  value                    fixed value             (line 95)

[module.env_get]
  env                      fixed value             (line 113)
  name                     fixed value             (line 113)
  e                        stepper                 (line 115)

[module.env_set]
  env                      fixed value             (line 120)
  name                     fixed value             (line 120)
  value                    fixed value             (line 120)
  e                        stepper                 (line 122)

[module.main]
  reader                   fixed value             (line 130)
  program                  fixed value             (line 131)
  result                   fixed value             (line 132)
```

## inner.py

```

[module.outer]
  value                    fixed value             (line 1)
  i                        stepper                 (line 6)

[module.outer.inner]
  current                  fixed value             (line 2)
```

## oop.py

```

[module]
  object                   fixed value             (line 12)

[module.make_object]
  initial_value            fixed value             (line 1)
  private                  fixed value             (line 2)

[module.make_object.setter]
  new_value                fixed value             (line 7)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- adder.py
- closure_list.py
- dynamic.py

