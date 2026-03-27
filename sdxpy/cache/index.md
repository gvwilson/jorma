# Variable Role Analysis: cache

## cache_base.py

```

[module.CacheBase]
  CACHE_SUFFIX             fixed value             (line 9)

[module.CacheBase.__init__]
  cache_dir                fixed value             (line 11)
  index                    fixed value             (line 11)
  self                     fixed value             (line 11)

[module.CacheBase._add]
  identifier               fixed value             (line 40)
  local_path               fixed value             (line 40)
  self                     fixed value             (line 40)

[module.CacheBase._make_cache_path]
  identifier               fixed value             (line 36)
  self                     fixed value             (line 36)

[module.CacheBase._make_identifier]
  local_path               fixed value             (line 32)
  self                     fixed value             (line 32)
  reader                   fixed value             (line 33)

[module.CacheBase.add]
  local_path               fixed value             (line 15)
  self                     fixed value             (line 15)
  identifier               fixed value             (line 16)

[module.CacheBase.get_cache_path]
  identifier               fixed value             (line 21)
  self                     fixed value             (line 21)

[module.CacheBase.has]
  identifier               fixed value             (line 26)
  self                     fixed value             (line 26)

[module.CacheBase.known]
  self                     fixed value             (line 29)
```

## cache_filesystem.py

```

[module.CacheFilesystem._add]
  identifier               fixed value             (line 8)
  local_path               fixed value             (line 8)
  self                     fixed value             (line 8)
  cache_path               fixed value             (line 9)
```

## cache_io.py

```

[module.cache_open]
  cache                    fixed value             (line 6)
  filename                 unknown                 (line 6)
  reader                   fixed value             (line 12)
  identifier               fixed value             (line 13)
  cache_path               fixed value             (line 14)

[module.cache_save]
  cache                    container               (line 19)
  filename                 fixed value             (line 19)
  identifier               fixed value             (line 20)
  identifier_file          fixed value             (line 21)
  writer                   fixed value             (line 22)
```

## cache_limited.py

```

[module.CacheLimited.__init__]
  archive_dir              fixed value             (line 8)
  cache_dir                fixed value             (line 8)
  index                    fixed value             (line 8)
  local_limit              fixed value             (line 8)
  self                     fixed value             (line 8)

[module.CacheLimited._add]
  identifier               fixed value             (line 40)
  local_path               fixed value             (line 40)
  self                     fixed value             (line 40)

[module.CacheLimited._add_archive]
  identifier               fixed value             (line 46)
  local_path               fixed value             (line 46)
  self                     fixed value             (line 46)
  archive_path             fixed value             (line 47)

[module.CacheLimited._ensure_cache_space]
  self                     fixed value             (line 25)
  cache_dir                fixed value             (line 27)
  cache_files              container               (line 29)
  choice                   fixed value             (line 34)

[module.CacheLimited._make_archive_path]
  identifier               fixed value             (line 51)
  self                     fixed value             (line 51)

[module.CacheLimited.get_cache_path]
  identifier               fixed value             (line 15)
  self                     fixed value             (line 15)
  cache_path               fixed value             (line 16)
  archive_path             fixed value             (line 19)
```

## index_base.py

```

[module]
  CacheEntry               fixed value             (line 7)

[module.IndexBase]
  TIME_FORMAT              fixed value             (line 12)

[module.IndexBase.__init__]
  index_dir                fixed value             (line 14)
  self                     fixed value             (line 14)

[module.IndexBase._initialize_index]
  self                     fixed value             (line 48)

[module.IndexBase.add]
  identifier               fixed value             (line 31)
  self                     fixed value             (line 31)
  index                    log                     (line 32)
  entry                    fixed value             (line 33)

[module.IndexBase.get_index_dir]
  self                     fixed value             (line 17)

[module.IndexBase.has]
  identifier               fixed value             (line 24)
  self                     fixed value             (line 24)
  index                    fixed value             (line 25)

[module.IndexBase.known]
  self                     fixed value             (line 28)

[module.IndexBase.load]
  self                     fixed value             (line 40)

[module.IndexBase.save]
  index                    fixed value             (line 44)
  self                     fixed value             (line 44)

[module.IndexBase.set_index_dir]
  index_dir                fixed value             (line 20)
  self                     fixed value             (line 20)
```

## index_csv.py

```

[module.IndexCSV]
  INDEX_FILE               fixed value             (line 40)

[module.IndexCSV._initialize_index]
  self                     fixed value             (line 42)

[module.IndexCSV._make_index_path]
  self                     fixed value             (line 45)

[module.IndexCSV.load]
  self                     fixed value             (line 10)
  index_path               fixed value             (line 14)
  stream                   fixed value             (line 18)
  reader                   fixed value             (line 19)

[module.IndexCSV.save]
  index                    fixed value             (line 27)
  self                     fixed value             (line 27)
  index_path               fixed value             (line 31)
  stream                   fixed value             (line 32)
  writer                   fixed value             (line 33)
  entry                    stepper                 (line 34)
  when                     most-recent holder      (line 35)
```

## test_cache_filesystem.py

```

[module]
  CACHE_DIR                fixed value             (line 10)

[module.disk]
  fs                       fixed value             (line 13)

[module.test_filesystem_duplicate_content_only_saved_once]
  cache                    container               (line 59)
  disk                     fixed value             (line 59)
  contents                 fixed value             (line 60)
  ident_first              fixed value             (line 62)
  ident_second             fixed value             (line 64)

[module.test_filesystem_file_can_be_reloaded_after_deletion]
  cache                    container               (line 51)
  disk                     fixed value             (line 51)
  ident                    fixed value             (line 53)
  reader                   fixed value             (line 55)

[module.test_filesystem_no_files_before_add]
  cache                    fixed value             (line 23)
  disk                     fixed value             (line 23)

[module.test_filesystem_single_file_can_be_reloaded]
  cache                    container               (line 45)
  disk                     fixed value             (line 45)
  ident                    fixed value             (line 47)
  reader                   fixed value             (line 48)

[module.test_filesystem_single_file_present_after_add]
  cache                    container               (line 27)
  disk                     fixed value             (line 27)
  ident                    fixed value             (line 29)
  cache_path               fixed value             (line 32)

[module.test_filesystem_two_files_present_after_add]
  cache                    container               (line 36)
  disk                     fixed value             (line 36)
  names                    fixed value             (line 37)
  name                     stepper                 (line 38)
  filename                 most-recent holder      (line 39)
```

## test_cache_limited.py

```

[module]
  CACHE_DIR                fixed value             (line 10)
  ARCHIVE_DIR              fixed value             (line 11)
  LOCAL_LIMIT              fixed value             (line 12)

[module.cache]
  disk                     fixed value             (line 21)
  index                    fixed value             (line 22)

[module.disk]
  fs                       fixed value             (line 15)

[module.test_limited_all_files_can_be_retrieved]
  cache                    container               (line 83)
  disk                     fixed value             (line 83)
  names                    fixed value             (line 84)
  idents                   fixed value             (line 86)
  name                     stepper                 (line 88)
  local_file               most-recent holder      (line 89)
  ident                    stepper                 (line 93)
  cache_path               most-recent holder      (line 96)

[module.test_limited_duplicate_content_only_saved_once]
  cache                    container               (line 63)
  disk                     fixed value             (line 63)
  contents                 fixed value             (line 64)
  ident_first              fixed value             (line 66)
  ident_second             fixed value             (line 68)

[module.test_limited_file_can_be_reloaded_after_deletion]
  cache                    container               (line 55)
  disk                     fixed value             (line 55)
  ident                    fixed value             (line 57)
  reader                   fixed value             (line 59)

[module.test_limited_local_cache_size_stays_small]
  cache                    container               (line 72)
  disk                     fixed value             (line 72)
  names                    fixed value             (line 73)
  name                     stepper                 (line 75)
  local_file               most-recent holder      (line 76)

[module.test_limited_no_files_before_add]
  cache                    fixed value             (line 25)

[module.test_limited_single_file_can_be_reloaded]
  cache                    container               (line 49)
  disk                     fixed value             (line 49)
  ident                    fixed value             (line 51)
  reader                   fixed value             (line 52)

[module.test_limited_single_file_present_after_add]
  cache                    container               (line 29)
  disk                     fixed value             (line 29)
  ident                    fixed value             (line 31)
  cache_path               fixed value             (line 34)
  archive_path             fixed value             (line 36)

[module.test_limited_two_files_present_after_add]
  cache                    container               (line 40)
  disk                     fixed value             (line 40)
  names                    fixed value             (line 41)
  name                     stepper                 (line 43)
  filename                 most-recent holder      (line 44)
```

## test_index_csv.py

```

[module]
  CACHE_DIR                fixed value             (line 10)
  INDEX_FILE               fixed value             (line 11)
  LOCAL_DIR                fixed value             (line 12)

[module.disk]
  fs                       fixed value             (line 15)

[module.test_csv_has_entry]
  disk                     fixed value             (line 37)
  right_now                fixed value             (line 38)
  index                    container               (line 39)

[module.test_csv_loads_initially]
  disk                     fixed value             (line 20)
  index                    fixed value             (line 21)

[module.test_csv_saves_changes]
  disk                     fixed value             (line 27)
  right_now                fixed value             (line 28)
  index                    container               (line 29)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- test_io.py

