# Variable Role Analysis: binary

## binary_notation.py

Warning: no variables found.
### Static analysis

45

## bit_mask.py

Error during dynamic analysis (NameError): name 'val' is not defined
### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | mask     | fixed value | line 1   |
| module | val      | unknown     | line 2   |

## calcsize.py

### Static analysis

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | format   | stepper | line 3   |
format '4s' needs 4 bytes
format '3i4s5d' needs 56 bytes

## ex_dynamic_format.py

Error during dynamic analysis (TypeError): object of type 'type' has no len()
### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | format   | fixed value | line 1   |

## pack_count.py

Warning: no variables found.
### Static analysis

b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
b'hello'
b'a lon'

### Dynamic analysis

| Variable | Scope                                                                                  | Role  |
| :--------| :--------------------------------------------------------------------------------------| :-----|
| fullname | module._find_and_load._find_and_load_unlocked._find_spec.find_spec                     | phase |
| suffix   | module._find_and_load._find_and_load_unlocked._find_spec.find_spec._get_spec.find_spec | phase |

## pack_unpack.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | fmt      | fixed value | line 3   |
| module | x        | fixed value | line 4   |
| module | y        | fixed value | line 5   |
| module | binary   | fixed value | line 7   |
| module | normal   | fixed value | line 10  |
binary representation: b'\x1f\x00\x00\x00A\x00\x00\x00'
back to normal: (31, 65)

## variable_packing.py

### Static analysis

| Scope              | Variable  | Role        | Location |
| :------------------| :---------| :-----------| :--------|
| module             | result    | fixed value | line 14  |
| module.pack_string | as_string | fixed value | line 4   |
| module.pack_string | as_bytes  | fixed value | line 5   |
| module.pack_string | header    | fixed value | line 6   |
| module.pack_string | format    | fixed value | line 7   |
| module.pack_string | body      | fixed value | line 8   |
b'\x06\x00\x00\x00hello!'

## variable_unpacking.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'variable_packing'
### Static analysis

| Scope                | Variable | Role        | Location |
| :--------------------| :--------| :-----------| :--------|
| module               | buffer   | fixed value | line 12  |
| module               | result   | fixed value | line 13  |
| module.unpack_string | buffer   | fixed value | line 5   |
| module.unpack_string | body     | fixed value | line 6   |
| module.unpack_string | header   | fixed value | line 6   |
| module.unpack_string | length   | fixed value | line 7   |
| module.unpack_string | format   | fixed value | line 8   |
| module.unpack_string | result   | fixed value | line 9   |

