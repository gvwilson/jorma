# Variable Role Analysis: glob

## glob_any.py

```

[module.Any.__init__]
  rest                     fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Any.match]
  self                     fixed value             (line 5)
  start                    fixed value             (line 5)
  text                     fixed value             (line 5)
  i                        stepper                 (line 8)
```

## glob_either.py

```

[module.Either.__init__]
  left                     fixed value             (line 2)
  rest                     fixed value             (line 2)
  right                    fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Either.match]
  self                     fixed value             (line 7)
  start                    fixed value             (line 7)
  text                     fixed value             (line 7)
```

## glob_lit.py

```

[module.Lit.__init__]
  chars                    fixed value             (line 2)
  rest                     fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Lit.match]
  self                     fixed value             (line 6)
  start                    fixed value             (line 6)
  text                     fixed value             (line 6)
  end                      fixed value             (line 7)
```

## glob_null.py

```

[module.Any.__init__]
  rest                     fixed value             (line 22)
  self                     fixed value             (line 22)

[module.Any._match]
  self                     fixed value             (line 25)
  start                    fixed value             (line 25)
  text                     fixed value             (line 25)
  i                        stepper                 (line 26)
  end                      most-recent holder      (line 27)

[module.Either.__init__]
  left                     fixed value             (line 35)
  rest                     fixed value             (line 35)
  right                    fixed value             (line 35)
  self                     fixed value             (line 35)

[module.Either._match]
  self                     fixed value             (line 40)
  start                    fixed value             (line 40)
  text                     fixed value             (line 40)
  pat                      stepper                 (line 41)
  end                      gatherer                (line 42)

[module.Lit.__init__]
  chars                    fixed value             (line 52)
  rest                     fixed value             (line 52)
  self                     fixed value             (line 52)

[module.Lit._match]
  self                     fixed value             (line 56)
  start                    fixed value             (line 56)
  text                     fixed value             (line 56)
  end                      fixed value             (line 57)

[module.Match.__init__]
  rest                     fixed value             (line 3)
  self                     fixed value             (line 3)

[module.Match.match]
  self                     fixed value             (line 6)
  text                     fixed value             (line 6)
  result                   fixed value             (line 7)

[module.Null.__init__]
  self                     fixed value             (line 13)

[module.Null._match]
  self                     fixed value             (line 16)
  start                    fixed value             (line 16)
  text                     fixed value             (line 16)
```

## test_glob_any.py

```
Warning: no variables found.
```

## test_glob_either.py

```
Warning: no variables found.
```

## test_glob_lit.py

```
Warning: no variables found.
```

## test_glob_problem.py

```
Warning: no variables found.
```

