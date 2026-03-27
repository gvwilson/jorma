# dup

## brute_force_1.py

### Static analysis

| Scope                  | Variable    | Role        | Location |
| :----------------------| :-----------| :-----------| :--------|
| module                 | duplicates  | fixed value | line 20  |
| module                 | left        | stepper     | line 21  |
| module                 | right       | stepper     | line 21  |
| module.find_duplicates | filenames   | fixed value | line 10  |
| module.find_duplicates | matches     | log         | line 11  |
| module.find_duplicates | left        | stepper     | line 12  |
| module.find_duplicates | right       | stepper     | line 13  |
| module.same_bytes      | left_name   | fixed value | line 4   |
| module.same_bytes      | right_name  | fixed value | line 4   |
| module.same_bytes      | left_bytes  | fixed value | line 5   |
| module.same_bytes      | right_bytes | fixed value | line 6   |

### Dynamic analysis

| Variable | Scope                  | Role     |
| :--------| :----------------------| :--------|
| matches  | module.find_duplicates | snapshot |

## brute_force_2.py

### Static analysis

| Scope                  | Variable    | Role               | Location |
| :----------------------| :-----------| :------------------| :--------|
| module                 | duplicates  | fixed value        | line 22  |
| module                 | left        | stepper            | line 23  |
| module                 | right       | stepper            | line 23  |
| module.find_duplicates | filenames   | fixed value        | line 10  |
| module.find_duplicates | matches     | log                | line 11  |
| module.find_duplicates | i_left      | stepper            | line 12  |
| module.find_duplicates | left        | most-recent holder | line 13  |
| module.find_duplicates | i_right     | stepper            | line 14  |
| module.find_duplicates | right       | most-recent holder | line 15  |
| module.same_bytes      | left_name   | fixed value        | line 4   |
| module.same_bytes      | right_name  | fixed value        | line 4   |
| module.same_bytes      | left_bytes  | fixed value        | line 5   |
| module.same_bytes      | right_bytes | fixed value        | line 6   |

### Dynamic analysis

| Variable | Scope                  | Role     |
| :--------| :----------------------| :--------|
| matches  | module.find_duplicates | snapshot |

## dup.py

### Static analysis

| Scope              | Variable  | Role               | Location |
| :------------------| :---------| :------------------| :--------|
| module             | groups    | fixed value        | line 17  |
| module             | filenames | stepper            | line 18  |
| module.find_groups | filenames | fixed value        | line 5   |
| module.find_groups | groups    | fixed value        | line 6   |
| module.find_groups | fn        | stepper            | line 7   |
| module.find_groups | data      | most-recent holder | line 8   |
| module.find_groups | hash_code | most-recent holder | line 9   |

## grouped.py

### Static analysis

| Scope                  | Variable    | Role               | Location |
| :----------------------| :-----------| :------------------| :--------|
| module                 | groups      | fixed value        | line 34  |
| module                 | filenames   | stepper            | line 35  |
| module                 | duplicates  | most-recent holder | line 36  |
| module                 | left        | stepper            | line 37  |
| module                 | right       | stepper            | line 37  |
| module.find_duplicates | filenames   | fixed value        | line 11  |
| module.find_duplicates | matches     | log                | line 12  |
| module.find_duplicates | i_left      | stepper            | line 13  |
| module.find_duplicates | left        | most-recent holder | line 14  |
| module.find_duplicates | i_right     | stepper            | line 15  |
| module.find_duplicates | right       | most-recent holder | line 16  |
| module.find_groups     | filenames   | fixed value        | line 22  |
| module.find_groups     | groups      | fixed value        | line 23  |
| module.find_groups     | fn          | stepper            | line 24  |
| module.find_groups     | data        | most-recent holder | line 25  |
| module.find_groups     | hash_code   | most-recent holder | line 26  |
| module.same_bytes      | left_name   | fixed value        | line 5   |
| module.same_bytes      | right_name  | fixed value        | line 5   |
| module.same_bytes      | left_bytes  | fixed value        | line 6   |
| module.same_bytes      | right_bytes | fixed value        | line 7   |

## naive_hash.py

### Static analysis

| Scope             | Variable  | Role               | Location |
| :-----------------| :---------| :------------------| :--------|
| module            | example   | fixed value        | line 6   |
| module            | i         | stepper            | line 7   |
| module            | substring | most-recent holder | line 8   |
| module            | hash      | most-recent holder | line 9   |
| module.naive_hash | data      | fixed value        | line 1   |

## using_sha256.py

### Static analysis

| Scope  | Variable  | Role               | Location |
| :------| :---------| :------------------| :--------|
| module | example   | fixed value        | line 4   |
| module | i         | stepper            | line 5   |
| module | substring | most-recent holder | line 6   |
| module | hash      | most-recent holder | line 7   |

