# Variable Role Analysis: build

## build_better.py

```

[module]
  reader                   fixed value             (line 68)
  config                   fixed value             (line 69)
  builder                  fixed value             (line 70)
  actions                  fixed value             (line 71)
  a                        stepper                 (line 72)

[module.BuildBetter._check]
  details                  fixed value             (line 30)
  known                    fixed value             (line 30)
  name                     fixed value             (line 30)
  self                     fixed value             (line 30)
  depends                  fixed value             (line 32)
  result                   fixed value             (line 36)

[module.BuildBetter._check_keys]
  details                  fixed value             (line 40)
  name                     fixed value             (line 40)
  self                     fixed value             (line 40)

[module.BuildBetter._configure]
  config                   fixed value             (line 25)
  self                     fixed value             (line 25)
  known                    fixed value             (line 26)

[module.BuildBetter._must]
  condition                fixed value             (line 19)
  message                  fixed value             (line 19)
  self                     fixed value             (line 19)

[module.BuildBetter._refresh]
  actions                  log                     (line 15)
  config                   fixed value             (line 15)
  node                     fixed value             (line 15)
  self                     fixed value             (line 15)

[module.BuildBetter._topo_sort]
  config                   fixed value             (line 48)
  self                     fixed value             (line 48)
  graph                    gatherer                (line 49)
  result                   log                     (line 50)
  available                most-recent holder      (line 52)

[module.BuildBetter.build]
  config                   unknown                 (line 7)
  self                     fixed value             (line 7)
  ordered                  fixed value             (line 9)
  actions                  fixed value             (line 10)
  node                     stepper                 (line 11)
```

## build_simple.py

```

[module]
  builder                  fixed value             (line 57)

[module.BuildBase._check]
  details                  fixed value             (line 30)
  known                    fixed value             (line 30)
  name                     fixed value             (line 30)
  self                     fixed value             (line 30)
  depends                  fixed value             (line 33)

[module.BuildBase._configure]
  config_file              fixed value             (line 19)
  self                     fixed value             (line 19)
  reader                   fixed value             (line 20)
  config                   fixed value             (line 21)
  known                    fixed value             (line 22)

[module.BuildBase._refresh]
  config                   fixed value             (line 13)
  node                     fixed value             (line 13)
  self                     fixed value             (line 13)

[module.BuildBase._topo_sort]
  config                   fixed value             (line 40)
  self                     fixed value             (line 40)
  graph                    gatherer                (line 41)
  result                   log                     (line 42)
  available                most-recent holder      (line 44)

[module.BuildBase.build]
  config_file              fixed value             (line 7)
  self                     fixed value             (line 7)
  config                   fixed value             (line 8)
  ordered                  fixed value             (line 9)
  node                     stepper                 (line 10)
```

## build_time.py

```

[module]
  reader                   fixed value             (line 27)
  config                   fixed value             (line 28)
  builder                  fixed value             (line 29)
  actions                  fixed value             (line 30)
  a                        stepper                 (line 31)

[module.BuildTime._check_keys]
  details                  fixed value             (line 9)
  name                     fixed value             (line 9)
  self                     fixed value             (line 9)

[module.BuildTime._needs_update]
  config                   fixed value             (line 18)
  node                     fixed value             (line 18)
  self                     fixed value             (line 18)

[module.BuildTime._refresh]
  actions                  log                     (line 13)
  config                   fixed value             (line 13)
  node                     fixed value             (line 13)
  self                     fixed value             (line 13)
```

## test_build_better.py

```

[module.test_circular]
  action_A                 fixed value             (line 16)
  action_B                 fixed value             (line 17)
  config                   fixed value             (line 18)

[module.test_diamond_dep]
  action_A                 fixed value             (line 52)
  action_B                 fixed value             (line 53)
  action_C                 fixed value             (line 54)
  action_D                 fixed value             (line 55)
  config                   fixed value             (line 56)

[module.test_linear_dep]
  action_A                 fixed value             (line 42)
  action_B                 fixed value             (line 43)
  config                   fixed value             (line 44)

[module.test_no_dep]
  action_A                 fixed value             (line 31)
  action_B                 fixed value             (line 32)
  config                   fixed value             (line 33)

[module.test_single]
  action_A                 fixed value             (line 9)
  config                   fixed value             (line 10)
```

## test_build_time.py

```

[module.test_circular]
  action_A                 fixed value             (line 15)
  action_B                 fixed value             (line 16)
  config                   fixed value             (line 17)

[module.test_diamond_dep]
  action_A                 fixed value             (line 60)
  action_B                 fixed value             (line 61)
  action_C                 fixed value             (line 62)
  action_D                 fixed value             (line 63)
  config                   fixed value             (line 64)

[module.test_linear_dep_needs_update]
  action_A                 fixed value             (line 39)
  action_B                 fixed value             (line 40)
  config                   fixed value             (line 41)

[module.test_linear_dep_no_need_update]
  action_A                 fixed value             (line 49)
  action_B                 fixed value             (line 50)
  config                   fixed value             (line 51)

[module.test_no_dep]
  action_A                 fixed value             (line 29)
  action_B                 fixed value             (line 30)
  config                   fixed value             (line 31)

[module.test_single]
  action_A                 fixed value             (line 9)
  config                   fixed value             (line 10)
```

