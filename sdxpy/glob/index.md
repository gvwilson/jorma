# Matching Patterns

## glob_lit.py

| Variable | Scope | Role |
|---|---|---|
| chars | module.Lit.__init__ | fixed value |
| rest | module.Lit.__init__ | fixed value |
| self | module.Lit.__init__ | fixed value |
| self | module.Lit.match | fixed value |
| start | module.Lit.match | fixed value |
| text | module.Lit.match | fixed value |
| end | module.Lit.match | fixed value |

## test_glob_lit.py

*No variables identified by jorma.*

## glob_any.py

| Variable | Scope | Role |
|---|---|---|
| rest | module.Any.__init__ | fixed value |
| self | module.Any.__init__ | fixed value |
| self | module.Any.match | fixed value |
| start | module.Any.match | fixed value |
| text | module.Any.match | fixed value |
| i | module.Any.match | stepper |

## test_glob_any.py

*No variables identified by jorma.*

## glob_either.py

| Variable | Scope | Role |
|---|---|---|
| left | module.Either.__init__ | fixed value |
| rest | module.Either.__init__ | fixed value |
| right | module.Either.__init__ | fixed value |
| self | module.Either.__init__ | fixed value |
| self | module.Either.match | fixed value |
| start | module.Either.match | fixed value |
| text | module.Either.match | fixed value |

## test_glob_either.py

*No variables identified by jorma.*

## test_glob_problem.py

*No variables identified by jorma.*

## glob_null.py

| Variable | Scope | Role |
|---|---|---|
| rest | module.Any.__init__ | fixed value |
| self | module.Any.__init__ | fixed value |
| self | module.Any._match | fixed value |
| start | module.Any._match | fixed value |
| text | module.Any._match | fixed value |
| i | module.Any._match | stepper |
| end | module.Any._match | most-recent holder |
| left | module.Either.__init__ | fixed value |
| rest | module.Either.__init__ | fixed value |
| right | module.Either.__init__ | fixed value |
| self | module.Either.__init__ | fixed value |
| self | module.Either._match | fixed value |
| start | module.Either._match | fixed value |
| text | module.Either._match | fixed value |
| pat | module.Either._match | stepper |
| end | module.Either._match | gatherer |
| chars | module.Lit.__init__ | fixed value |
| rest | module.Lit.__init__ | fixed value |
| self | module.Lit.__init__ | fixed value |
| self | module.Lit._match | fixed value |
| start | module.Lit._match | fixed value |
| text | module.Lit._match | fixed value |
| end | module.Lit._match | fixed value |
| rest | module.Match.__init__ | fixed value |
| self | module.Match.__init__ | fixed value |
| self | module.Match.match | fixed value |
| text | module.Match.match | fixed value |
| result | module.Match.match | fixed value |
| self | module.Null.__init__ | fixed value |
| self | module.Null._match | fixed value |
| start | module.Null._match | fixed value |
| text | module.Null._match | fixed value |

