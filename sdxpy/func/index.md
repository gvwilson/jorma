# func
| Scope                    | Variable   | Role        | Location |
| :------------------------| :----------| :-----------| :--------|
| module                   | adder_func | fixed value | line 8   |
| module.make_adder        | to_add     | fixed value | line 1   |
| module.make_adder._inner | value      | fixed value | line 2   |
| Scope              | Variable   | Role        | Location |
| :------------------| :----------| :-----------| :--------|
| module             | has_secret | fixed value | line 8   |
| module.make_hidden | thing      | fixed value | line 1   |
| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module             | odds     | fixed value | line 8   |
| module             | first    | fixed value | line 9   |
| module             | evens    | log         | line 15  |
| module             | second   | fixed value | line 16  |
| module.wrap        | extra    | fixed value | line 1   |
| module.wrap._inner | f        | fixed value | line 2   |
| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module              | c        | fixed value | line 11  |
| module              | i        | stepper     | line 12  |
| module.make_counter | value    | fixed value | line 2   |
| Scope       | Variable | Role        | Location |
| :-----------| :--------| :-----------| :--------|
| module      | double   | fixed value | line 9   |
| module.same | num      | fixed value | line 1   |
| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.outer       | value    | fixed value | line 1   |
| module.outer       | i        | stepper     | line 6   |
| module.outer.inner | current  | fixed value | line 2   |
| Scope                     | Variable      | Role        | Location |
| :-------------------------| :-------------| :-----------| :--------|
| module                    | object        | fixed value | line 13  |
| module.make_object        | initial_value | fixed value | line 1   |
| module.make_object        | private       | fixed value | line 2   |
| module.make_object.setter | new_value     | fixed value | line 7   |
