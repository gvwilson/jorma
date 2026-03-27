# Object Persistence

## builtin.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.load | fixed value |
| line | module.load | fixed value |
| fields | module.load | fixed value |
| key | module.load | fixed value |
| value | module.load | fixed value |
| names | module.load | fixed value |
| lines | module.load | fixed value |
| result | module.load | fixed value |
| _ | module.load | stepper |
| k | module.load | most-recent holder |
| v | module.load | most-recent holder |
| thing | module.save | fixed value |
| writer | module.save | fixed value |
| lines | module.save | fixed value |
| line | module.save | stepper |
| item | module.save | stepper |
| key | module.save | stepper |
| value | module.save | stepper |

## save_builtin.py

*No variables identified by jorma.*

## test_builtin.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.test_load_bool_single | fixed value |
| fixture | module.test_load_dict_empty | fixed value |
| fixture | module.test_load_dict_flat | fixed value |
| fixture | module.test_load_float_single | fixed value |
| fixture | module.test_load_int_single | fixed value |
| fixture | module.test_load_list_flat | fixed value |
| fixture | module.test_load_set_flat | fixed value |
| fixture | module.test_load_str_single | fixed value |
| expected | module.test_load_str_single | fixed value |
| fixture | module.test_roundtrip | fixed value |
| output | module.test_roundtrip | fixed value |
| archive | module.test_roundtrip | fixed value |
| result | module.test_roundtrip | fixed value |
| output | module.test_save_bool_single | fixed value |
| output | module.test_save_dict_empty | fixed value |
| fixture | module.test_save_dict_flat | fixed value |
| expected | module.test_save_dict_flat | fixed value |
| output | module.test_save_dict_flat | fixed value |
| output | module.test_save_float_single | fixed value |
| output | module.test_save_int_single | fixed value |
| fixture | module.test_save_list_flat | fixed value |
| expected | module.test_save_list_flat | fixed value |
| output | module.test_save_list_flat | fixed value |
| fixture | module.test_save_set_flat | fixed value |
| first | module.test_save_set_flat | fixed value |
| second | module.test_save_set_flat | fixed value |
| output | module.test_save_set_flat | fixed value |
| actual | module.test_save_set_flat | fixed value |
| fixture | module.test_save_str_single | fixed value |
| expected | module.test_save_str_single | fixed value |
| output | module.test_save_str_single | fixed value |

## attr.py

| Variable | Scope | Role |
|---|---|---|
| ex | module | fixed value |
| method | module | fixed value |
| label | module.Example.__init__ | fixed value |
| self | module.Example.__init__ | fixed value |
| self | module.Example.get_size | fixed value |

## objects.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.LoadObjects.__init__ | fixed value |
| self | module.LoadObjects.__init__ | fixed value |
| self | module.LoadObjects.load | fixed value |
| line | module.LoadObjects.load | fixed value |
| fields | module.LoadObjects.load | fixed value |
| key | module.LoadObjects.load | fixed value |
| value | module.LoadObjects.load | fixed value |
| method | module.LoadObjects.load | fixed value |
| self | module.LoadObjects.load_bool | fixed value |
| value | module.LoadObjects.load_bool | fixed value |
| names | module.LoadObjects.load_bool | fixed value |
| self | module.LoadObjects.load_dict | fixed value |
| value | module.LoadObjects.load_dict | fixed value |
| result | module.LoadObjects.load_dict | fixed value |
| _ | module.LoadObjects.load_dict | stepper |
| k | module.LoadObjects.load_dict | most-recent holder |
| v | module.LoadObjects.load_dict | most-recent holder |
| self | module.LoadObjects.load_float | fixed value |
| value | module.LoadObjects.load_float | fixed value |
| self | module.LoadObjects.load_int | fixed value |
| value | module.LoadObjects.load_int | fixed value |
| self | module.LoadObjects.load_list | fixed value |
| value | module.LoadObjects.load_list | fixed value |
| self | module.LoadObjects.load_set | fixed value |
| value | module.LoadObjects.load_set | fixed value |
| self | module.LoadObjects.load_str | fixed value |
| value | module.LoadObjects.load_str | fixed value |
| self | module.SaveObjects.__init__ | fixed value |
| writer | module.SaveObjects.__init__ | fixed value |
| fields | module.SaveObjects._write | fixed value |
| self | module.SaveObjects._write | fixed value |
| self | module.SaveObjects.save | fixed value |
| thing | module.SaveObjects.save | fixed value |
| typename | module.SaveObjects.save | fixed value |
| method | module.SaveObjects.save | fixed value |
| self | module.SaveObjects.save_bool | fixed value |
| thing | module.SaveObjects.save_bool | fixed value |
| self | module.SaveObjects.save_dict | fixed value |
| thing | module.SaveObjects.save_dict | fixed value |
| key | module.SaveObjects.save_dict | stepper |
| value | module.SaveObjects.save_dict | stepper |
| self | module.SaveObjects.save_float | fixed value |
| thing | module.SaveObjects.save_float | fixed value |
| self | module.SaveObjects.save_int | fixed value |
| thing | module.SaveObjects.save_int | fixed value |
| self | module.SaveObjects.save_list | fixed value |
| thing | module.SaveObjects.save_list | fixed value |
| item | module.SaveObjects.save_list | stepper |
| self | module.SaveObjects.save_set | fixed value |
| thing | module.SaveObjects.save_set | fixed value |
| item | module.SaveObjects.save_set | stepper |
| self | module.SaveObjects.save_str | fixed value |
| thing | module.SaveObjects.save_str | fixed value |
| lines | module.SaveObjects.save_str | fixed value |
| line | module.SaveObjects.save_str | stepper |

## ex_aliasing.py

| Variable | Scope | Role |
|---|---|---|
| shared | module | fixed value |
| fixture | module | fixed value |

## aliasing_wrong.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.LoadAlias.__init__ | fixed value |
| self | module.LoadAlias.__init__ | fixed value |
| self | module.LoadAlias.load | fixed value |
| line | module.LoadAlias.load | fixed value |
| fields | module.LoadAlias.load | fixed value |
| ident | module.LoadAlias.load | fixed value |
| key | module.LoadAlias.load | fixed value |
| value | module.LoadAlias.load | fixed value |
| method | module.LoadAlias.load | fixed value |
| result | module.LoadAlias.load | fixed value |
| self | module.SaveAlias.__init__ | fixed value |
| writer | module.SaveAlias.__init__ | fixed value |
| self | module.SaveAlias.save | fixed value |
| thing | module.SaveAlias.save | fixed value |
| thing_id | module.SaveAlias.save | fixed value |
| typename | module.SaveAlias.save | fixed value |
| method | module.SaveAlias.save | fixed value |
| self | module.SaveAlias.save_bool | fixed value |
| thing | module.SaveAlias.save_bool | fixed value |
| self | module.SaveAlias.save_dict | fixed value |
| thing | module.SaveAlias.save_dict | fixed value |
| key | module.SaveAlias.save_dict | stepper |
| value | module.SaveAlias.save_dict | stepper |
| self | module.SaveAlias.save_float | fixed value |
| thing | module.SaveAlias.save_float | fixed value |
| self | module.SaveAlias.save_int | fixed value |
| thing | module.SaveAlias.save_int | fixed value |
| self | module.SaveAlias.save_list | fixed value |
| thing | module.SaveAlias.save_list | fixed value |
| item | module.SaveAlias.save_list | stepper |
| self | module.SaveAlias.save_set | fixed value |
| thing | module.SaveAlias.save_set | fixed value |
| item | module.SaveAlias.save_set | stepper |
| self | module.SaveAlias.save_str | fixed value |
| thing | module.SaveAlias.save_str | fixed value |
| lines | module.SaveAlias.save_str | fixed value |
| line | module.SaveAlias.save_str | stepper |

## test_aliasing_wrong.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module.roundtrip | fixed value |
| writer | module.roundtrip | fixed value |
| reader | module.roundtrip | fixed value |
| fixture | module.test_aliasing_circular | log |
| result | module.test_aliasing_circular | fixed value |
| fixture | module.test_aliasing_no_aliasing | fixed value |
| shared | module.test_aliasing_shared_child | fixed value |
| fixture | module.test_aliasing_shared_child | fixed value |
| result | module.test_aliasing_shared_child | fixed value |

## ex_circular.py

| Variable | Scope | Role |
|---|---|---|
| fixture | module | log |

## aliasing.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.LoadAlias.__init__ | fixed value |
| self | module.LoadAlias.__init__ | fixed value |
| self | module.LoadAlias.load | fixed value |
| line | module.LoadAlias.load | fixed value |
| fields | module.LoadAlias.load | fixed value |
| ident | module.LoadAlias.load | fixed value |
| key | module.LoadAlias.load | fixed value |
| value | module.LoadAlias.load | fixed value |
| method | module.LoadAlias.load | fixed value |
| ident | module.LoadAlias.load_bool | fixed value |
| self | module.LoadAlias.load_bool | fixed value |
| value | module.LoadAlias.load_bool | fixed value |
| ident | module.LoadAlias.load_dict | fixed value |
| length | module.LoadAlias.load_dict | fixed value |
| self | module.LoadAlias.load_dict | fixed value |
| result | module.LoadAlias.load_dict | fixed value |
| _ | module.LoadAlias.load_dict | stepper |
| k | module.LoadAlias.load_dict | most-recent holder |
| v | module.LoadAlias.load_dict | most-recent holder |
| ident | module.LoadAlias.load_float | fixed value |
| self | module.LoadAlias.load_float | fixed value |
| value | module.LoadAlias.load_float | fixed value |
| ident | module.LoadAlias.load_int | fixed value |
| self | module.LoadAlias.load_int | fixed value |
| value | module.LoadAlias.load_int | fixed value |
| ident | module.LoadAlias.load_list | fixed value |
| length | module.LoadAlias.load_list | fixed value |
| self | module.LoadAlias.load_list | fixed value |
| result | module.LoadAlias.load_list | log |
| _ | module.LoadAlias.load_list | stepper |
| ident | module.LoadAlias.load_set | fixed value |
| length | module.LoadAlias.load_set | fixed value |
| self | module.LoadAlias.load_set | fixed value |
| result | module.LoadAlias.load_set | container |
| _ | module.LoadAlias.load_set | stepper |
| ident | module.LoadAlias.load_str | fixed value |
| self | module.LoadAlias.load_str | fixed value |
| value | module.LoadAlias.load_str | fixed value |
| self | module.SaveAlias.__init__ | fixed value |
| writer | module.SaveAlias.__init__ | fixed value |
| self | module.SaveAlias.save | fixed value |
| thing | module.SaveAlias.save | fixed value |
| thing_id | module.SaveAlias.save | fixed value |
| typename | module.SaveAlias.save | fixed value |
| method | module.SaveAlias.save | fixed value |
| self | module.SaveAlias.save_bool | fixed value |
| thing | module.SaveAlias.save_bool | fixed value |
| self | module.SaveAlias.save_dict | fixed value |
| thing | module.SaveAlias.save_dict | fixed value |
| key | module.SaveAlias.save_dict | stepper |
| value | module.SaveAlias.save_dict | stepper |
| self | module.SaveAlias.save_float | fixed value |
| thing | module.SaveAlias.save_float | fixed value |
| self | module.SaveAlias.save_int | fixed value |
| thing | module.SaveAlias.save_int | fixed value |
| self | module.SaveAlias.save_list | fixed value |
| thing | module.SaveAlias.save_list | fixed value |
| item | module.SaveAlias.save_list | stepper |
| self | module.SaveAlias.save_set | fixed value |
| thing | module.SaveAlias.save_set | fixed value |
| item | module.SaveAlias.save_set | stepper |
| self | module.SaveAlias.save_str | fixed value |
| thing | module.SaveAlias.save_str | fixed value |
| lines | module.SaveAlias.save_str | fixed value |
| line | module.SaveAlias.save_str | stepper |

## save_aliasing.py

| Variable | Scope | Role |
|---|---|---|
| word | module | fixed value |
| child | module | fixed value |
| parent | module | log |
| saver | module | fixed value |

