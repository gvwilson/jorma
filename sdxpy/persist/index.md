# Variable Role Analysis: persist

## aliasing.py

```

[module.LoadAlias.__init__]
  reader                   fixed value             (line 57)
  self                     fixed value             (line 57)

[module.LoadAlias.load]
  self                     fixed value             (line 61)
  line                     fixed value             (line 62)
  fields                   fixed value             (line 65)
  ident                    fixed value             (line 67)
  key                      fixed value             (line 67)
  value                    fixed value             (line 67)
  method                   fixed value             (line 73)

[module.LoadAlias.load_bool]
  ident                    fixed value             (line 77)
  self                     fixed value             (line 77)
  value                    fixed value             (line 77)

[module.LoadAlias.load_dict]
  ident                    fixed value             (line 109)
  length                   fixed value             (line 109)
  self                     fixed value             (line 109)
  result                   fixed value             (line 110)
  _                        stepper                 (line 112)
  k                        most-recent holder      (line 113)
  v                        most-recent holder      (line 114)

[module.LoadAlias.load_float]
  ident                    fixed value             (line 81)
  self                     fixed value             (line 81)
  value                    fixed value             (line 81)

[module.LoadAlias.load_int]
  ident                    fixed value             (line 85)
  self                     fixed value             (line 85)
  value                    fixed value             (line 85)

[module.LoadAlias.load_list]
  ident                    fixed value             (line 94)
  length                   fixed value             (line 94)
  self                     fixed value             (line 94)
  result                   log                     (line 95)
  _                        stepper                 (line 97)

[module.LoadAlias.load_set]
  ident                    fixed value             (line 102)
  length                   fixed value             (line 102)
  self                     fixed value             (line 102)
  result                   container               (line 103)
  _                        stepper                 (line 105)

[module.LoadAlias.load_str]
  ident                    fixed value             (line 89)
  self                     fixed value             (line 89)
  value                    fixed value             (line 89)

[module.SaveAlias.__init__]
  self                     fixed value             (line 5)
  writer                   fixed value             (line 5)

[module.SaveAlias.save]
  self                     fixed value             (line 10)
  thing                    fixed value             (line 10)
  thing_id                 fixed value             (line 11)
  typename                 fixed value             (line 17)
  method                   fixed value             (line 18)

[module.SaveAlias.save_bool]
  self                     fixed value             (line 24)
  thing                    fixed value             (line 24)

[module.SaveAlias.save_dict]
  self                     fixed value             (line 49)
  thing                    fixed value             (line 49)
  key                      stepper                 (line 51)
  value                    stepper                 (line 51)

[module.SaveAlias.save_float]
  self                     fixed value             (line 27)
  thing                    fixed value             (line 27)

[module.SaveAlias.save_int]
  self                     fixed value             (line 30)
  thing                    fixed value             (line 30)

[module.SaveAlias.save_list]
  self                     fixed value             (line 33)
  thing                    fixed value             (line 33)
  item                     stepper                 (line 35)

[module.SaveAlias.save_set]
  self                     fixed value             (line 38)
  thing                    fixed value             (line 38)
  item                     stepper                 (line 40)

[module.SaveAlias.save_str]
  self                     fixed value             (line 43)
  thing                    fixed value             (line 43)
  lines                    fixed value             (line 44)
  line                     stepper                 (line 46)
```

## aliasing_wrong.py

```

[module.LoadAlias.__init__]
  reader                   fixed value             (line 59)
  self                     fixed value             (line 59)

[module.LoadAlias.load]
  self                     fixed value             (line 63)
  line                     fixed value             (line 64)
  fields                   fixed value             (line 66)
  ident                    fixed value             (line 68)
  key                      fixed value             (line 68)
  value                    fixed value             (line 68)
  method                   fixed value             (line 75)
  result                   fixed value             (line 77)

[module.SaveAlias.__init__]
  self                     fixed value             (line 6)
  writer                   fixed value             (line 6)

[module.SaveAlias.save]
  self                     fixed value             (line 10)
  thing                    fixed value             (line 10)
  thing_id                 fixed value             (line 11)
  typename                 fixed value             (line 17)
  method                   fixed value             (line 18)

[module.SaveAlias.save_bool]
  self                     fixed value             (line 23)
  thing                    fixed value             (line 23)

[module.SaveAlias.save_dict]
  self                     fixed value             (line 50)
  thing                    fixed value             (line 50)
  key                      stepper                 (line 52)
  value                    stepper                 (line 52)

[module.SaveAlias.save_float]
  self                     fixed value             (line 26)
  thing                    fixed value             (line 26)

[module.SaveAlias.save_int]
  self                     fixed value             (line 29)
  thing                    fixed value             (line 29)

[module.SaveAlias.save_list]
  self                     fixed value             (line 33)
  thing                    fixed value             (line 33)
  item                     stepper                 (line 35)

[module.SaveAlias.save_set]
  self                     fixed value             (line 39)
  thing                    fixed value             (line 39)
  item                     stepper                 (line 41)

[module.SaveAlias.save_str]
  self                     fixed value             (line 44)
  thing                    fixed value             (line 44)
  lines                    fixed value             (line 45)
  line                     stepper                 (line 47)
```

## attr.py

```

[module]
  ex                       fixed value             (line 8)
  method                   fixed value             (line 12)

[module.Example.__init__]
  label                    fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Example.get_size]
  self                     fixed value             (line 5)
```

## builtin.py

```

[module.load]
  reader                   fixed value             (line 48)
  line                     fixed value             (line 49)
  fields                   fixed value             (line 51)
  key                      fixed value             (line 53)
  value                    fixed value             (line 53)
  names                    fixed value             (line 56)
  lines                    fixed value             (line 68)
  result                   fixed value             (line 80)
  _                        stepper                 (line 81)
  k                        most-recent holder      (line 82)
  v                        most-recent holder      (line 83)

[module.save]
  thing                    fixed value             (line 2)
  writer                   fixed value             (line 2)
  lines                    fixed value             (line 15)
  line                     stepper                 (line 17)
  item                     stepper                 (line 24)
  key                      stepper                 (line 38)
  value                    stepper                 (line 38)
```

## ex_aliasing.py

```

[module]
  shared                   fixed value             (line 1)
  fixture                  fixed value             (line 2)
```

## ex_circular.py

```

[module]
  fixture                  log                     (line 1)
```

## objects.py

```

[module.LoadObjects.__init__]
  reader                   fixed value             (line 53)
  self                     fixed value             (line 53)

[module.LoadObjects.load]
  self                     fixed value             (line 56)
  line                     fixed value             (line 57)
  fields                   fixed value             (line 59)
  key                      fixed value             (line 61)
  value                    fixed value             (line 61)
  method                   fixed value             (line 62)

[module.LoadObjects.load_bool]
  self                     fixed value             (line 67)
  value                    fixed value             (line 67)
  names                    fixed value             (line 68)

[module.LoadObjects.load_dict]
  self                     fixed value             (line 93)
  value                    fixed value             (line 93)
  result                   fixed value             (line 94)
  _                        stepper                 (line 95)
  k                        most-recent holder      (line 96)
  v                        most-recent holder      (line 97)

[module.LoadObjects.load_float]
  self                     fixed value             (line 73)
  value                    fixed value             (line 73)

[module.LoadObjects.load_int]
  self                     fixed value             (line 77)
  value                    fixed value             (line 77)

[module.LoadObjects.load_list]
  self                     fixed value             (line 86)
  value                    fixed value             (line 86)

[module.LoadObjects.load_set]
  self                     fixed value             (line 90)
  value                    fixed value             (line 90)

[module.LoadObjects.load_str]
  self                     fixed value             (line 80)
  value                    fixed value             (line 80)

[module.SaveObjects.__init__]
  self                     fixed value             (line 3)
  writer                   fixed value             (line 3)

[module.SaveObjects._write]
  fields                   fixed value             (line 14)
  self                     fixed value             (line 14)

[module.SaveObjects.save]
  self                     fixed value             (line 6)
  thing                    fixed value             (line 6)
  typename                 fixed value             (line 7)
  method                   fixed value             (line 8)

[module.SaveObjects.save_bool]
  self                     fixed value             (line 17)
  thing                    fixed value             (line 17)

[module.SaveObjects.save_dict]
  self                     fixed value             (line 44)
  thing                    fixed value             (line 44)
  key                      stepper                 (line 46)
  value                    stepper                 (line 46)

[module.SaveObjects.save_float]
  self                     fixed value             (line 20)
  thing                    fixed value             (line 20)

[module.SaveObjects.save_int]
  self                     fixed value             (line 24)
  thing                    fixed value             (line 24)

[module.SaveObjects.save_list]
  self                     fixed value             (line 34)
  thing                    fixed value             (line 34)
  item                     stepper                 (line 36)

[module.SaveObjects.save_set]
  self                     fixed value             (line 39)
  thing                    fixed value             (line 39)
  item                     stepper                 (line 41)

[module.SaveObjects.save_str]
  self                     fixed value             (line 27)
  thing                    fixed value             (line 27)
  lines                    fixed value             (line 28)
  line                     stepper                 (line 30)
```

## save_aliasing.py

```

[module]
  word                     fixed value             (line 5)
  child                    fixed value             (line 6)
  parent                   log                     (line 7)
  saver                    fixed value             (line 11)
```

## save_builtin.py

```
Warning: no variables found.
```

## test_aliasing_wrong.py

```

[module.roundtrip]
  fixture                  fixed value             (line 8)
  writer                   fixed value             (line 9)
  reader                   fixed value             (line 11)

[module.test_aliasing_circular]
  fixture                  log                     (line 35)
  result                   fixed value             (line 37)

[module.test_aliasing_no_aliasing]
  fixture                  fixed value             (line 17)

[module.test_aliasing_shared_child]
  shared                   fixed value             (line 23)
  fixture                  fixed value             (line 24)
  result                   fixed value             (line 25)
```

## test_builtin.py

```

[module.test_load_bool_single]
  fixture                  fixed value             (line 102)

[module.test_load_dict_empty]
  fixture                  fixed value             (line 107)

[module.test_load_dict_flat]
  fixture                  fixed value             (line 112)

[module.test_load_float_single]
  fixture                  fixed value             (line 127)

[module.test_load_int_single]
  fixture                  fixed value             (line 132)

[module.test_load_list_flat]
  fixture                  fixed value             (line 137)

[module.test_load_set_flat]
  fixture                  fixed value             (line 172)

[module.test_load_str_single]
  fixture                  fixed value             (line 150)
  expected                 fixed value             (line 161)

[module.test_roundtrip]
  fixture                  fixed value             (line 186)
  output                   fixed value             (line 187)
  archive                  fixed value             (line 189)
  result                   fixed value             (line 190)

[module.test_save_bool_single]
  output                   fixed value             (line 8)

[module.test_save_dict_empty]
  output                   fixed value             (line 14)

[module.test_save_dict_flat]
  fixture                  fixed value             (line 20)
  expected                 fixed value             (line 21)
  output                   fixed value             (line 30)

[module.test_save_float_single]
  output                   fixed value             (line 36)

[module.test_save_int_single]
  output                   fixed value             (line 42)

[module.test_save_list_flat]
  fixture                  fixed value             (line 49)
  expected                 fixed value             (line 50)
  output                   fixed value             (line 55)

[module.test_save_set_flat]
  fixture                  fixed value             (line 80)
  first                    fixed value             (line 81)
  second                   fixed value             (line 88)
  output                   fixed value             (line 95)
  actual                   fixed value             (line 97)

[module.test_save_str_single]
  fixture                  fixed value             (line 62)
  expected                 fixed value             (line 67)
  output                   fixed value             (line 74)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- test_aliasing.py

