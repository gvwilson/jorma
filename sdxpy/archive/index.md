# Variable Role Analysis: archive

## backup.py

| Scope                 | Variable      | Role               | Location |
| :---------------------| :-------------| :------------------| :--------|
| module.backup         | backup_dir    | fixed value        | line 11  |
| module.backup         | source_dir    | fixed value        | line 11  |
| module.backup         | manifest      | fixed value        | line 12  |
| module.backup         | timestamp     | fixed value        | line 13  |
| module.copy_files     | backup_dir    | fixed value        | line 20  |
| module.copy_files     | manifest      | fixed value        | line 20  |
| module.copy_files     | source_dir    | fixed value        | line 20  |
| module.copy_files     | filename      | stepper            | line 21  |
| module.copy_files     | hash_code     | stepper            | line 21  |
| module.copy_files     | source_path   | most-recent holder | line 22  |
| module.copy_files     | backup_path   | most-recent holder | line 23  |
| module.write_manifest | backup_dir    | unknown            | line 34  |
| module.write_manifest | manifest      | fixed value        | line 34  |
| module.write_manifest | timestamp     | fixed value        | line 34  |
| module.write_manifest | manifest_file | fixed value        | line 38  |
| module.write_manifest | raw           | fixed value        | line 39  |
| module.write_manifest | writer        | fixed value        | line 40  |

## backup_oop.py

| Scope                               | Variable      | Role               | Location |
| :-----------------------------------| :-------------| :------------------| :--------|
| module                              | source_dir    | fixed value        | line 68  |
| module                              | backup_dir    | fixed value        | line 69  |
| module                              | archiver      | fixed value        | line 71  |
| module.Archive.__init__             | self          | fixed value        | line 11  |
| module.Archive.__init__             | source_dir    | fixed value        | line 11  |
| module.Archive.backup               | self          | fixed value        | line 14  |
| module.Archive.backup               | manifest      | fixed value        | line 15  |
| module.ArchiveLocal.__init__        | backup_dir    | fixed value        | line 23  |
| module.ArchiveLocal.__init__        | self          | fixed value        | line 23  |
| module.ArchiveLocal.__init__        | source_dir    | fixed value        | line 23  |
| module.ArchiveLocal._copy_files     | manifest      | fixed value        | line 27  |
| module.ArchiveLocal._copy_files     | self          | fixed value        | line 27  |
| module.ArchiveLocal._copy_files     | filename      | stepper            | line 28  |
| module.ArchiveLocal._copy_files     | hash_code     | stepper            | line 28  |
| module.ArchiveLocal._copy_files     | source_path   | most-recent holder | line 29  |
| module.ArchiveLocal._copy_files     | backup_path   | most-recent holder | line 30  |
| module.ArchiveLocal._timestamp      | self          | fixed value        | line 45  |
| module.ArchiveLocal._write_manifest | manifest      | fixed value        | line 34  |
| module.ArchiveLocal._write_manifest | self          | fixed value        | line 34  |
| module.ArchiveLocal._write_manifest | t             | fixed value        | line 35  |
| module.ArchiveLocal._write_manifest | backup_dir    | fixed value        | line 36  |
| module.ArchiveLocal._write_manifest | manifest_file | fixed value        | line 39  |
| module.ArchiveLocal._write_manifest | raw           | fixed value        | line 40  |
| module.ArchiveLocal._write_manifest | writer        | fixed value        | line 41  |
| module.analyze_and_save             | archiver      | fixed value        | line 59  |
| module.analyze_and_save             | options       | fixed value        | line 59  |
| module.analyze_and_save             | data          | fixed value        | line 60  |
| module.analyze_and_save             | results       | fixed value        | line 61  |
| module.analyze_data                 | data          | fixed value        | line 51  |
| module.read_data                    | options       | fixed value        | line 48  |
| module.save_everything              | result        | fixed value        | line 54  |

## hash_all.py

| Scope           | Variable  | Role               | Location |
| :---------------| :---------| :------------------| :--------|
| module          | HASH_LEN  | fixed value        | line 8   |
| module          | root      | fixed value        | line 22  |
| module          | table     | fixed value        | line 23  |
| module          | writer    | fixed value        | line 24  |
| module.hash_all | root      | fixed value        | line 10  |
| module.hash_all | result    | log                | line 11  |
| module.hash_all | name      | stepper            | line 12  |
| module.hash_all | full_name | most-recent holder | line 13  |
| module.hash_all | reader    | fixed value        | line 14  |
| module.hash_all | data      | most-recent holder | line 15  |
| module.hash_all | hash_code | most-recent holder | line 16  |

## test_backup.py

| Scope                      | Variable  | Role        | Location |
| :--------------------------| :---------| :-----------| :--------|
| module                     | FILES     | fixed value | line 8   |
| module.our_fs              | fs        | fixed value | line 11  |
| module.our_fs              | contents  | stepper     | line 12  |
| module.our_fs              | name      | stepper     | line 12  |
| module.test_nested_example | our_fs    | fixed value | line 17  |
| module.test_nested_example | timestamp | fixed value | line 18  |
| module.test_nested_example | manifest  | fixed value | line 20  |
| module.test_nested_example | filename  | stepper     | line 22  |
| module.test_nested_example | hash_code | stepper     | line 22  |

## test_hash_all.py

| Scope               | Variable | Role        | Location |
| :-------------------| :--------| :-----------| :--------|
| module.our_fs       | fs       | fixed value | line 6   |
| module.test_change  | our_fs   | fixed value | line 18  |
| module.test_change  | original | unknown     | line 19  |
| module.test_change  | writer   | fixed value | line 21  |
| module.test_change  | changed  | unknown     | line 23  |
| module.test_hashing | our_fs   | fixed value | line 11  |
| module.test_hashing | result   | fixed value | line 12  |
| module.test_hashing | expected | fixed value | line 13  |

## test_mock_fs.py

| Scope                      | Variable | Role        | Location |
| :--------------------------| :--------| :-----------| :--------|
| module.test_simple_example | fs       | fixed value | line 3   |
| module.test_simple_example | sentence | fixed value | line 4   |
| module.test_simple_example | writer   | fixed value | line 5   |
| module.test_simple_example | reader   | fixed value | line 8   |

## test_mock_tree.py

| Scope                        | Variable | Role        | Location |
| :----------------------------| :--------| :-----------| :--------|
| module.our_fs                | fs       | fixed value | line 5   |
| module.test_deletion_example | our_fs   | fixed value | line 15  |
| module.test_nested_example   | our_fs   | fixed value | line 10  |

