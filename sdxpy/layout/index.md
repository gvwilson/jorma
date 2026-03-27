# layout
| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module.Block.__init__   | height   | fixed value | line 2   |
| module.Block.__init__   | self     | fixed value | line 2   |
| module.Block.__init__   | width    | fixed value | line 2   |
| module.Block.get_height | self     | fixed value | line 9   |
| module.Block.get_width  | self     | fixed value | line 6   |
| module.Col.__init__     | children | fixed value | line 25  |
| module.Col.__init__     | self     | fixed value | line 25  |
| module.Col.get_height   | self     | fixed value | line 31  |
| module.Col.get_width    | self     | fixed value | line 28  |
| module.Row.__init__     | children | fixed value | line 14  |
| module.Row.__init__     | self     | fixed value | line 14  |
| module.Row.get_height   | self     | fixed value | line 20  |
| module.Row.get_width    | self     | fixed value | line 17  |
| Scope                       | Variable  | Role               | Location |
| :---------------------------| :---------| :------------------| :--------|
| module.PlacedBlock.__init__ | height    | fixed value        | line 5   |
| module.PlacedBlock.__init__ | self      | fixed value        | line 5   |
| module.PlacedBlock.__init__ | width     | fixed value        | line 5   |
| module.PlacedBlock.place    | self      | fixed value        | line 10  |
| module.PlacedBlock.place    | x0        | fixed value        | line 10  |
| module.PlacedBlock.place    | y0        | fixed value        | line 10  |
| module.PlacedBlock.report   | self      | fixed value        | line 14  |
| module.PlacedCol.__init__   | children  | fixed value        | line 19  |
| module.PlacedCol.__init__   | self      | fixed value        | line 19  |
| module.PlacedCol.place      | self      | fixed value        | line 25  |
| module.PlacedCol.place      | x0        | fixed value        | line 25  |
| module.PlacedCol.place      | y0        | fixed value        | line 25  |
| module.PlacedCol.place      | y_current | gatherer           | line 28  |
| module.PlacedCol.place      | child     | stepper            | line 29  |
| module.PlacedCol.report     | self      | fixed value        | line 33  |
| module.PlacedRow.__init__   | children  | fixed value        | line 44  |
| module.PlacedRow.__init__   | self      | fixed value        | line 44  |
| module.PlacedRow.place      | self      | fixed value        | line 50  |
| module.PlacedRow.place      | x0        | fixed value        | line 50  |
| module.PlacedRow.place      | y0        | fixed value        | line 50  |
| module.PlacedRow.place      | y1        | fixed value        | line 53  |
| module.PlacedRow.place      | x_current | gatherer           | line 54  |
| module.PlacedRow.place      | child     | stepper            | line 55  |
| module.PlacedRow.place      | child_y   | most-recent holder | line 56  |
| module.PlacedRow.report     | self      | fixed value        | line 60  |
| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.draw        | fill     | gatherer    | line 17  |
| module.draw        | node     | fixed value | line 17  |
| module.draw        | screen   | fixed value | line 17  |
| module.draw        | child    | stepper     | line 21  |
| module.make_screen | height   | fixed value | line 10  |
| module.make_screen | width    | fixed value | line 10  |
| module.make_screen | screen   | log         | line 11  |
| module.make_screen | i        | stepper     | line 12  |
| module.next_fill   | fill     | fixed value | line 26  |
| module.render      | root     | fixed value | line 1   |
| module.render      | width    | fixed value | line 3   |
| module.render      | height   | fixed value | line 4   |
| module.render      | screen   | fixed value | line 5   |
| Scope                    | Variable | Role        | Location |
| :------------------------| :--------| :-----------| :--------|
| module.Renderable.render | fill     | fixed value | line 5   |
| module.Renderable.render | screen   | fixed value | line 5   |
| module.Renderable.render | self     | fixed value | line 5   |
| module.Renderable.render | ix       | stepper     | line 6   |
| module.Renderable.render | iy       | stepper     | line 7   |
| Scope                                          | Variable | Role        | Location |
| :----------------------------------------------| :--------| :-----------| :--------|
| module.test_lays_out_a_column_of_two_blocks    | fixture  | fixed value | line 23  |
| module.test_lays_out_a_grid_of_rows_of_columns | fixture  | fixed value | line 29  |
| module.test_lays_out_a_large_block             | fixture  | fixed value | line 11  |
| module.test_lays_out_a_row_of_two_blocks       | fixture  | fixed value | line 17  |
| module.test_lays_out_a_single_unit_block       | fixture  | fixed value | line 5   |
| Scope                                        | Variable | Role        | Location |
| :--------------------------------------------| :--------| :-----------| :--------|
| module.test_places_a_column_of_two_blocks    | fixture  | fixed value | line 33  |
| module.test_places_a_grid_of_rows_of_columns | fixture  | fixed value | line 47  |
| module.test_places_a_large_block             | fixture  | fixed value | line 13  |
| module.test_places_a_row_of_two_blocks       | fixture  | fixed value | line 19  |
| module.test_places_a_single_unit_block       | fixture  | fixed value | line 7   |
| Scope                                         | Variable | Role        | Location |
| :---------------------------------------------| :--------| :-----------| :--------|
| module.test_renders_a_column_of_two_blocks    | fixture  | fixed value | line 26  |
| module.test_renders_a_column_of_two_blocks    | expected | fixed value | line 28  |
| module.test_renders_a_grid_of_rows_of_columns | fixture  | fixed value | line 33  |
| module.test_renders_a_large_block             | fixture  | fixed value | line 14  |
| module.test_renders_a_row_of_two_blocks       | fixture  | fixed value | line 20  |
| module.test_renders_a_single_unit_block       | fixture  | fixed value | line 8   |
| Scope                                                                 | Variable | Role        | Location |
| :---------------------------------------------------------------------| :--------| :-----------| :--------|
| module.test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row       | fixture  | fixed value | line 119 |
| module.test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row       | wrapped  | fixed value | line 120 |
| module.test_wrap_a_row_of_two_blocks_that_fit_on_one_row              | fixture  | fixed value | line 19  |
| module.test_wrap_a_row_of_two_blocks_that_fit_on_one_row              | wrapped  | fixed value | line 20  |
| module.test_wrap_multiple_blocks_that_do_not_fit_on_one_row           | fixture  | fixed value | line 141 |
| module.test_wrap_multiple_blocks_that_do_not_fit_on_one_row           | wrapped  | fixed value | line 148 |
| module.test_wraps_a_column_of_two_blocks                              | fixture  | fixed value | line 40  |
| module.test_wraps_a_column_of_two_blocks                              | wrapped  | fixed value | line 41  |
| module.test_wraps_a_grid_of_rows_of_columns_that_all_fit_on_their_row | fixture  | fixed value | line 55  |
| module.test_wraps_a_grid_of_rows_of_columns_that_all_fit_on_their_row | wrapped  | fixed value | line 61  |
| module.test_wraps_a_large_block                                       | fixture  | fixed value | line 12  |
| module.test_wraps_a_large_block                                       | wrapped  | fixed value | line 13  |
| module.test_wraps_a_single_unit_block                                 | fixture  | fixed value | line 5   |
| module.test_wraps_a_single_unit_block                                 | wrapped  | fixed value | line 6   |
| Scope                       | Variable    | Role               | Location |
| :---------------------------| :-----------| :------------------| :--------|
| module.WrappedBlock.wrap    | self        | fixed value        | line 5   |
| module.WrappedCol.wrap      | self        | fixed value        | line 10  |
| module.WrappedRow.__init__  | children    | fixed value        | line 15  |
| module.WrappedRow.__init__  | self        | fixed value        | line 15  |
| module.WrappedRow.__init__  | width       | fixed value        | line 15  |
| module.WrappedRow._bucket   | children    | fixed value        | line 30  |
| module.WrappedRow._bucket   | self        | fixed value        | line 30  |
| module.WrappedRow._bucket   | result      | log                | line 31  |
| module.WrappedRow._bucket   | current_row | log                | line 32  |
| module.WrappedRow._bucket   | current_x   | gatherer           | line 33  |
| module.WrappedRow._bucket   | child       | stepper            | line 35  |
| module.WrappedRow._bucket   | child_width | most-recent holder | line 36  |
| module.WrappedRow.get_width | self        | fixed value        | line 20  |
| module.WrappedRow.wrap      | self        | fixed value        | line 23  |
| module.WrappedRow.wrap      | children    | fixed value        | line 24  |
| module.WrappedRow.wrap      | rows        | fixed value        | line 25  |
| module.WrappedRow.wrap      | new_rows    | fixed value        | line 26  |
| module.WrappedRow.wrap      | new_col     | fixed value        | line 27  |
