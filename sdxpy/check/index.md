# Variable Role Analysis: check

## attrs.py

```

[module]
  text                     fixed value             (line 10)
  doc                      fixed value             (line 20)

[module.display]
  node                     fixed value             (line 2)
  child                    stepper                 (line 5)
```

## catalog.py

```

[module]
  reader                   fixed value             (line 20)
  text                     fixed value             (line 21)
  doc                      fixed value             (line 22)
  cataloger                fixed value             (line 24)
  result                   fixed value             (line 26)
  contents                 stepper                 (line 28)
  tag                      stepper                 (line 28)

[module.Catalog.__init__]
  self                     fixed value             (line 7)

[module.Catalog._tag_enter]
  node                     fixed value             (line 11)
  self                     fixed value             (line 11)
  child                    stepper                 (line 14)
```

## check.py

```

[module]
  manifest                 fixed value             (line 31)
  reader                   fixed value             (line 32)
  text                     fixed value             (line 33)
  doc                      fixed value             (line 34)
  checker                  fixed value             (line 36)
  key                      stepper                 (line 38)
  value                    stepper                 (line 38)

[module.Check.__init__]
  manifest                 fixed value             (line 9)
  self                     fixed value             (line 9)

[module.Check._tag_enter]
  node                     fixed value             (line 13)
  self                     fixed value             (line 13)
  actual                   fixed value             (line 14)
  errors                   unknown                 (line 16)

[module.read_manifest]
  filename                 fixed value             (line 24)
  reader                   fixed value             (line 25)
  result                   fixed value             (line 26)
  key                      stepper                 (line 27)
```

## contains.py

```

[module]
  reader                   fixed value             (line 19)
  text                     fixed value             (line 20)
  doc                      fixed value             (line 21)
  catalog                  fixed value             (line 22)
  contents                 stepper                 (line 23)
  tag                      stepper                 (line 23)

[module.recurse]
  catalog                  fixed value             (line 5)
  node                     fixed value             (line 5)
  child                    stepper                 (line 11)
```

## ex_flatten.py

```

[module]
  node                     stepper                 (line 1)
```

## parse.py

```

[module]
  text                     fixed value             (line 13)
  doc                      fixed value             (line 24)

[module.display]
  node                     fixed value             (line 2)
  child                    stepper                 (line 8)
```

## visitor.py

```

[module.Visitor._tag_enter]
  node                     fixed value             (line 14)
  self                     fixed value             (line 14)

[module.Visitor._tag_exit]
  node                     fixed value             (line 16)
  self                     fixed value             (line 16)

[module.Visitor._text]
  node                     fixed value             (line 18)
  self                     fixed value             (line 18)

[module.Visitor.visit]
  node                     fixed value             (line 5)
  self                     fixed value             (line 5)
  child                    stepper                 (line 10)
```

