# check

## attrs.py

### Static analysis

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module         | text     | fixed value | line 8   |
| module         | doc      | fixed value | line 16  |
| module.display | node     | fixed value | line 1   |
| module.display | child    | stepper     | line 4   |

## parse.py

### Static analysis

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module         | text     | fixed value | line 11  |
| module         | doc      | fixed value | line 20  |
| module.display | node     | fixed value | line 1   |
| module.display | child    | stepper     | line 7   |

## visitor.py

### Static analysis

| Scope                     | Variable | Role        | Location |
| :-------------------------| :--------| :-----------| :--------|
| module.Visitor._tag_enter | node     | fixed value | line 14  |
| module.Visitor._tag_enter | self     | fixed value | line 14  |
| module.Visitor._tag_exit  | node     | fixed value | line 17  |
| module.Visitor._tag_exit  | self     | fixed value | line 17  |
| module.Visitor._text      | node     | fixed value | line 20  |
| module.Visitor._text      | self     | fixed value | line 20  |
| module.Visitor.visit      | node     | fixed value | line 5   |
| module.Visitor.visit      | self     | fixed value | line 5   |
| module.Visitor.visit      | child    | stepper     | line 10  |

