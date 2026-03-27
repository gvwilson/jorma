# Variable Role Analysis: func

## closure.py

| Scope              | Variable   | Role        | Location |
| :------------------| :----------| :-----------| :--------|
| module             | has_secret | fixed value | line 6   |
| module.make_hidden | thing      | fixed value | line 1   |

## counter_fail.py

| Scope                      | Variable | Role        | Location |
| :--------------------------| :--------| :-----------| :--------|
| module                     | c        | fixed value | line 8   |
| module                     | i        | stepper     | line 9   |
| module.make_counter        | value    | fixed value | line 2   |
| module.make_counter._inner | value    | unknown     | line 4   |

## counter_succeed.py

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module              | c        | fixed value | line 8   |
| module              | i        | stepper     | line 9   |
| module.make_counter | value    | fixed value | line 2   |

## ex_dict_zip.py

Warning: no variables found.

## example_def.py

| Scope       | Variable | Role        | Location |
| :-----------| :--------| :-----------| :--------|
| module      | double   | fixed value | line 15  |
| module.same | num      | fixed value | line 2   |

## func.py

| Scope             | Variable    | Role               | Location |
| :-----------------| :-----------| :------------------| :--------|
| module            | OPERATIONS  | fixed value        | line 100 |
| module.do         | env         | fixed value        | line 106 |
| module.do         | instruction | fixed value        | line 106 |
| module.do         | args        | fixed value        | line 109 |
| module.do         | op          | fixed value        | line 109 |
| module.do_add     | args        | fixed value        | line 4   |
| module.do_add     | env         | fixed value        | line 4   |
| module.do_add     | left        | fixed value        | line 6   |
| module.do_add     | right       | fixed value        | line 7   |
| module.do_call    | args        | fixed value        | line 11  |
| module.do_call    | env         | container          | line 11  |
| module.do_call    | name        | fixed value        | line 14  |
| module.do_call    | values      | fixed value        | line 15  |
| module.do_call    | func        | fixed value        | line 18  |
| module.do_call    | body        | fixed value        | line 20  |
| module.do_call    | params      | fixed value        | line 20  |
| module.do_call    | result      | fixed value        | line 25  |
| module.do_comment | args        | fixed value        | line 32  |
| module.do_comment | env         | fixed value        | line 32  |
| module.do_func    | args        | fixed value        | line 36  |
| module.do_func    | env         | fixed value        | line 36  |
| module.do_func    | params      | fixed value        | line 38  |
| module.do_func    | body        | fixed value        | line 39  |
| module.do_get     | args        | fixed value        | line 43  |
| module.do_get     | env         | fixed value        | line 43  |
| module.do_gt      | args        | fixed value        | line 47  |
| module.do_gt      | env         | fixed value        | line 47  |
| module.do_if      | args        | fixed value        | line 51  |
| module.do_if      | env         | fixed value        | line 51  |
| module.do_if      | cond        | fixed value        | line 53  |
| module.do_if      | choice      | fixed value        | line 54  |
| module.do_leq     | args        | fixed value        | line 57  |
| module.do_leq     | env         | fixed value        | line 57  |
| module.do_neg     | args        | fixed value        | line 61  |
| module.do_neg     | env         | fixed value        | line 61  |
| module.do_not     | args        | fixed value        | line 65  |
| module.do_not     | env         | fixed value        | line 65  |
| module.do_or      | args        | fixed value        | line 69  |
| module.do_or      | env         | fixed value        | line 69  |
| module.do_or      | temp        | fixed value        | line 71  |
| module.do_print   | args        | unknown            | line 75  |
| module.do_print   | env         | fixed value        | line 75  |
| module.do_repeat  | args        | fixed value        | line 80  |
| module.do_repeat  | env         | fixed value        | line 80  |
| module.do_repeat  | count       | fixed value        | line 82  |
| module.do_repeat  | i           | stepper            | line 83  |
| module.do_repeat  | result      | most-recent holder | line 84  |
| module.do_seq     | args        | fixed value        | line 87  |
| module.do_seq     | env         | fixed value        | line 87  |
| module.do_seq     | a           | stepper            | line 88  |
| module.do_seq     | result      | most-recent holder | line 89  |
| module.do_set     | args        | fixed value        | line 92  |
| module.do_set     | env         | fixed value        | line 92  |
| module.do_set     | name        | fixed value        | line 94  |
| module.do_set     | value       | fixed value        | line 95  |
| module.env_get    | env         | fixed value        | line 113 |
| module.env_get    | name        | fixed value        | line 113 |
| module.env_get    | e           | stepper            | line 115 |
| module.env_set    | env         | fixed value        | line 120 |
| module.env_set    | name        | fixed value        | line 120 |
| module.env_set    | value       | fixed value        | line 120 |
| module.env_set    | e           | stepper            | line 122 |
| module.main       | reader      | fixed value        | line 130 |
| module.main       | program     | fixed value        | line 131 |
| module.main       | result      | fixed value        | line 132 |

## inner.py

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.outer       | value    | fixed value | line 1   |
| module.outer       | i        | stepper     | line 6   |
| module.outer.inner | current  | fixed value | line 2   |

## oop.py

| Scope                     | Variable      | Role        | Location |
| :-------------------------| :-------------| :-----------| :--------|
| module                    | object        | fixed value | line 12  |
| module.make_object        | initial_value | fixed value | line 1   |
| module.make_object        | private       | fixed value | line 2   |
| module.make_object.setter | new_value     | fixed value | line 7   |

