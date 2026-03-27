# A Virtual Machine

## architecture.py

| Variable | Scope | Role |
|---|---|---|
| NUM_REG | module | fixed value |
| RAM_LEN | module | fixed value |
| OPS | module | fixed value |
| OP_MASK | module | fixed value |
| OP_SHIFT | module | fixed value |
| OP_WIDTH | module | fixed value |

## vm.py

| Variable | Scope | Role |
|---|---|---|
| COLUMNS | module | fixed value |
| DIGITS | module | fixed value |
| self | module.VirtualMachine.__init__ | fixed value |
| self | module.VirtualMachine.fetch | fixed value |
| instruction | module.VirtualMachine.fetch | unknown |
| op | module.VirtualMachine.fetch | fixed value |
| arg0 | module.VirtualMachine.fetch | fixed value |
| arg1 | module.VirtualMachine.fetch | fixed value |
| program | module.VirtualMachine.initialize | fixed value |
| self | module.VirtualMachine.initialize | fixed value |
| self | module.VirtualMachine.run | fixed value |
| running | module.VirtualMachine.run | one-way flag |
| arg0 | module.VirtualMachine.run | most-recent holder |
| arg1 | module.VirtualMachine.run | most-recent holder |
| op | module.VirtualMachine.run | most-recent holder |
| self | module.VirtualMachine.show | fixed value |
| writer | module.VirtualMachine.show | fixed value |
| i | module.VirtualMachine.show | stepper |
| r | module.VirtualMachine.show | stepper |
| top | module.VirtualMachine.show | fixed value |
| base | module.VirtualMachine.show | gatherer |
| output | module.VirtualMachine.show | gatherer |
| vm_cls | module.main | fixed value |
| reader | module.main | fixed value |
| writer | module.main | fixed value |
| lines | module.main | fixed value |
| program | module.main | fixed value |
| vm | module.main | fixed value |

## assembler.py

| Variable | Scope | Role |
|---|---|---|
| args | module.Assembler._combine | fixed value |
| self | module.Assembler._combine | fixed value |
| result | module.Assembler._combine | gatherer |
| a | module.Assembler._combine | stepper |
| instruction | module.Assembler._compile | fixed value |
| labels | module.Assembler._compile | fixed value |
| self | module.Assembler._compile | fixed value |
| tokens | module.Assembler._compile | fixed value |
| args | module.Assembler._compile | fixed value |
| op | module.Assembler._compile | fixed value |
| code | module.Assembler._compile | fixed value |
| fmt | module.Assembler._compile | fixed value |
| lines | module.Assembler._find_labels | fixed value |
| self | module.Assembler._find_labels | fixed value |
| result | module.Assembler._find_labels | fixed value |
| loc | module.Assembler._find_labels | stepper |
| ln | module.Assembler._find_labels | stepper |
| label | module.Assembler._find_labels | most-wanted holder |
| lines | module.Assembler._get_lines | unknown |
| self | module.Assembler._get_lines | fixed value |
| line | module.Assembler._is_comment | fixed value |
| self | module.Assembler._is_comment | fixed value |
| line | module.Assembler._is_label | fixed value |
| self | module.Assembler._is_label | fixed value |
| self | module.Assembler._reg | fixed value |
| token | module.Assembler._reg | fixed value |
| r | module.Assembler._reg | fixed value |
| program | module.Assembler._to_text | fixed value |
| self | module.Assembler._to_text | fixed value |
| labels | module.Assembler._val | fixed value |
| self | module.Assembler._val | fixed value |
| token | module.Assembler._val | fixed value |
| lbl | module.Assembler._val | fixed value |
| lines | module.Assembler.assemble | unknown |
| self | module.Assembler.assemble | fixed value |
| labels | module.Assembler.assemble | fixed value |
| instructions | module.Assembler.assemble | fixed value |
| compiled | module.Assembler.assemble | fixed value |
| program | module.Assembler.assemble | fixed value |
| assembler_cls | module.main | fixed value |
| reader | module.main | fixed value |
| writer | module.main | fixed value |
| lines | module.main | fixed value |
| assembler | module.main | fixed value |
| program | module.main | fixed value |
| instruction | module.main | stepper |

## arrays.py

| Variable | Scope | Role |
|---|---|---|
| DIVIDER | module.DataAllocator | fixed value |
| base_of_data | module.DataAllocator._add_allocations | gatherer |
| labels | module.DataAllocator._add_allocations | fixed value |
| self | module.DataAllocator._add_allocations | fixed value |
| to_allocate | module.DataAllocator._add_allocations | fixed value |
| alloc | module.DataAllocator._add_allocations | stepper |
| fields | module.DataAllocator._add_allocations | most-recent holder |
| lbl | module.DataAllocator._add_allocations | most-recent holder |
| num_words_text | module.DataAllocator._add_allocations | most-recent holder |
| num_words | module.DataAllocator._add_allocations | most-recent holder |
| lines | module.DataAllocator._split | fixed value |
| self | module.DataAllocator._split | fixed value |
| split | module.DataAllocator._split | fixed value |
| lines | module.DataAllocator.assemble | unknown |
| self | module.DataAllocator.assemble | fixed value |
| to_allocate | module.DataAllocator.assemble | fixed value |
| to_compile | module.DataAllocator.assemble | fixed value |
| labels | module.DataAllocator.assemble | fixed value |
| instructions | module.DataAllocator.assemble | fixed value |
| base_of_data | module.DataAllocator.assemble | fixed value |
| compiled | module.DataAllocator.assemble | fixed value |
| program | module.DataAllocator.assemble | fixed value |

