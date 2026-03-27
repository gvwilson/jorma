# A Code Linter

## simple.py

| Variable | Scope | Role |
|---|---|---|
| result | module | fixed value |
| x | module.double | fixed value |

## dump_ast.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| source | module | fixed value |
| tree | module | fixed value |

## walk_ast.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| source | module | fixed value |
| tree | module | fixed value |
| collector | module | fixed value |
| self | module.CollectNames.__init__ | fixed value |
| name | module.CollectNames.add | fixed value |
| node | module.CollectNames.add | fixed value |
| self | module.CollectNames.add | fixed value |
| loc | module.CollectNames.add | fixed value |
| node | module.CollectNames.position | fixed value |
| self | module.CollectNames.position | fixed value |
| node | module.CollectNames.visit_Assign | fixed value |
| self | module.CollectNames.visit_Assign | container |
| var | module.CollectNames.visit_Assign | stepper |
| node | module.CollectNames.visit_FunctionDef | fixed value |
| self | module.CollectNames.visit_FunctionDef | container |

## has_duplicate_keys.py

| Variable | Scope | Role |
|---|---|---|
| has_duplicates | module | fixed value |

## find_duplicate_keys.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| source | module | fixed value |
| tree | module | fixed value |
| finder | module | fixed value |
| node | module.FindDuplicateKeys.report | fixed value |
| problems | module.FindDuplicateKeys.report | fixed value |
| self | module.FindDuplicateKeys.report | fixed value |
| msg | module.FindDuplicateKeys.report | fixed value |
| node | module.FindDuplicateKeys.visit_Dict | fixed value |
| self | module.FindDuplicateKeys.visit_Dict | fixed value |
| seen | module.FindDuplicateKeys.visit_Dict | fixed value |
| key | module.FindDuplicateKeys.visit_Dict | stepper |
| problems | module.FindDuplicateKeys.visit_Dict | fixed value |

## function_keys.py

*No variables identified by jorma.*

## find_unused_variables.py

| Variable | Scope | Role |
|---|---|---|
| Scope | module | fixed value |
| reader | module | fixed value |
| source | module | fixed value |
| tree | module | fixed value |
| finder | module | fixed value |
| self | module.FindUnusedVariables.__init__ | fixed value |
| scope | module.FindUnusedVariables.check | fixed value |
| self | module.FindUnusedVariables.check | fixed value |
| unused | module.FindUnusedVariables.check | fixed value |
| names | module.FindUnusedVariables.check | fixed value |
| name | module.FindUnusedVariables.search | fixed value |
| node | module.FindUnusedVariables.search | fixed value |
| self | module.FindUnusedVariables.search | fixed value |
| scope | module.FindUnusedVariables.search | fixed value |
| node | module.FindUnusedVariables.visit_FunctionDef | fixed value |
| self | module.FindUnusedVariables.visit_FunctionDef | fixed value |
| node | module.FindUnusedVariables.visit_Module | fixed value |
| self | module.FindUnusedVariables.visit_Module | fixed value |
| node | module.FindUnusedVariables.visit_Name | fixed value |
| self | module.FindUnusedVariables.visit_Name | fixed value |

## has_unused_variables.py

| Variable | Scope | Role |
|---|---|---|
| used | module | fixed value |
| distractor | module | fixed value |
| not_used | module | fixed value |
| param | module.has_unused | fixed value |
| used | module.has_unused | fixed value |
| not_used | module.has_unused | fixed value |
| distractor | module.has_unused | fixed value |
| param | module.no_unused | fixed value |
| result | module.no_unused | fixed value |

## ex_redundant.py

| Variable | Scope | Role |
|---|---|---|
| x | module | fixed value |

