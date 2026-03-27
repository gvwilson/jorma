# Variable Role Analysis: cache

## cache_base.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'exceptions'
### Static analysis

| Scope                             | Variable     | Role        | Location |
| :---------------------------------| :------------| :-----------| :--------|
| module.CacheBase                  | CACHE_SUFFIX | fixed value | line 9   |
| module.CacheBase.__init__         | cache_dir    | fixed value | line 11  |
| module.CacheBase.__init__         | index        | fixed value | line 11  |
| module.CacheBase.__init__         | self         | fixed value | line 11  |
| module.CacheBase._add             | identifier   | fixed value | line 40  |
| module.CacheBase._add             | local_path   | fixed value | line 40  |
| module.CacheBase._add             | self         | fixed value | line 40  |
| module.CacheBase._make_cache_path | identifier   | fixed value | line 36  |
| module.CacheBase._make_cache_path | self         | fixed value | line 36  |
| module.CacheBase._make_identifier | local_path   | fixed value | line 32  |
| module.CacheBase._make_identifier | self         | fixed value | line 32  |
| module.CacheBase._make_identifier | reader       | fixed value | line 33  |
| module.CacheBase.add              | local_path   | fixed value | line 15  |
| module.CacheBase.add              | self         | fixed value | line 15  |
| module.CacheBase.add              | identifier   | fixed value | line 16  |
| module.CacheBase.get_cache_path   | identifier   | fixed value | line 21  |
| module.CacheBase.get_cache_path   | self         | fixed value | line 21  |
| module.CacheBase.has              | identifier   | fixed value | line 26  |
| module.CacheBase.has              | self         | fixed value | line 26  |
| module.CacheBase.known            | self         | fixed value | line 29  |

## cache_filesystem.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'cache_base'
### Static analysis

| Scope                       | Variable   | Role        | Location |
| :---------------------------| :----------| :-----------| :--------|
| module.CacheFilesystem._add | identifier | fixed value | line 8   |
| module.CacheFilesystem._add | local_path | fixed value | line 8   |
| module.CacheFilesystem._add | self       | fixed value | line 8   |
| module.CacheFilesystem._add | cache_path | fixed value | line 9   |

## cache_io.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'cache_base'
### Static analysis

| Scope             | Variable        | Role        | Location |
| :-----------------| :---------------| :-----------| :--------|
| module.cache_open | cache           | fixed value | line 6   |
| module.cache_open | filename        | unknown     | line 6   |
| module.cache_open | reader          | fixed value | line 12  |
| module.cache_open | identifier      | fixed value | line 13  |
| module.cache_open | cache_path      | fixed value | line 14  |
| module.cache_save | cache           | container   | line 19  |
| module.cache_save | filename        | fixed value | line 19  |
| module.cache_save | identifier      | fixed value | line 20  |
| module.cache_save | identifier_file | fixed value | line 21  |
| module.cache_save | writer          | fixed value | line 22  |

## cache_limited.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'cache_filesystem'
### Static analysis

| Scope                                   | Variable     | Role        | Location |
| :---------------------------------------| :------------| :-----------| :--------|
| module.CacheLimited.__init__            | archive_dir  | fixed value | line 8   |
| module.CacheLimited.__init__            | cache_dir    | fixed value | line 8   |
| module.CacheLimited.__init__            | index        | fixed value | line 8   |
| module.CacheLimited.__init__            | local_limit  | fixed value | line 8   |
| module.CacheLimited.__init__            | self         | fixed value | line 8   |
| module.CacheLimited._add                | identifier   | fixed value | line 40  |
| module.CacheLimited._add                | local_path   | fixed value | line 40  |
| module.CacheLimited._add                | self         | fixed value | line 40  |
| module.CacheLimited._add_archive        | identifier   | fixed value | line 46  |
| module.CacheLimited._add_archive        | local_path   | fixed value | line 46  |
| module.CacheLimited._add_archive        | self         | fixed value | line 46  |
| module.CacheLimited._add_archive        | archive_path | fixed value | line 47  |
| module.CacheLimited._ensure_cache_space | self         | fixed value | line 25  |
| module.CacheLimited._ensure_cache_space | cache_dir    | fixed value | line 27  |
| module.CacheLimited._ensure_cache_space | cache_files  | container   | line 29  |
| module.CacheLimited._ensure_cache_space | choice       | fixed value | line 34  |
| module.CacheLimited._make_archive_path  | identifier   | fixed value | line 51  |
| module.CacheLimited._make_archive_path  | self         | fixed value | line 51  |
| module.CacheLimited.get_cache_path      | identifier   | fixed value | line 15  |
| module.CacheLimited.get_cache_path      | self         | fixed value | line 15  |
| module.CacheLimited.get_cache_path      | cache_path   | fixed value | line 16  |
| module.CacheLimited.get_cache_path      | archive_path | fixed value | line 19  |

## index_base.py

### Static analysis

| Scope                              | Variable    | Role        | Location |
| :----------------------------------| :-----------| :-----------| :--------|
| module                             | CacheEntry  | fixed value | line 7   |
| module.IndexBase                   | TIME_FORMAT | fixed value | line 12  |
| module.IndexBase.__init__          | index_dir   | fixed value | line 14  |
| module.IndexBase.__init__          | self        | fixed value | line 14  |
| module.IndexBase._initialize_index | self        | fixed value | line 48  |
| module.IndexBase.add               | identifier  | fixed value | line 31  |
| module.IndexBase.add               | self        | fixed value | line 31  |
| module.IndexBase.add               | index       | log         | line 32  |
| module.IndexBase.add               | entry       | fixed value | line 33  |
| module.IndexBase.get_index_dir     | self        | fixed value | line 17  |
| module.IndexBase.has               | identifier  | fixed value | line 24  |
| module.IndexBase.has               | self        | fixed value | line 24  |
| module.IndexBase.has               | index       | fixed value | line 25  |
| module.IndexBase.known             | self        | fixed value | line 28  |
| module.IndexBase.load              | self        | fixed value | line 40  |
| module.IndexBase.save              | index       | fixed value | line 44  |
| module.IndexBase.save              | self        | fixed value | line 44  |
| module.IndexBase.set_index_dir     | index_dir   | fixed value | line 20  |
| module.IndexBase.set_index_dir     | self        | fixed value | line 20  |

### Dynamic analysis

| Variable | Scope                                                                                  | Role  |
| :--------| :--------------------------------------------------------------------------------------| :-----|
| fullname | module._find_and_load._find_and_load_unlocked._find_spec.find_spec                     | phase |
| name     | module.namedtuple                                                                      | phase |
| name     | module.namedtuple.<genexpr>                                                            | phase |
| suffix   | module._find_and_load._find_and_load_unlocked._find_spec.find_spec._get_spec.find_spec | phase |

## index_csv.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'exceptions'
### Static analysis

| Scope                             | Variable   | Role               | Location |
| :---------------------------------| :----------| :------------------| :--------|
| module.IndexCSV                   | INDEX_FILE | fixed value        | line 40  |
| module.IndexCSV._initialize_index | self       | fixed value        | line 42  |
| module.IndexCSV._make_index_path  | self       | fixed value        | line 45  |
| module.IndexCSV.load              | self       | fixed value        | line 10  |
| module.IndexCSV.load              | index_path | fixed value        | line 14  |
| module.IndexCSV.load              | stream     | fixed value        | line 18  |
| module.IndexCSV.load              | reader     | fixed value        | line 19  |
| module.IndexCSV.save              | index      | fixed value        | line 27  |
| module.IndexCSV.save              | self       | fixed value        | line 27  |
| module.IndexCSV.save              | index_path | fixed value        | line 31  |
| module.IndexCSV.save              | stream     | fixed value        | line 32  |
| module.IndexCSV.save              | writer     | fixed value        | line 33  |
| module.IndexCSV.save              | entry      | stepper            | line 34  |
| module.IndexCSV.save              | when       | most-recent holder | line 35  |

## test_cache_filesystem.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'cache_filesystem'
### Static analysis

| Scope                                                      | Variable     | Role               | Location |
| :----------------------------------------------------------| :------------| :------------------| :--------|
| module                                                     | CACHE_DIR    | fixed value        | line 10  |
| module.disk                                                | fs           | fixed value        | line 13  |
| module.test_filesystem_duplicate_content_only_saved_once   | cache        | container          | line 59  |
| module.test_filesystem_duplicate_content_only_saved_once   | disk         | fixed value        | line 59  |
| module.test_filesystem_duplicate_content_only_saved_once   | contents     | fixed value        | line 60  |
| module.test_filesystem_duplicate_content_only_saved_once   | ident_first  | fixed value        | line 62  |
| module.test_filesystem_duplicate_content_only_saved_once   | ident_second | fixed value        | line 64  |
| module.test_filesystem_file_can_be_reloaded_after_deletion | cache        | container          | line 51  |
| module.test_filesystem_file_can_be_reloaded_after_deletion | disk         | fixed value        | line 51  |
| module.test_filesystem_file_can_be_reloaded_after_deletion | ident        | fixed value        | line 53  |
| module.test_filesystem_file_can_be_reloaded_after_deletion | reader       | fixed value        | line 55  |
| module.test_filesystem_no_files_before_add                 | cache        | fixed value        | line 23  |
| module.test_filesystem_no_files_before_add                 | disk         | fixed value        | line 23  |
| module.test_filesystem_single_file_can_be_reloaded         | cache        | container          | line 45  |
| module.test_filesystem_single_file_can_be_reloaded         | disk         | fixed value        | line 45  |
| module.test_filesystem_single_file_can_be_reloaded         | ident        | fixed value        | line 47  |
| module.test_filesystem_single_file_can_be_reloaded         | reader       | fixed value        | line 48  |
| module.test_filesystem_single_file_present_after_add       | cache        | container          | line 27  |
| module.test_filesystem_single_file_present_after_add       | disk         | fixed value        | line 27  |
| module.test_filesystem_single_file_present_after_add       | ident        | fixed value        | line 29  |
| module.test_filesystem_single_file_present_after_add       | cache_path   | fixed value        | line 32  |
| module.test_filesystem_two_files_present_after_add         | cache        | container          | line 36  |
| module.test_filesystem_two_files_present_after_add         | disk         | fixed value        | line 36  |
| module.test_filesystem_two_files_present_after_add         | names        | fixed value        | line 37  |
| module.test_filesystem_two_files_present_after_add         | name         | stepper            | line 38  |
| module.test_filesystem_two_files_present_after_add         | filename     | most-recent holder | line 39  |

## test_cache_limited.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'cache_limited'
### Static analysis

| Scope                                                   | Variable     | Role               | Location |
| :-------------------------------------------------------| :------------| :------------------| :--------|
| module                                                  | CACHE_DIR    | fixed value        | line 10  |
| module                                                  | ARCHIVE_DIR  | fixed value        | line 11  |
| module                                                  | LOCAL_LIMIT  | fixed value        | line 12  |
| module.cache                                            | disk         | fixed value        | line 21  |
| module.cache                                            | index        | fixed value        | line 22  |
| module.disk                                             | fs           | fixed value        | line 15  |
| module.test_limited_all_files_can_be_retrieved          | cache        | container          | line 83  |
| module.test_limited_all_files_can_be_retrieved          | disk         | fixed value        | line 83  |
| module.test_limited_all_files_can_be_retrieved          | names        | fixed value        | line 84  |
| module.test_limited_all_files_can_be_retrieved          | idents       | fixed value        | line 86  |
| module.test_limited_all_files_can_be_retrieved          | name         | stepper            | line 88  |
| module.test_limited_all_files_can_be_retrieved          | local_file   | most-recent holder | line 89  |
| module.test_limited_all_files_can_be_retrieved          | ident        | stepper            | line 93  |
| module.test_limited_all_files_can_be_retrieved          | cache_path   | most-recent holder | line 96  |
| module.test_limited_duplicate_content_only_saved_once   | cache        | container          | line 63  |
| module.test_limited_duplicate_content_only_saved_once   | disk         | fixed value        | line 63  |
| module.test_limited_duplicate_content_only_saved_once   | contents     | fixed value        | line 64  |
| module.test_limited_duplicate_content_only_saved_once   | ident_first  | fixed value        | line 66  |
| module.test_limited_duplicate_content_only_saved_once   | ident_second | fixed value        | line 68  |
| module.test_limited_file_can_be_reloaded_after_deletion | cache        | container          | line 55  |
| module.test_limited_file_can_be_reloaded_after_deletion | disk         | fixed value        | line 55  |
| module.test_limited_file_can_be_reloaded_after_deletion | ident        | fixed value        | line 57  |
| module.test_limited_file_can_be_reloaded_after_deletion | reader       | fixed value        | line 59  |
| module.test_limited_local_cache_size_stays_small        | cache        | container          | line 72  |
| module.test_limited_local_cache_size_stays_small        | disk         | fixed value        | line 72  |
| module.test_limited_local_cache_size_stays_small        | names        | fixed value        | line 73  |
| module.test_limited_local_cache_size_stays_small        | name         | stepper            | line 75  |
| module.test_limited_local_cache_size_stays_small        | local_file   | most-recent holder | line 76  |
| module.test_limited_no_files_before_add                 | cache        | fixed value        | line 25  |
| module.test_limited_single_file_can_be_reloaded         | cache        | container          | line 49  |
| module.test_limited_single_file_can_be_reloaded         | disk         | fixed value        | line 49  |
| module.test_limited_single_file_can_be_reloaded         | ident        | fixed value        | line 51  |
| module.test_limited_single_file_can_be_reloaded         | reader       | fixed value        | line 52  |
| module.test_limited_single_file_present_after_add       | cache        | container          | line 29  |
| module.test_limited_single_file_present_after_add       | disk         | fixed value        | line 29  |
| module.test_limited_single_file_present_after_add       | ident        | fixed value        | line 31  |
| module.test_limited_single_file_present_after_add       | cache_path   | fixed value        | line 34  |
| module.test_limited_single_file_present_after_add       | archive_path | fixed value        | line 36  |
| module.test_limited_two_files_present_after_add         | cache        | container          | line 40  |
| module.test_limited_two_files_present_after_add         | disk         | fixed value        | line 40  |
| module.test_limited_two_files_present_after_add         | names        | fixed value        | line 41  |
| module.test_limited_two_files_present_after_add         | name         | stepper            | line 43  |
| module.test_limited_two_files_present_after_add         | filename     | most-recent holder | line 44  |

## test_index_csv.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'index_base'
### Static analysis

| Scope                           | Variable   | Role        | Location |
| :-------------------------------| :----------| :-----------| :--------|
| module                          | CACHE_DIR  | fixed value | line 10  |
| module                          | INDEX_FILE | fixed value | line 11  |
| module                          | LOCAL_DIR  | fixed value | line 12  |
| module.disk                     | fs         | fixed value | line 15  |
| module.test_csv_has_entry       | disk       | fixed value | line 37  |
| module.test_csv_has_entry       | right_now  | fixed value | line 38  |
| module.test_csv_has_entry       | index      | container   | line 39  |
| module.test_csv_loads_initially | disk       | fixed value | line 20  |
| module.test_csv_loads_initially | index      | fixed value | line 21  |
| module.test_csv_saves_changes   | disk       | fixed value | line 27  |
| module.test_csv_saves_changes   | right_now  | fixed value | line 28  |
| module.test_csv_saves_changes   | index      | container   | line 29  |

