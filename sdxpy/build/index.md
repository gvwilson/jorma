# Variable Role Analysis: build

## build_better.py

| Scope                          | Variable  | Role               | Location |
| :------------------------------| :---------| :------------------| :--------|
| module                         | reader    | fixed value        | line 68  |
| module                         | config    | fixed value        | line 69  |
| module                         | builder   | fixed value        | line 70  |
| module                         | actions   | fixed value        | line 71  |
| module                         | a         | stepper            | line 72  |
| module.BuildBetter._check      | details   | fixed value        | line 30  |
| module.BuildBetter._check      | known     | fixed value        | line 30  |
| module.BuildBetter._check      | name      | fixed value        | line 30  |
| module.BuildBetter._check      | self      | fixed value        | line 30  |
| module.BuildBetter._check      | depends   | fixed value        | line 32  |
| module.BuildBetter._check      | result    | fixed value        | line 36  |
| module.BuildBetter._check_keys | details   | fixed value        | line 40  |
| module.BuildBetter._check_keys | name      | fixed value        | line 40  |
| module.BuildBetter._check_keys | self      | fixed value        | line 40  |
| module.BuildBetter._configure  | config    | fixed value        | line 25  |
| module.BuildBetter._configure  | self      | fixed value        | line 25  |
| module.BuildBetter._configure  | known     | fixed value        | line 26  |
| module.BuildBetter._must       | condition | fixed value        | line 19  |
| module.BuildBetter._must       | message   | fixed value        | line 19  |
| module.BuildBetter._must       | self      | fixed value        | line 19  |
| module.BuildBetter._refresh    | actions   | log                | line 15  |
| module.BuildBetter._refresh    | config    | fixed value        | line 15  |
| module.BuildBetter._refresh    | node      | fixed value        | line 15  |
| module.BuildBetter._refresh    | self      | fixed value        | line 15  |
| module.BuildBetter._topo_sort  | config    | fixed value        | line 48  |
| module.BuildBetter._topo_sort  | self      | fixed value        | line 48  |
| module.BuildBetter._topo_sort  | graph     | gatherer           | line 49  |
| module.BuildBetter._topo_sort  | result    | log                | line 50  |
| module.BuildBetter._topo_sort  | available | most-recent holder | line 52  |
| module.BuildBetter.build       | config    | unknown            | line 7   |
| module.BuildBetter.build       | self      | fixed value        | line 7   |
| module.BuildBetter.build       | ordered   | fixed value        | line 9   |
| module.BuildBetter.build       | actions   | fixed value        | line 10  |
| module.BuildBetter.build       | node      | stepper            | line 11  |

## build_simple.py

| Scope                       | Variable    | Role               | Location |
| :---------------------------| :-----------| :------------------| :--------|
| module                      | builder     | fixed value        | line 57  |
| module.BuildBase._check     | details     | fixed value        | line 30  |
| module.BuildBase._check     | known       | fixed value        | line 30  |
| module.BuildBase._check     | name        | fixed value        | line 30  |
| module.BuildBase._check     | self        | fixed value        | line 30  |
| module.BuildBase._check     | depends     | fixed value        | line 33  |
| module.BuildBase._configure | config_file | fixed value        | line 19  |
| module.BuildBase._configure | self        | fixed value        | line 19  |
| module.BuildBase._configure | reader      | fixed value        | line 20  |
| module.BuildBase._configure | config      | fixed value        | line 21  |
| module.BuildBase._configure | known       | fixed value        | line 22  |
| module.BuildBase._refresh   | config      | fixed value        | line 13  |
| module.BuildBase._refresh   | node        | fixed value        | line 13  |
| module.BuildBase._refresh   | self        | fixed value        | line 13  |
| module.BuildBase._topo_sort | config      | fixed value        | line 40  |
| module.BuildBase._topo_sort | self        | fixed value        | line 40  |
| module.BuildBase._topo_sort | graph       | gatherer           | line 41  |
| module.BuildBase._topo_sort | result      | log                | line 42  |
| module.BuildBase._topo_sort | available   | most-recent holder | line 44  |
| module.BuildBase.build      | config_file | fixed value        | line 7   |
| module.BuildBase.build      | self        | fixed value        | line 7   |
| module.BuildBase.build      | config      | fixed value        | line 8   |
| module.BuildBase.build      | ordered     | fixed value        | line 9   |
| module.BuildBase.build      | node        | stepper            | line 10  |

## build_time.py

| Scope                          | Variable | Role        | Location |
| :------------------------------| :--------| :-----------| :--------|
| module                         | reader   | fixed value | line 27  |
| module                         | config   | fixed value | line 28  |
| module                         | builder  | fixed value | line 29  |
| module                         | actions  | fixed value | line 30  |
| module                         | a        | stepper     | line 31  |
| module.BuildTime._check_keys   | details  | fixed value | line 9   |
| module.BuildTime._check_keys   | name     | fixed value | line 9   |
| module.BuildTime._check_keys   | self     | fixed value | line 9   |
| module.BuildTime._needs_update | config   | fixed value | line 18  |
| module.BuildTime._needs_update | node     | fixed value | line 18  |
| module.BuildTime._needs_update | self     | fixed value | line 18  |
| module.BuildTime._refresh      | actions  | log         | line 13  |
| module.BuildTime._refresh      | config   | fixed value | line 13  |
| module.BuildTime._refresh      | node     | fixed value | line 13  |
| module.BuildTime._refresh      | self     | fixed value | line 13  |

## test_build_better.py

| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module.test_circular    | action_A | fixed value | line 16  |
| module.test_circular    | action_B | fixed value | line 17  |
| module.test_circular    | config   | fixed value | line 18  |
| module.test_diamond_dep | action_A | fixed value | line 52  |
| module.test_diamond_dep | action_B | fixed value | line 53  |
| module.test_diamond_dep | action_C | fixed value | line 54  |
| module.test_diamond_dep | action_D | fixed value | line 55  |
| module.test_diamond_dep | config   | fixed value | line 56  |
| module.test_linear_dep  | action_A | fixed value | line 42  |
| module.test_linear_dep  | action_B | fixed value | line 43  |
| module.test_linear_dep  | config   | fixed value | line 44  |
| module.test_no_dep      | action_A | fixed value | line 31  |
| module.test_no_dep      | action_B | fixed value | line 32  |
| module.test_no_dep      | config   | fixed value | line 33  |
| module.test_single      | action_A | fixed value | line 9   |
| module.test_single      | config   | fixed value | line 10  |

## test_build_time.py

| Scope                                 | Variable | Role        | Location |
| :-------------------------------------| :--------| :-----------| :--------|
| module.test_circular                  | action_A | fixed value | line 15  |
| module.test_circular                  | action_B | fixed value | line 16  |
| module.test_circular                  | config   | fixed value | line 17  |
| module.test_diamond_dep               | action_A | fixed value | line 60  |
| module.test_diamond_dep               | action_B | fixed value | line 61  |
| module.test_diamond_dep               | action_C | fixed value | line 62  |
| module.test_diamond_dep               | action_D | fixed value | line 63  |
| module.test_diamond_dep               | config   | fixed value | line 64  |
| module.test_linear_dep_needs_update   | action_A | fixed value | line 39  |
| module.test_linear_dep_needs_update   | action_B | fixed value | line 40  |
| module.test_linear_dep_needs_update   | config   | fixed value | line 41  |
| module.test_linear_dep_no_need_update | action_A | fixed value | line 49  |
| module.test_linear_dep_no_need_update | action_B | fixed value | line 50  |
| module.test_linear_dep_no_need_update | config   | fixed value | line 51  |
| module.test_no_dep                    | action_A | fixed value | line 29  |
| module.test_no_dep                    | action_B | fixed value | line 30  |
| module.test_no_dep                    | config   | fixed value | line 31  |
| module.test_single                    | action_A | fixed value | line 9   |
| module.test_single                    | config   | fixed value | line 10  |

