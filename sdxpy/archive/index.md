# archive

## test_backup.py

### Static analysis

| Scope                      | Variable  | Role        | Location |
| :--------------------------| :---------| :-----------| :--------|
| module                     | FILES     | fixed value | line 7   |
| module.our_fs              | fs        | fixed value | line 11  |
| module.our_fs              | contents  | stepper     | line 12  |
| module.our_fs              | name      | stepper     | line 12  |
| module.test_nested_example | our_fs    | fixed value | line 16  |
| module.test_nested_example | timestamp | fixed value | line 17  |
| module.test_nested_example | manifest  | fixed value | line 19  |
| module.test_nested_example | filename  | stepper     | line 21  |
| module.test_nested_example | hash_code | stepper     | line 21  |

## test_mock_tree.py

### Static analysis

| Scope                        | Variable | Role        | Location |
| :----------------------------| :--------| :-----------| :--------|
| module.our_fs                | fs       | fixed value | line 6   |
| module.test_deletion_example | our_fs   | fixed value | line 18  |
| module.test_nested_example   | our_fs   | fixed value | line 12  |

