# Variable Role Analysis: interp

## add_example.py

```
Warning: no variables found.
```

## ex_assign_expr.py

```
Syntax error in '/Users/gvwilson/jorma/sdxpy/interp/ex_assign_expr.py': invalid syntax (<unknown>, line 2)
```

## expr.py

```

[module.do]
  expr                     fixed value             (line 20)

[module.do_abs]
  args                     fixed value             (line 5)
  val                      fixed value             (line 7)

[module.do_add]
  args                     fixed value             (line 12)
  left                     fixed value             (line 14)
  right                    fixed value             (line 15)

[module.main]
  reader                   fixed value             (line 37)
  program                  fixed value             (line 38)
  result                   fixed value             (line 39)
```

## vars.py

```

[module.do]
  env                      fixed value             (line 43)
  expr                     fixed value             (line 43)

[module.do_abs]
  args                     fixed value             (line 5)
  env                      fixed value             (line 5)
  val                      fixed value             (line 7)

[module.do_add]
  args                     fixed value             (line 11)
  env                      fixed value             (line 11)
  left                     fixed value             (line 13)
  right                    fixed value             (line 14)

[module.do_get]
  args                     fixed value             (line 18)
  env                      fixed value             (line 18)

[module.do_seq]
  args                     fixed value             (line 26)
  env                      fixed value             (line 26)
  item                     stepper                 (line 28)
  result                   most-recent holder      (line 29)

[module.do_set]
  args                     fixed value             (line 34)
  env                      fixed value             (line 34)
  value                    fixed value             (line 37)

[module.main]
  reader                   fixed value             (line 62)
  program                  fixed value             (line 63)
  result                   fixed value             (line 64)
```

## vars_reflect.py

```

[module]
  OPS                      fixed value             (line 37)

[module.do]
  env                      fixed value             (line 45)
  expr                     fixed value             (line 45)
  func                     fixed value             (line 53)

[module.do_abs]
  args                     fixed value             (line 6)
  env                      fixed value             (line 6)
  val                      fixed value             (line 8)

[module.do_add]
  args                     fixed value             (line 11)
  env                      fixed value             (line 11)
  left                     fixed value             (line 13)
  right                    fixed value             (line 14)

[module.do_get]
  args                     fixed value             (line 17)
  env                      fixed value             (line 17)

[module.do_seq]
  args                     fixed value             (line 23)
  env                      fixed value             (line 23)
  item                     stepper                 (line 25)
  result                   most-recent holder      (line 26)

[module.do_set]
  args                     fixed value             (line 29)
  env                      fixed value             (line 29)
  value                    fixed value             (line 32)

[module.main]
  reader                   fixed value             (line 59)
  program                  fixed value             (line 60)
  result                   fixed value             (line 61)
```

## vars_table.py

```

[module]
  OPS                      fixed value             (line 40)

[module.do]
  env                      fixed value             (line 50)
  expr                     fixed value             (line 50)
  func                     fixed value             (line 58)

[module.do_abs]
  args                     fixed value             (line 4)
  env                      fixed value             (line 4)
  val                      fixed value             (line 7)

[module.do_add]
  args                     fixed value             (line 10)
  env                      fixed value             (line 10)
  left                     fixed value             (line 13)
  right                    fixed value             (line 14)

[module.do_get]
  args                     fixed value             (line 17)
  env                      fixed value             (line 17)

[module.do_seq]
  args                     fixed value             (line 24)
  env                      fixed value             (line 24)
  item                     stepper                 (line 27)
  result                   most-recent holder      (line 28)

[module.do_set]
  args                     fixed value             (line 31)
  env                      fixed value             (line 31)
  value                    fixed value             (line 35)

[module.main]
  reader                   fixed value             (line 64)
  program                  fixed value             (line 65)
  result                   fixed value             (line 66)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- doubling.py
- repeat_zero.py

