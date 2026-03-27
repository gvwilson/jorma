# Variable Role Analysis: layout

## easy_mode.py

```

[module.Block.__init__]
  height                   fixed value             (line 3)
  self                     fixed value             (line 3)
  width                    fixed value             (line 3)

[module.Block.get_height]
  self                     fixed value             (line 10)

[module.Block.get_width]
  self                     fixed value             (line 7)

[module.Col.__init__]
  children                 fixed value             (line 31)
  self                     fixed value             (line 31)

[module.Col.get_height]
  self                     fixed value             (line 40)

[module.Col.get_width]
  self                     fixed value             (line 34)

[module.Row.__init__]
  children                 fixed value             (line 16)
  self                     fixed value             (line 16)

[module.Row.get_height]
  self                     fixed value             (line 22)

[module.Row.get_width]
  self                     fixed value             (line 19)
```

## placed.py

```

[module.PlacedBlock.__init__]
  height                   fixed value             (line 5)
  self                     fixed value             (line 5)
  width                    fixed value             (line 5)

[module.PlacedBlock.place]
  self                     fixed value             (line 10)
  x0                       fixed value             (line 10)
  y0                       fixed value             (line 10)

[module.PlacedBlock.report]
  self                     fixed value             (line 14)

[module.PlacedCol.__init__]
  children                 fixed value             (line 23)
  self                     fixed value             (line 23)

[module.PlacedCol.place]
  self                     fixed value             (line 30)
  x0                       fixed value             (line 30)
  y0                       fixed value             (line 30)
  y_current                gatherer                (line 33)
  child                    stepper                 (line 34)

[module.PlacedCol.report]
  self                     fixed value             (line 39)

[module.PlacedRow.__init__]
  children                 fixed value             (line 47)
  self                     fixed value             (line 47)

[module.PlacedRow.place]
  self                     fixed value             (line 54)
  x0                       fixed value             (line 54)
  y0                       fixed value             (line 54)
  y1                       fixed value             (line 57)
  x_current                gatherer                (line 58)
  child                    stepper                 (line 59)
  child_y                  most-recent holder      (line 60)

[module.PlacedRow.report]
  self                     fixed value             (line 65)
```

## render.py

```

[module.draw]
  fill                     gatherer                (line 19)
  node                     fixed value             (line 19)
  screen                   fixed value             (line 19)
  child                    stepper                 (line 23)

[module.make_screen]
  height                   fixed value             (line 11)
  width                    fixed value             (line 11)
  screen                   log                     (line 12)
  i                        stepper                 (line 13)

[module.next_fill]
  fill                     fixed value             (line 27)

[module.render]
  root                     fixed value             (line 1)
  width                    fixed value             (line 3)
  height                   fixed value             (line 4)
  screen                   fixed value             (line 5)
```

## rendered.py

```

[module.Renderable.render]
  fill                     fixed value             (line 5)
  screen                   fixed value             (line 5)
  self                     fixed value             (line 5)
  ix                       stepper                 (line 6)
  iy                       stepper                 (line 7)
```

## test_easy_mode.py

```

[module.test_lays_out_a_column_of_two_blocks]
  fixture                  fixed value             (line 19)

[module.test_lays_out_a_grid_of_rows_of_columns]
  fixture                  fixed value             (line 25)

[module.test_lays_out_a_large_block]
  fixture                  fixed value             (line 9)

[module.test_lays_out_a_row_of_two_blocks]
  fixture                  fixed value             (line 14)

[module.test_lays_out_a_single_unit_block]
  fixture                  fixed value             (line 4)
```

## test_placed.py

```

[module.test_places_a_column_of_two_blocks]
  fixture                  fixed value             (line 27)

[module.test_places_a_grid_of_rows_of_columns]
  fixture                  fixed value             (line 38)

[module.test_places_a_large_block]
  fixture                  fixed value             (line 11)

[module.test_places_a_row_of_two_blocks]
  fixture                  fixed value             (line 16)

[module.test_places_a_single_unit_block]
  fixture                  fixed value             (line 6)
```

## test_rendered.py

```

[module.test_renders_a_column_of_two_blocks]
  fixture                  fixed value             (line 23)
  expected                 fixed value             (line 25)

[module.test_renders_a_grid_of_rows_of_columns]
  fixture                  fixed value             (line 30)

[module.test_renders_a_large_block]
  fixture                  fixed value             (line 12)

[module.test_renders_a_row_of_two_blocks]
  fixture                  fixed value             (line 17)

[module.test_renders_a_single_unit_block]
  fixture                  fixed value             (line 7)
```

## test_wrapped.py

```

[module.test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row]
  fixture                  fixed value             (line 112)
  wrapped                  fixed value             (line 113)

[module.test_wrap_a_row_of_two_blocks_that_fit_on_one_row]
  fixture                  fixed value             (line 16)
  wrapped                  fixed value             (line 17)

[module.test_wrap_multiple_blocks_that_do_not_fit_on_one_row]
  fixture                  fixed value             (line 128)
  wrapped                  fixed value             (line 129)

[module.test_wraps_a_column_of_two_blocks]
  fixture                  fixed value             (line 36)
  wrapped                  fixed value             (line 37)

[module.test_wraps_a_grid_of_rows_of_columns_that_all_fit_on_their_row]
  fixture                  fixed value             (line 50)
  wrapped                  fixed value             (line 54)

[module.test_wraps_a_large_block]
  fixture                  fixed value             (line 10)
  wrapped                  fixed value             (line 11)

[module.test_wraps_a_single_unit_block]
  fixture                  fixed value             (line 4)
  wrapped                  fixed value             (line 5)
```

## wrapped.py

```

[module.WrappedBlock.wrap]
  self                     fixed value             (line 5)

[module.WrappedCol.wrap]
  self                     fixed value             (line 9)

[module.WrappedRow.__init__]
  children                 fixed value             (line 15)
  self                     fixed value             (line 15)
  width                    fixed value             (line 15)

[module.WrappedRow._bucket]
  children                 fixed value             (line 34)
  self                     fixed value             (line 34)
  result                   log                     (line 35)
  current_row              log                     (line 36)
  current_x                gatherer                (line 37)
  child                    stepper                 (line 39)
  child_width              most-recent holder      (line 40)

[module.WrappedRow.get_width]
  self                     fixed value             (line 20)

[module.WrappedRow.wrap]
  self                     fixed value             (line 25)
  children                 fixed value             (line 26)
  rows                     fixed value             (line 27)
  new_rows                 fixed value             (line 28)
  new_col                  fixed value             (line 29)
```

