# A Build Manager

## build_simple.py

| Variable | Scope | Role |
|---|---|---|
| builder | module | fixed value |
| details | module.BuildBase._check | fixed value |
| known | module.BuildBase._check | fixed value |
| name | module.BuildBase._check | fixed value |
| self | module.BuildBase._check | fixed value |
| depends | module.BuildBase._check | fixed value |
| config_file | module.BuildBase._configure | fixed value |
| self | module.BuildBase._configure | fixed value |
| reader | module.BuildBase._configure | fixed value |
| config | module.BuildBase._configure | fixed value |
| known | module.BuildBase._configure | fixed value |
| config | module.BuildBase._refresh | fixed value |
| node | module.BuildBase._refresh | fixed value |
| self | module.BuildBase._refresh | fixed value |
| config | module.BuildBase._topo_sort | fixed value |
| self | module.BuildBase._topo_sort | fixed value |
| graph | module.BuildBase._topo_sort | gatherer |
| result | module.BuildBase._topo_sort | log |
| available | module.BuildBase._topo_sort | most-recent holder |
| config_file | module.BuildBase.build | fixed value |
| self | module.BuildBase.build | fixed value |
| config | module.BuildBase.build | fixed value |
| ordered | module.BuildBase.build | fixed value |
| node | module.BuildBase.build | stepper |

## build_better.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| config | module | fixed value |
| builder | module | fixed value |
| actions | module | fixed value |
| a | module | stepper |
| details | module.BuildBetter._check | fixed value |
| known | module.BuildBetter._check | fixed value |
| name | module.BuildBetter._check | fixed value |
| self | module.BuildBetter._check | fixed value |
| depends | module.BuildBetter._check | fixed value |
| result | module.BuildBetter._check | fixed value |
| details | module.BuildBetter._check_keys | fixed value |
| name | module.BuildBetter._check_keys | fixed value |
| self | module.BuildBetter._check_keys | fixed value |
| config | module.BuildBetter._configure | fixed value |
| self | module.BuildBetter._configure | fixed value |
| known | module.BuildBetter._configure | fixed value |
| condition | module.BuildBetter._must | fixed value |
| message | module.BuildBetter._must | fixed value |
| self | module.BuildBetter._must | fixed value |
| actions | module.BuildBetter._refresh | log |
| config | module.BuildBetter._refresh | fixed value |
| node | module.BuildBetter._refresh | fixed value |
| self | module.BuildBetter._refresh | fixed value |
| config | module.BuildBetter._topo_sort | fixed value |
| self | module.BuildBetter._topo_sort | fixed value |
| graph | module.BuildBetter._topo_sort | gatherer |
| result | module.BuildBetter._topo_sort | log |
| available | module.BuildBetter._topo_sort | most-recent holder |
| config | module.BuildBetter.build | unknown |
| self | module.BuildBetter.build | fixed value |
| ordered | module.BuildBetter.build | fixed value |
| actions | module.BuildBetter.build | fixed value |
| node | module.BuildBetter.build | stepper |

## test_build_better.py

| Variable | Scope | Role |
|---|---|---|
| action_A | module.test_circular | fixed value |
| action_B | module.test_circular | fixed value |
| config | module.test_circular | fixed value |
| action_A | module.test_diamond_dep | fixed value |
| action_B | module.test_diamond_dep | fixed value |
| action_C | module.test_diamond_dep | fixed value |
| action_D | module.test_diamond_dep | fixed value |
| config | module.test_diamond_dep | fixed value |
| action_A | module.test_linear_dep | fixed value |
| action_B | module.test_linear_dep | fixed value |
| config | module.test_linear_dep | fixed value |
| action_A | module.test_no_dep | fixed value |
| action_B | module.test_no_dep | fixed value |
| config | module.test_no_dep | fixed value |
| action_A | module.test_single | fixed value |
| config | module.test_single | fixed value |

## test_build_time.py

| Variable | Scope | Role |
|---|---|---|
| action_A | module.test_circular | fixed value |
| action_B | module.test_circular | fixed value |
| config | module.test_circular | fixed value |
| action_A | module.test_diamond_dep | fixed value |
| action_B | module.test_diamond_dep | fixed value |
| action_C | module.test_diamond_dep | fixed value |
| action_D | module.test_diamond_dep | fixed value |
| config | module.test_diamond_dep | fixed value |
| action_A | module.test_linear_dep_needs_update | fixed value |
| action_B | module.test_linear_dep_needs_update | fixed value |
| config | module.test_linear_dep_needs_update | fixed value |
| action_A | module.test_linear_dep_no_need_update | fixed value |
| action_B | module.test_linear_dep_no_need_update | fixed value |
| config | module.test_linear_dep_no_need_update | fixed value |
| action_A | module.test_no_dep | fixed value |
| action_B | module.test_no_dep | fixed value |
| config | module.test_no_dep | fixed value |
| action_A | module.test_single | fixed value |
| config | module.test_single | fixed value |

## build_time.py

| Variable | Scope | Role |
|---|---|---|
| reader | module | fixed value |
| config | module | fixed value |
| builder | module | fixed value |
| actions | module | fixed value |
| a | module | stepper |
| details | module.BuildTime._check_keys | fixed value |
| name | module.BuildTime._check_keys | fixed value |
| self | module.BuildTime._check_keys | fixed value |
| config | module.BuildTime._needs_update | fixed value |
| node | module.BuildTime._needs_update | fixed value |
| self | module.BuildTime._needs_update | fixed value |
| actions | module.BuildTime._refresh | log |
| config | module.BuildTime._refresh | fixed value |
| node | module.BuildTime._refresh | fixed value |
| self | module.BuildTime._refresh | fixed value |

