# binary

## binary_notation.py

### Static analysis


## calcsize.py

### Static analysis

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | format   | stepper | line 3   |

## dynamic_format.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | text     | fixed value | line 1   |

## hex_notation.py

### Static analysis


## pack_count.py

### Static analysis


## pack_unicode.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | result   | fixed value | line 3   |

## pack_unpack.py

### Static analysis

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | fmt      | fixed value | line 3   |
| module | x        | fixed value | line 4   |
| module | y        | fixed value | line 5   |
| module | binary   | fixed value | line 7   |
| module | normal   | fixed value | line 10  |

## variable_packing.py

### Static analysis

| Scope              | Variable  | Role        | Location |
| :------------------| :---------| :-----------| :--------|
| module             | result    | fixed value | line 13  |
| module.pack_string | as_string | fixed value | line 4   |
| module.pack_string | as_bytes  | fixed value | line 5   |
| module.pack_string | header    | fixed value | line 6   |
| module.pack_string | format    | fixed value | line 7   |
| module.pack_string | body      | fixed value | line 8   |

## variable_unpacking.py

### Static analysis

| Scope                | Variable | Role        | Location |
| :--------------------| :--------| :-----------| :--------|
| module               | buffer   | fixed value | line 13  |
| module               | result   | fixed value | line 14  |
| module.unpack_string | buffer   | fixed value | line 5   |
| module.unpack_string | body     | fixed value | line 6   |
| module.unpack_string | header   | fixed value | line 6   |
| module.unpack_string | length   | fixed value | line 7   |
| module.unpack_string | format   | fixed value | line 8   |
| module.unpack_string | result   | fixed value | line 9   |

