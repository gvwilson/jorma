# Variable Role Analysis: archive

## backup.py

```

[module.backup]
  backup_dir               fixed value             (line 11)
  source_dir               fixed value             (line 11)
  manifest                 fixed value             (line 12)
  timestamp                fixed value             (line 13)

[module.copy_files]
  backup_dir               fixed value             (line 20)
  manifest                 fixed value             (line 20)
  source_dir               fixed value             (line 20)
  filename                 stepper                 (line 21)
  hash_code                stepper                 (line 21)
  source_path              most-recent holder      (line 22)
  backup_path              most-recent holder      (line 23)

[module.write_manifest]
  backup_dir               unknown                 (line 34)
  manifest                 fixed value             (line 34)
  timestamp                fixed value             (line 34)
  manifest_file            fixed value             (line 38)
  raw                      fixed value             (line 39)
  writer                   fixed value             (line 40)
```

## backup_oop.py

```

[module]
  source_dir               fixed value             (line 68)
  backup_dir               fixed value             (line 69)
  archiver                 fixed value             (line 71)

[module.Archive.__init__]
  self                     fixed value             (line 11)
  source_dir               fixed value             (line 11)

[module.Archive.backup]
  self                     fixed value             (line 14)
  manifest                 fixed value             (line 15)

[module.ArchiveLocal.__init__]
  backup_dir               fixed value             (line 23)
  self                     fixed value             (line 23)
  source_dir               fixed value             (line 23)

[module.ArchiveLocal._copy_files]
  manifest                 fixed value             (line 27)
  self                     fixed value             (line 27)
  filename                 stepper                 (line 28)
  hash_code                stepper                 (line 28)
  source_path              most-recent holder      (line 29)
  backup_path              most-recent holder      (line 30)

[module.ArchiveLocal._timestamp]
  self                     fixed value             (line 45)

[module.ArchiveLocal._write_manifest]
  manifest                 fixed value             (line 34)
  self                     fixed value             (line 34)
  t                        fixed value             (line 35)
  backup_dir               fixed value             (line 36)
  manifest_file            fixed value             (line 39)
  raw                      fixed value             (line 40)
  writer                   fixed value             (line 41)

[module.analyze_and_save]
  archiver                 fixed value             (line 59)
  options                  fixed value             (line 59)
  data                     fixed value             (line 60)
  results                  fixed value             (line 61)

[module.analyze_data]
  data                     fixed value             (line 51)

[module.read_data]
  options                  fixed value             (line 48)

[module.save_everything]
  result                   fixed value             (line 54)
```

## hash_all.py

```

[module]
  HASH_LEN                 fixed value             (line 8)
  root                     fixed value             (line 22)
  table                    fixed value             (line 23)
  writer                   fixed value             (line 24)

[module.hash_all]
  root                     fixed value             (line 10)
  result                   log                     (line 11)
  name                     stepper                 (line 12)
  full_name                most-recent holder      (line 13)
  reader                   fixed value             (line 14)
  data                     most-recent holder      (line 15)
  hash_code                most-recent holder      (line 16)
```

## test_backup.py

```

[module]
  FILES                    fixed value             (line 8)

[module.our_fs]
  fs                       fixed value             (line 11)
  contents                 stepper                 (line 12)
  name                     stepper                 (line 12)

[module.test_nested_example]
  our_fs                   fixed value             (line 17)
  timestamp                fixed value             (line 18)
  manifest                 fixed value             (line 20)
  filename                 stepper                 (line 22)
  hash_code                stepper                 (line 22)
```

## test_hash_all.py

```

[module.our_fs]
  fs                       fixed value             (line 6)

[module.test_change]
  our_fs                   fixed value             (line 18)
  original                 unknown                 (line 19)
  writer                   fixed value             (line 21)
  changed                  unknown                 (line 23)

[module.test_hashing]
  our_fs                   fixed value             (line 11)
  result                   fixed value             (line 12)
  expected                 fixed value             (line 13)
```

## test_mock_fs.py

```

[module.test_simple_example]
  fs                       fixed value             (line 3)
  sentence                 fixed value             (line 4)
  writer                   fixed value             (line 5)
  reader                   fixed value             (line 8)
```

## test_mock_tree.py

```

[module.our_fs]
  fs                       fixed value             (line 5)

[module.test_deletion_example]
  our_fs                   fixed value             (line 15)

[module.test_nested_example]
  our_fs                   fixed value             (line 10)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- sample_dir.py

