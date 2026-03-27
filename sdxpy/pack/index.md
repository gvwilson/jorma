# Variable Role Analysis: pack

## exhaustive.py

```

[module.compatible]
  combination              fixed value             (line 25)
  manifest                 fixed value             (line 25)
  package_i                stepper                 (line 26)
  version_i                stepper                 (line 26)
  lookup_i                 most-recent holder      (line 27)
  package_j                stepper                 (line 28)
  version_j                stepper                 (line 28)

[module.main]
  manifest                 fixed value             (line 7)
  possible                 fixed value             (line 8)
  allowed                  fixed value             (line 10)
  a                        stepper                 (line 12)

[module.make_possibilities]
  manifest                 fixed value             (line 17)
  available                log                     (line 18)
  package                  stepper                 (line 19)
  versions                 stepper                 (line 19)
```

## incremental.py

```

[module.compatible]
  candidate                fixed value             (line 35)
  manifest                 fixed value             (line 35)
  package_i                stepper                 (line 36)
  version_i                stepper                 (line 36)
  lookup_i                 most-recent holder      (line 37)
  package_j                stepper                 (line 38)
  version_j                stepper                 (line 38)

[module.find]
  accum                    log                     (line 20)
  count                    stepper                 (line 20)
  current                  fixed value             (line 20)
  manifest                 fixed value             (line 20)
  remaining                fixed value             (line 20)
  head                     fixed value             (line 25)
  tail                     fixed value             (line 25)
  version                  stepper                 (line 26)
  candidate                most-recent holder      (line 27)

[module.main]
  manifest                 fixed value             (line 6)
  packages                 organizer               (line 7)
  accum                    fixed value             (line 11)
  count                    fixed value             (line 12)
  a                        stepper                 (line 15)
```

## manual.py

```

[module._make_possible]
  accum                    log                     (line 25)
  current                  fixed value             (line 25)
  remaining                fixed value             (line 25)
  head                     fixed value             (line 29)
  tail                     fixed value             (line 29)
  h                        stepper                 (line 30)

[module.compatible]
  combination              fixed value             (line 34)
  manifest                 fixed value             (line 34)
  package_i                stepper                 (line 35)
  version_i                stepper                 (line 35)
  lookup_i                 most-recent holder      (line 36)
  package_j                stepper                 (line 37)
  version_j                stepper                 (line 37)

[module.main]
  manifest                 fixed value             (line 5)
  possible                 fixed value             (line 6)
  allowed                  fixed value             (line 8)
  a                        stepper                 (line 10)

[module.make_possibilities]
  manifest                 fixed value             (line 14)
  available                log                     (line 15)
  package                  stepper                 (line 16)
  versions                 stepper                 (line 16)
  accum                    fixed value             (line 19)
```

## z3_complete.py

```

[module]
  A1                       fixed value             (line 3)
  A2                       fixed value             (line 4)
  A3                       fixed value             (line 5)
  B1                       fixed value             (line 7)
  B2                       fixed value             (line 8)
  B3                       fixed value             (line 9)
  C1                       fixed value             (line 11)
  C2                       fixed value             (line 12)
  solver                   container               (line 14)
  everything               fixed value             (line 37)
  model                    most-recent holder      (line 39)
  settings                 most-recent holder      (line 41)
  cond                     most-recent holder      (line 42)
```

## z3_equal.py

```

[module]
  A                        fixed value             (line 6)
  B                        fixed value             (line 7)
  C                        fixed value             (line 8)
  solver                   container               (line 21)

[module.report]
  result                   fixed value             (line 12)
  title                    fixed value             (line 12)
  model                    fixed value             (line 15)
  term                     stepper                 (line 16)
```

## z3_part_equal.py

```

[module]
  A                        fixed value             (line 10)
  B                        fixed value             (line 11)
  C                        fixed value             (line 12)
  solver                   container               (line 15)

[module.report]
  result                   fixed value             (line 3)
  title                    fixed value             (line 3)
  model                    fixed value             (line 6)
  term                     stepper                 (line 7)
```

## z3_setup.py

```

[module]
  A                        fixed value             (line 3)
  B                        fixed value             (line 4)
  C                        fixed value             (line 5)
```

## z3_triple.py

```

[module]
  A1                       fixed value             (line 4)
  A2                       fixed value             (line 5)
  A3                       fixed value             (line 6)
  B1                       fixed value             (line 8)
  B2                       fixed value             (line 9)
  B3                       fixed value             (line 10)
  C1                       fixed value             (line 12)
  C2                       fixed value             (line 13)
  solver                   container               (line 17)
```

## z3_unequal.py

```

[module]
  A                        fixed value             (line 10)
  B                        fixed value             (line 11)
  C                        fixed value             (line 12)
  solver                   container               (line 15)

[module.report]
  result                   fixed value             (line 3)
  title                    fixed value             (line 3)
  model                    fixed value             (line 6)
  term                     stepper                 (line 7)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- incremental_reverse.py

