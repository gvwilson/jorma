# Variable Role Analysis: vm

## architecture.py

```

[module]
  NUM_REG                  fixed value             (line 1)
  RAM_LEN                  fixed value             (line 2)
  OPS                      fixed value             (line 4)
  OP_MASK                  fixed value             (line 18)
  OP_SHIFT                 fixed value             (line 19)
  OP_WIDTH                 fixed value             (line 20)
```

## arrays.py

```

[module.DataAllocator]
  DIVIDER                  fixed value             (line 7)

[module.DataAllocator._add_allocations]
  base_of_data             gatherer                (line 32)
  labels                   fixed value             (line 32)
  self                     fixed value             (line 32)
  to_allocate              fixed value             (line 32)
  alloc                    stepper                 (line 33)
  fields                   most-recent holder      (line 34)
  lbl                      most-recent holder      (line 36)
  num_words_text           most-recent holder      (line 36)
  num_words                most-recent holder      (line 38)

[module.DataAllocator._split]
  lines                    fixed value             (line 23)
  self                     fixed value             (line 23)
  split                    fixed value             (line 25)

[module.DataAllocator.assemble]
  lines                    unknown                 (line 9)
  self                     fixed value             (line 9)
  to_allocate              fixed value             (line 11)
  to_compile               fixed value             (line 11)
  labels                   fixed value             (line 13)
  instructions             fixed value             (line 14)
  base_of_data             fixed value             (line 16)
  compiled                 fixed value             (line 19)
  program                  fixed value             (line 20)
```

## assembler.py

```

[module.Assembler._combine]
  args                     fixed value             (line 70)
  self                     fixed value             (line 70)
  result                   gatherer                (line 72)
  a                        stepper                 (line 73)

[module.Assembler._compile]
  instruction              fixed value             (line 37)
  labels                   fixed value             (line 37)
  self                     fixed value             (line 37)
  tokens                   fixed value             (line 38)
  args                     fixed value             (line 39)
  op                       fixed value             (line 39)
  code                     fixed value             (line 40)
  fmt                      fixed value             (line 40)

[module.Assembler._find_labels]
  lines                    fixed value             (line 20)
  self                     fixed value             (line 20)
  result                   fixed value             (line 21)
  loc                      stepper                 (line 22)
  ln                       stepper                 (line 23)
  label                    most-wanted holder      (line 25)

[module.Assembler._get_lines]
  lines                    unknown                 (line 82)
  self                     fixed value             (line 82)

[module.Assembler._is_comment]
  line                     fixed value             (line 88)
  self                     fixed value             (line 88)

[module.Assembler._is_label]
  line                     fixed value             (line 32)
  self                     fixed value             (line 32)

[module.Assembler._reg]
  self                     fixed value             (line 91)
  token                    fixed value             (line 91)
  r                        fixed value             (line 93)

[module.Assembler._to_text]
  program                  fixed value             (line 79)
  self                     fixed value             (line 79)

[module.Assembler._val]
  labels                   fixed value             (line 61)
  self                     fixed value             (line 61)
  token                    fixed value             (line 61)
  lbl                      fixed value             (line 64)

[module.Assembler.assemble]
  lines                    unknown                 (line 6)
  self                     fixed value             (line 6)
  labels                   fixed value             (line 8)
  instructions             fixed value             (line 9)
  compiled                 fixed value             (line 12)
  program                  fixed value             (line 15)

[module.main]
  assembler_cls            fixed value             (line 97)
  reader                   fixed value             (line 99)
  writer                   fixed value             (line 100)
  lines                    fixed value             (line 101)
  assembler                fixed value             (line 102)
  program                  fixed value             (line 103)
  instruction              stepper                 (line 104)
```

## vm.py

```

[module]
  COLUMNS                  fixed value             (line 4)
  DIGITS                   fixed value             (line 5)

[module.VirtualMachine.__init__]
  self                     fixed value             (line 10)

[module.VirtualMachine.fetch]
  self                     fixed value             (line 25)
  instruction              unknown                 (line 26)
  op                       fixed value             (line 28)
  arg0                     fixed value             (line 30)
  arg1                     fixed value             (line 32)

[module.VirtualMachine.initialize]
  program                  fixed value             (line 14)
  self                     fixed value             (line 14)

[module.VirtualMachine.run]
  self                     fixed value             (line 54)
  running                  one-way flag            (line 55)
  arg0                     most-recent holder      (line 57)
  arg1                     most-recent holder      (line 57)
  op                       most-recent holder      (line 57)

[module.VirtualMachine.show]
  self                     fixed value             (line 36)
  writer                   fixed value             (line 36)
  i                        stepper                 (line 38)
  r                        stepper                 (line 38)
  top                      fixed value             (line 42)
  base                     gatherer                (line 45)
  output                   gatherer                (line 47)

[module.main]
  vm_cls                   fixed value             (line 95)
  reader                   fixed value             (line 97)
  writer                   fixed value             (line 98)
  lines                    fixed value             (line 100)
  program                  fixed value             (line 101)
  vm                       fixed value             (line 102)
```

## Programs Not Analyzed

The following programs are referenced in the lesson Makefile
but are not present in this directory:

- count_up.py
- fill_array.py
- halt.py
- print_r1.py

