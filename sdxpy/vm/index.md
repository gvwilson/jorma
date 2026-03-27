# Variable Role Analysis: vm

## architecture.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | NUM_REG  | fixed value | line 1   |
| module | RAM_LEN  | fixed value | line 2   |
| module | OPS      | fixed value | line 4   |
| module | OP_MASK  | fixed value | line 18  |
| module | OP_SHIFT | fixed value | line 19  |
| module | OP_WIDTH | fixed value | line 20  |

## arrays.py

| Scope                                 | Variable       | Role               | Location |
| :-------------------------------------| :--------------| :------------------| :--------|
| module.DataAllocator                  | DIVIDER        | fixed value        | line 7   |
| module.DataAllocator._add_allocations | base_of_data   | gatherer           | line 32  |
| module.DataAllocator._add_allocations | labels         | fixed value        | line 32  |
| module.DataAllocator._add_allocations | self           | fixed value        | line 32  |
| module.DataAllocator._add_allocations | to_allocate    | fixed value        | line 32  |
| module.DataAllocator._add_allocations | alloc          | stepper            | line 33  |
| module.DataAllocator._add_allocations | fields         | most-recent holder | line 34  |
| module.DataAllocator._add_allocations | lbl            | most-recent holder | line 36  |
| module.DataAllocator._add_allocations | num_words_text | most-recent holder | line 36  |
| module.DataAllocator._add_allocations | num_words      | most-recent holder | line 38  |
| module.DataAllocator._split           | lines          | fixed value        | line 23  |
| module.DataAllocator._split           | self           | fixed value        | line 23  |
| module.DataAllocator._split           | split          | fixed value        | line 25  |
| module.DataAllocator.assemble         | lines          | unknown            | line 9   |
| module.DataAllocator.assemble         | self           | fixed value        | line 9   |
| module.DataAllocator.assemble         | to_allocate    | fixed value        | line 11  |
| module.DataAllocator.assemble         | to_compile     | fixed value        | line 11  |
| module.DataAllocator.assemble         | labels         | fixed value        | line 13  |
| module.DataAllocator.assemble         | instructions   | fixed value        | line 14  |
| module.DataAllocator.assemble         | base_of_data   | fixed value        | line 16  |
| module.DataAllocator.assemble         | compiled       | fixed value        | line 19  |
| module.DataAllocator.assemble         | program        | fixed value        | line 20  |

## assembler.py

| Scope                         | Variable      | Role               | Location |
| :-----------------------------| :-------------| :------------------| :--------|
| module.Assembler._combine     | args          | fixed value        | line 70  |
| module.Assembler._combine     | self          | fixed value        | line 70  |
| module.Assembler._combine     | result        | gatherer           | line 72  |
| module.Assembler._combine     | a             | stepper            | line 73  |
| module.Assembler._compile     | instruction   | fixed value        | line 37  |
| module.Assembler._compile     | labels        | fixed value        | line 37  |
| module.Assembler._compile     | self          | fixed value        | line 37  |
| module.Assembler._compile     | tokens        | fixed value        | line 38  |
| module.Assembler._compile     | args          | fixed value        | line 39  |
| module.Assembler._compile     | op            | fixed value        | line 39  |
| module.Assembler._compile     | code          | fixed value        | line 40  |
| module.Assembler._compile     | fmt           | fixed value        | line 40  |
| module.Assembler._find_labels | lines         | fixed value        | line 20  |
| module.Assembler._find_labels | self          | fixed value        | line 20  |
| module.Assembler._find_labels | result        | fixed value        | line 21  |
| module.Assembler._find_labels | loc           | stepper            | line 22  |
| module.Assembler._find_labels | ln            | stepper            | line 23  |
| module.Assembler._find_labels | label         | most-wanted holder | line 25  |
| module.Assembler._get_lines   | lines         | unknown            | line 82  |
| module.Assembler._get_lines   | self          | fixed value        | line 82  |
| module.Assembler._is_comment  | line          | fixed value        | line 88  |
| module.Assembler._is_comment  | self          | fixed value        | line 88  |
| module.Assembler._is_label    | line          | fixed value        | line 32  |
| module.Assembler._is_label    | self          | fixed value        | line 32  |
| module.Assembler._reg         | self          | fixed value        | line 91  |
| module.Assembler._reg         | token         | fixed value        | line 91  |
| module.Assembler._reg         | r             | fixed value        | line 93  |
| module.Assembler._to_text     | program       | fixed value        | line 79  |
| module.Assembler._to_text     | self          | fixed value        | line 79  |
| module.Assembler._val         | labels        | fixed value        | line 61  |
| module.Assembler._val         | self          | fixed value        | line 61  |
| module.Assembler._val         | token         | fixed value        | line 61  |
| module.Assembler._val         | lbl           | fixed value        | line 64  |
| module.Assembler.assemble     | lines         | unknown            | line 6   |
| module.Assembler.assemble     | self          | fixed value        | line 6   |
| module.Assembler.assemble     | labels        | fixed value        | line 8   |
| module.Assembler.assemble     | instructions  | fixed value        | line 9   |
| module.Assembler.assemble     | compiled      | fixed value        | line 12  |
| module.Assembler.assemble     | program       | fixed value        | line 15  |
| module.main                   | assembler_cls | fixed value        | line 97  |
| module.main                   | reader        | fixed value        | line 99  |
| module.main                   | writer        | fixed value        | line 100 |
| module.main                   | lines         | fixed value        | line 101 |
| module.main                   | assembler     | fixed value        | line 102 |
| module.main                   | program       | fixed value        | line 103 |
| module.main                   | instruction   | stepper            | line 104 |

## vm.py

| Scope                            | Variable    | Role               | Location |
| :--------------------------------| :-----------| :------------------| :--------|
| module                           | COLUMNS     | fixed value        | line 4   |
| module                           | DIGITS      | fixed value        | line 5   |
| module.VirtualMachine.__init__   | self        | fixed value        | line 10  |
| module.VirtualMachine.fetch      | self        | fixed value        | line 25  |
| module.VirtualMachine.fetch      | instruction | unknown            | line 26  |
| module.VirtualMachine.fetch      | op          | fixed value        | line 28  |
| module.VirtualMachine.fetch      | arg0        | fixed value        | line 30  |
| module.VirtualMachine.fetch      | arg1        | fixed value        | line 32  |
| module.VirtualMachine.initialize | program     | fixed value        | line 14  |
| module.VirtualMachine.initialize | self        | fixed value        | line 14  |
| module.VirtualMachine.run        | self        | fixed value        | line 54  |
| module.VirtualMachine.run        | running     | one-way flag       | line 55  |
| module.VirtualMachine.run        | arg0        | most-recent holder | line 57  |
| module.VirtualMachine.run        | arg1        | most-recent holder | line 57  |
| module.VirtualMachine.run        | op          | most-recent holder | line 57  |
| module.VirtualMachine.show       | self        | fixed value        | line 36  |
| module.VirtualMachine.show       | writer      | fixed value        | line 36  |
| module.VirtualMachine.show       | i           | stepper            | line 38  |
| module.VirtualMachine.show       | r           | stepper            | line 38  |
| module.VirtualMachine.show       | top         | fixed value        | line 42  |
| module.VirtualMachine.show       | base        | gatherer           | line 45  |
| module.VirtualMachine.show       | output      | gatherer           | line 47  |
| module.main                      | vm_cls      | fixed value        | line 95  |
| module.main                      | reader      | fixed value        | line 97  |
| module.main                      | writer      | fixed value        | line 98  |
| module.main                      | lines       | fixed value        | line 100 |
| module.main                      | program     | fixed value        | line 101 |
| module.main                      | vm          | fixed value        | line 102 |

