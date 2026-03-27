# Running Tests

## func_list.py

| Variable | Scope | Role |
|---|---|---|
| everything | module | fixed value |
| func | module | stepper |

## signature.py

| Variable | Scope | Role |
|---|---|---|
| func | module | stepper |
| value | module.one | fixed value |

## manual.py

| Variable | Scope | Role |
|---|---|---|
| TESTS | module | fixed value |
| all_tests | module.run_tests | fixed value |
| results | module.run_tests | fixed value |
| test | module.run_tests | stepper |
| value | module.sign | fixed value |

## globals.py

*No variables identified by jorma.*

## globals_plus.py

| Variable | Scope | Role |
|---|---|---|
| my_variable | module | fixed value |

## find_test_funcs.py

| Variable | Scope | Role |
|---|---|---|
| prefix | module.find_tests | fixed value |
| func | module.find_tests | stepper |
| name | module.find_tests | stepper |
| value | module.sign | fixed value |

## runner.py

| Variable | Scope | Role |
|---|---|---|
| results | module.run_tests | fixed value |
| name | module.run_tests | stepper |
| test | module.run_tests | stepper |
| value | module.sign | fixed value |

## ex_loop_globals_2.py

| Variable | Scope | Role |
|---|---|---|
| name | module | stepper |

## type_int.py

*No variables identified by jorma.*

## type_func.py

*No variables identified by jorma.*

## type_len.py

*No variables identified by jorma.*

## callable.py

*No variables identified by jorma.*

## locals.py

| Variable | Scope | Role |
|---|---|---|
| high | module.show_locals | fixed value |
| low | module.show_locals | fixed value |
| i | module.show_locals | stepper |

