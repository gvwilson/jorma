# glob

## glob_any.py

### Static analysis

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module.Any.__init__ | rest     | fixed value | line 2   |
| module.Any.__init__ | self     | fixed value | line 2   |
| module.Any.match    | self     | fixed value | line 5   |
| module.Any.match    | start    | fixed value | line 5   |
| module.Any.match    | text     | fixed value | line 5   |
| module.Any.match    | i        | stepper     | line 8   |

## glob_either.py

### Static analysis

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

### Static analysis

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

### Static analysis

| Scope                  | Variable | Role               | Location |
| :----------------------| :--------| :------------------| :--------|
| module.Any.__init__    | rest     | fixed value        | line 19  |
| module.Any.__init__    | self     | fixed value        | line 19  |
| module.Any._match      | self     | fixed value        | line 22  |
| module.Any._match      | start    | fixed value        | line 22  |
| module.Any._match      | text     | fixed value        | line 22  |
| module.Any._match      | i        | stepper            | line 23  |
| module.Any._match      | end      | most-recent holder | line 24  |
| module.Either.__init__ | left     | fixed value        | line 31  |
| module.Either.__init__ | rest     | fixed value        | line 31  |
| module.Either.__init__ | right    | fixed value        | line 31  |
| module.Either.__init__ | self     | fixed value        | line 31  |
| module.Either._match   | self     | fixed value        | line 36  |
| module.Either._match   | start    | fixed value        | line 36  |
| module.Either._match   | text     | fixed value        | line 36  |
| module.Either._match   | pat      | stepper            | line 37  |
| module.Either._match   | end      | gatherer           | line 38  |
| module.Lit.__init__    | chars    | fixed value        | line 47  |
| module.Lit.__init__    | rest     | fixed value        | line 47  |
| module.Lit.__init__    | self     | fixed value        | line 47  |
| module.Lit._match      | self     | fixed value        | line 51  |
| module.Lit._match      | start    | fixed value        | line 51  |
| module.Lit._match      | text     | fixed value        | line 51  |
| module.Lit._match      | end      | fixed value        | line 52  |
| module.Match.__init__  | rest     | fixed value        | line 2   |
| module.Match.__init__  | self     | fixed value        | line 2   |
| module.Match.match     | self     | fixed value        | line 5   |
| module.Match.match     | text     | fixed value        | line 5   |
| module.Match.match     | result   | fixed value        | line 6   |
| module.Null.__init__   | self     | fixed value        | line 11  |
| module.Null._match     | self     | fixed value        | line 14  |
| module.Null._match     | start    | fixed value        | line 14  |
| module.Null._match     | text     | fixed value        | line 14  |

## simpler_match.py

### Static analysis

| Scope                    | Variable  | Role               | Location |
| :------------------------| :---------| :------------------| :--------|
| module.Any.__init__      | rest      | fixed value        | line 18  |
| module.Any.__init__      | self      | fixed value        | line 18  |
| module.Any._do_match     | self      | fixed value        | line 21  |
| module.Any._do_match     | text      | fixed value        | line 21  |
| module.Any._do_match     | i         | stepper            | line 22  |
| module.Either.__init__   | left      | fixed value        | line 29  |
| module.Either.__init__   | rest      | fixed value        | line 29  |
| module.Either.__init__   | right     | fixed value        | line 29  |
| module.Either.__init__   | self      | fixed value        | line 29  |
| module.Either._do_match  | self      | fixed value        | line 33  |
| module.Either._do_match  | text      | fixed value        | line 33  |
| module.Either._do_match  | pat       | stepper            | line 34  |
| module.Either._do_match  | remainder | most-recent holder | line 35  |
| module.Lit.__init__      | chars     | fixed value        | line 44  |
| module.Lit.__init__      | rest      | fixed value        | line 44  |
| module.Lit.__init__      | self      | fixed value        | line 44  |
| module.Lit._do_match     | self      | fixed value        | line 48  |
| module.Lit._do_match     | text      | fixed value        | line 48  |
| module.Lit._do_match     | end       | fixed value        | line 49  |
| module.Match.__init__    | rest      | fixed value        | line 2   |
| module.Match.__init__    | self      | fixed value        | line 2   |
| module.Match.match       | self      | fixed value        | line 5   |
| module.Match.match       | text      | fixed value        | line 5   |
| module.Nothing.__init__  | rest      | fixed value        | line 10  |
| module.Nothing.__init__  | self      | fixed value        | line 10  |
| module.Nothing._do_match | self      | fixed value        | line 13  |
| module.Nothing._do_match | text      | fixed value        | line 13  |

## test_glob_any.py

### Static analysis


## test_glob_either.py

### Static analysis


## test_glob_lit.py

### Static analysis


## test_glob_null.py

### Static analysis


## test_glob_problem.py

### Static analysis


## test_simpler_match.py

### Static analysis


