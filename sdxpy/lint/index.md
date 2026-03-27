# lint

## double.py

### Static analysis

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | value    | fixed value | line 6   |
| module        | result   | fixed value | line 7   |
| module.double | x        | fixed value | line 1   |
| module.double | result   | fixed value | line 2   |

## ex_redundant.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | x        | fixed value | line 1   |

## function_keys.py

### Static analysis

| Scope  | Variable                    | Role        | Location |
| :------| :---------------------------| :-----------| :--------|
| module | actually_has_duplicate_keys | fixed value | line 5   |

## has_duplicate_keys.py

### Static analysis

| Scope  | Variable       | Role        | Location |
| :------| :--------------| :-----------| :--------|
| module | has_duplicates | fixed value | line 1   |

## has_unused_variables.py

### Static analysis

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

### Static analysis

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | result   | fixed value | line 5   |
| module.double | x        | fixed value | line 1   |

