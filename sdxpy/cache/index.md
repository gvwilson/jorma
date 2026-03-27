# A File Cache

## index_base.py

| Variable | Scope | Role |
|---|---|---|
| CacheEntry | module | fixed value |
| TIME_FORMAT | module.IndexBase | fixed value |
| index_dir | module.IndexBase.__init__ | fixed value |
| self | module.IndexBase.__init__ | fixed value |
| self | module.IndexBase._initialize_index | fixed value |
| identifier | module.IndexBase.add | fixed value |
| self | module.IndexBase.add | fixed value |
| index | module.IndexBase.add | log |
| entry | module.IndexBase.add | fixed value |
| self | module.IndexBase.get_index_dir | fixed value |
| identifier | module.IndexBase.has | fixed value |
| self | module.IndexBase.has | fixed value |
| index | module.IndexBase.has | fixed value |
| self | module.IndexBase.known | fixed value |
| self | module.IndexBase.load | fixed value |
| index | module.IndexBase.save | fixed value |
| self | module.IndexBase.save | fixed value |
| index_dir | module.IndexBase.set_index_dir | fixed value |
| self | module.IndexBase.set_index_dir | fixed value |

## index_csv.py

| Variable | Scope | Role |
|---|---|---|
| INDEX_FILE | module.IndexCSV | fixed value |
| self | module.IndexCSV._initialize_index | fixed value |
| self | module.IndexCSV._make_index_path | fixed value |
| self | module.IndexCSV.load | fixed value |
| index_path | module.IndexCSV.load | fixed value |
| stream | module.IndexCSV.load | fixed value |
| reader | module.IndexCSV.load | fixed value |
| index | module.IndexCSV.save | fixed value |
| self | module.IndexCSV.save | fixed value |
| index_path | module.IndexCSV.save | fixed value |
| stream | module.IndexCSV.save | fixed value |
| writer | module.IndexCSV.save | fixed value |
| entry | module.IndexCSV.save | stepper |
| when | module.IndexCSV.save | most-recent holder |

## test_index_csv.py

| Variable | Scope | Role |
|---|---|---|
| CACHE_DIR | module | fixed value |
| INDEX_FILE | module | fixed value |
| LOCAL_DIR | module | fixed value |
| fs | module.disk | fixed value |
| disk | module.test_csv_has_entry | fixed value |
| right_now | module.test_csv_has_entry | fixed value |
| index | module.test_csv_has_entry | container |
| disk | module.test_csv_loads_initially | fixed value |
| index | module.test_csv_loads_initially | fixed value |
| disk | module.test_csv_saves_changes | fixed value |
| right_now | module.test_csv_saves_changes | fixed value |
| index | module.test_csv_saves_changes | container |

## cache_base.py

| Variable | Scope | Role |
|---|---|---|
| CACHE_SUFFIX | module.CacheBase | fixed value |
| cache_dir | module.CacheBase.__init__ | fixed value |
| index | module.CacheBase.__init__ | fixed value |
| self | module.CacheBase.__init__ | fixed value |
| identifier | module.CacheBase._add | fixed value |
| local_path | module.CacheBase._add | fixed value |
| self | module.CacheBase._add | fixed value |
| identifier | module.CacheBase._make_cache_path | fixed value |
| self | module.CacheBase._make_cache_path | fixed value |
| local_path | module.CacheBase._make_identifier | fixed value |
| self | module.CacheBase._make_identifier | fixed value |
| reader | module.CacheBase._make_identifier | fixed value |
| local_path | module.CacheBase.add | fixed value |
| self | module.CacheBase.add | fixed value |
| identifier | module.CacheBase.add | fixed value |
| identifier | module.CacheBase.get_cache_path | fixed value |
| self | module.CacheBase.get_cache_path | fixed value |
| identifier | module.CacheBase.has | fixed value |
| self | module.CacheBase.has | fixed value |
| self | module.CacheBase.known | fixed value |

## cache_filesystem.py

| Variable | Scope | Role |
|---|---|---|
| identifier | module.CacheFilesystem._add | fixed value |
| local_path | module.CacheFilesystem._add | fixed value |
| self | module.CacheFilesystem._add | fixed value |
| cache_path | module.CacheFilesystem._add | fixed value |

## test_cache_filesystem.py

| Variable | Scope | Role |
|---|---|---|
| CACHE_DIR | module | fixed value |
| fs | module.disk | fixed value |
| cache | module.test_filesystem_duplicate_content_only_saved_once | container |
| disk | module.test_filesystem_duplicate_content_only_saved_once | fixed value |
| contents | module.test_filesystem_duplicate_content_only_saved_once | fixed value |
| ident_first | module.test_filesystem_duplicate_content_only_saved_once | fixed value |
| ident_second | module.test_filesystem_duplicate_content_only_saved_once | fixed value |
| cache | module.test_filesystem_file_can_be_reloaded_after_deletion | container |
| disk | module.test_filesystem_file_can_be_reloaded_after_deletion | fixed value |
| ident | module.test_filesystem_file_can_be_reloaded_after_deletion | fixed value |
| reader | module.test_filesystem_file_can_be_reloaded_after_deletion | fixed value |
| cache | module.test_filesystem_no_files_before_add | fixed value |
| disk | module.test_filesystem_no_files_before_add | fixed value |
| cache | module.test_filesystem_single_file_can_be_reloaded | container |
| disk | module.test_filesystem_single_file_can_be_reloaded | fixed value |
| ident | module.test_filesystem_single_file_can_be_reloaded | fixed value |
| reader | module.test_filesystem_single_file_can_be_reloaded | fixed value |
| cache | module.test_filesystem_single_file_present_after_add | container |
| disk | module.test_filesystem_single_file_present_after_add | fixed value |
| ident | module.test_filesystem_single_file_present_after_add | fixed value |
| cache_path | module.test_filesystem_single_file_present_after_add | fixed value |
| cache | module.test_filesystem_two_files_present_after_add | container |
| disk | module.test_filesystem_two_files_present_after_add | fixed value |
| names | module.test_filesystem_two_files_present_after_add | fixed value |
| name | module.test_filesystem_two_files_present_after_add | stepper |
| filename | module.test_filesystem_two_files_present_after_add | most-recent holder |

## cache_limited.py

| Variable | Scope | Role |
|---|---|---|
| archive_dir | module.CacheLimited.__init__ | fixed value |
| cache_dir | module.CacheLimited.__init__ | fixed value |
| index | module.CacheLimited.__init__ | fixed value |
| local_limit | module.CacheLimited.__init__ | fixed value |
| self | module.CacheLimited.__init__ | fixed value |
| identifier | module.CacheLimited._add | fixed value |
| local_path | module.CacheLimited._add | fixed value |
| self | module.CacheLimited._add | fixed value |
| identifier | module.CacheLimited._add_archive | fixed value |
| local_path | module.CacheLimited._add_archive | fixed value |
| self | module.CacheLimited._add_archive | fixed value |
| archive_path | module.CacheLimited._add_archive | fixed value |
| self | module.CacheLimited._ensure_cache_space | fixed value |
| cache_dir | module.CacheLimited._ensure_cache_space | fixed value |
| cache_files | module.CacheLimited._ensure_cache_space | container |
| choice | module.CacheLimited._ensure_cache_space | fixed value |
| identifier | module.CacheLimited._make_archive_path | fixed value |
| self | module.CacheLimited._make_archive_path | fixed value |
| identifier | module.CacheLimited.get_cache_path | fixed value |
| self | module.CacheLimited.get_cache_path | fixed value |
| cache_path | module.CacheLimited.get_cache_path | fixed value |
| archive_path | module.CacheLimited.get_cache_path | fixed value |

## test_cache_limited.py

| Variable | Scope | Role |
|---|---|---|
| CACHE_DIR | module | fixed value |
| ARCHIVE_DIR | module | fixed value |
| LOCAL_LIMIT | module | fixed value |
| disk | module.cache | fixed value |
| index | module.cache | fixed value |
| fs | module.disk | fixed value |
| cache | module.test_limited_all_files_can_be_retrieved | container |
| disk | module.test_limited_all_files_can_be_retrieved | fixed value |
| names | module.test_limited_all_files_can_be_retrieved | fixed value |
| idents | module.test_limited_all_files_can_be_retrieved | fixed value |
| name | module.test_limited_all_files_can_be_retrieved | stepper |
| local_file | module.test_limited_all_files_can_be_retrieved | most-recent holder |
| ident | module.test_limited_all_files_can_be_retrieved | stepper |
| cache_path | module.test_limited_all_files_can_be_retrieved | most-recent holder |
| cache | module.test_limited_duplicate_content_only_saved_once | container |
| disk | module.test_limited_duplicate_content_only_saved_once | fixed value |
| contents | module.test_limited_duplicate_content_only_saved_once | fixed value |
| ident_first | module.test_limited_duplicate_content_only_saved_once | fixed value |
| ident_second | module.test_limited_duplicate_content_only_saved_once | fixed value |
| cache | module.test_limited_file_can_be_reloaded_after_deletion | container |
| disk | module.test_limited_file_can_be_reloaded_after_deletion | fixed value |
| ident | module.test_limited_file_can_be_reloaded_after_deletion | fixed value |
| reader | module.test_limited_file_can_be_reloaded_after_deletion | fixed value |
| cache | module.test_limited_local_cache_size_stays_small | container |
| disk | module.test_limited_local_cache_size_stays_small | fixed value |
| names | module.test_limited_local_cache_size_stays_small | fixed value |
| name | module.test_limited_local_cache_size_stays_small | stepper |
| local_file | module.test_limited_local_cache_size_stays_small | most-recent holder |
| cache | module.test_limited_no_files_before_add | fixed value |
| cache | module.test_limited_single_file_can_be_reloaded | container |
| disk | module.test_limited_single_file_can_be_reloaded | fixed value |
| ident | module.test_limited_single_file_can_be_reloaded | fixed value |
| reader | module.test_limited_single_file_can_be_reloaded | fixed value |
| cache | module.test_limited_single_file_present_after_add | container |
| disk | module.test_limited_single_file_present_after_add | fixed value |
| ident | module.test_limited_single_file_present_after_add | fixed value |
| cache_path | module.test_limited_single_file_present_after_add | fixed value |
| archive_path | module.test_limited_single_file_present_after_add | fixed value |
| cache | module.test_limited_two_files_present_after_add | container |
| disk | module.test_limited_two_files_present_after_add | fixed value |
| names | module.test_limited_two_files_present_after_add | fixed value |
| name | module.test_limited_two_files_present_after_add | stepper |
| filename | module.test_limited_two_files_present_after_add | most-recent holder |

## cache_io.py

| Variable | Scope | Role |
|---|---|---|
| cache | module.cache_open | fixed value |
| filename | module.cache_open | unknown |
| reader | module.cache_open | fixed value |
| identifier | module.cache_open | fixed value |
| cache_path | module.cache_open | fixed value |
| cache | module.cache_save | container |
| filename | module.cache_save | fixed value |
| identifier | module.cache_save | fixed value |
| identifier_file | module.cache_save | fixed value |
| writer | module.cache_save | fixed value |

