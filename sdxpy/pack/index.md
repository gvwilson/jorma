# Variable Role Analysis: pack

## exhaustive.py

| Scope                     | Variable    | Role               | Location |
| :-------------------------| :-----------| :------------------| :--------|
| module.compatible         | combination | fixed value        | line 25  |
| module.compatible         | manifest    | fixed value        | line 25  |
| module.compatible         | package_i   | stepper            | line 26  |
| module.compatible         | version_i   | stepper            | line 26  |
| module.compatible         | lookup_i    | most-recent holder | line 27  |
| module.compatible         | package_j   | stepper            | line 28  |
| module.compatible         | version_j   | stepper            | line 28  |
| module.main               | manifest    | fixed value        | line 7   |
| module.main               | possible    | fixed value        | line 8   |
| module.main               | allowed     | fixed value        | line 10  |
| module.main               | a           | stepper            | line 12  |
| module.make_possibilities | manifest    | fixed value        | line 17  |
| module.make_possibilities | available   | log                | line 18  |
| module.make_possibilities | package     | stepper            | line 19  |
| module.make_possibilities | versions    | stepper            | line 19  |

## incremental.py

| Scope             | Variable  | Role               | Location |
| :-----------------| :---------| :------------------| :--------|
| module.compatible | candidate | fixed value        | line 35  |
| module.compatible | manifest  | fixed value        | line 35  |
| module.compatible | package_i | stepper            | line 36  |
| module.compatible | version_i | stepper            | line 36  |
| module.compatible | lookup_i  | most-recent holder | line 37  |
| module.compatible | package_j | stepper            | line 38  |
| module.compatible | version_j | stepper            | line 38  |
| module.find       | accum     | log                | line 20  |
| module.find       | count     | stepper            | line 20  |
| module.find       | current   | fixed value        | line 20  |
| module.find       | manifest  | fixed value        | line 20  |
| module.find       | remaining | fixed value        | line 20  |
| module.find       | head      | fixed value        | line 25  |
| module.find       | tail      | fixed value        | line 25  |
| module.find       | version   | stepper            | line 26  |
| module.find       | candidate | most-recent holder | line 27  |
| module.main       | manifest  | fixed value        | line 6   |
| module.main       | packages  | organizer          | line 7   |
| module.main       | accum     | fixed value        | line 11  |
| module.main       | count     | fixed value        | line 12  |
| module.main       | a         | stepper            | line 15  |

## manual.py

| Scope                     | Variable    | Role               | Location |
| :-------------------------| :-----------| :------------------| :--------|
| module._make_possible     | accum       | log                | line 25  |
| module._make_possible     | current     | fixed value        | line 25  |
| module._make_possible     | remaining   | fixed value        | line 25  |
| module._make_possible     | head        | fixed value        | line 29  |
| module._make_possible     | tail        | fixed value        | line 29  |
| module._make_possible     | h           | stepper            | line 30  |
| module.compatible         | combination | fixed value        | line 34  |
| module.compatible         | manifest    | fixed value        | line 34  |
| module.compatible         | package_i   | stepper            | line 35  |
| module.compatible         | version_i   | stepper            | line 35  |
| module.compatible         | lookup_i    | most-recent holder | line 36  |
| module.compatible         | package_j   | stepper            | line 37  |
| module.compatible         | version_j   | stepper            | line 37  |
| module.main               | manifest    | fixed value        | line 5   |
| module.main               | possible    | fixed value        | line 6   |
| module.main               | allowed     | fixed value        | line 8   |
| module.main               | a           | stepper            | line 10  |
| module.make_possibilities | manifest    | fixed value        | line 14  |
| module.make_possibilities | available   | log                | line 15  |
| module.make_possibilities | package     | stepper            | line 16  |
| module.make_possibilities | versions    | stepper            | line 16  |
| module.make_possibilities | accum       | fixed value        | line 19  |

## z3_complete.py

| Scope  | Variable   | Role               | Location |
| :------| :----------| :------------------| :--------|
| module | A1         | fixed value        | line 3   |
| module | A2         | fixed value        | line 4   |
| module | A3         | fixed value        | line 5   |
| module | B1         | fixed value        | line 7   |
| module | B2         | fixed value        | line 8   |
| module | B3         | fixed value        | line 9   |
| module | C1         | fixed value        | line 11  |
| module | C2         | fixed value        | line 12  |
| module | solver     | container          | line 14  |
| module | everything | fixed value        | line 37  |
| module | model      | most-recent holder | line 39  |
| module | settings   | most-recent holder | line 41  |
| module | cond       | most-recent holder | line 42  |

## z3_equal.py

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | A        | fixed value | line 6   |
| module        | B        | fixed value | line 7   |
| module        | C        | fixed value | line 8   |
| module        | solver   | container   | line 21  |
| module.report | result   | fixed value | line 12  |
| module.report | title    | fixed value | line 12  |
| module.report | model    | fixed value | line 15  |
| module.report | term     | stepper     | line 16  |

## z3_part_equal.py

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | A        | fixed value | line 10  |
| module        | B        | fixed value | line 11  |
| module        | C        | fixed value | line 12  |
| module        | solver   | container   | line 15  |
| module.report | result   | fixed value | line 3   |
| module.report | title    | fixed value | line 3   |
| module.report | model    | fixed value | line 6   |
| module.report | term     | stepper     | line 7   |

## z3_setup.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | A        | fixed value | line 3   |
| module | B        | fixed value | line 4   |
| module | C        | fixed value | line 5   |

## z3_triple.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | A1       | fixed value | line 4   |
| module | A2       | fixed value | line 5   |
| module | A3       | fixed value | line 6   |
| module | B1       | fixed value | line 8   |
| module | B2       | fixed value | line 9   |
| module | B3       | fixed value | line 10  |
| module | C1       | fixed value | line 12  |
| module | C2       | fixed value | line 13  |
| module | solver   | container   | line 17  |

## z3_unequal.py

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module        | A        | fixed value | line 10  |
| module        | B        | fixed value | line 11  |
| module        | C        | fixed value | line 12  |
| module        | solver   | container   | line 15  |
| module.report | result   | fixed value | line 3   |
| module.report | title    | fixed value | line 3   |
| module.report | model    | fixed value | line 6   |
| module.report | term     | stepper     | line 7   |

