# Variable Role Analysis: perf

## df_base.py

```

[module.DataFrame.cols]
  self                     fixed value             (line 8)

[module.DataFrame.eq]
  other                    fixed value             (line 11)
  self                     fixed value             (line 11)

[module.DataFrame.filter]
  func                     fixed value             (line 20)
  self                     fixed value             (line 20)

[module.DataFrame.get]
  col                      fixed value             (line 14)
  row                      fixed value             (line 14)
  self                     fixed value             (line 14)

[module.DataFrame.ncol]
  self                     fixed value             (line 2)

[module.DataFrame.nrow]
  self                     fixed value             (line 5)

[module.DataFrame.select]
  names                    fixed value             (line 17)
  self                     fixed value             (line 17)
```

## df_col.py

```

[module.DfCol.__init__]
  kwargs                   fixed value             (line 6)
  self                     fixed value             (line 6)
  k                        stepper                 (line 9)

[module.DfCol.__str__]
  self                     fixed value             (line 60)

[module.DfCol.cols]
  self                     fixed value             (line 22)

[module.DfCol.eq]
  other                    fixed value             (line 32)
  self                     fixed value             (line 32)
  n                        stepper                 (line 34)
  i                        stepper                 (line 37)

[module.DfCol.filter]
  func                     fixed value             (line 50)
  self                     fixed value             (line 50)
  result                   fixed value             (line 51)
  i                        stepper                 (line 52)
  args                     most-recent holder      (line 53)
  n                        stepper                 (line 55)

[module.DfCol.get]
  col                      fixed value             (line 25)
  row                      fixed value             (line 25)
  self                     fixed value             (line 25)

[module.DfCol.ncol]
  self                     fixed value             (line 15)

[module.DfCol.nrow]
  self                     fixed value             (line 18)
  n                        fixed value             (line 19)

[module.DfCol.select]
  names                    fixed value             (line 44)
  self                     fixed value             (line 44)
```

## df_row.py

```

[module.DfRow.__init__]
  rows                     fixed value             (line 6)
  self                     fixed value             (line 6)

[module.DfRow.__str__]
  self                     fixed value             (line 53)

[module.DfRow.cols]
  self                     fixed value             (line 19)

[module.DfRow.eq]
  other                    fixed value             (line 29)
  self                     fixed value             (line 29)
  i                        stepper                 (line 31)
  row                      stepper                 (line 31)
  key                      stepper                 (line 32)

[module.DfRow.filter]
  func                     fixed value             (line 48)
  self                     fixed value             (line 48)
  result                   fixed value             (line 49)

[module.DfRow.get]
  col                      fixed value             (line 22)
  row                      fixed value             (line 22)
  self                     fixed value             (line 22)

[module.DfRow.ncol]
  self                     fixed value             (line 13)

[module.DfRow.nrow]
  self                     fixed value             (line 16)

[module.DfRow.select]
  names                    fixed value             (line 41)
  self                     fixed value             (line 41)
  rows                     fixed value             (line 43)
```

## ex_map_2.py

```
Warning: no variables found.
```

## test_df_col.py

```

[module.test_construct_with_single_value]
  df                       fixed value             (line 4)

[module.test_construct_with_two_pairs]
  df                       fixed value             (line 9)

[module.test_equality]
  left                     fixed value             (line 23)
  right                    fixed value             (line 24)

[module.test_filter]
  df                       fixed value             (line 42)

[module.test_filter.odd]
  a                        fixed value             (line 39)
  b                        fixed value             (line 39)

[module.test_inequality]
  left                     fixed value             (line 28)

[module.test_select]
  df                       fixed value             (line 33)
  selected                 fixed value             (line 34)
```

## test_df_row.py

```

[module.test_construct_with_single_value]
  df                       fixed value             (line 12)

[module.test_construct_with_two_pairs]
  df                       fixed value             (line 17)

[module.test_equality]
  left                     fixed value             (line 33)
  right                    fixed value             (line 34)

[module.test_filter]
  df                       fixed value             (line 51)

[module.test_filter.odd]
  a                        fixed value             (line 48)
  b                        fixed value             (line 48)

[module.test_inequality]
  repeated                 fixed value             (line 39)

[module.test_ncol]
  df                       fixed value             (line 29)

[module.test_nrow]
  df                       fixed value             (line 25)

[module.test_select]
  selected                 fixed value             (line 43)
```

## timing.py

```

[module]
  RANGE                    fixed value             (line 9)
  FILTER                   fixed value             (line 28)
  SELECT                   fixed value             (line 39)
  silent                   fixed value             (line 82)
  spec                     fixed value             (line 83)
  sizes                    fixed value             (line 87)
  result                   fixed value             (line 88)

[module.make_col]
  ncol                     fixed value             (line 11)
  nrow                     fixed value             (line 11)
  fill                     fixed value             (line 14)

[module.make_col._col]
  n                        fixed value             (line 12)
  start                    fixed value             (line 12)

[module.make_row]
  ncol                     fixed value             (line 17)
  nrow                     fixed value             (line 17)
  labels                   fixed value             (line 18)
  fill                     fixed value             (line 23)

[module.make_row._row]
  r                        fixed value             (line 19)

[module.report]
  result                   fixed value             (line 71)
  writer                   fixed value             (line 72)
  row                      stepper                 (line 76)

[module.setup]
  spec                     fixed value             (line 66)
  sizes                    fixed value             (line 67)

[module.sweep]
  sizes                    fixed value             (line 50)
  result                   log                     (line 51)
  ncol                     stepper                 (line 52)
  nrow                     stepper                 (line 52)
  df_col                   most-recent holder      (line 53)
  df_row                   most-recent holder      (line 54)
  times                    most-recent holder      (line 55)

[module.time_filter]
  df                       fixed value             (line 30)
  start                    fixed value             (line 33)

[module.time_filter.f]
  args                     fixed value             (line 31)
  label_0                  fixed value             (line 31)

[module.time_select]
  df                       fixed value             (line 41)
  indices                  fixed value             (line 42)
  labels                   fixed value             (line 43)
  start                    fixed value             (line 44)
```

## util.py

```

[module.all_eq]
  values                   fixed value             (line 2)

[module.dict_match]
  d                        fixed value             (line 7)
  prototype                fixed value             (line 7)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- analysis.py
- make.py

