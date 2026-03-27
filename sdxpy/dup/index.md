# Variable Role Analysis: dup

## brute_force_2.py

```

[module]
  duplicates               fixed value             (line 24)
  left                     stepper                 (line 25)
  right                    stepper                 (line 25)

[module.find_duplicates]
  filenames                fixed value             (line 11)
  matches                  log                     (line 12)
  i_left                   stepper                 (line 13)
  left                     most-recent holder      (line 14)
  i_right                  stepper                 (line 15)
  right                    most-recent holder      (line 16)

[module.same_bytes]
  left_name                fixed value             (line 4)
  right_name               fixed value             (line 4)
  left_bytes               fixed value             (line 5)
  right_bytes              fixed value             (line 6)
```

## dup.py

```

[module]
  groups                   fixed value             (line 16)
  filenames                stepper                 (line 17)

[module.find_groups]
  filenames                fixed value             (line 4)
  groups                   fixed value             (line 5)
  fn                       stepper                 (line 6)
  data                     most-recent holder      (line 7)
  hash_code                most-recent holder      (line 8)
```

## grouped.py

```

[module]
  groups                   fixed value             (line 37)
  filenames                stepper                 (line 38)
  duplicates               most-recent holder      (line 39)
  left                     stepper                 (line 40)
  right                    stepper                 (line 40)

[module.find_duplicates]
  filenames                fixed value             (line 11)
  matches                  log                     (line 12)
  i_left                   stepper                 (line 13)
  left                     most-recent holder      (line 14)
  i_right                  stepper                 (line 15)
  right                    most-recent holder      (line 16)

[module.find_groups]
  filenames                fixed value             (line 23)
  groups                   fixed value             (line 24)
  fn                       stepper                 (line 25)
  data                     most-recent holder      (line 26)
  hash_code                most-recent holder      (line 27)

[module.same_bytes]
  left_name                fixed value             (line 5)
  right_name               fixed value             (line 5)
  left_bytes               fixed value             (line 6)
  right_bytes              fixed value             (line 7)
```

## naive_hash.py

```

[module]
  example                  fixed value             (line 8)
  i                        stepper                 (line 9)
  substring                most-recent holder      (line 10)
  hash                     most-recent holder      (line 11)

[module.naive_hash]
  data                     fixed value             (line 2)
```

## using_sha256.py

```

[module]
  example                  fixed value             (line 5)
  i                        stepper                 (line 6)
  substring                most-recent holder      (line 7)
  hash                     most-recent holder      (line 8)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- brute_force_1.py

