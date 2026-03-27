# Functions and Closures

## example_def.py

| Variable | Scope | Role |
|---|---|---|
| double | module | fixed value |
| num | module.same | fixed value |

## func.py

| Variable | Scope | Role |
|---|---|---|
| OPERATIONS | module | fixed value |
| env | module.do | fixed value |
| instruction | module.do | fixed value |
| args | module.do | fixed value |
| op | module.do | fixed value |
| args | module.do_add | fixed value |
| env | module.do_add | fixed value |
| left | module.do_add | fixed value |
| right | module.do_add | fixed value |
| args | module.do_call | fixed value |
| env | module.do_call | container |
| name | module.do_call | fixed value |
| values | module.do_call | fixed value |
| func | module.do_call | fixed value |
| body | module.do_call | fixed value |
| params | module.do_call | fixed value |
| result | module.do_call | fixed value |
| args | module.do_comment | fixed value |
| env | module.do_comment | fixed value |
| args | module.do_func | fixed value |
| env | module.do_func | fixed value |
| params | module.do_func | fixed value |
| body | module.do_func | fixed value |
| args | module.do_get | fixed value |
| env | module.do_get | fixed value |
| args | module.do_gt | fixed value |
| env | module.do_gt | fixed value |
| args | module.do_if | fixed value |
| env | module.do_if | fixed value |
| cond | module.do_if | fixed value |
| choice | module.do_if | fixed value |
| args | module.do_leq | fixed value |
| env | module.do_leq | fixed value |
| args | module.do_neg | fixed value |
| env | module.do_neg | fixed value |
| args | module.do_not | fixed value |
| env | module.do_not | fixed value |
| args | module.do_or | fixed value |
| env | module.do_or | fixed value |
| temp | module.do_or | fixed value |
| args | module.do_print | unknown |
| env | module.do_print | fixed value |
| args | module.do_repeat | fixed value |
| env | module.do_repeat | fixed value |
| count | module.do_repeat | fixed value |
| i | module.do_repeat | stepper |
| result | module.do_repeat | most-recent holder |
| args | module.do_seq | fixed value |
| env | module.do_seq | fixed value |
| a | module.do_seq | stepper |
| result | module.do_seq | most-recent holder |
| args | module.do_set | fixed value |
| env | module.do_set | fixed value |
| name | module.do_set | fixed value |
| value | module.do_set | fixed value |
| env | module.env_get | fixed value |
| name | module.env_get | fixed value |
| e | module.env_get | stepper |
| env | module.env_set | fixed value |
| name | module.env_set | fixed value |
| value | module.env_set | fixed value |
| e | module.env_set | stepper |
| reader | module.main | fixed value |
| program | module.main | fixed value |
| result | module.main | fixed value |

## ex_dict_zip.py

*No variables identified by jorma.*

## inner.py

| Variable | Scope | Role |
|---|---|---|
| value | module.outer | fixed value |
| i | module.outer | stepper |
| current | module.outer.inner | fixed value |

## closure.py

| Variable | Scope | Role |
|---|---|---|
| has_secret | module | fixed value |
| thing | module.make_hidden | fixed value |

## oop.py

| Variable | Scope | Role |
|---|---|---|
| object | module | fixed value |
| initial_value | module.make_object | fixed value |
| private | module.make_object | fixed value |
| new_value | module.make_object.setter | fixed value |

## counter_fail.py

| Variable | Scope | Role |
|---|---|---|
| c | module | fixed value |
| i | module | stepper |
| value | module.make_counter | fixed value |
| value | module.make_counter._inner | unknown |

## counter_succeed.py

| Variable | Scope | Role |
|---|---|---|
| c | module | fixed value |
| i | module | stepper |
| value | module.make_counter | fixed value |

