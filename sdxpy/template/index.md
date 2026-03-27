# Variable Role Analysis: template

## env.py

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module.Env.__init__ | initial  | fixed value | line 3   |
| module.Env.__init__ | self     | fixed value | line 3   |
| module.Env.__str__  | self     | fixed value | line 19  |
| module.Env.find     | name     | fixed value | line 12  |
| module.Env.find     | self     | fixed value | line 12  |
| module.Env.find     | frame    | stepper     | line 13  |
| module.Env.pop      | self     | fixed value | line 9   |
| module.Env.push     | frame    | fixed value | line 6   |
| module.Env.push     | self     | fixed value | line 6   |

## example_call.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | data     | fixed value | line 1   |
| module | dom      | fixed value | line 3   |
| module | expander | fixed value | line 4   |

## expander.py

| Scope                      | Variable  | Role        | Location |
| :--------------------------| :---------| :-----------| :--------|
| module                     | HANDLERS  | fixed value | line 11  |
| module.Expander.__init__   | root      | fixed value | line 22  |
| module.Expander.__init__   | self      | fixed value | line 22  |
| module.Expander.__init__   | variables | fixed value | line 22  |
| module.Expander.close      | node      | fixed value | line 42  |
| module.Expander.close      | self      | fixed value | line 42  |
| module.Expander.getHandler | node      | fixed value | line 58  |
| module.Expander.getHandler | self      | fixed value | line 58  |
| module.Expander.getHandler | possible  | fixed value | line 59  |
| module.Expander.getResult  | self      | fixed value | line 81  |
| module.Expander.hasHandler | node      | fixed value | line 52  |
| module.Expander.hasHandler | self      | fixed value | line 52  |
| module.Expander.open       | node      | fixed value | line 30  |
| module.Expander.open       | self      | fixed value | line 30  |
| module.Expander.output     | self      | fixed value | line 78  |
| module.Expander.output     | text      | fixed value | line 78  |
| module.Expander.showTag    | closing   | fixed value | line 68  |
| module.Expander.showTag    | node      | fixed value | line 68  |
| module.Expander.showTag    | self      | fixed value | line 68  |
| module.Expander.showTag    | name      | stepper     | line 73  |

## template.py

| Scope       | Variable  | Role        | Location |
| :-----------| :---------| :-----------| :--------|
| module.main | reader    | fixed value | line 7   |
| module.main | variables | fixed value | line 8   |
| module.main | doc       | fixed value | line 11  |
| module.main | template  | fixed value | line 12  |
| module.main | expander  | fixed value | line 14  |

## visitor.py

| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module.Visitor.__init__ | root     | fixed value | line 2   |
| module.Visitor.__init__ | self     | fixed value | line 2   |
| module.Visitor.close    | node     | fixed value | line 16  |
| module.Visitor.close    | self     | fixed value | line 16  |
| module.Visitor.open     | node     | fixed value | line 13  |
| module.Visitor.open     | self     | fixed value | line 13  |
| module.Visitor.walk     | node     | fixed value | line 5   |
| module.Visitor.walk     | self     | fixed value | line 5   |
| module.Visitor.walk     | child    | stepper     | line 9   |

## z_if.py

| Scope        | Variable | Role        | Location |
| :------------| :--------| :-----------| :--------|
| module.close | expander | fixed value | line 7   |
| module.close | node     | fixed value | line 7   |
| module.open  | expander | fixed value | line 1   |
| module.open  | node     | fixed value | line 1   |
| module.open  | check    | fixed value | line 2   |

## z_loop.py

| Scope        | Variable    | Role        | Location |
| :------------| :-----------| :-----------| :--------|
| module.close | expander    | fixed value | line 12  |
| module.close | node        | fixed value | line 12  |
| module.open  | expander    | fixed value | line 1   |
| module.open  | node        | fixed value | line 1   |
| module.open  | index_name  | fixed value | line 2   |
| module.open  | target_name | fixed value | line 2   |
| module.open  | target      | fixed value | line 4   |
| module.open  | value       | stepper     | line 5   |
| module.open  | child       | stepper     | line 7   |

## z_num.py

| Scope        | Variable | Role        | Location |
| :------------| :--------| :-----------| :--------|
| module.close | expander | fixed value | line 5   |
| module.close | node     | fixed value | line 5   |
| module.open  | expander | fixed value | line 1   |
| module.open  | node     | fixed value | line 1   |

## z_var.py

| Scope        | Variable | Role        | Location |
| :------------| :--------| :-----------| :--------|
| module.close | expander | fixed value | line 5   |
| module.close | node     | fixed value | line 5   |
| module.open  | expander | fixed value | line 1   |
| module.open  | node     | fixed value | line 1   |

