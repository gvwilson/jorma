# A Package Manager

## exhaustive.py

| Variable | Scope | Role |
|---|---|---|
| combination | module.compatible | fixed value |
| manifest | module.compatible | fixed value |
| package_i | module.compatible | stepper |
| version_i | module.compatible | stepper |
| lookup_i | module.compatible | most-recent holder |
| package_j | module.compatible | stepper |
| version_j | module.compatible | stepper |
| manifest | module.main | fixed value |
| possible | module.main | fixed value |
| allowed | module.main | fixed value |
| a | module.main | stepper |
| manifest | module.make_possibilities | fixed value |
| available | module.make_possibilities | log |
| package | module.make_possibilities | stepper |
| versions | module.make_possibilities | stepper |

## manual.py

| Variable | Scope | Role |
|---|---|---|
| accum | module._make_possible | log |
| current | module._make_possible | fixed value |
| remaining | module._make_possible | fixed value |
| head | module._make_possible | fixed value |
| tail | module._make_possible | fixed value |
| h | module._make_possible | stepper |
| combination | module.compatible | fixed value |
| manifest | module.compatible | fixed value |
| package_i | module.compatible | stepper |
| version_i | module.compatible | stepper |
| lookup_i | module.compatible | most-recent holder |
| package_j | module.compatible | stepper |
| version_j | module.compatible | stepper |
| manifest | module.main | fixed value |
| possible | module.main | fixed value |
| allowed | module.main | fixed value |
| a | module.main | stepper |
| manifest | module.make_possibilities | fixed value |
| available | module.make_possibilities | log |
| package | module.make_possibilities | stepper |
| versions | module.make_possibilities | stepper |
| accum | module.make_possibilities | fixed value |

## incremental.py

| Variable | Scope | Role |
|---|---|---|
| candidate | module.compatible | fixed value |
| manifest | module.compatible | fixed value |
| package_i | module.compatible | stepper |
| version_i | module.compatible | stepper |
| lookup_i | module.compatible | most-recent holder |
| package_j | module.compatible | stepper |
| version_j | module.compatible | stepper |
| accum | module.find | log |
| count | module.find | stepper |
| current | module.find | fixed value |
| manifest | module.find | fixed value |
| remaining | module.find | fixed value |
| head | module.find | fixed value |
| tail | module.find | fixed value |
| version | module.find | stepper |
| candidate | module.find | most-recent holder |
| manifest | module.main | fixed value |
| packages | module.main | organizer |
| accum | module.main | fixed value |
| count | module.main | fixed value |
| a | module.main | stepper |

## z3_setup.py

| Variable | Scope | Role |
|---|---|---|
| A | module | fixed value |
| B | module | fixed value |
| C | module | fixed value |

## z3_equal.py

| Variable | Scope | Role |
|---|---|---|
| A | module | fixed value |
| B | module | fixed value |
| C | module | fixed value |
| solver | module | container |
| result | module.report | fixed value |
| title | module.report | fixed value |
| model | module.report | fixed value |
| term | module.report | stepper |

## z3_part_equal.py

| Variable | Scope | Role |
|---|---|---|
| A | module | fixed value |
| B | module | fixed value |
| C | module | fixed value |
| solver | module | container |
| result | module.report | fixed value |
| title | module.report | fixed value |
| model | module.report | fixed value |
| term | module.report | stepper |

## z3_unequal.py

| Variable | Scope | Role |
|---|---|---|
| A | module | fixed value |
| B | module | fixed value |
| C | module | fixed value |
| solver | module | container |
| result | module.report | fixed value |
| title | module.report | fixed value |
| model | module.report | fixed value |
| term | module.report | stepper |

## z3_triple.py

| Variable | Scope | Role |
|---|---|---|
| A1 | module | fixed value |
| A2 | module | fixed value |
| A3 | module | fixed value |
| B1 | module | fixed value |
| B2 | module | fixed value |
| B3 | module | fixed value |
| C1 | module | fixed value |
| C2 | module | fixed value |
| solver | module | container |

## z3_complete.py

| Variable | Scope | Role |
|---|---|---|
| A1 | module | fixed value |
| A2 | module | fixed value |
| A3 | module | fixed value |
| B1 | module | fixed value |
| B2 | module | fixed value |
| B3 | module | fixed value |
| C1 | module | fixed value |
| C2 | module | fixed value |
| solver | module | container |
| everything | module | fixed value |
| model | module | most-recent holder |
| settings | module | most-recent holder |
| cond | module | most-recent holder |

