# Page Layout

## easy_mode.py

| Variable | Scope | Role |
|---|---|---|
| height | module.Block.__init__ | fixed value |
| self | module.Block.__init__ | fixed value |
| width | module.Block.__init__ | fixed value |
| self | module.Block.get_height | fixed value |
| self | module.Block.get_width | fixed value |
| children | module.Col.__init__ | fixed value |
| self | module.Col.__init__ | fixed value |
| self | module.Col.get_height | fixed value |
| self | module.Col.get_width | fixed value |
| children | module.Row.__init__ | fixed value |
| self | module.Row.__init__ | fixed value |
| self | module.Row.get_height | fixed value |
| self | module.Row.get_width | fixed value |

## test_easy_mode.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.test_lays_out_a_column_of_two_blocks | fixed value |
| fixture | module.test_lays_out_a_grid_of_rows_of_columns | fixed value |
| fixture | module.test_lays_out_a_large_block | fixed value |
| fixture | module.test_lays_out_a_row_of_two_blocks | fixed value |
| fixture | module.test_lays_out_a_single_unit_block | fixed value |

## placed.py

| Variable | Scope | Role |
|---|---|---|
| height | module.PlacedBlock.__init__ | fixed value |
| self | module.PlacedBlock.__init__ | fixed value |
| width | module.PlacedBlock.__init__ | fixed value |
| self | module.PlacedBlock.place | fixed value |
| x0 | module.PlacedBlock.place | fixed value |
| y0 | module.PlacedBlock.place | fixed value |
| self | module.PlacedBlock.report | fixed value |
| children | module.PlacedCol.__init__ | fixed value |
| self | module.PlacedCol.__init__ | fixed value |
| self | module.PlacedCol.place | fixed value |
| x0 | module.PlacedCol.place | fixed value |
| y0 | module.PlacedCol.place | fixed value |
| y_current | module.PlacedCol.place | gatherer |
| child | module.PlacedCol.place | stepper |
| self | module.PlacedCol.report | fixed value |
| children | module.PlacedRow.__init__ | fixed value |
| self | module.PlacedRow.__init__ | fixed value |
| self | module.PlacedRow.place | fixed value |
| x0 | module.PlacedRow.place | fixed value |
| y0 | module.PlacedRow.place | fixed value |
| y1 | module.PlacedRow.place | fixed value |
| x_current | module.PlacedRow.place | gatherer |
| child | module.PlacedRow.place | stepper |
| child_y | module.PlacedRow.place | most-recent holder |
| self | module.PlacedRow.report | fixed value |

## test_placed.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.test_places_a_column_of_two_blocks | fixed value |
| fixture | module.test_places_a_grid_of_rows_of_columns | fixed value |
| fixture | module.test_places_a_large_block | fixed value |
| fixture | module.test_places_a_row_of_two_blocks | fixed value |
| fixture | module.test_places_a_single_unit_block | fixed value |

## render.py

| Variable | Scope | Role |
|---|---|---|
| fill | module.draw | gatherer |
| node | module.draw | fixed value |
| screen | module.draw | fixed value |
| child | module.draw | stepper |
| height | module.make_screen | fixed value |
| width | module.make_screen | fixed value |
| screen | module.make_screen | log |
| i | module.make_screen | stepper |
| fill | module.next_fill | fixed value |
| root | module.render | fixed value |
| width | module.render | fixed value |
| height | module.render | fixed value |
| screen | module.render | fixed value |

## rendered.py

| Variable | Scope | Role |
|---|---|---|
| fill | module.Renderable.render | fixed value |
| screen | module.Renderable.render | fixed value |
| self | module.Renderable.render | fixed value |
| ix | module.Renderable.render | stepper |
| iy | module.Renderable.render | stepper |

## test_rendered.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.test_renders_a_column_of_two_blocks | fixed value |
| expected | module.test_renders_a_column_of_two_blocks | fixed value |
| fixture | module.test_renders_a_grid_of_rows_of_columns | fixed value |
| fixture | module.test_renders_a_large_block | fixed value |
| fixture | module.test_renders_a_row_of_two_blocks | fixed value |
| fixture | module.test_renders_a_single_unit_block | fixed value |

## wrapped.py

| Variable | Scope | Role |
|---|---|---|
| self | module.WrappedBlock.wrap | fixed value |
| self | module.WrappedCol.wrap | fixed value |
| children | module.WrappedRow.__init__ | fixed value |
| self | module.WrappedRow.__init__ | fixed value |
| width | module.WrappedRow.__init__ | fixed value |
| children | module.WrappedRow._bucket | fixed value |
| self | module.WrappedRow._bucket | fixed value |
| result | module.WrappedRow._bucket | log |
| current_row | module.WrappedRow._bucket | log |
| current_x | module.WrappedRow._bucket | gatherer |
| child | module.WrappedRow._bucket | stepper |
| child_width | module.WrappedRow._bucket | most-recent holder |
| self | module.WrappedRow.get_width | fixed value |
| self | module.WrappedRow.wrap | fixed value |
| children | module.WrappedRow.wrap | fixed value |
| rows | module.WrappedRow.wrap | fixed value |
| new_rows | module.WrappedRow.wrap | fixed value |
| new_col | module.WrappedRow.wrap | fixed value |

## test_wrapped.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row | fixed value |
| wrapped | module.test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row | fixed value |
| fixture | module.test_wrap_a_row_of_two_blocks_that_fit_on_one_row | fixed value |
| wrapped | module.test_wrap_a_row_of_two_blocks_that_fit_on_one_row | fixed value |
| fixture | module.test_wrap_multiple_blocks_that_do_not_fit_on_one_row | fixed value |
| wrapped | module.test_wrap_multiple_blocks_that_do_not_fit_on_one_row | fixed value |
| fixture | module.test_wraps_a_column_of_two_blocks | fixed value |
| wrapped | module.test_wraps_a_column_of_two_blocks | fixed value |
| fixture | module.test_wraps_a_grid_of_rows_of_columns_that_all_fit_on_their_row | fixed value |
| wrapped | module.test_wraps_a_grid_of_rows_of_columns_that_all_fit_on_their_row | fixed value |
| fixture | module.test_wraps_a_large_block | fixed value |
| wrapped | module.test_wraps_a_large_block | fixed value |
| fixture | module.test_wraps_a_single_unit_block | fixed value |
| wrapped | module.test_wraps_a_single_unit_block | fixed value |

