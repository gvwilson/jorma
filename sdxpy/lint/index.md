# Variable Role Analysis: lint

## dump_ast.py

```

[module]
  reader                   fixed value             (line 4)
  source                   fixed value             (line 5)
  tree                     fixed value             (line 7)
```

## ex_redundant.py

```

[module]
  x                        fixed value             (line 1)
```

## find_duplicate_keys.py

```

[module]
  reader                   fixed value             (line 22)
  source                   fixed value             (line 23)
  tree                     fixed value             (line 24)
  finder                   fixed value             (line 25)

[module.FindDuplicateKeys.report]
  node                     fixed value             (line 16)
  problems                 fixed value             (line 16)
  self                     fixed value             (line 16)
  msg                      fixed value             (line 18)

[module.FindDuplicateKeys.visit_Dict]
  node                     fixed value             (line 7)
  self                     fixed value             (line 7)
  seen                     fixed value             (line 8)
  key                      stepper                 (line 9)
  problems                 fixed value             (line 12)
```

## find_unused_variables.py

```

[module]
  Scope                    fixed value             (line 6)
  reader                   fixed value             (line 50)
  source                   fixed value             (line 51)
  tree                     fixed value             (line 52)
  finder                   fixed value             (line 53)

[module.FindUnusedVariables.__init__]
  self                     fixed value             (line 11)

[module.FindUnusedVariables.check]
  scope                    fixed value             (line 29)
  self                     fixed value             (line 29)
  unused                   fixed value             (line 30)
  names                    fixed value             (line 32)

[module.FindUnusedVariables.search]
  name                     fixed value             (line 23)
  node                     fixed value             (line 23)
  self                     fixed value             (line 23)
  scope                    fixed value             (line 26)

[module.FindUnusedVariables.visit_FunctionDef]
  node                     fixed value             (line 18)
  self                     fixed value             (line 18)

[module.FindUnusedVariables.visit_Module]
  node                     fixed value             (line 15)
  self                     fixed value             (line 15)

[module.FindUnusedVariables.visit_Name]
  node                     fixed value             (line 37)
  self                     fixed value             (line 37)
```

## function_keys.py

```

[module]
  actually_has_duplicate_keys fixed value             (line 4)
```

## has_duplicate_keys.py

```

[module]
  has_duplicates           fixed value             (line 1)
```

## has_unused_variables.py

```

[module]
  used                     fixed value             (line 1)
  distractor               fixed value             (line 2)
  not_used                 fixed value             (line 3)

[module.has_unused]
  param                    fixed value             (line 11)
  used                     fixed value             (line 12)
  not_used                 fixed value             (line 13)
  distractor               fixed value             (line 14)

[module.no_unused]
  param                    fixed value             (line 6)
  result                   fixed value             (line 7)
```

## simple.py

```

[module]
  result                   fixed value             (line 4)

[module.double]
  x                        fixed value             (line 1)
```

## walk_ast.py

```

[module]
  reader                   fixed value             (line 30)
  source                   fixed value             (line 31)
  tree                     fixed value             (line 32)
  collector                fixed value             (line 33)

[module.CollectNames.__init__]
  self                     fixed value             (line 7)

[module.CollectNames.add]
  name                     fixed value             (line 20)
  node                     fixed value             (line 20)
  self                     fixed value             (line 20)
  loc                      fixed value             (line 21)

[module.CollectNames.position]
  node                     fixed value             (line 25)
  self                     fixed value             (line 25)

[module.CollectNames.visit_Assign]
  node                     fixed value             (line 11)
  self                     container               (line 11)
  var                      stepper                 (line 12)

[module.CollectNames.visit_FunctionDef]
  node                     fixed value             (line 16)
  self                     container               (line 16)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- double.py
- dump_ast_double.py
- dump_ast_simple.py

