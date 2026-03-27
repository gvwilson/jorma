# An HTML Validator

## parse.py

| Variable | Scope | Role |
|---|---|---|
| text | module | fixed value |
| doc | module | fixed value |
| node | module.display | fixed value |
| child | module.display | stepper |

## attrs.py

| Variable | Scope | Role |
|---|---|---|
| text | module | fixed value |
| doc | module | fixed value |
| node | module.display | fixed value |
| child | module.display | stepper |

## contains.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| text | module | fixed value |
| doc | module | fixed value |
| catalog | module | fixed value |
| contents | module | stepper |
| tag | module | stepper |
| catalog | module.recurse | fixed value |
| node | module.recurse | fixed value |
| child | module.recurse | stepper |

## visitor.py

| Variable | Scope | Role |
|---|---|---|
| node | module.Visitor._tag_enter | fixed value |
| self | module.Visitor._tag_enter | fixed value |
| node | module.Visitor._tag_exit | fixed value |
| self | module.Visitor._tag_exit | fixed value |
| node | module.Visitor._text | fixed value |
| self | module.Visitor._text | fixed value |
| node | module.Visitor.visit | fixed value |
| self | module.Visitor.visit | fixed value |
| child | module.Visitor.visit | stepper |

## catalog.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| text | module | fixed value |
| doc | module | fixed value |
| cataloger | module | fixed value |
| result | module | fixed value |
| contents | module | stepper |
| tag | module | stepper |
| self | module.Catalog.__init__ | fixed value |
| node | module.Catalog._tag_enter | fixed value |
| self | module.Catalog._tag_enter | fixed value |
| child | module.Catalog._tag_enter | stepper |

## check.py

| Variable | Scope | Role |
|---|---|---|
| manifest | module | fixed value |
| reader | module | fixed value |
| text | module | fixed value |
| doc | module | fixed value |
| checker | module | fixed value |
| key | module | stepper |
| value | module | stepper |
| manifest | module.Check.__init__ | fixed value |
| self | module.Check.__init__ | fixed value |
| node | module.Check._tag_enter | fixed value |
| self | module.Check._tag_enter | fixed value |
| actual | module.Check._tag_enter | fixed value |
| errors | module.Check._tag_enter | unknown |
| filename | module.read_manifest | fixed value |
| reader | module.read_manifest | fixed value |
| result | module.read_manifest | fixed value |
| key | module.read_manifest | stepper |

## ex_flatten.py

| Variable | Scope | Role |
|---|---|---|
| node | module | stepper |

