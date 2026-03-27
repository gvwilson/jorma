# Variable Role Analysis: glob

## glob_any.py

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module.Any.__init__ | rest     | fixed value | line 2   |
| module.Any.__init__ | self     | fixed value | line 2   |
| module.Any.match    | self     | fixed value | line 5   |
| module.Any.match    | start    | fixed value | line 5   |
| module.Any.match    | text     | fixed value | line 5   |
| module.Any.match    | i        | stepper     | line 8   |

## glob_either.py

| Scope                  | Variable | Role        | Location |
| :----------------------| :--------| :-----------| :--------|
| module.Either.__init__ | left     | fixed value | line 2   |
| module.Either.__init__ | rest     | fixed value | line 2   |
| module.Either.__init__ | right    | fixed value | line 2   |
| module.Either.__init__ | self     | fixed value | line 2   |
| module.Either.match    | self     | fixed value | line 7   |
| module.Either.match    | start    | fixed value | line 7   |
| module.Either.match    | text     | fixed value | line 7   |

## glob_lit.py

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module.Lit.__init__ | chars    | fixed value | line 2   |
| module.Lit.__init__ | rest     | fixed value | line 2   |
| module.Lit.__init__ | self     | fixed value | line 2   |
| module.Lit.match    | self     | fixed value | line 6   |
| module.Lit.match    | start    | fixed value | line 6   |
| module.Lit.match    | text     | fixed value | line 6   |
| module.Lit.match    | end      | fixed value | line 7   |

## glob_null.py

| Scope                  | Variable | Role               | Location |
| :----------------------| :--------| :------------------| :--------|
| module.Any.__init__    | rest     | fixed value        | line 22  |
| module.Any.__init__    | self     | fixed value        | line 22  |
| module.Any._match      | self     | fixed value        | line 25  |
| module.Any._match      | start    | fixed value        | line 25  |
| module.Any._match      | text     | fixed value        | line 25  |
| module.Any._match      | i        | stepper            | line 26  |
| module.Any._match      | end      | most-recent holder | line 27  |
| module.Either.__init__ | left     | fixed value        | line 35  |
| module.Either.__init__ | rest     | fixed value        | line 35  |
| module.Either.__init__ | right    | fixed value        | line 35  |
| module.Either.__init__ | self     | fixed value        | line 35  |
| module.Either._match   | self     | fixed value        | line 40  |
| module.Either._match   | start    | fixed value        | line 40  |
| module.Either._match   | text     | fixed value        | line 40  |
| module.Either._match   | pat      | stepper            | line 41  |
| module.Either._match   | end      | gatherer           | line 42  |
| module.Lit.__init__    | chars    | fixed value        | line 52  |
| module.Lit.__init__    | rest     | fixed value        | line 52  |
| module.Lit.__init__    | self     | fixed value        | line 52  |
| module.Lit._match      | self     | fixed value        | line 56  |
| module.Lit._match      | start    | fixed value        | line 56  |
| module.Lit._match      | text     | fixed value        | line 56  |
| module.Lit._match      | end      | fixed value        | line 57  |
| module.Match.__init__  | rest     | fixed value        | line 3   |
| module.Match.__init__  | self     | fixed value        | line 3   |
| module.Match.match     | self     | fixed value        | line 6   |
| module.Match.match     | text     | fixed value        | line 6   |
| module.Match.match     | result   | fixed value        | line 7   |
| module.Null.__init__   | self     | fixed value        | line 13  |
| module.Null._match     | self     | fixed value        | line 16  |
| module.Null._match     | start    | fixed value        | line 16  |
| module.Null._match     | text     | fixed value        | line 16  |

## test_glob_any.py

Warning: no variables found.

## test_glob_either.py

Warning: no variables found.

## test_glob_lit.py

Warning: no variables found.

## test_glob_problem.py

Warning: no variables found.

