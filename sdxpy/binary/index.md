# Variable Role Analysis: binary

## binary_notation.py

Warning: no variables found.

## bit_mask.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | mask     | fixed value | line 1   |
| module | val      | unknown     | line 2   |

## calcsize.py

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | format   | stepper | line 3   |

## ex_dynamic_format.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | format   | fixed value | line 1   |

## pack_count.py

Warning: no variables found.

## pack_unpack.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | fmt      | fixed value | line 3   |
| module | x        | fixed value | line 4   |
| module | y        | fixed value | line 5   |
| module | binary   | fixed value | line 7   |
| module | normal   | fixed value | line 10  |

## variable_packing.py

| Scope              | Variable  | Role        | Location |
| :------------------| :---------| :-----------| :--------|
| module             | result    | fixed value | line 14  |
| module.pack_string | as_string | fixed value | line 4   |
| module.pack_string | as_bytes  | fixed value | line 5   |
| module.pack_string | header    | fixed value | line 6   |
| module.pack_string | format    | fixed value | line 7   |
| module.pack_string | body      | fixed value | line 8   |

## variable_unpacking.py

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

