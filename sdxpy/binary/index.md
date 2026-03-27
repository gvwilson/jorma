# Variable Role Analysis: binary

## binary_notation.py

```
Warning: no variables found.
```

## bit_mask.py

```

[module]
  mask                     fixed value             (line 1)
  val                      unknown                 (line 2)
```

## calcsize.py

```

[module]
  format                   stepper                 (line 3)
```

## ex_dynamic_format.py

```

[module]
  format                   fixed value             (line 1)
```

## pack_count.py

```
Warning: no variables found.
```

## pack_unpack.py

```

[module]
  fmt                      fixed value             (line 3)
  x                        fixed value             (line 4)
  y                        fixed value             (line 5)
  binary                   fixed value             (line 7)
  normal                   fixed value             (line 10)
```

## variable_packing.py

```

[module]
  result                   fixed value             (line 14)

[module.pack_string]
  as_string                fixed value             (line 4)
  as_bytes                 fixed value             (line 5)
  header                   fixed value             (line 6)
  format                   fixed value             (line 7)
  body                     fixed value             (line 8)
```

## variable_unpacking.py

```

[module]
  buffer                   fixed value             (line 12)
  result                   fixed value             (line 13)

[module.unpack_string]
  buffer                   fixed value             (line 5)
  body                     fixed value             (line 6)
  header                   fixed value             (line 6)
  length                   fixed value             (line 7)
  format                   fixed value             (line 8)
  result                   fixed value             (line 9)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- dynamic_format.py
- hex_notation.py
- pack_unicode.py

