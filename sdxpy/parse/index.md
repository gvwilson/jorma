# Parsing Text

## tokenizer.py

| Variable | Scope | Role |
|---|---|---|
| CHARS | module | fixed value |
| self | module.Tokenizer.__init__ | fixed value |
| self | module.Tokenizer._add | fixed value |
| thing | module.Tokenizer._add | fixed value |
| self | module.Tokenizer._setup | fixed value |
| self | module.Tokenizer.tok | fixed value |
| text | module.Tokenizer.tok | fixed value |
| ch | module.Tokenizer.tok | stepper |

## test_tokenizer.py

*No variables identified by jorma.*

## parser.py

| Variable | Scope | Role |
|---|---|---|
| self | module.Parser._parse | fixed value |
| tokens | module.Parser._parse | fixed value |
| back | module.Parser._parse | fixed value |
| front | module.Parser._parse | fixed value |
| handler | module.Parser._parse | fixed value |
| back | module.Parser._parse_Any | fixed value |
| rest | module.Parser._parse_Any | fixed value |
| self | module.Parser._parse_Any | fixed value |
| back | module.Parser._parse_EitherStart | fixed value |
| rest | module.Parser._parse_EitherStart | fixed value |
| self | module.Parser._parse_EitherStart | fixed value |
| left | module.Parser._parse_EitherStart | fixed value |
| right | module.Parser._parse_EitherStart | fixed value |
| back | module.Parser._parse_Lit | fixed value |
| rest | module.Parser._parse_Lit | fixed value |
| self | module.Parser._parse_Lit | fixed value |
| self | module.Parser.parse | fixed value |
| text | module.Parser.parse | fixed value |
| tokens | module.Parser.parse | fixed value |

## better_parser.py

| Variable | Scope | Role |
|---|---|---|
| back | module.BetterParser._parse_EitherStart | stepper |
| rest | module.BetterParser._parse_EitherStart | fixed value |
| self | module.BetterParser._parse_EitherStart | fixed value |
| children | module.BetterParser._parse_EitherStart | log |

## test_parser.py

*No variables identified by jorma.*

## match.py

| Variable | Scope | Role |
|---|---|---|
| rest | module.Any.__init__ | fixed value |
| self | module.Any.__init__ | fixed value |
| other | module.Either.__eq__ | fixed value |
| self | module.Either.__eq__ | fixed value |
| children | module.Either.__init__ | fixed value |
| rest | module.Either.__init__ | fixed value |
| self | module.Either.__init__ | fixed value |
| other | module.Lit.__eq__ | fixed value |
| self | module.Lit.__eq__ | fixed value |
| chars | module.Lit.__init__ | fixed value |
| rest | module.Lit.__init__ | fixed value |
| self | module.Lit.__init__ | fixed value |
| other | module.Match.__eq__ | fixed value |
| self | module.Match.__eq__ | fixed value |
| rest | module.Match.__init__ | fixed value |
| self | module.Match.__init__ | fixed value |
| self | module.Null.__init__ | fixed value |

