# Variable Role Analysis: check

## attrs.py

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module         | text     | fixed value | line 10  |
| module         | doc      | fixed value | line 20  |
| module.display | node     | fixed value | line 2   |
| module.display | child    | stepper     | line 5   |

## catalog.py

| Scope                     | Variable  | Role        | Location |
| :-------------------------| :---------| :-----------| :--------|
| module                    | reader    | fixed value | line 20  |
| module                    | text      | fixed value | line 21  |
| module                    | doc       | fixed value | line 22  |
| module                    | cataloger | fixed value | line 24  |
| module                    | result    | fixed value | line 26  |
| module                    | contents  | stepper     | line 28  |
| module                    | tag       | stepper     | line 28  |
| module.Catalog.__init__   | self      | fixed value | line 7   |
| module.Catalog._tag_enter | node      | fixed value | line 11  |
| module.Catalog._tag_enter | self      | fixed value | line 11  |
| module.Catalog._tag_enter | child     | stepper     | line 14  |

## check.py

| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module                  | manifest | fixed value | line 31  |
| module                  | reader   | fixed value | line 32  |
| module                  | text     | fixed value | line 33  |
| module                  | doc      | fixed value | line 34  |
| module                  | checker  | fixed value | line 36  |
| module                  | key      | stepper     | line 38  |
| module                  | value    | stepper     | line 38  |
| module.Check.__init__   | manifest | fixed value | line 9   |
| module.Check.__init__   | self     | fixed value | line 9   |
| module.Check._tag_enter | node     | fixed value | line 13  |
| module.Check._tag_enter | self     | fixed value | line 13  |
| module.Check._tag_enter | actual   | fixed value | line 14  |
| module.Check._tag_enter | errors   | unknown     | line 16  |
| module.read_manifest    | filename | fixed value | line 24  |
| module.read_manifest    | reader   | fixed value | line 25  |
| module.read_manifest    | result   | fixed value | line 26  |
| module.read_manifest    | key      | stepper     | line 27  |

## contains.py

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module         | reader   | fixed value | line 19  |
| module         | text     | fixed value | line 20  |
| module         | doc      | fixed value | line 21  |
| module         | catalog  | fixed value | line 22  |
| module         | contents | stepper     | line 23  |
| module         | tag      | stepper     | line 23  |
| module.recurse | catalog  | fixed value | line 5   |
| module.recurse | node     | fixed value | line 5   |
| module.recurse | child    | stepper     | line 11  |

## ex_flatten.py

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | node     | stepper | line 1   |

## parse.py

| Scope          | Variable | Role        | Location |
| :--------------| :--------| :-----------| :--------|
| module         | text     | fixed value | line 13  |
| module         | doc      | fixed value | line 24  |
| module.display | node     | fixed value | line 2   |
| module.display | child    | stepper     | line 8   |

## visitor.py

| Scope                     | Variable | Role        | Location |
| :-------------------------| :--------| :-----------| :--------|
| module.Visitor._tag_enter | node     | fixed value | line 14  |
| module.Visitor._tag_enter | self     | fixed value | line 14  |
| module.Visitor._tag_exit  | node     | fixed value | line 16  |
| module.Visitor._tag_exit  | self     | fixed value | line 16  |
| module.Visitor._text      | node     | fixed value | line 18  |
| module.Visitor._text      | self     | fixed value | line 18  |
| module.Visitor.visit      | node     | fixed value | line 5   |
| module.Visitor.visit      | self     | fixed value | line 5   |
| module.Visitor.visit      | child    | stepper     | line 10  |

