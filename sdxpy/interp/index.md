# Variable Role Analysis: interp

## add_example.py

Warning: no variables found.
### Static analysis


## ex_assign_expr.py

Syntax error in '/Users/gvwilson/jorma/sdxpy/interp/ex_assign_expr.py': invalid syntax (<unknown>, line 2)

## expr.py

Error during dynamic analysis (AssertionError): Usage: expr.py filename
### Static analysis

| Scope         | Variable | Role        | Location |
| :-------------| :--------| :-----------| :--------|
| module.do     | expr     | fixed value | line 20  |
| module.do_abs | args     | fixed value | line 5   |
| module.do_abs | val      | fixed value | line 7   |
| module.do_add | args     | fixed value | line 12  |
| module.do_add | left     | fixed value | line 14  |
| module.do_add | right    | fixed value | line 15  |
| module.main   | reader   | fixed value | line 37  |
| module.main   | program  | fixed value | line 38  |
| module.main   | result   | fixed value | line 39  |

## vars.py

Error during dynamic analysis (AssertionError): Usage: vars.py filename
### Static analysis

| Scope         | Variable | Role               | Location |
| :-------------| :--------| :------------------| :--------|
| module.do     | env      | fixed value        | line 43  |
| module.do     | expr     | fixed value        | line 43  |
| module.do_abs | args     | fixed value        | line 5   |
| module.do_abs | env      | fixed value        | line 5   |
| module.do_abs | val      | fixed value        | line 7   |
| module.do_add | args     | fixed value        | line 11  |
| module.do_add | env      | fixed value        | line 11  |
| module.do_add | left     | fixed value        | line 13  |
| module.do_add | right    | fixed value        | line 14  |
| module.do_get | args     | fixed value        | line 18  |
| module.do_get | env      | fixed value        | line 18  |
| module.do_seq | args     | fixed value        | line 26  |
| module.do_seq | env      | fixed value        | line 26  |
| module.do_seq | item     | stepper            | line 28  |
| module.do_seq | result   | most-recent holder | line 29  |
| module.do_set | args     | fixed value        | line 34  |
| module.do_set | env      | fixed value        | line 34  |
| module.do_set | value    | fixed value        | line 37  |
| module.main   | reader   | fixed value        | line 62  |
| module.main   | program  | fixed value        | line 63  |
| module.main   | result   | fixed value        | line 64  |

## vars_reflect.py

Error during dynamic analysis (AssertionError): Usage: vars_reflect.py filename
### Static analysis

| Scope         | Variable | Role               | Location |
| :-------------| :--------| :------------------| :--------|
| module        | OPS      | fixed value        | line 37  |
| module.do     | env      | fixed value        | line 45  |
| module.do     | expr     | fixed value        | line 45  |
| module.do     | func     | fixed value        | line 53  |
| module.do_abs | args     | fixed value        | line 6   |
| module.do_abs | env      | fixed value        | line 6   |
| module.do_abs | val      | fixed value        | line 8   |
| module.do_add | args     | fixed value        | line 11  |
| module.do_add | env      | fixed value        | line 11  |
| module.do_add | left     | fixed value        | line 13  |
| module.do_add | right    | fixed value        | line 14  |
| module.do_get | args     | fixed value        | line 17  |
| module.do_get | env      | fixed value        | line 17  |
| module.do_seq | args     | fixed value        | line 23  |
| module.do_seq | env      | fixed value        | line 23  |
| module.do_seq | item     | stepper            | line 25  |
| module.do_seq | result   | most-recent holder | line 26  |
| module.do_set | args     | fixed value        | line 29  |
| module.do_set | env      | fixed value        | line 29  |
| module.do_set | value    | fixed value        | line 32  |
| module.main   | reader   | fixed value        | line 59  |
| module.main   | program  | fixed value        | line 60  |
| module.main   | result   | fixed value        | line 61  |

## vars_table.py

Error during dynamic analysis (AssertionError): Usage: vars_table.py filename
### Static analysis

| Scope         | Variable | Role               | Location |
| :-------------| :--------| :------------------| :--------|
| module        | OPS      | fixed value        | line 40  |
| module.do     | env      | fixed value        | line 50  |
| module.do     | expr     | fixed value        | line 50  |
| module.do     | func     | fixed value        | line 58  |
| module.do_abs | args     | fixed value        | line 4   |
| module.do_abs | env      | fixed value        | line 4   |
| module.do_abs | val      | fixed value        | line 7   |
| module.do_add | args     | fixed value        | line 10  |
| module.do_add | env      | fixed value        | line 10  |
| module.do_add | left     | fixed value        | line 13  |
| module.do_add | right    | fixed value        | line 14  |
| module.do_get | args     | fixed value        | line 17  |
| module.do_get | env      | fixed value        | line 17  |
| module.do_seq | args     | fixed value        | line 24  |
| module.do_seq | env      | fixed value        | line 24  |
| module.do_seq | item     | stepper            | line 27  |
| module.do_seq | result   | most-recent holder | line 28  |
| module.do_set | args     | fixed value        | line 31  |
| module.do_set | env      | fixed value        | line 31  |
| module.do_set | value    | fixed value        | line 35  |
| module.main   | reader   | fixed value        | line 64  |
| module.main   | program  | fixed value        | line 65  |
| module.main   | result   | fixed value        | line 66  |

