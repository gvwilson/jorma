# Variable Role Analysis: dup

## brute_force_2.py

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

| Scope             | Variable  | Role               | Location |
| :-----------------| :---------| :------------------| :--------|
| module            | example   | fixed value        | line 8   |
| module            | i         | stepper            | line 9   |
| module            | substring | most-recent holder | line 10  |
| module            | hash      | most-recent holder | line 11  |
| module.naive_hash | data      | fixed value        | line 2   |

## using_sha256.py

| Scope  | Variable  | Role               | Location |
| :------| :---------| :------------------| :--------|
| module | example   | fixed value        | line 5   |
| module | i         | stepper            | line 6   |
| module | substring | most-recent holder | line 7   |
| module | hash      | most-recent holder | line 8   |

