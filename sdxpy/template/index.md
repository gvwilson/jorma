# Variable Role Analysis: template

## env.py

```

[module.Env.__init__]
  initial                  fixed value             (line 3)
  self                     fixed value             (line 3)

[module.Env.__str__]
  self                     fixed value             (line 19)

[module.Env.find]
  name                     fixed value             (line 12)
  self                     fixed value             (line 12)
  frame                    stepper                 (line 13)

[module.Env.pop]
  self                     fixed value             (line 9)

[module.Env.push]
  frame                    fixed value             (line 6)
  self                     fixed value             (line 6)
```

## example_call.py

```

[module]
  data                     fixed value             (line 1)
  dom                      fixed value             (line 3)
  expander                 fixed value             (line 4)
```

## expander.py

```

[module]
  HANDLERS                 fixed value             (line 11)

[module.Expander.__init__]
  root                     fixed value             (line 22)
  self                     fixed value             (line 22)
  variables                fixed value             (line 22)

[module.Expander.close]
  node                     fixed value             (line 42)
  self                     fixed value             (line 42)

[module.Expander.getHandler]
  node                     fixed value             (line 58)
  self                     fixed value             (line 58)
  possible                 fixed value             (line 59)

[module.Expander.getResult]
  self                     fixed value             (line 81)

[module.Expander.hasHandler]
  node                     fixed value             (line 52)
  self                     fixed value             (line 52)

[module.Expander.open]
  node                     fixed value             (line 30)
  self                     fixed value             (line 30)

[module.Expander.output]
  self                     fixed value             (line 78)
  text                     fixed value             (line 78)

[module.Expander.showTag]
  closing                  fixed value             (line 68)
  node                     fixed value             (line 68)
  self                     fixed value             (line 68)
  name                     stepper                 (line 73)
```

## template.py

```

[module.main]
  reader                   fixed value             (line 7)
  variables                fixed value             (line 8)
  doc                      fixed value             (line 11)
  template                 fixed value             (line 12)
  expander                 fixed value             (line 14)
```

## visitor.py

```

[module.Visitor.__init__]
  root                     fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Visitor.close]
  node                     fixed value             (line 16)
  self                     fixed value             (line 16)

[module.Visitor.open]
  node                     fixed value             (line 13)
  self                     fixed value             (line 13)

[module.Visitor.walk]
  node                     fixed value             (line 5)
  self                     fixed value             (line 5)
  child                    stepper                 (line 9)
```

## z_if.py

```

[module.close]
  expander                 fixed value             (line 7)
  node                     fixed value             (line 7)

[module.open]
  expander                 fixed value             (line 1)
  node                     fixed value             (line 1)
  check                    fixed value             (line 2)
```

## z_loop.py

```

[module.close]
  expander                 fixed value             (line 12)
  node                     fixed value             (line 12)

[module.open]
  expander                 fixed value             (line 1)
  node                     fixed value             (line 1)
  index_name               fixed value             (line 2)
  target_name              fixed value             (line 2)
  target                   fixed value             (line 4)
  value                    stepper                 (line 5)
  child                    stepper                 (line 7)
```

## z_num.py

```

[module.close]
  expander                 fixed value             (line 5)
  node                     fixed value             (line 5)

[module.open]
  expander                 fixed value             (line 1)
  node                     fixed value             (line 1)
```

## z_var.py

```

[module.close]
  expander                 fixed value             (line 5)
  node                     fixed value             (line 5)

[module.open]
  expander                 fixed value             (line 1)
  node                     fixed value             (line 1)
```

