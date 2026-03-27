# Variable Role Analysis: dup

## brute_force_2.py

### Static analysis

| Scope                  | Variable    | Role               | Location |
| :----------------------| :-----------| :------------------| :--------|
| module                 | duplicates  | fixed value        | line 24  |
| module                 | left        | stepper            | line 25  |
| module                 | right       | stepper            | line 25  |
| module.find_duplicates | filenames   | fixed value        | line 11  |
| module.find_duplicates | matches     | log                | line 12  |
| module.find_duplicates | i_left      | stepper            | line 13  |
| module.find_duplicates | left        | most-recent holder | line 14  |
| module.find_duplicates | i_right     | stepper            | line 15  |
| module.find_duplicates | right       | most-recent holder | line 16  |
| module.same_bytes      | left_name   | fixed value        | line 4   |
| module.same_bytes      | right_name  | fixed value        | line 4   |
| module.same_bytes      | left_bytes  | fixed value        | line 5   |
| module.same_bytes      | right_bytes | fixed value        | line 6   |

## dup.py

### Static analysis

| Scope              | Variable  | Role               | Location |
| :------------------| :---------| :------------------| :--------|
| module             | groups    | fixed value        | line 16  |
| module             | filenames | stepper            | line 17  |
| module.find_groups | filenames | fixed value        | line 4   |
| module.find_groups | groups    | fixed value        | line 5   |
| module.find_groups | fn        | stepper            | line 6   |
| module.find_groups | data      | most-recent holder | line 7   |
| module.find_groups | hash_code | most-recent holder | line 8   |

## grouped.py

Error during dynamic analysis (ModuleNotFoundError): No module named 'naive_hash'
### Static analysis

| Scope                  | Variable    | Role               | Location |
| :----------------------| :-----------| :------------------| :--------|
| module                 | groups      | fixed value        | line 37  |
| module                 | filenames   | stepper            | line 38  |
| module                 | duplicates  | most-recent holder | line 39  |
| module                 | left        | stepper            | line 40  |
| module                 | right       | stepper            | line 40  |
| module.find_duplicates | filenames   | fixed value        | line 11  |
| module.find_duplicates | matches     | log                | line 12  |
| module.find_duplicates | i_left      | stepper            | line 13  |
| module.find_duplicates | left        | most-recent holder | line 14  |
| module.find_duplicates | i_right     | stepper            | line 15  |
| module.find_duplicates | right       | most-recent holder | line 16  |
| module.find_groups     | filenames   | fixed value        | line 23  |
| module.find_groups     | groups      | fixed value        | line 24  |
| module.find_groups     | fn          | stepper            | line 25  |
| module.find_groups     | data        | most-recent holder | line 26  |
| module.find_groups     | hash_code   | most-recent holder | line 27  |
| module.same_bytes      | left_name   | fixed value        | line 5   |
| module.same_bytes      | right_name  | fixed value        | line 5   |
| module.same_bytes      | left_bytes  | fixed value        | line 6   |
| module.same_bytes      | right_bytes | fixed value        | line 7   |

## naive_hash.py

### Static analysis

| Scope             | Variable  | Role               | Location |
| :-----------------| :---------| :------------------| :--------|
| module            | example   | fixed value        | line 8   |
| module            | i         | stepper            | line 9   |
| module            | substring | most-recent holder | line 10  |
| module            | hash      | most-recent holder | line 11  |
| module.naive_hash | data      | fixed value        | line 2   |
 0 b'h'
 6 b'ha'
 4 b'has'
 4 b'hash'
 5 b'hashi'
11 b'hashin'
10 b'hashing'

## using_sha256.py

### Static analysis

| Scope  | Variable  | Role               | Location |
| :------| :---------| :------------------| :--------|
| module | example   | fixed value        | line 5   |
| module | i         | stepper            | line 6   |
| module | substring | most-recent holder | line 7   |
| module | hash      | most-recent holder | line 8   |
b'h'
aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123
b'ha'
8693873cd8f8a2d9c7c596477180f851e525f4eaf55a4f637b445cb442a5e340
b'has'
9150c74c5f92d51a92857f4b9678105ba5a676d308339a353b20bd38cd669ce7
b'hash'
d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa

