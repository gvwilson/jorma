# A Database

## interface_original.py

| Variable | Scope | Role |
|---|---|---|
| key_func | module.Database.__init__ | fixed value |
| self | module.Database.__init__ | fixed value |
| record | module.Database.add | fixed value |
| self | module.Database.add | fixed value |
| key | module.Database.get | fixed value |
| self | module.Database.get | fixed value |

## just_dict_original.py

| Variable | Scope | Role |
|---|---|---|
| key_func | module.JustDict.__init__ | fixed value |
| self | module.JustDict.__init__ | fixed value |
| record | module.JustDict.add | fixed value |
| self | module.JustDict.add | fixed value |
| key | module.JustDict.add | fixed value |
| key | module.JustDict.get | fixed value |
| self | module.JustDict.get | fixed value |

## record_original.py

| Variable | Scope | Role |
|---|---|---|
| MAX_NAME_LEN | module.BasicRec | fixed value |
| TIMESTAMP_LEN | module.BasicRec | fixed value |
| MAX_READING | module.BasicRec | fixed value |
| MAX_READING_LEN | module.BasicRec | fixed value |
| MAX_READINGS_NUM | module.BasicRec | fixed value |
| other | module.BasicRec.__eq__ | fixed value |
| self | module.BasicRec.__eq__ | fixed value |
| name | module.BasicRec.__init__ | fixed value |
| readings | module.BasicRec.__init__ | fixed value |
| self | module.BasicRec.__init__ | fixed value |
| timestamp | module.BasicRec.__init__ | fixed value |
| self | module.BasicRec.__str__ | fixed value |
| joined | module.BasicRec.__str__ | fixed value |
| record | module.BasicRec.key | fixed value |

## test_db_original.py

| Variable | Scope | Role |
|---|---|---|
| db | module.test_add_then_get | container |
| ex01 | module.test_add_then_get | fixed value |
| db | module.test_add_then_overwrite | container |
| ex01 | module.test_add_then_overwrite | fixed value |
| db | module.test_add_two_then_get_both | container |
| ex01 | module.test_add_two_then_get_both | fixed value |
| ex02 | module.test_add_two_then_get_both | fixed value |
| db | module.test_construct | fixed value |
| db | module.test_get_nothing_from_empty_db | fixed value |

## interface.py

| Variable | Scope | Role |
|---|---|---|
| record_cls | module.Database.__init__ | fixed value |
| self | module.Database.__init__ | fixed value |
| record | module.Database.add | fixed value |
| self | module.Database.add | fixed value |
| key | module.Database.get | fixed value |
| self | module.Database.get | fixed value |

## just_dict_refactored.py

| Variable | Scope | Role |
|---|---|---|
| record_cls | module.JustDictRefactored.__init__ | fixed value |
| self | module.JustDictRefactored.__init__ | fixed value |
| record | module.JustDictRefactored.add | fixed value |
| self | module.JustDictRefactored.add | fixed value |
| key | module.JustDictRefactored.add | fixed value |
| key | module.JustDictRefactored.get | fixed value |
| self | module.JustDictRefactored.get | fixed value |

## record.py

| Variable | Scope | Role |
|---|---|---|
| RECORD_LEN | module.Experiment | fixed value |
| record | module.Experiment.key | fixed value |
| record | module.Experiment.pack | fixed value |
| readings | module.Experiment.pack | fixed value |
| result | module.Experiment.pack | unknown |
| records | module.Experiment.pack_multi | fixed value |
| raw | module.Experiment.unpack | fixed value |
| parts | module.Experiment.unpack | fixed value |
| name | module.Experiment.unpack | fixed value |
| timestamp | module.Experiment.unpack | fixed value |
| readings | module.Experiment.unpack | fixed value |
| raw | module.Experiment.unpack_multi | fixed value |
| size | module.Experiment.unpack_multi | fixed value |
| split | module.Experiment.unpack_multi | fixed value |

## show_packed_records.py

| Variable | Scope | Role |
|---|---|---|
| ex | module | fixed value |

## file_backed.py

| Variable | Scope | Role |
|---|---|---|
| filename | module.FileBacked.__init__ | fixed value |
| record_cls | module.FileBacked.__init__ | fixed value |
| self | module.FileBacked.__init__ | fixed value |
| self | module.FileBacked._load | fixed value |
| reader | module.FileBacked._load | fixed value |
| raw | module.FileBacked._load | fixed value |
| records | module.FileBacked._load | fixed value |
| self | module.FileBacked._save | fixed value |
| packed | module.FileBacked._save | fixed value |
| writer | module.FileBacked._save | fixed value |
| record | module.FileBacked.add | fixed value |
| self | module.FileBacked.add | fixed value |
| key | module.FileBacked.add | fixed value |
| key | module.FileBacked.get | fixed value |
| self | module.FileBacked.get | fixed value |

## blocked.py

| Variable | Scope | Role |
|---|---|---|
| RECORDS_PER_BLOCK | module.Blocked | fixed value |
| record_cls | module.Blocked.__init__ | fixed value |
| self | module.Blocked.__init__ | fixed value |
| block_id | module.Blocked._get_block | fixed value |
| self | module.Blocked._get_block | fixed value |
| self | module.Blocked._get_block_id | fixed value |
| seq_id | module.Blocked._get_block_id | fixed value |
| self | module.Blocked._next_seq_id | fixed value |
| seq_id | module.Blocked._next_seq_id | fixed value |
| record | module.Blocked.add | fixed value |
| self | module.Blocked.add | fixed value |
| key | module.Blocked.add | fixed value |
| seq_id | module.Blocked.add | fixed value |
| block_id | module.Blocked.add | fixed value |
| block | module.Blocked.add | fixed value |
| key | module.Blocked.get | fixed value |
| self | module.Blocked.get | fixed value |
| seq_id | module.Blocked.get | fixed value |
| block_id | module.Blocked.get | fixed value |
| block | module.Blocked.get | fixed value |
| self | module.Blocked.num_blocks | fixed value |
| self | module.Blocked.num_records | fixed value |

## blocked_file.py

| Variable | Scope | Role |
|---|---|---|
| db_dir | module.BlockedFile.__init__ | fixed value |
| record_cls | module.BlockedFile.__init__ | fixed value |
| self | module.BlockedFile.__init__ | fixed value |
| self | module.BlockedFile._build_index | fixed value |
| seq_id | module.BlockedFile._build_index | stepper |
| block_id | module.BlockedFile._build_index | stepper |
| filename | module.BlockedFile._build_index | stepper |
| record | module.BlockedFile._build_index | stepper |
| key | module.BlockedFile._build_index | most-recent holder |
| block_id | module.BlockedFile._get_filename | fixed value |
| self | module.BlockedFile._get_filename | fixed value |
| key | module.BlockedFile._load | fixed value |
| self | module.BlockedFile._load | fixed value |
| seq_id | module.BlockedFile._load | fixed value |
| block_id | module.BlockedFile._load | fixed value |
| filename | module.BlockedFile._load | fixed value |
| block_id | module.BlockedFile._load_block | fixed value |
| filename | module.BlockedFile._load_block | fixed value |
| self | module.BlockedFile._load_block | fixed value |
| reader | module.BlockedFile._load_block | fixed value |
| raw | module.BlockedFile._load_block | fixed value |
| records | module.BlockedFile._load_block | fixed value |
| base | module.BlockedFile._load_block | fixed value |
| block | module.BlockedFile._load_block | fixed value |
| i | module.BlockedFile._load_block | stepper |
| r | module.BlockedFile._load_block | stepper |
| record | module.BlockedFile._save | fixed value |
| self | module.BlockedFile._save | fixed value |
| key | module.BlockedFile._save | fixed value |
| seq_id | module.BlockedFile._save | fixed value |
| block_id | module.BlockedFile._save | fixed value |
| block | module.BlockedFile._save | fixed value |
| packed | module.BlockedFile._save | fixed value |
| filename | module.BlockedFile._save | fixed value |
| writer | module.BlockedFile._save | fixed value |
| record | module.BlockedFile.add | fixed value |
| self | module.BlockedFile.add | fixed value |
| key | module.BlockedFile.get | fixed value |
| self | module.BlockedFile.get | fixed value |

## cleanup.py

| Variable | Scope | Role |
|---|---|---|
| self | module.Cleanup._cleanup | fixed value |
| new_seq | module.Cleanup._cleanup | fixed value |
| keep | module.Cleanup._cleanup | fixed value |
| renaming | module.Cleanup._cleanup | fixed value |
| garbage_ids | module.Cleanup._cleanup | fixed value |
| new_index | module.Cleanup._cleanup | fixed value |
| garbage_ids | module.Cleanup._delete_blocks | fixed value |
| self | module.Cleanup._delete_blocks | fixed value |
| i | module.Cleanup._delete_blocks | stepper |
| filename | module.Cleanup._delete_blocks | most-recent holder |
| renaming | module.Cleanup._rename_blocks | fixed value |
| self | module.Cleanup._rename_blocks | fixed value |
| new_id | module.Cleanup._rename_blocks | stepper |
| old_id | module.Cleanup._rename_blocks | stepper |
| old_filename | module.Cleanup._rename_blocks | most-recent holder |
| new_filename | module.Cleanup._rename_blocks | most-recent holder |
| record | module.Cleanup.add | fixed value |
| self | module.Cleanup.add | fixed value |

