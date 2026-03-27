# A Template Expander

## example_call.py

| Variable | Scope | Role |
|---|---|---|
| data | module | fixed value |
| dom | module | fixed value |
| expander | module | fixed value |

## env.py

| Variable | Scope | Role |
|---|---|---|
| initial | module.Env.__init__ | fixed value |
| self | module.Env.__init__ | fixed value |
| self | module.Env.__str__ | fixed value |
| name | module.Env.find | fixed value |
| self | module.Env.find | fixed value |
| frame | module.Env.find | stepper |
| self | module.Env.pop | fixed value |
| frame | module.Env.push | fixed value |
| self | module.Env.push | fixed value |

## visitor.py

| Variable | Scope | Role |
|---|---|---|
| root | module.Visitor.__init__ | fixed value |
| self | module.Visitor.__init__ | fixed value |
| node | module.Visitor.close | fixed value |
| self | module.Visitor.close | fixed value |
| node | module.Visitor.open | fixed value |
| self | module.Visitor.open | fixed value |
| node | module.Visitor.walk | fixed value |
| self | module.Visitor.walk | fixed value |
| child | module.Visitor.walk | stepper |

## expander.py

| Variable | Scope | Role |
|---|---|---|
| HANDLERS | module | fixed value |
| root | module.Expander.__init__ | fixed value |
| self | module.Expander.__init__ | fixed value |
| variables | module.Expander.__init__ | fixed value |
| node | module.Expander.close | fixed value |
| self | module.Expander.close | fixed value |
| node | module.Expander.getHandler | fixed value |
| self | module.Expander.getHandler | fixed value |
| possible | module.Expander.getHandler | fixed value |
| self | module.Expander.getResult | fixed value |
| node | module.Expander.hasHandler | fixed value |
| self | module.Expander.hasHandler | fixed value |
| node | module.Expander.open | fixed value |
| self | module.Expander.open | fixed value |
| self | module.Expander.output | fixed value |
| text | module.Expander.output | fixed value |
| closing | module.Expander.showTag | fixed value |
| node | module.Expander.showTag | fixed value |
| self | module.Expander.showTag | fixed value |
| name | module.Expander.showTag | stepper |

## z_num.py

| Variable | Scope | Role |
|---|---|---|
| expander | module.close | fixed value |
| node | module.close | fixed value |
| expander | module.open | fixed value |
| node | module.open | fixed value |

## z_var.py

| Variable | Scope | Role |
|---|---|---|
| expander | module.close | fixed value |
| node | module.close | fixed value |
| expander | module.open | fixed value |
| node | module.open | fixed value |

## template.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.main | fixed value |
| variables | module.main | fixed value |
| doc | module.main | fixed value |
| template | module.main | fixed value |
| expander | module.main | fixed value |

## z_if.py

| Variable | Scope | Role |
|---|---|---|
| expander | module.close | fixed value |
| node | module.close | fixed value |
| expander | module.open | fixed value |
| node | module.open | fixed value |
| check | module.open | fixed value |

## z_loop.py

| Variable | Scope | Role |
|---|---|---|
| expander | module.close | fixed value |
| node | module.close | fixed value |
| expander | module.open | fixed value |
| node | module.open | fixed value |
| index_name | module.open | fixed value |
| target_name | module.open | fixed value |
| target | module.open | fixed value |
| value | module.open | stepper |
| child | module.open | stepper |

