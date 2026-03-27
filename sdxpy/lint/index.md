# Variable Role Analysis: lint

## dump_ast.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | reader   | fixed value | line 4   |
| module | source   | fixed value | line 5   |
| module | tree     | fixed value | line 7   |

## ex_redundant.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | x        | fixed value | line 1   |

## find_duplicate_keys.py

| Scope                               | Variable | Role        | Location |
| :-----------------------------------| :--------| :-----------| :--------|
| module                              | reader   | fixed value | line 22  |
| module                              | source   | fixed value | line 23  |
| module                              | tree     | fixed value | line 24  |
| module                              | finder   | fixed value | line 25  |
| module.FindDuplicateKeys.report     | node     | fixed value | line 16  |
| module.FindDuplicateKeys.report     | problems | fixed value | line 16  |
| module.FindDuplicateKeys.report     | self     | fixed value | line 16  |
| module.FindDuplicateKeys.report     | msg      | fixed value | line 18  |
| module.FindDuplicateKeys.visit_Dict | node     | fixed value | line 7   |
| module.FindDuplicateKeys.visit_Dict | self     | fixed value | line 7   |
| module.FindDuplicateKeys.visit_Dict | seen     | fixed value | line 8   |
| module.FindDuplicateKeys.visit_Dict | key      | stepper     | line 9   |
| module.FindDuplicateKeys.visit_Dict | problems | fixed value | line 12  |

## find_unused_variables.py

| Scope                                        | Variable | Role        | Location |
| :--------------------------------------------| :--------| :-----------| :--------|
| module                                       | Scope    | fixed value | line 6   |
| module                                       | reader   | fixed value | line 50  |
| module                                       | source   | fixed value | line 51  |
| module                                       | tree     | fixed value | line 52  |
| module                                       | finder   | fixed value | line 53  |
| module.FindUnusedVariables.__init__          | self     | fixed value | line 11  |
| module.FindUnusedVariables.check             | scope    | fixed value | line 29  |
| module.FindUnusedVariables.check             | self     | fixed value | line 29  |
| module.FindUnusedVariables.check             | unused   | fixed value | line 30  |
| module.FindUnusedVariables.check             | names    | fixed value | line 32  |
| module.FindUnusedVariables.search            | name     | fixed value | line 23  |
| module.FindUnusedVariables.search            | node     | fixed value | line 23  |
| module.FindUnusedVariables.search            | self     | fixed value | line 23  |
| module.FindUnusedVariables.search            | scope    | fixed value | line 26  |
| module.FindUnusedVariables.visit_FunctionDef | node     | fixed value | line 18  |
| module.FindUnusedVariables.visit_FunctionDef | self     | fixed value | line 18  |
| module.FindUnusedVariables.visit_Module      | node     | fixed value | line 15  |
| module.FindUnusedVariables.visit_Module      | self     | fixed value | line 15  |
| module.FindUnusedVariables.visit_Name        | node     | fixed value | line 37  |
| module.FindUnusedVariables.visit_Name        | self     | fixed value | line 37  |

## function_keys.py

| Scope  | Variable                    | Role        | Location |
| :------| :---------------------------| :-----------| :--------|
| module | actually_has_duplicate_keys | fixed value | line 4   |

## has_duplicate_keys.py

| Scope  | Variable       | Role        | Location |
| :------| :--------------| :-----------| :--------|
| module | has_duplicates | fixed value | line 1   |

## has_unused_variables.py

| Scope             | Variable   | Role        | Location |
| :-----------------| :----------| :-----------| :--------|
| module            | used       | fixed value | line 1   |
| module            | distractor | fixed value | line 2   |
| module            | not_used   | fixed value | line 3   |
| module.has_unused | param      | fixed value | line 11  |
| module.has_unused | used       | fixed value | line 12  |
| module.has_unused | not_used   | fixed value | line 13  |
| module.has_unused | distractor | fixed value | line 14  |
| module.no_unused  | param      | fixed value | line 6   |
| module.no_unused  | result     | fixed value | line 7   |

## simple.py

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | result   | fixed value | line 4   |
| module.double | x        | fixed value | line 1   |

## walk_ast.py

| Scope                                 | Variable  | Role        | Location |
| :-------------------------------------| :---------| :-----------| :--------|
| module                                | reader    | fixed value | line 30  |
| module                                | source    | fixed value | line 31  |
| module                                | tree      | fixed value | line 32  |
| module                                | collector | fixed value | line 33  |
| module.CollectNames.__init__          | self      | fixed value | line 7   |
| module.CollectNames.add               | name      | fixed value | line 20  |
| module.CollectNames.add               | node      | fixed value | line 20  |
| module.CollectNames.add               | self      | fixed value | line 20  |
| module.CollectNames.add               | loc       | fixed value | line 21  |
| module.CollectNames.position          | node      | fixed value | line 25  |
| module.CollectNames.position          | self      | fixed value | line 25  |
| module.CollectNames.visit_Assign      | node      | fixed value | line 11  |
| module.CollectNames.visit_Assign      | self      | container   | line 11  |
| module.CollectNames.visit_Assign      | var       | stepper     | line 12  |
| module.CollectNames.visit_FunctionDef | node      | fixed value | line 16  |
| module.CollectNames.visit_FunctionDef | self      | container   | line 16  |

