# A File Archiver

## hash_all.py

| Variable | Scope | Role |
|---|---|---|
| HASH_LEN | module | fixed value |
| root | module | fixed value |
| table | module | fixed value |
| writer | module | fixed value |
| root | module.hash_all | fixed value |
| result | module.hash_all | log |
| name | module.hash_all | stepper |
| full_name | module.hash_all | most-recent holder |
| reader | module.hash_all | fixed value |
| data | module.hash_all | most-recent holder |
| hash_code | module.hash_all | most-recent holder |

## test_mock_fs.py

| Variable | Scope | Role |
|---|---|---|
| fs | module.test_simple_example | fixed value |
| sentence | module.test_simple_example | fixed value |
| writer | module.test_simple_example | fixed value |
| reader | module.test_simple_example | fixed value |

## test_mock_tree.py

| Variable | Scope | Role |
|---|---|---|
| fs | module.our_fs | fixed value |
| our_fs | module.test_deletion_example | fixed value |
| our_fs | module.test_nested_example | fixed value |

## test_hash_all.py

| Variable | Scope | Role |
|---|---|---|
| fs | module.our_fs | fixed value |
| our_fs | module.test_change | fixed value |
| original | module.test_change | unknown |
| writer | module.test_change | fixed value |
| changed | module.test_change | unknown |
| our_fs | module.test_hashing | fixed value |
| result | module.test_hashing | fixed value |
| expected | module.test_hashing | fixed value |

## backup.py

| Variable | Scope | Role |
|---|---|---|
| backup_dir | module.backup | fixed value |
| source_dir | module.backup | fixed value |
| manifest | module.backup | fixed value |
| timestamp | module.backup | fixed value |
| backup_dir | module.copy_files | fixed value |
| manifest | module.copy_files | fixed value |
| source_dir | module.copy_files | fixed value |
| filename | module.copy_files | stepper |
| hash_code | module.copy_files | stepper |
| source_path | module.copy_files | most-recent holder |
| backup_path | module.copy_files | most-recent holder |
| backup_dir | module.write_manifest | unknown |
| manifest | module.write_manifest | fixed value |
| timestamp | module.write_manifest | fixed value |
| manifest_file | module.write_manifest | fixed value |
| raw | module.write_manifest | fixed value |
| writer | module.write_manifest | fixed value |

## test_backup.py

| Variable | Scope | Role |
|---|---|---|
| FILES | module | fixed value |
| fs | module.our_fs | fixed value |
| contents | module.our_fs | stepper |
| name | module.our_fs | stepper |
| our_fs | module.test_nested_example | fixed value |
| timestamp | module.test_nested_example | fixed value |
| manifest | module.test_nested_example | fixed value |
| filename | module.test_nested_example | stepper |
| hash_code | module.test_nested_example | stepper |

## backup_oop.py

| Variable | Scope | Role |
|---|---|---|
| source_dir | module | fixed value |
| backup_dir | module | fixed value |
| archiver | module | fixed value |
| self | module.Archive.__init__ | fixed value |
| source_dir | module.Archive.__init__ | fixed value |
| self | module.Archive.backup | fixed value |
| manifest | module.Archive.backup | fixed value |
| backup_dir | module.ArchiveLocal.__init__ | fixed value |
| self | module.ArchiveLocal.__init__ | fixed value |
| source_dir | module.ArchiveLocal.__init__ | fixed value |
| manifest | module.ArchiveLocal._copy_files | fixed value |
| self | module.ArchiveLocal._copy_files | fixed value |
| filename | module.ArchiveLocal._copy_files | stepper |
| hash_code | module.ArchiveLocal._copy_files | stepper |
| source_path | module.ArchiveLocal._copy_files | most-recent holder |
| backup_path | module.ArchiveLocal._copy_files | most-recent holder |
| self | module.ArchiveLocal._timestamp | fixed value |
| manifest | module.ArchiveLocal._write_manifest | fixed value |
| self | module.ArchiveLocal._write_manifest | fixed value |
| t | module.ArchiveLocal._write_manifest | fixed value |
| backup_dir | module.ArchiveLocal._write_manifest | fixed value |
| manifest_file | module.ArchiveLocal._write_manifest | fixed value |
| raw | module.ArchiveLocal._write_manifest | fixed value |
| writer | module.ArchiveLocal._write_manifest | fixed value |
| archiver | module.analyze_and_save | fixed value |
| options | module.analyze_and_save | fixed value |
| data | module.analyze_and_save | fixed value |
| results | module.analyze_and_save | fixed value |
| data | module.analyze_data | fixed value |
| options | module.read_data | fixed value |
| result | module.save_everything | fixed value |

