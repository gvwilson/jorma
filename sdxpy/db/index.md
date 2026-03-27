# Variable Role Analysis: db

## blocked.py

| Scope                        | Variable          | Role        | Location |
| :----------------------------| :-----------------| :-----------| :--------|
| module.Blocked               | RECORDS_PER_BLOCK | fixed value | line 5   |
| module.Blocked.__init__      | record_cls        | fixed value | line 11  |
| module.Blocked.__init__      | self              | fixed value | line 11  |
| module.Blocked._get_block    | block_id          | fixed value | line 53  |
| module.Blocked._get_block    | self              | fixed value | line 53  |
| module.Blocked._get_block_id | self              | fixed value | line 50  |
| module.Blocked._get_block_id | seq_id            | fixed value | line 50  |
| module.Blocked._next_seq_id  | self              | fixed value | line 45  |
| module.Blocked._next_seq_id  | seq_id            | fixed value | line 46  |
| module.Blocked.add           | record            | fixed value | line 25  |
| module.Blocked.add           | self              | fixed value | line 25  |
| module.Blocked.add           | key               | fixed value | line 26  |
| module.Blocked.add           | seq_id            | fixed value | line 27  |
| module.Blocked.add           | block_id          | fixed value | line 29  |
| module.Blocked.add           | block             | fixed value | line 30  |
| module.Blocked.get           | key               | fixed value | line 35  |
| module.Blocked.get           | self              | fixed value | line 35  |
| module.Blocked.get           | seq_id            | fixed value | line 38  |
| module.Blocked.get           | block_id          | fixed value | line 39  |
| module.Blocked.get           | block             | fixed value | line 40  |
| module.Blocked.num_blocks    | self              | fixed value | line 17  |
| module.Blocked.num_records   | self              | fixed value | line 20  |

## blocked_file.py

| Scope                            | Variable   | Role               | Location |
| :--------------------------------| :----------| :------------------| :--------|
| module.BlockedFile.__init__      | db_dir     | fixed value        | line 7   |
| module.BlockedFile.__init__      | record_cls | fixed value        | line 7   |
| module.BlockedFile.__init__      | self       | fixed value        | line 7   |
| module.BlockedFile._build_index  | self       | fixed value        | line 59  |
| module.BlockedFile._build_index  | seq_id     | stepper            | line 60  |
| module.BlockedFile._build_index  | block_id   | stepper            | line 61  |
| module.BlockedFile._build_index  | filename   | stepper            | line 61  |
| module.BlockedFile._build_index  | record     | stepper            | line 65  |
| module.BlockedFile._build_index  | key        | most-recent holder | line 66  |
| module.BlockedFile._get_filename | block_id   | fixed value        | line 55  |
| module.BlockedFile._get_filename | self       | fixed value        | line 55  |
| module.BlockedFile._load         | key        | fixed value        | line 38  |
| module.BlockedFile._load         | self       | fixed value        | line 38  |
| module.BlockedFile._load         | seq_id     | fixed value        | line 39  |
| module.BlockedFile._load         | block_id   | fixed value        | line 40  |
| module.BlockedFile._load         | filename   | fixed value        | line 41  |
| module.BlockedFile._load_block   | block_id   | fixed value        | line 44  |
| module.BlockedFile._load_block   | filename   | fixed value        | line 44  |
| module.BlockedFile._load_block   | self       | fixed value        | line 44  |
| module.BlockedFile._load_block   | reader     | fixed value        | line 45  |
| module.BlockedFile._load_block   | raw        | fixed value        | line 46  |
| module.BlockedFile._load_block   | records    | fixed value        | line 48  |
| module.BlockedFile._load_block   | base       | fixed value        | line 49  |
| module.BlockedFile._load_block   | block      | fixed value        | line 50  |
| module.BlockedFile._load_block   | i          | stepper            | line 51  |
| module.BlockedFile._load_block   | r          | stepper            | line 51  |
| module.BlockedFile._save         | record     | fixed value        | line 24  |
| module.BlockedFile._save         | self       | fixed value        | line 24  |
| module.BlockedFile._save         | key        | fixed value        | line 25  |
| module.BlockedFile._save         | seq_id     | fixed value        | line 26  |
| module.BlockedFile._save         | block_id   | fixed value        | line 27  |
| module.BlockedFile._save         | block      | fixed value        | line 29  |
| module.BlockedFile._save         | packed     | fixed value        | line 30  |
| module.BlockedFile._save         | filename   | fixed value        | line 32  |
| module.BlockedFile._save         | writer     | fixed value        | line 33  |
| module.BlockedFile.add           | record     | fixed value        | line 12  |
| module.BlockedFile.add           | self       | fixed value        | line 12  |
| module.BlockedFile.get           | key        | fixed value        | line 16  |
| module.BlockedFile.get           | self       | fixed value        | line 16  |

## cleanup.py

| Scope                         | Variable     | Role               | Location |
| :-----------------------------| :------------| :------------------| :--------|
| module.Cleanup._cleanup       | self         | fixed value        | line 11  |
| module.Cleanup._cleanup       | new_seq      | fixed value        | line 12  |
| module.Cleanup._cleanup       | keep         | fixed value        | line 15  |
| module.Cleanup._cleanup       | renaming     | fixed value        | line 17  |
| module.Cleanup._cleanup       | garbage_ids  | fixed value        | line 18  |
| module.Cleanup._cleanup       | new_index    | fixed value        | line 26  |
| module.Cleanup._delete_blocks | garbage_ids  | fixed value        | line 33  |
| module.Cleanup._delete_blocks | self         | fixed value        | line 33  |
| module.Cleanup._delete_blocks | i            | stepper            | line 34  |
| module.Cleanup._delete_blocks | filename     | most-recent holder | line 35  |
| module.Cleanup._rename_blocks | renaming     | fixed value        | line 39  |
| module.Cleanup._rename_blocks | self         | fixed value        | line 39  |
| module.Cleanup._rename_blocks | new_id       | stepper            | line 40  |
| module.Cleanup._rename_blocks | old_id       | stepper            | line 40  |
| module.Cleanup._rename_blocks | old_filename | most-recent holder | line 41  |
| module.Cleanup._rename_blocks | new_filename | most-recent holder | line 42  |
| module.Cleanup.add            | record       | fixed value        | line 6   |
| module.Cleanup.add            | self         | fixed value        | line 6   |

## file_backed.py

| Scope                      | Variable   | Role        | Location |
| :--------------------------| :----------| :-----------| :--------|
| module.FileBacked.__init__ | filename   | fixed value | line 7   |
| module.FileBacked.__init__ | record_cls | fixed value | line 7   |
| module.FileBacked.__init__ | self       | fixed value | line 7   |
| module.FileBacked._load    | self       | fixed value | line 29  |
| module.FileBacked._load    | reader     | fixed value | line 31  |
| module.FileBacked._load    | raw        | fixed value | line 32  |
| module.FileBacked._load    | records    | fixed value | line 33  |
| module.FileBacked._save    | self       | fixed value | line 24  |
| module.FileBacked._save    | packed     | fixed value | line 25  |
| module.FileBacked._save    | writer     | fixed value | line 26  |
| module.FileBacked.add      | record     | fixed value | line 14  |
| module.FileBacked.add      | self       | fixed value | line 14  |
| module.FileBacked.add      | key        | fixed value | line 15  |
| module.FileBacked.get      | key        | fixed value | line 19  |
| module.FileBacked.get      | self       | fixed value | line 19  |

## interface.py

| Scope                    | Variable   | Role        | Location |
| :------------------------| :----------| :-----------| :--------|
| module.Database.__init__ | record_cls | fixed value | line 2   |
| module.Database.__init__ | self       | fixed value | line 2   |
| module.Database.add      | record     | fixed value | line 6   |
| module.Database.add      | self       | fixed value | line 6   |
| module.Database.get      | key        | fixed value | line 10  |
| module.Database.get      | self       | fixed value | line 10  |

## interface_original.py

| Scope                    | Variable | Role        | Location |
| :------------------------| :--------| :-----------| :--------|
| module.Database.__init__ | key_func | fixed value | line 2   |
| module.Database.__init__ | self     | fixed value | line 2   |
| module.Database.add      | record   | fixed value | line 6   |
| module.Database.add      | self     | fixed value | line 6   |
| module.Database.get      | key      | fixed value | line 10  |
| module.Database.get      | self     | fixed value | line 10  |

## just_dict_original.py

| Scope                    | Variable | Role        | Location |
| :------------------------| :--------| :-----------| :--------|
| module.JustDict.__init__ | key_func | fixed value | line 4   |
| module.JustDict.__init__ | self     | fixed value | line 4   |
| module.JustDict.add      | record   | fixed value | line 8   |
| module.JustDict.add      | self     | fixed value | line 8   |
| module.JustDict.add      | key      | fixed value | line 9   |
| module.JustDict.get      | key      | fixed value | line 12  |
| module.JustDict.get      | self     | fixed value | line 12  |

## just_dict_refactored.py

| Scope                              | Variable   | Role        | Location |
| :----------------------------------| :----------| :-----------| :--------|
| module.JustDictRefactored.__init__ | record_cls | fixed value | line 4   |
| module.JustDictRefactored.__init__ | self       | fixed value | line 4   |
| module.JustDictRefactored.add      | record     | fixed value | line 8   |
| module.JustDictRefactored.add      | self       | fixed value | line 8   |
| module.JustDictRefactored.add      | key        | fixed value | line 9   |
| module.JustDictRefactored.get      | key        | fixed value | line 12  |
| module.JustDictRefactored.get      | self       | fixed value | line 12  |

## record.py

| Scope                          | Variable   | Role        | Location |
| :------------------------------| :----------| :-----------| :--------|
| module.Experiment              | RECORD_LEN | fixed value | line 5   |
| module.Experiment.key          | record     | fixed value | line 16  |
| module.Experiment.pack         | record     | fixed value | line 22  |
| module.Experiment.pack         | readings   | fixed value | line 24  |
| module.Experiment.pack         | result     | unknown     | line 25  |
| module.Experiment.pack_multi   | records    | fixed value | line 44  |
| module.Experiment.unpack       | raw        | fixed value | line 33  |
| module.Experiment.unpack       | parts      | fixed value | line 35  |
| module.Experiment.unpack       | name       | fixed value | line 36  |
| module.Experiment.unpack       | timestamp  | fixed value | line 37  |
| module.Experiment.unpack       | readings   | fixed value | line 38  |
| module.Experiment.unpack_multi | raw        | fixed value | line 48  |
| module.Experiment.unpack_multi | size       | fixed value | line 49  |
| module.Experiment.unpack_multi | split      | fixed value | line 50  |

## record_original.py

| Scope                    | Variable         | Role        | Location |
| :------------------------| :----------------| :-----------| :--------|
| module.BasicRec          | MAX_NAME_LEN     | fixed value | line 2   |
| module.BasicRec          | TIMESTAMP_LEN    | fixed value | line 3   |
| module.BasicRec          | MAX_READING      | fixed value | line 4   |
| module.BasicRec          | MAX_READING_LEN  | fixed value | line 5   |
| module.BasicRec          | MAX_READINGS_NUM | fixed value | line 6   |
| module.BasicRec.__eq__   | other            | fixed value | line 26  |
| module.BasicRec.__eq__   | self             | fixed value | line 26  |
| module.BasicRec.__init__ | name             | fixed value | line 13  |
| module.BasicRec.__init__ | readings         | fixed value | line 13  |
| module.BasicRec.__init__ | self             | fixed value | line 13  |
| module.BasicRec.__init__ | timestamp        | fixed value | line 13  |
| module.BasicRec.__str__  | self             | fixed value | line 22  |
| module.BasicRec.__str__  | joined           | fixed value | line 23  |
| module.BasicRec.key      | record           | fixed value | line 9   |

## show_packed_records.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | ex       | fixed value | line 3   |

## test_db_original.py

| Scope                                 | Variable | Role        | Location |
| :-------------------------------------| :--------| :-----------| :--------|
| module.test_add_then_get              | db       | container   | line 27  |
| module.test_add_then_get              | ex01     | fixed value | line 27  |
| module.test_add_then_overwrite        | db       | container   | line 37  |
| module.test_add_then_overwrite        | ex01     | fixed value | line 37  |
| module.test_add_two_then_get_both     | db       | container   | line 31  |
| module.test_add_two_then_get_both     | ex01     | fixed value | line 31  |
| module.test_add_two_then_get_both     | ex02     | fixed value | line 31  |
| module.test_construct                 | db       | fixed value | line 21  |
| module.test_get_nothing_from_empty_db | db       | fixed value | line 24  |

