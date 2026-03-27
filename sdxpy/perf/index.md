# Performance Profiling

## df_base.py

| Variable | Scope | Role |
|---|---|---|
| self | module.DataFrame.cols | fixed value |
| other | module.DataFrame.eq | fixed value |
| self | module.DataFrame.eq | fixed value |
| func | module.DataFrame.filter | fixed value |
| self | module.DataFrame.filter | fixed value |
| col | module.DataFrame.get | fixed value |
| row | module.DataFrame.get | fixed value |
| self | module.DataFrame.get | fixed value |
| self | module.DataFrame.ncol | fixed value |
| self | module.DataFrame.nrow | fixed value |
| names | module.DataFrame.select | fixed value |
| self | module.DataFrame.select | fixed value |

## df_row.py

| Variable | Scope | Role |
|---|---|---|
| rows | module.DfRow.__init__ | fixed value |
| self | module.DfRow.__init__ | fixed value |
| self | module.DfRow.__str__ | fixed value |
| self | module.DfRow.cols | fixed value |
| other | module.DfRow.eq | fixed value |
| self | module.DfRow.eq | fixed value |
| i | module.DfRow.eq | stepper |
| row | module.DfRow.eq | stepper |
| key | module.DfRow.eq | stepper |
| func | module.DfRow.filter | fixed value |
| self | module.DfRow.filter | fixed value |
| result | module.DfRow.filter | fixed value |
| col | module.DfRow.get | fixed value |
| row | module.DfRow.get | fixed value |
| self | module.DfRow.get | fixed value |
| self | module.DfRow.ncol | fixed value |
| self | module.DfRow.nrow | fixed value |
| names | module.DfRow.select | fixed value |
| self | module.DfRow.select | fixed value |
| rows | module.DfRow.select | fixed value |

## util.py

| Variable | Scope | Role |
|---|---|---|
| values | module.all_eq | fixed value |
| d | module.dict_match | fixed value |
| prototype | module.dict_match | fixed value |

## test_df_row.py

| Variable | Scope | Role |
|---|---|---|
| df | module.test_construct_with_single_value | fixed value |
| df | module.test_construct_with_two_pairs | fixed value |
| left | module.test_equality | fixed value |
| right | module.test_equality | fixed value |
| df | module.test_filter | fixed value |
| a | module.test_filter.odd | fixed value |
| b | module.test_filter.odd | fixed value |
| repeated | module.test_inequality | fixed value |
| df | module.test_ncol | fixed value |
| df | module.test_nrow | fixed value |
| selected | module.test_select | fixed value |

## df_col.py

| Variable | Scope | Role |
|---|---|---|
| kwargs | module.DfCol.__init__ | fixed value |
| self | module.DfCol.__init__ | fixed value |
| k | module.DfCol.__init__ | stepper |
| self | module.DfCol.__str__ | fixed value |
| self | module.DfCol.cols | fixed value |
| other | module.DfCol.eq | fixed value |
| self | module.DfCol.eq | fixed value |
| n | module.DfCol.eq | stepper |
| i | module.DfCol.eq | stepper |
| func | module.DfCol.filter | fixed value |
| self | module.DfCol.filter | fixed value |
| result | module.DfCol.filter | fixed value |
| i | module.DfCol.filter | stepper |
| args | module.DfCol.filter | most-recent holder |
| n | module.DfCol.filter | stepper |
| col | module.DfCol.get | fixed value |
| row | module.DfCol.get | fixed value |
| self | module.DfCol.get | fixed value |
| self | module.DfCol.ncol | fixed value |
| self | module.DfCol.nrow | fixed value |
| n | module.DfCol.nrow | fixed value |
| names | module.DfCol.select | fixed value |
| self | module.DfCol.select | fixed value |

## test_df_col.py

| Variable | Scope | Role |
|---|---|---|
| df | module.test_construct_with_single_value | fixed value |
| df | module.test_construct_with_two_pairs | fixed value |
| left | module.test_equality | fixed value |
| right | module.test_equality | fixed value |
| df | module.test_filter | fixed value |
| a | module.test_filter.odd | fixed value |
| b | module.test_filter.odd | fixed value |
| left | module.test_inequality | fixed value |
| df | module.test_select | fixed value |
| selected | module.test_select | fixed value |

## timing.py

| Variable | Scope | Role |
|---|---|---|
| RANGE | module | fixed value |
| FILTER | module | fixed value |
| SELECT | module | fixed value |
| silent | module | fixed value |
| spec | module | fixed value |
| sizes | module | fixed value |
| result | module | fixed value |
| ncol | module.make_col | fixed value |
| nrow | module.make_col | fixed value |
| fill | module.make_col | fixed value |
| n | module.make_col._col | fixed value |
| start | module.make_col._col | fixed value |
| ncol | module.make_row | fixed value |
| nrow | module.make_row | fixed value |
| labels | module.make_row | fixed value |
| fill | module.make_row | fixed value |
| r | module.make_row._row | fixed value |
| result | module.report | fixed value |
| writer | module.report | fixed value |
| row | module.report | stepper |
| spec | module.setup | fixed value |
| sizes | module.setup | fixed value |
| sizes | module.sweep | fixed value |
| result | module.sweep | log |
| ncol | module.sweep | stepper |
| nrow | module.sweep | stepper |
| df_col | module.sweep | most-recent holder |
| df_row | module.sweep | most-recent holder |
| times | module.sweep | most-recent holder |
| df | module.time_filter | fixed value |
| start | module.time_filter | fixed value |
| args | module.time_filter.f | fixed value |
| label_0 | module.time_filter.f | fixed value |
| df | module.time_select | fixed value |
| indices | module.time_select | fixed value |
| labels | module.time_select | fixed value |
| start | module.time_select | fixed value |

## ex_map_2.py

*No variables identified by jorma.*

