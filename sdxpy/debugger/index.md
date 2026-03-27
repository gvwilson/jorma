# A Debugger

## vm_base.py

| Variable | Scope | Role |
|---|---|---|
| COLUMNS | module | fixed value |
| DIGITS | module | fixed value |
| self | module.VirtualMachineBase.__init__ | fixed value |
| writer | module.VirtualMachineBase.__init__ | fixed value |
| addr | module.VirtualMachineBase.assert_is_address | fixed value |
| self | module.VirtualMachineBase.assert_is_address | fixed value |
| reg | module.VirtualMachineBase.assert_is_register | fixed value |
| self | module.VirtualMachineBase.assert_is_register | fixed value |
| instruction | module.VirtualMachineBase.decode | unknown |
| self | module.VirtualMachineBase.decode | fixed value |
| op | module.VirtualMachineBase.decode | fixed value |
| arg0 | module.VirtualMachineBase.decode | fixed value |
| arg1 | module.VirtualMachineBase.decode | fixed value |
| arg0 | module.VirtualMachineBase.execute | fixed value |
| arg1 | module.VirtualMachineBase.execute | fixed value |
| op | module.VirtualMachineBase.execute | fixed value |
| self | module.VirtualMachineBase.execute | fixed value |
| self | module.VirtualMachineBase.fetch | fixed value |
| old_ip | module.VirtualMachineBase.fetch | fixed value |
| instruction | module.VirtualMachineBase.fetch | fixed value |
| program | module.VirtualMachineBase.initialize | fixed value |
| self | module.VirtualMachineBase.initialize | fixed value |
| cls | module.VirtualMachineBase.main | fixed value |
| reader | module.VirtualMachineBase.main | fixed value |
| lines | module.VirtualMachineBase.main | fixed value |
| program | module.VirtualMachineBase.main | fixed value |
| vm | module.VirtualMachineBase.main | fixed value |
| self | module.VirtualMachineBase.run | fixed value |
| addr | module.VirtualMachineBase.run | most-recent holder |
| arg0 | module.VirtualMachineBase.run | most-recent holder |
| arg1 | module.VirtualMachineBase.run | most-recent holder |
| op | module.VirtualMachineBase.run | most-recent holder |
| self | module.VirtualMachineBase.show | fixed value |
| i | module.VirtualMachineBase.show | stepper |
| r | module.VirtualMachineBase.show | stepper |
| top | module.VirtualMachineBase.show | fixed value |
| base | module.VirtualMachineBase.show | gatherer |
| output | module.VirtualMachineBase.show | gatherer |
| args | module.VirtualMachineBase.write | fixed value |
| self | module.VirtualMachineBase.write | fixed value |
| msg | module.VirtualMachineBase.write | fixed value |

## architecture.py

| Variable | Scope | Role |
|---|---|---|
| OPS | module | fixed value |
| OP_MASK | module | fixed value |
| OP_SHIFT | module | fixed value |
| OP_WIDTH | module | fixed value |
| NUM_REG | module | fixed value |
| RAM_LEN | module | fixed value |
| FINISHED | module.VMState | fixed value |
| STEPPING | module.VMState | fixed value |
| RUNNING | module.VMState | fixed value |

## vm_step.py

| Variable | Scope | Role |
|---|---|---|
| OPS_LOOKUP | module | fixed value |
| reader | module.VirtualMachineStep.__init__ | fixed value |
| self | module.VirtualMachineStep.__init__ | fixed value |
| writer | module.VirtualMachineStep.__init__ | fixed value |
| addr | module.VirtualMachineStep.disassemble | fixed value |
| instruction | module.VirtualMachineStep.disassemble | fixed value |
| self | module.VirtualMachineStep.disassemble | fixed value |
| arg0 | module.VirtualMachineStep.disassemble | fixed value |
| arg1 | module.VirtualMachineStep.disassemble | fixed value |
| op | module.VirtualMachineStep.disassemble | fixed value |
| addr | module.VirtualMachineStep.interact | fixed value |
| self | module.VirtualMachineStep.interact | fixed value |
| command | module.VirtualMachineStep.interact | most-recent holder |
| prompt | module.VirtualMachineStep.read | fixed value |
| self | module.VirtualMachineStep.read | fixed value |
| self | module.VirtualMachineStep.run | fixed value |
| instruction | module.VirtualMachineStep.run | most-recent holder |
| arg0 | module.VirtualMachineStep.run | most-recent holder |
| arg1 | module.VirtualMachineStep.run | most-recent holder |
| op | module.VirtualMachineStep.run | most-recent holder |

## test_vm.py

| Variable | Scope | Role |
|---|---|---|
| prompt | module.Reader.__call__ | fixed value |
| self | module.Reader.__call__ | fixed value |
| args | module.Reader.__init__ | fixed value |
| self | module.Reader.__init__ | fixed value |
| self | module.Writer.__init__ | fixed value |
| args | module.Writer.write | fixed value |
| self | module.Writer.write | fixed value |
| reader | module.execute | fixed value |
| source | module.execute | fixed value |
| writer | module.execute | fixed value |
| program | module.execute | fixed value |
| vm | module.execute | fixed value |
| source | module.test_disassemble | fixed value |
| reader | module.test_disassemble | fixed value |
| writer | module.test_disassemble | fixed value |
| source | module.test_print_two_values | fixed value |
| reader | module.test_print_two_values | fixed value |
| writer | module.test_print_two_values | fixed value |
| source | module.test_show_memory | fixed value |
| reader | module.test_show_memory | fixed value |
| writer | module.test_show_memory | fixed value |

## vm_extend.py

| Variable | Scope | Role |
|---|---|---|
| reader | module.VirtualMachineExtend.__init__ | fixed value |
| self | module.VirtualMachineExtend.__init__ | fixed value |
| writer | module.VirtualMachineExtend.__init__ | fixed value |
| addr | module.VirtualMachineExtend._do_disassemble | fixed value |
| self | module.VirtualMachineExtend._do_disassemble | fixed value |
| addr | module.VirtualMachineExtend._do_ip | fixed value |
| self | module.VirtualMachineExtend._do_ip | fixed value |
| addr | module.VirtualMachineExtend._do_memory | fixed value |
| self | module.VirtualMachineExtend._do_memory | fixed value |
| addr | module.VirtualMachineExtend._do_quit | fixed value |
| self | module.VirtualMachineExtend._do_quit | fixed value |
| addr | module.VirtualMachineExtend._do_run | fixed value |
| self | module.VirtualMachineExtend._do_run | fixed value |
| addr | module.VirtualMachineExtend._do_step | fixed value |
| self | module.VirtualMachineExtend._do_step | fixed value |
| addr | module.VirtualMachineExtend.interact | fixed value |
| self | module.VirtualMachineExtend.interact | fixed value |
| prompt | module.VirtualMachineExtend.interact | fixed value |
| interacting | module.VirtualMachineExtend.interact | one-way flag |
| command | module.VirtualMachineExtend.interact | most-recent holder |

## vm_break.py

| Variable | Scope | Role |
|---|---|---|
| self | module.VirtualMachineBreak.__init__ | fixed value |
| addr | module.VirtualMachineBreak._do_add_breakpoint | fixed value |
| self | module.VirtualMachineBreak._do_add_breakpoint | fixed value |
| addr | module.VirtualMachineBreak._do_clear_breakpoint | fixed value |
| self | module.VirtualMachineBreak._do_clear_breakpoint | fixed value |
| self | module.VirtualMachineBreak.run | fixed value |
| instruction | module.VirtualMachineBreak.run | most-recent holder |
| arg0 | module.VirtualMachineBreak.run | most-recent holder |
| arg1 | module.VirtualMachineBreak.run | most-recent holder |
| op | module.VirtualMachineBreak.run | most-recent holder |
| original | module.VirtualMachineBreak.run | most-wanted holder |
| self | module.VirtualMachineBreak.show | fixed value |
| instruction | module.VirtualMachineBreak.show | stepper |
| key | module.VirtualMachineBreak.show | stepper |

