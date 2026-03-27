# Finding Duplicate Files

## brute_force_2.py

| Variable | Scope | Role |
|---|---|---|
| duplicates | module | fixed value |
| left | module | stepper |
| right | module | stepper |
| filenames | module.find_duplicates | fixed value |
| matches | module.find_duplicates | log |
| i_left | module.find_duplicates | stepper |
| left | module.find_duplicates | most-recent holder |
| i_right | module.find_duplicates | stepper |
| right | module.find_duplicates | most-recent holder |
| left_name | module.same_bytes | fixed value |
| right_name | module.same_bytes | fixed value |
| left_bytes | module.same_bytes | fixed value |
| right_bytes | module.same_bytes | fixed value |

## naive_hash.py

| Variable | Scope | Role |
|---|---|---|
| example | module | fixed value |
| i | module | stepper |
| substring | module | most-recent holder |
| hash | module | most-recent holder |
| data | module.naive_hash | fixed value |

## grouped.py

| Variable | Scope | Role |
|---|---|---|
| groups | module | fixed value |
| filenames | module | stepper |
| duplicates | module | most-recent holder |
| left | module | stepper |
| right | module | stepper |
| filenames | module.find_duplicates | fixed value |
| matches | module.find_duplicates | log |
| i_left | module.find_duplicates | stepper |
| left | module.find_duplicates | most-recent holder |
| i_right | module.find_duplicates | stepper |
| right | module.find_duplicates | most-recent holder |
| filenames | module.find_groups | fixed value |
| groups | module.find_groups | fixed value |
| fn | module.find_groups | stepper |
| data | module.find_groups | most-recent holder |
| hash_code | module.find_groups | most-recent holder |
| left_name | module.same_bytes | fixed value |
| right_name | module.same_bytes | fixed value |
| left_bytes | module.same_bytes | fixed value |
| right_bytes | module.same_bytes | fixed value |

## using_sha256.py

| Variable | Scope | Role |
|---|---|---|
| example | module | fixed value |
| i | module | stepper |
| substring | module | most-recent holder |
| hash | module | most-recent holder |

## dup.py

| Variable | Scope | Role |
|---|---|---|
| groups | module | fixed value |
| filenames | module | stepper |
| filenames | module.find_groups | fixed value |
| groups | module.find_groups | fixed value |
| fn | module.find_groups | stepper |
| data | module.find_groups | most-recent holder |
| hash_code | module.find_groups | most-recent holder |

