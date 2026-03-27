# Variable Role Analysis: db

## blocked.py

```

[module.Blocked]
  RECORDS_PER_BLOCK        fixed value             (line 5)

[module.Blocked.__init__]
  record_cls               fixed value             (line 11)
  self                     fixed value             (line 11)

[module.Blocked._get_block]
  block_id                 fixed value             (line 53)
  self                     fixed value             (line 53)

[module.Blocked._get_block_id]
  self                     fixed value             (line 50)
  seq_id                   fixed value             (line 50)

[module.Blocked._next_seq_id]
  self                     fixed value             (line 45)
  seq_id                   fixed value             (line 46)

[module.Blocked.add]
  record                   fixed value             (line 25)
  self                     fixed value             (line 25)
  key                      fixed value             (line 26)
  seq_id                   fixed value             (line 27)
  block_id                 fixed value             (line 29)
  block                    fixed value             (line 30)

[module.Blocked.get]
  key                      fixed value             (line 35)
  self                     fixed value             (line 35)
  seq_id                   fixed value             (line 38)
  block_id                 fixed value             (line 39)
  block                    fixed value             (line 40)

[module.Blocked.num_blocks]
  self                     fixed value             (line 17)

[module.Blocked.num_records]
  self                     fixed value             (line 20)
```

## blocked_file.py

```

[module.BlockedFile.__init__]
  db_dir                   fixed value             (line 7)
  record_cls               fixed value             (line 7)
  self                     fixed value             (line 7)

[module.BlockedFile._build_index]
  self                     fixed value             (line 59)
  seq_id                   stepper                 (line 60)
  block_id                 stepper                 (line 61)
  filename                 stepper                 (line 61)
  record                   stepper                 (line 65)
  key                      most-recent holder      (line 66)

[module.BlockedFile._get_filename]
  block_id                 fixed value             (line 55)
  self                     fixed value             (line 55)

[module.BlockedFile._load]
  key                      fixed value             (line 38)
  self                     fixed value             (line 38)
  seq_id                   fixed value             (line 39)
  block_id                 fixed value             (line 40)
  filename                 fixed value             (line 41)

[module.BlockedFile._load_block]
  block_id                 fixed value             (line 44)
  filename                 fixed value             (line 44)
  self                     fixed value             (line 44)
  reader                   fixed value             (line 45)
  raw                      fixed value             (line 46)
  records                  fixed value             (line 48)
  base                     fixed value             (line 49)
  block                    fixed value             (line 50)
  i                        stepper                 (line 51)
  r                        stepper                 (line 51)

[module.BlockedFile._save]
  record                   fixed value             (line 24)
  self                     fixed value             (line 24)
  key                      fixed value             (line 25)
  seq_id                   fixed value             (line 26)
  block_id                 fixed value             (line 27)
  block                    fixed value             (line 29)
  packed                   fixed value             (line 30)
  filename                 fixed value             (line 32)
  writer                   fixed value             (line 33)

[module.BlockedFile.add]
  record                   fixed value             (line 12)
  self                     fixed value             (line 12)

[module.BlockedFile.get]
  key                      fixed value             (line 16)
  self                     fixed value             (line 16)
```

## cleanup.py

```

[module.Cleanup._cleanup]
  self                     fixed value             (line 11)
  new_seq                  fixed value             (line 12)
  keep                     fixed value             (line 15)
  renaming                 fixed value             (line 17)
  garbage_ids              fixed value             (line 18)
  new_index                fixed value             (line 26)

[module.Cleanup._delete_blocks]
  garbage_ids              fixed value             (line 33)
  self                     fixed value             (line 33)
  i                        stepper                 (line 34)
  filename                 most-recent holder      (line 35)

[module.Cleanup._rename_blocks]
  renaming                 fixed value             (line 39)
  self                     fixed value             (line 39)
  new_id                   stepper                 (line 40)
  old_id                   stepper                 (line 40)
  old_filename             most-recent holder      (line 41)
  new_filename             most-recent holder      (line 42)

[module.Cleanup.add]
  record                   fixed value             (line 6)
  self                     fixed value             (line 6)
```

## file_backed.py

```

[module.FileBacked.__init__]
  filename                 fixed value             (line 7)
  record_cls               fixed value             (line 7)
  self                     fixed value             (line 7)

[module.FileBacked._load]
  self                     fixed value             (line 29)
  reader                   fixed value             (line 31)
  raw                      fixed value             (line 32)
  records                  fixed value             (line 33)

[module.FileBacked._save]
  self                     fixed value             (line 24)
  packed                   fixed value             (line 25)
  writer                   fixed value             (line 26)

[module.FileBacked.add]
  record                   fixed value             (line 14)
  self                     fixed value             (line 14)
  key                      fixed value             (line 15)

[module.FileBacked.get]
  key                      fixed value             (line 19)
  self                     fixed value             (line 19)
```

## interface.py

```

[module.Database.__init__]
  record_cls               fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Database.add]
  record                   fixed value             (line 6)
  self                     fixed value             (line 6)

[module.Database.get]
  key                      fixed value             (line 10)
  self                     fixed value             (line 10)
```

## interface_original.py

```

[module.Database.__init__]
  key_func                 fixed value             (line 2)
  self                     fixed value             (line 2)

[module.Database.add]
  record                   fixed value             (line 6)
  self                     fixed value             (line 6)

[module.Database.get]
  key                      fixed value             (line 10)
  self                     fixed value             (line 10)
```

## just_dict_original.py

```

[module.JustDict.__init__]
  key_func                 fixed value             (line 4)
  self                     fixed value             (line 4)

[module.JustDict.add]
  record                   fixed value             (line 8)
  self                     fixed value             (line 8)
  key                      fixed value             (line 9)

[module.JustDict.get]
  key                      fixed value             (line 12)
  self                     fixed value             (line 12)
```

## just_dict_refactored.py

```

[module.JustDictRefactored.__init__]
  record_cls               fixed value             (line 4)
  self                     fixed value             (line 4)

[module.JustDictRefactored.add]
  record                   fixed value             (line 8)
  self                     fixed value             (line 8)
  key                      fixed value             (line 9)

[module.JustDictRefactored.get]
  key                      fixed value             (line 12)
  self                     fixed value             (line 12)
```

## record.py

```

[module.Experiment]
  RECORD_LEN               fixed value             (line 5)

[module.Experiment.key]
  record                   fixed value             (line 16)

[module.Experiment.pack]
  record                   fixed value             (line 22)
  readings                 fixed value             (line 24)
  result                   unknown                 (line 25)

[module.Experiment.pack_multi]
  records                  fixed value             (line 44)

[module.Experiment.unpack]
  raw                      fixed value             (line 33)
  parts                    fixed value             (line 35)
  name                     fixed value             (line 36)
  timestamp                fixed value             (line 37)
  readings                 fixed value             (line 38)

[module.Experiment.unpack_multi]
  raw                      fixed value             (line 48)
  size                     fixed value             (line 49)
  split                    fixed value             (line 50)
```

## record_original.py

```

[module.BasicRec]
  MAX_NAME_LEN             fixed value             (line 2)
  TIMESTAMP_LEN            fixed value             (line 3)
  MAX_READING              fixed value             (line 4)
  MAX_READING_LEN          fixed value             (line 5)
  MAX_READINGS_NUM         fixed value             (line 6)

[module.BasicRec.__eq__]
  other                    fixed value             (line 26)
  self                     fixed value             (line 26)

[module.BasicRec.__init__]
  name                     fixed value             (line 13)
  readings                 fixed value             (line 13)
  self                     fixed value             (line 13)
  timestamp                fixed value             (line 13)

[module.BasicRec.__str__]
  self                     fixed value             (line 22)
  joined                   fixed value             (line 23)

[module.BasicRec.key]
  record                   fixed value             (line 9)
```

## show_packed_records.py

```

[module]
  ex                       fixed value             (line 3)
```

## test_db_original.py

```

[module.test_add_then_get]
  db                       container               (line 27)
  ex01                     fixed value             (line 27)

[module.test_add_then_overwrite]
  db                       container               (line 37)
  ex01                     fixed value             (line 37)

[module.test_add_two_then_get_both]
  db                       container               (line 31)
  ex01                     fixed value             (line 31)
  ex02                     fixed value             (line 31)

[module.test_construct]
  db                       fixed value             (line 21)

[module.test_get_nothing_from_empty_db]
  db                       fixed value             (line 24)
```

