# Variable Role Analysis: test

## callable.py

Warning: no variables found.

## ex_loop_globals_2.py

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | name     | stepper | line 1   |

## find_test_funcs.py

| Scope             | Variable | Role        | Location |
| :-----------------| :--------| :-----------| :--------|
| module.find_tests | prefix   | fixed value | line 20  |
| module.find_tests | func     | stepper     | line 21  |
| module.find_tests | name     | stepper     | line 21  |
| module.sign       | value    | fixed value | line 1   |

## func_list.py

| Scope  | Variable   | Role        | Location |
| :------| :----------| :-----------| :--------|
| module | everything | fixed value | line 10  |
| module | func       | stepper     | line 11  |

## globals.py

Warning: no variables found.

## globals_plus.py

| Scope  | Variable    | Role        | Location |
| :------| :-----------| :-----------| :--------|
| module | my_variable | fixed value | line 2   |

## locals.py

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.show_locals | high     | fixed value | line 1   |
| module.show_locals | low      | fixed value | line 1   |
| module.show_locals | i        | stepper     | line 3   |

## manual.py

| Scope            | Variable  | Role        | Location |
| :----------------| :---------| :-----------| :--------|
| module           | TESTS     | fixed value | line 40  |
| module.run_tests | all_tests | fixed value | line 24  |
| module.run_tests | results   | fixed value | line 25  |
| module.run_tests | test      | stepper     | line 26  |
| module.sign      | value     | fixed value | line 2   |

## runner.py

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.run_tests | results  | fixed value | line 21  |
| module.run_tests | name     | stepper     | line 22  |
| module.run_tests | test     | stepper     | line 22  |
| module.sign      | value    | fixed value | line 1   |

## signature.py

| Scope      | Variable | Role        | Location |
| :----------| :--------| :-----------| :--------|
| module     | func     | stepper     | line 7   |
| module.one | value    | fixed value | line 4   |

## type_func.py

Warning: no variables found.

## type_int.py

Warning: no variables found.

## type_len.py

Warning: no variables found.

