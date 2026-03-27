# Variable Role Analysis: persist

## aliasing.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'objects'
### Static analysis

| Scope                       | Variable | Role               | Location |
| :---------------------------| :--------| :------------------| :--------|
| module.LoadAlias.__init__   | reader   | fixed value        | line 57  |
| module.LoadAlias.__init__   | self     | fixed value        | line 57  |
| module.LoadAlias.load       | self     | fixed value        | line 61  |
| module.LoadAlias.load       | line     | fixed value        | line 62  |
| module.LoadAlias.load       | fields   | fixed value        | line 65  |
| module.LoadAlias.load       | ident    | fixed value        | line 67  |
| module.LoadAlias.load       | key      | fixed value        | line 67  |
| module.LoadAlias.load       | value    | fixed value        | line 67  |
| module.LoadAlias.load       | method   | fixed value        | line 73  |
| module.LoadAlias.load_bool  | ident    | fixed value        | line 77  |
| module.LoadAlias.load_bool  | self     | fixed value        | line 77  |
| module.LoadAlias.load_bool  | value    | fixed value        | line 77  |
| module.LoadAlias.load_dict  | ident    | fixed value        | line 109 |
| module.LoadAlias.load_dict  | length   | fixed value        | line 109 |
| module.LoadAlias.load_dict  | self     | fixed value        | line 109 |
| module.LoadAlias.load_dict  | result   | fixed value        | line 110 |
| module.LoadAlias.load_dict  | _        | stepper            | line 112 |
| module.LoadAlias.load_dict  | k        | most-recent holder | line 113 |
| module.LoadAlias.load_dict  | v        | most-recent holder | line 114 |
| module.LoadAlias.load_float | ident    | fixed value        | line 81  |
| module.LoadAlias.load_float | self     | fixed value        | line 81  |
| module.LoadAlias.load_float | value    | fixed value        | line 81  |
| module.LoadAlias.load_int   | ident    | fixed value        | line 85  |
| module.LoadAlias.load_int   | self     | fixed value        | line 85  |
| module.LoadAlias.load_int   | value    | fixed value        | line 85  |
| module.LoadAlias.load_list  | ident    | fixed value        | line 94  |
| module.LoadAlias.load_list  | length   | fixed value        | line 94  |
| module.LoadAlias.load_list  | self     | fixed value        | line 94  |
| module.LoadAlias.load_list  | result   | log                | line 95  |
| module.LoadAlias.load_list  | _        | stepper            | line 97  |
| module.LoadAlias.load_set   | ident    | fixed value        | line 102 |
| module.LoadAlias.load_set   | length   | fixed value        | line 102 |
| module.LoadAlias.load_set   | self     | fixed value        | line 102 |
| module.LoadAlias.load_set   | result   | container          | line 103 |
| module.LoadAlias.load_set   | _        | stepper            | line 105 |
| module.LoadAlias.load_str   | ident    | fixed value        | line 89  |
| module.LoadAlias.load_str   | self     | fixed value        | line 89  |
| module.LoadAlias.load_str   | value    | fixed value        | line 89  |
| module.SaveAlias.__init__   | self     | fixed value        | line 5   |
| module.SaveAlias.__init__   | writer   | fixed value        | line 5   |
| module.SaveAlias.save       | self     | fixed value        | line 10  |
| module.SaveAlias.save       | thing    | fixed value        | line 10  |
| module.SaveAlias.save       | thing_id | fixed value        | line 11  |
| module.SaveAlias.save       | typename | fixed value        | line 17  |
| module.SaveAlias.save       | method   | fixed value        | line 18  |
| module.SaveAlias.save_bool  | self     | fixed value        | line 24  |
| module.SaveAlias.save_bool  | thing    | fixed value        | line 24  |
| module.SaveAlias.save_dict  | self     | fixed value        | line 49  |
| module.SaveAlias.save_dict  | thing    | fixed value        | line 49  |
| module.SaveAlias.save_dict  | key      | stepper            | line 51  |
| module.SaveAlias.save_dict  | value    | stepper            | line 51  |
| module.SaveAlias.save_float | self     | fixed value        | line 27  |
| module.SaveAlias.save_float | thing    | fixed value        | line 27  |
| module.SaveAlias.save_int   | self     | fixed value        | line 30  |
| module.SaveAlias.save_int   | thing    | fixed value        | line 30  |
| module.SaveAlias.save_list  | self     | fixed value        | line 33  |
| module.SaveAlias.save_list  | thing    | fixed value        | line 33  |
| module.SaveAlias.save_list  | item     | stepper            | line 35  |
| module.SaveAlias.save_set   | self     | fixed value        | line 38  |
| module.SaveAlias.save_set   | thing    | fixed value        | line 38  |
| module.SaveAlias.save_set   | item     | stepper            | line 40  |
| module.SaveAlias.save_str   | self     | fixed value        | line 43  |
| module.SaveAlias.save_str   | thing    | fixed value        | line 43  |
| module.SaveAlias.save_str   | lines    | fixed value        | line 44  |
| module.SaveAlias.save_str   | line     | stepper            | line 46  |

## aliasing_wrong.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'objects'
### Static analysis

| Scope                       | Variable | Role        | Location |
| :---------------------------| :--------| :-----------| :--------|
| module.LoadAlias.__init__   | reader   | fixed value | line 59  |
| module.LoadAlias.__init__   | self     | fixed value | line 59  |
| module.LoadAlias.load       | self     | fixed value | line 63  |
| module.LoadAlias.load       | line     | fixed value | line 64  |
| module.LoadAlias.load       | fields   | fixed value | line 66  |
| module.LoadAlias.load       | ident    | fixed value | line 68  |
| module.LoadAlias.load       | key      | fixed value | line 68  |
| module.LoadAlias.load       | value    | fixed value | line 68  |
| module.LoadAlias.load       | method   | fixed value | line 75  |
| module.LoadAlias.load       | result   | fixed value | line 77  |
| module.SaveAlias.__init__   | self     | fixed value | line 6   |
| module.SaveAlias.__init__   | writer   | fixed value | line 6   |
| module.SaveAlias.save       | self     | fixed value | line 10  |
| module.SaveAlias.save       | thing    | fixed value | line 10  |
| module.SaveAlias.save       | thing_id | fixed value | line 11  |
| module.SaveAlias.save       | typename | fixed value | line 17  |
| module.SaveAlias.save       | method   | fixed value | line 18  |
| module.SaveAlias.save_bool  | self     | fixed value | line 23  |
| module.SaveAlias.save_bool  | thing    | fixed value | line 23  |
| module.SaveAlias.save_dict  | self     | fixed value | line 50  |
| module.SaveAlias.save_dict  | thing    | fixed value | line 50  |
| module.SaveAlias.save_dict  | key      | stepper     | line 52  |
| module.SaveAlias.save_dict  | value    | stepper     | line 52  |
| module.SaveAlias.save_float | self     | fixed value | line 26  |
| module.SaveAlias.save_float | thing    | fixed value | line 26  |
| module.SaveAlias.save_int   | self     | fixed value | line 29  |
| module.SaveAlias.save_int   | thing    | fixed value | line 29  |
| module.SaveAlias.save_list  | self     | fixed value | line 33  |
| module.SaveAlias.save_list  | thing    | fixed value | line 33  |
| module.SaveAlias.save_list  | item     | stepper     | line 35  |
| module.SaveAlias.save_set   | self     | fixed value | line 39  |
| module.SaveAlias.save_set   | thing    | fixed value | line 39  |
| module.SaveAlias.save_set   | item     | stepper     | line 41  |
| module.SaveAlias.save_str   | self     | fixed value | line 44  |
| module.SaveAlias.save_str   | thing    | fixed value | line 44  |
| module.SaveAlias.save_str   | lines    | fixed value | line 45  |
| module.SaveAlias.save_str   | line     | stepper     | line 47  |

## attr.py

### Static analysis

| Scope                   | Variable | Role        | Location |
| :-----------------------| :--------| :-----------| :--------|
| module                  | ex       | fixed value | line 8   |
| module                  | method   | fixed value | line 12  |
| module.Example.__init__ | label    | fixed value | line 2   |
| module.Example.__init__ | self     | fixed value | line 2   |
| module.Example.get_size | self     | fixed value | line 5   |
ex has missing False
ex has label True with value thing
ex has get_size True
result of calling method 5

## builtin.py

### Static analysis

| Scope       | Variable | Role               | Location |
| :-----------| :--------| :------------------| :--------|
| module.load | reader   | fixed value        | line 48  |
| module.load | line     | fixed value        | line 49  |
| module.load | fields   | fixed value        | line 51  |
| module.load | key      | fixed value        | line 53  |
| module.load | value    | fixed value        | line 53  |
| module.load | names    | fixed value        | line 56  |
| module.load | lines    | fixed value        | line 68  |
| module.load | result   | fixed value        | line 80  |
| module.load | _        | stepper            | line 81  |
| module.load | k        | most-recent holder | line 82  |
| module.load | v        | most-recent holder | line 83  |
| module.save | thing    | fixed value        | line 2   |
| module.save | writer   | fixed value        | line 2   |
| module.save | lines    | fixed value        | line 15  |
| module.save | line     | stepper            | line 17  |
| module.save | item     | stepper            | line 24  |
| module.save | key      | stepper            | line 38  |
| module.save | value    | stepper            | line 38  |

## ex_aliasing.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | shared   | fixed value | line 1   |
| module | fixture  | fixed value | line 2   |

## ex_circular.py

### Static analysis

| Scope  | Variable | Role | Location |
| :------| :--------| :----| :--------|
| module | fixture  | log  | line 1   |

## objects.py

### Static analysis

| Scope                         | Variable | Role               | Location |
| :-----------------------------| :--------| :------------------| :--------|
| module.LoadObjects.__init__   | reader   | fixed value        | line 53  |
| module.LoadObjects.__init__   | self     | fixed value        | line 53  |
| module.LoadObjects.load       | self     | fixed value        | line 56  |
| module.LoadObjects.load       | line     | fixed value        | line 57  |
| module.LoadObjects.load       | fields   | fixed value        | line 59  |
| module.LoadObjects.load       | key      | fixed value        | line 61  |
| module.LoadObjects.load       | value    | fixed value        | line 61  |
| module.LoadObjects.load       | method   | fixed value        | line 62  |
| module.LoadObjects.load_bool  | self     | fixed value        | line 67  |
| module.LoadObjects.load_bool  | value    | fixed value        | line 67  |
| module.LoadObjects.load_bool  | names    | fixed value        | line 68  |
| module.LoadObjects.load_dict  | self     | fixed value        | line 93  |
| module.LoadObjects.load_dict  | value    | fixed value        | line 93  |
| module.LoadObjects.load_dict  | result   | fixed value        | line 94  |
| module.LoadObjects.load_dict  | _        | stepper            | line 95  |
| module.LoadObjects.load_dict  | k        | most-recent holder | line 96  |
| module.LoadObjects.load_dict  | v        | most-recent holder | line 97  |
| module.LoadObjects.load_float | self     | fixed value        | line 73  |
| module.LoadObjects.load_float | value    | fixed value        | line 73  |
| module.LoadObjects.load_int   | self     | fixed value        | line 77  |
| module.LoadObjects.load_int   | value    | fixed value        | line 77  |
| module.LoadObjects.load_list  | self     | fixed value        | line 86  |
| module.LoadObjects.load_list  | value    | fixed value        | line 86  |
| module.LoadObjects.load_set   | self     | fixed value        | line 90  |
| module.LoadObjects.load_set   | value    | fixed value        | line 90  |
| module.LoadObjects.load_str   | self     | fixed value        | line 80  |
| module.LoadObjects.load_str   | value    | fixed value        | line 80  |
| module.SaveObjects.__init__   | self     | fixed value        | line 3   |
| module.SaveObjects.__init__   | writer   | fixed value        | line 3   |
| module.SaveObjects._write     | fields   | fixed value        | line 14  |
| module.SaveObjects._write     | self     | fixed value        | line 14  |
| module.SaveObjects.save       | self     | fixed value        | line 6   |
| module.SaveObjects.save       | thing    | fixed value        | line 6   |
| module.SaveObjects.save       | typename | fixed value        | line 7   |
| module.SaveObjects.save       | method   | fixed value        | line 8   |
| module.SaveObjects.save_bool  | self     | fixed value        | line 17  |
| module.SaveObjects.save_bool  | thing    | fixed value        | line 17  |
| module.SaveObjects.save_dict  | self     | fixed value        | line 44  |
| module.SaveObjects.save_dict  | thing    | fixed value        | line 44  |
| module.SaveObjects.save_dict  | key      | stepper            | line 46  |
| module.SaveObjects.save_dict  | value    | stepper            | line 46  |
| module.SaveObjects.save_float | self     | fixed value        | line 20  |
| module.SaveObjects.save_float | thing    | fixed value        | line 20  |
| module.SaveObjects.save_int   | self     | fixed value        | line 24  |
| module.SaveObjects.save_int   | thing    | fixed value        | line 24  |
| module.SaveObjects.save_list  | self     | fixed value        | line 34  |
| module.SaveObjects.save_list  | thing    | fixed value        | line 34  |
| module.SaveObjects.save_list  | item     | stepper            | line 36  |
| module.SaveObjects.save_set   | self     | fixed value        | line 39  |
| module.SaveObjects.save_set   | thing    | fixed value        | line 39  |
| module.SaveObjects.save_set   | item     | stepper            | line 41  |
| module.SaveObjects.save_str   | self     | fixed value        | line 27  |
| module.SaveObjects.save_str   | thing    | fixed value        | line 27  |
| module.SaveObjects.save_str   | lines    | fixed value        | line 28  |
| module.SaveObjects.save_str   | line     | stepper            | line 30  |

## save_aliasing.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'aliasing'
### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | word     | fixed value | line 5   |
| module | child    | fixed value | line 6   |
| module | parent   | log         | line 7   |
| module | saver    | fixed value | line 11  |

## save_builtin.py

Warning: no variables found.
Error during dynamic analysis (ModuleNotFoundError): No module named 'builtin'
### Static analysis


## test_aliasing_wrong.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'aliasing_wrong'
### Static analysis

| Scope                             | Variable | Role        | Location |
| :---------------------------------| :--------| :-----------| :--------|
| module.roundtrip                  | fixture  | fixed value | line 8   |
| module.roundtrip                  | writer   | fixed value | line 9   |
| module.roundtrip                  | reader   | fixed value | line 11  |
| module.test_aliasing_circular     | fixture  | log         | line 35  |
| module.test_aliasing_circular     | result   | fixed value | line 37  |
| module.test_aliasing_no_aliasing  | fixture  | fixed value | line 17  |
| module.test_aliasing_shared_child | shared   | fixed value | line 23  |
| module.test_aliasing_shared_child | fixture  | fixed value | line 24  |
| module.test_aliasing_shared_child | result   | fixed value | line 25  |

## test_builtin.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'builtin'
### Static analysis

| Scope                         | Variable | Role        | Location |
| :-----------------------------| :--------| :-----------| :--------|
| module.test_load_bool_single  | fixture  | fixed value | line 102 |
| module.test_load_dict_empty   | fixture  | fixed value | line 107 |
| module.test_load_dict_flat    | fixture  | fixed value | line 112 |
| module.test_load_float_single | fixture  | fixed value | line 127 |
| module.test_load_int_single   | fixture  | fixed value | line 132 |
| module.test_load_list_flat    | fixture  | fixed value | line 137 |
| module.test_load_set_flat     | fixture  | fixed value | line 172 |
| module.test_load_str_single   | fixture  | fixed value | line 150 |
| module.test_load_str_single   | expected | fixed value | line 161 |
| module.test_roundtrip         | fixture  | fixed value | line 186 |
| module.test_roundtrip         | output   | fixed value | line 187 |
| module.test_roundtrip         | archive  | fixed value | line 189 |
| module.test_roundtrip         | result   | fixed value | line 190 |
| module.test_save_bool_single  | output   | fixed value | line 8   |
| module.test_save_dict_empty   | output   | fixed value | line 14  |
| module.test_save_dict_flat    | fixture  | fixed value | line 20  |
| module.test_save_dict_flat    | expected | fixed value | line 21  |
| module.test_save_dict_flat    | output   | fixed value | line 30  |
| module.test_save_float_single | output   | fixed value | line 36  |
| module.test_save_int_single   | output   | fixed value | line 42  |
| module.test_save_list_flat    | fixture  | fixed value | line 49  |
| module.test_save_list_flat    | expected | fixed value | line 50  |
| module.test_save_list_flat    | output   | fixed value | line 55  |
| module.test_save_set_flat     | fixture  | fixed value | line 80  |
| module.test_save_set_flat     | first    | fixed value | line 81  |
| module.test_save_set_flat     | second   | fixed value | line 88  |
| module.test_save_set_flat     | output   | fixed value | line 95  |
| module.test_save_set_flat     | actual   | fixed value | line 97  |
| module.test_save_str_single   | fixture  | fixed value | line 62  |
| module.test_save_str_single   | expected | fixed value | line 67  |
| module.test_save_str_single   | output   | fixed value | line 74  |

