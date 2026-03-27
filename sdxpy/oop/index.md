# oop

## func_obj.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | alias    | fixed value | line 5   |

## inherit_class.py

### Static analysis

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Shape       | fixed value        | line 8   |
| module                  | Square      | fixed value        | line 23  |
| module                  | Circle      | fixed value        | line 43  |
| module                  | examples    | fixed value        | line 68  |
| module                  | ex          | stepper            | line 69  |
| module                  | n           | most-recent holder | line 70  |
| module                  | d           | most-recent holder | line 71  |
| module.call             | args        | fixed value        | line 55  |
| module.call             | method_name | fixed value        | line 55  |
| module.call             | thing       | fixed value        | line 55  |
| module.call             | method      | fixed value        | line 56  |
| module.circle_area      | thing       | fixed value        | line 39  |
| module.circle_new       | name        | fixed value        | line 51  |
| module.circle_new       | radius      | fixed value        | line 51  |
| module.circle_perimeter | thing       | fixed value        | line 35  |
| module.find             | cls         | stepper            | line 60  |
| module.find             | method_name | fixed value        | line 60  |
| module.shape_density    | thing       | fixed value        | line 4   |
| module.shape_density    | weight      | fixed value        | line 4   |
| module.shape_new        | name        | fixed value        | line 11  |
| module.square_area      | thing       | fixed value        | line 19  |
| module.square_new       | name        | fixed value        | line 31  |
| module.square_new       | side        | fixed value        | line 31  |
| module.square_perimeter | thing       | fixed value        | line 15  |

## inherit_constructor.py

### Static analysis

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Shape       | fixed value        | line 12  |
| module                  | Square      | fixed value        | line 36  |
| module                  | Circle      | fixed value        | line 57  |
| module                  | examples    | fixed value        | line 79  |
| module                  | ex          | stepper            | line 80  |
| module                  | n           | most-recent holder | line 81  |
| module                  | d           | most-recent holder | line 82  |
| module.call             | args        | fixed value        | line 74  |
| module.call             | method_name | fixed value        | line 74  |
| module.call             | thing       | fixed value        | line 74  |
| module.call             | method      | fixed value        | line 75  |
| module.circle_area      | thing       | fixed value        | line 49  |
| module.circle_new       | name        | fixed value        | line 53  |
| module.circle_new       | radius      | fixed value        | line 53  |
| module.circle_perimeter | thing       | fixed value        | line 45  |
| module.find             | cls         | fixed value        | line 66  |
| module.find             | method_name | fixed value        | line 66  |
| module.make             | args        | fixed value        | line 20  |
| module.make             | cls         | fixed value        | line 20  |
| module.shape_density    | thing       | fixed value        | line 4   |
| module.shape_density    | weight      | fixed value        | line 4   |
| module.shape_new        | name        | fixed value        | line 8   |
| module.square_area      | thing       | fixed value        | line 28  |
| module.square_new       | name        | fixed value        | line 32  |
| module.square_new       | side        | fixed value        | line 32  |
| module.square_perimeter | thing       | fixed value        | line 24  |

## inherit_original.py

### Static analysis

| Scope                   | Variable | Role               | Location |
| :-----------------------| :--------| :------------------| :--------|
| module                  | examples | fixed value        | line 42  |
| module                  | ex       | stepper            | line 43  |
| module                  | n        | most-recent holder | line 44  |
| module                  | d        | most-recent holder | line 45  |
| module.Circle.__init__  | name     | fixed value        | line 31  |
| module.Circle.__init__  | radius   | fixed value        | line 31  |
| module.Circle.__init__  | self     | fixed value        | line 31  |
| module.Circle.area      | self     | fixed value        | line 38  |
| module.Circle.perimeter | self     | fixed value        | line 35  |
| module.Shape.__init__   | name     | fixed value        | line 5   |
| module.Shape.__init__   | self     | fixed value        | line 5   |
| module.Shape.area       | self     | fixed value        | line 11  |
| module.Shape.density    | self     | fixed value        | line 14  |
| module.Shape.density    | weight   | fixed value        | line 14  |
| module.Shape.perimeter  | self     | fixed value        | line 8   |
| module.Square.__init__  | name     | fixed value        | line 19  |
| module.Square.__init__  | self     | fixed value        | line 19  |
| module.Square.__init__  | side     | fixed value        | line 19  |
| module.Square.area      | self     | fixed value        | line 26  |
| module.Square.perimeter | self     | fixed value        | line 23  |

## larger.py

### Static analysis

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Square      | fixed value        | line 16  |
| module                  | Circle      | fixed value        | line 40  |
| module                  | examples    | fixed value        | line 56  |
| module                  | ex          | stepper            | line 57  |
| module                  | result      | most-recent holder | line 58  |
| module.call             | args        | fixed value        | line 52  |
| module.call             | method_name | fixed value        | line 52  |
| module.call             | thing       | fixed value        | line 52  |
| module.circle_area      | thing       | fixed value        | line 32  |
| module.circle_larger    | size        | fixed value        | line 36  |
| module.circle_larger    | thing       | fixed value        | line 36  |
| module.circle_new       | name        | fixed value        | line 48  |
| module.circle_new       | radius      | fixed value        | line 48  |
| module.circle_perimeter | thing       | fixed value        | line 28  |
| module.square_area      | thing       | fixed value        | line 8   |
| module.square_larger    | size        | fixed value        | line 12  |
| module.square_larger    | thing       | fixed value        | line 12  |
| module.square_new       | name        | fixed value        | line 24  |
| module.square_new       | side        | fixed value        | line 24  |
| module.square_perimeter | thing       | fixed value        | line 4   |

## shapes_class.py

### Static analysis

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Square      | fixed value        | line 12  |
| module                  | Circle      | fixed value        | line 27  |
| module                  | examples    | fixed value        | line 38  |
| module                  | ex          | stepper            | line 39  |
| module                  | n           | most-recent holder | line 40  |
| module                  | p           | most-recent holder | line 41  |
| module                  | a           | most-recent holder | line 42  |
| module                  | c           | most-recent holder | line 43  |
| module.call             | method_name | fixed value        | line 34  |
| module.call             | thing       | fixed value        | line 34  |
| module.circle_area      | thing       | fixed value        | line 23  |
| module.circle_new       | name        | fixed value        | line 30  |
| module.circle_new       | radius      | fixed value        | line 30  |
| module.circle_perimeter | thing       | fixed value        | line 19  |
| module.square_area      | thing       | fixed value        | line 8   |
| module.square_new       | name        | fixed value        | line 15  |
| module.square_new       | side        | fixed value        | line 15  |
| module.square_perimeter | thing       | fixed value        | line 4   |

### Dynamic analysis

| Variable    | Scope       | Role  |
| :-----------| :-----------| :-----|
| method_name | module.call | phase |

## shapes_dict.py

### Static analysis

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | examples    | fixed value        | line 42  |
| module                  | ex          | stepper            | line 43  |
| module                  | n           | most-recent holder | line 44  |
| module                  | p           | most-recent holder | line 45  |
| module                  | a           | most-recent holder | line 46  |
| module.call             | method_name | fixed value        | line 38  |
| module.call             | thing       | fixed value        | line 38  |
| module.circle_area      | thing       | fixed value        | line 25  |
| module.circle_new       | name        | fixed value        | line 29  |
| module.circle_new       | radius      | fixed value        | line 29  |
| module.circle_perimeter | thing       | fixed value        | line 21  |
| module.square_area      | thing       | fixed value        | line 8   |
| module.square_new       | name        | fixed value        | line 12  |
| module.square_new       | side        | fixed value        | line 12  |
| module.square_perimeter | thing       | fixed value        | line 4   |

### Dynamic analysis

| Variable    | Scope       | Role  |
| :-----------| :-----------| :-----|
| method_name | module.call | phase |

## shapes_original.py

### Static analysis

| Scope                   | Variable | Role               | Location |
| :-----------------------| :--------| :------------------| :--------|
| module                  | examples | fixed value        | line 39  |
| module                  | thing    | stepper            | line 40  |
| module                  | n        | most-recent holder | line 41  |
| module                  | p        | most-recent holder | line 42  |
| module                  | a        | most-recent holder | line 43  |
| module.Circle.__init__  | name     | fixed value        | line 28  |
| module.Circle.__init__  | radius   | fixed value        | line 28  |
| module.Circle.__init__  | self     | fixed value        | line 28  |
| module.Circle.area      | self     | fixed value        | line 35  |
| module.Circle.perimeter | self     | fixed value        | line 32  |
| module.Shape.__init__   | name     | fixed value        | line 5   |
| module.Shape.__init__   | self     | fixed value        | line 5   |
| module.Shape.area       | self     | fixed value        | line 11  |
| module.Shape.perimeter  | self     | fixed value        | line 8   |
| module.Square.__init__  | name     | fixed value        | line 16  |
| module.Square.__init__  | self     | fixed value        | line 16  |
| module.Square.__init__  | side     | fixed value        | line 16  |
| module.Square.area      | self     | fixed value        | line 23  |
| module.Square.perimeter | self     | fixed value        | line 20  |

## spread.py

### Static analysis

| Scope              | Variable    | Role        | Location |
| :------------------| :-----------| :-----------| :--------|
| module             | all_in_list | fixed value | line 5   |
| module             | all_in_dict | fixed value | line 8   |
| module.show_spread | left        | fixed value | line 1   |
| module.show_spread | middle      | fixed value | line 1   |
| module.show_spread | right       | fixed value | line 1   |

## varargs.py

### Static analysis

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.show_args | args     | fixed value | line 1   |
| module.show_args | kwargs   | fixed value | line 1   |
| module.show_args | title    | fixed value | line 1   |

