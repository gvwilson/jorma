# Variable Role Analysis: oop

## func_obj.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | alias    | fixed value | line 7   |

## inherit_class.py

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Shape       | fixed value        | line 7   |
| module                  | Square      | fixed value        | line 27  |
| module                  | Circle      | fixed value        | line 48  |
| module                  | examples    | fixed value        | line 76  |
| module                  | ex          | stepper            | line 77  |
| module                  | n           | most-recent holder | line 78  |
| module                  | d           | most-recent holder | line 79  |
| module.call             | args        | fixed value        | line 63  |
| module.call             | method_name | fixed value        | line 63  |
| module.call             | thing       | fixed value        | line 63  |
| module.call             | method      | fixed value        | line 64  |
| module.circle_area      | thing       | fixed value        | line 45  |
| module.circle_new       | name        | fixed value        | line 55  |
| module.circle_new       | radius      | fixed value        | line 55  |
| module.circle_perimeter | thing       | fixed value        | line 42  |
| module.find             | cls         | stepper            | line 67  |
| module.find             | method_name | fixed value        | line 67  |
| module.shape_density    | thing       | fixed value        | line 4   |
| module.shape_density    | weight      | fixed value        | line 4   |
| module.shape_new        | name        | fixed value        | line 14  |
| module.square_area      | thing       | fixed value        | line 23  |
| module.square_new       | name        | fixed value        | line 35  |
| module.square_new       | side        | fixed value        | line 35  |
| module.square_perimeter | thing       | fixed value        | line 20  |

## inherit_constructor.py

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Shape       | fixed value        | line 13  |
| module                  | Square      | fixed value        | line 39  |
| module                  | Circle      | fixed value        | line 60  |
| module                  | examples    | fixed value        | line 80  |
| module                  | ex          | stepper            | line 81  |
| module                  | n           | most-recent holder | line 82  |
| module                  | d           | most-recent holder | line 83  |
| module.call             | args        | fixed value        | line 75  |
| module.call             | method_name | fixed value        | line 75  |
| module.call             | thing       | fixed value        | line 75  |
| module.call             | method      | fixed value        | line 76  |
| module.circle_area      | thing       | fixed value        | line 51  |
| module.circle_new       | name        | fixed value        | line 54  |
| module.circle_new       | radius      | fixed value        | line 54  |
| module.circle_perimeter | thing       | fixed value        | line 48  |
| module.find             | cls         | fixed value        | line 68  |
| module.find             | method_name | fixed value        | line 68  |
| module.make             | args        | fixed value        | line 22  |
| module.make             | cls         | fixed value        | line 22  |
| module.shape_density    | thing       | fixed value        | line 3   |
| module.shape_density    | weight      | fixed value        | line 3   |
| module.shape_new        | name        | fixed value        | line 7   |
| module.square_area      | thing       | fixed value        | line 29  |
| module.square_new       | name        | fixed value        | line 33  |
| module.square_new       | side        | fixed value        | line 33  |
| module.square_perimeter | thing       | fixed value        | line 26  |

## inherit_original.py

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

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Square      | fixed value        | line 13  |
| module                  | Circle      | fixed value        | line 39  |
| module                  | examples    | fixed value        | line 59  |
| module                  | ex          | stepper            | line 60  |
| module                  | result      | most-recent holder | line 61  |
| module.call             | args        | fixed value        | line 54  |
| module.call             | method_name | fixed value        | line 54  |
| module.call             | thing       | fixed value        | line 54  |
| module.circle_area      | thing       | fixed value        | line 31  |
| module.circle_larger    | size        | fixed value        | line 35  |
| module.circle_larger    | thing       | fixed value        | line 35  |
| module.circle_new       | name        | fixed value        | line 46  |
| module.circle_new       | radius      | fixed value        | line 46  |
| module.circle_perimeter | thing       | fixed value        | line 28  |
| module.square_area      | thing       | fixed value        | line 6   |
| module.square_larger    | size        | fixed value        | line 10  |
| module.square_larger    | thing       | fixed value        | line 10  |
| module.square_new       | name        | fixed value        | line 21  |
| module.square_new       | side        | fixed value        | line 21  |
| module.square_perimeter | thing       | fixed value        | line 3   |

## shapes_class.py

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | Square      | fixed value        | line 10  |
| module                  | Circle      | fixed value        | line 30  |
| module                  | examples    | fixed value        | line 47  |
| module                  | ex          | stepper            | line 48  |
| module                  | n           | most-recent holder | line 49  |
| module                  | p           | most-recent holder | line 50  |
| module                  | a           | most-recent holder | line 51  |
| module                  | c           | most-recent holder | line 52  |
| module.call             | method_name | fixed value        | line 44  |
| module.call             | thing       | fixed value        | line 44  |
| module.circle_area      | thing       | fixed value        | line 27  |
| module.circle_new       | name        | fixed value        | line 36  |
| module.circle_new       | radius      | fixed value        | line 36  |
| module.circle_perimeter | thing       | fixed value        | line 24  |
| module.square_area      | thing       | fixed value        | line 7   |
| module.square_new       | name        | fixed value        | line 16  |
| module.square_new       | side        | fixed value        | line 16  |
| module.square_perimeter | thing       | fixed value        | line 4   |

## shapes_dict.py

| Scope                   | Variable    | Role               | Location |
| :-----------------------| :-----------| :------------------| :--------|
| module                  | examples    | fixed value        | line 37  |
| module                  | ex          | stepper            | line 38  |
| module                  | n           | most-recent holder | line 39  |
| module                  | p           | most-recent holder | line 40  |
| module                  | a           | most-recent holder | line 41  |
| module.call             | method_name | fixed value        | line 34  |
| module.call             | thing       | fixed value        | line 34  |
| module.circle_area      | thing       | fixed value        | line 22  |
| module.circle_new       | name        | fixed value        | line 25  |
| module.circle_new       | radius      | fixed value        | line 25  |
| module.circle_perimeter | thing       | fixed value        | line 19  |
| module.square_area      | thing       | fixed value        | line 7   |
| module.square_new       | name        | fixed value        | line 10  |
| module.square_new       | side        | fixed value        | line 10  |
| module.square_perimeter | thing       | fixed value        | line 4   |

## shapes_original.py

| Scope                   | Variable | Role               | Location |
| :-----------------------| :--------| :------------------| :--------|
| module                  | examples | fixed value        | line 40  |
| module                  | thing    | stepper            | line 41  |
| module                  | n        | most-recent holder | line 42  |
| module                  | p        | most-recent holder | line 43  |
| module                  | a        | most-recent holder | line 44  |
| module.Circle.__init__  | name     | fixed value        | line 28  |
| module.Circle.__init__  | radius   | fixed value        | line 28  |
| module.Circle.__init__  | self     | fixed value        | line 28  |
| module.Circle.area      | self     | fixed value        | line 35  |
| module.Circle.perimeter | self     | fixed value        | line 32  |
| module.Shape.__init__   | name     | fixed value        | line 5   |
| module.Shape.__init__   | self     | fixed value        | line 5   |
| module.Shape.area       | self     | fixed value        | line 11  |
| module.Shape.perimeter  | self     | fixed value        | line 8   |
| module.Square.__init__  | name     | fixed value        | line 17  |
| module.Square.__init__  | self     | fixed value        | line 17  |
| module.Square.__init__  | side     | fixed value        | line 17  |
| module.Square.area      | self     | fixed value        | line 24  |
| module.Square.perimeter | self     | fixed value        | line 21  |

## spread.py

| Scope              | Variable    | Role        | Location |
| :------------------| :-----------| :-----------| :--------|
| module             | all_in_list | fixed value | line 4   |
| module             | all_in_dict | fixed value | line 7   |
| module.show_spread | left        | fixed value | line 1   |
| module.show_spread | middle      | fixed value | line 1   |
| module.show_spread | right       | fixed value | line 1   |

## varargs.py

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.show_args | args     | fixed value | line 1   |
| module.show_args | kwargs   | fixed value | line 1   |
| module.show_args | title    | fixed value | line 1   |

