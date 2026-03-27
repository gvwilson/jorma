# test

## callable.py

### Static analysis


## ex_loop_globals_2.py

### Static analysis

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | name     | stepper | line 1   |

## find_test_funcs.py

### Static analysis

| Scope             | Variable | Role        | Location |
| :-----------------| :--------| :-----------| :--------|
| module.find_tests | prefix   | fixed value | line 24  |
| module.find_tests | func     | stepper     | line 25  |
| module.find_tests | name     | stepper     | line 25  |
| module.sign       | value    | fixed value | line 1   |

## func_list.py

### Static analysis

| Scope  | Variable   | Role        | Location |
| :------| :----------| :-----------| :--------|
| module | everything | fixed value | line 13  |
| module | func       | stepper     | line 14  |

## globals.py

### Static analysis


## globals_plus.py

### Static analysis

| Scope  | Variable    | Role        | Location |
| :------| :-----------| :-----------| :--------|
| module | my_variable | fixed value | line 3   |

## locals.py

### Static analysis

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.show_locals | high     | fixed value | line 1   |
| module.show_locals | low      | fixed value | line 1   |
| module.show_locals | i        | stepper     | line 3   |

## manual.py

### Static analysis

| Scope            | Variable  | Role        | Location |
| :----------------| :---------| :-----------| :--------|
| module           | TESTS     | fixed value | line 39  |
| module.run_tests | all_tests | fixed value | line 24  |
| module.run_tests | results   | fixed value | line 25  |
| module.run_tests | test      | stepper     | line 26  |
| module.sign      | value     | fixed value | line 1   |

## runner.py

### Static analysis

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.run_tests | results  | fixed value | line 25  |
| module.run_tests | name     | stepper     | line 26  |
| module.run_tests | test     | stepper     | line 26  |
| module.sign      | value    | fixed value | line 1   |

## type_func.py

### Static analysis


## type_int.py

### Static analysis


## type_len.py

### Static analysis


