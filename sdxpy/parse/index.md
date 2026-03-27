# Variable Role Analysis: parse

## better_parser.py

```

[module.BetterParser._parse_EitherStart]
  back                     stepper                 (line 7)
  rest                     fixed value             (line 7)
  self                     fixed value             (line 7)
  children                 log                     (line 8)
```

## match.py

```

[module.Any.__init__]
  rest                     fixed value             (line 24)
  self                     fixed value             (line 24)

[module.Either.__eq__]
  other                    fixed value             (line 33)
  self                     fixed value             (line 33)

[module.Either.__init__]
  children                 fixed value             (line 29)
  rest                     fixed value             (line 29)
  self                     fixed value             (line 29)

[module.Lit.__eq__]
  other                    fixed value             (line 16)
  self                     fixed value             (line 16)

[module.Lit.__init__]
  chars                    fixed value             (line 12)
  rest                     fixed value             (line 12)
  self                     fixed value             (line 12)

[module.Match.__eq__]
  other                    fixed value             (line 6)
  self                     fixed value             (line 6)

[module.Match.__init__]
  rest                     fixed value             (line 3)
  self                     fixed value             (line 3)

[module.Null.__init__]
  self                     fixed value             (line 40)
```

## parser.py

```

[module.Parser._parse]
  self                     fixed value             (line 20)
  tokens                   fixed value             (line 20)
  back                     fixed value             (line 24)
  front                    fixed value             (line 24)
  handler                  fixed value             (line 25)

[module.Parser._parse_Any]
  back                     fixed value             (line 12)
  rest                     fixed value             (line 12)
  self                     fixed value             (line 12)

[module.Parser._parse_EitherStart]
  back                     fixed value             (line 35)
  rest                     fixed value             (line 35)
  self                     fixed value             (line 35)
  left                     fixed value             (line 43)
  right                    fixed value             (line 44)

[module.Parser._parse_Lit]
  back                     fixed value             (line 15)
  rest                     fixed value             (line 15)
  self                     fixed value             (line 15)

[module.Parser.parse]
  self                     fixed value             (line 6)
  text                     fixed value             (line 6)
  tokens                   fixed value             (line 7)
```

## test_parser.py

```
Warning: no variables found.
```

## test_tokenizer.py

```
Warning: no variables found.
```

## tokenizer.py

```

[module]
  CHARS                    fixed value             (line 4)

[module.Tokenizer.__init__]
  self                     fixed value             (line 7)

[module.Tokenizer._add]
  self                     fixed value             (line 36)
  thing                    fixed value             (line 36)

[module.Tokenizer._setup]
  self                     fixed value             (line 10)

[module.Tokenizer.tok]
  self                     fixed value             (line 16)
  text                     fixed value             (line 16)
  ch                       stepper                 (line 18)
```

