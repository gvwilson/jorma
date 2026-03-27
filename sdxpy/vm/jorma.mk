# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := vm
PY_FILES := \
    architecture.py \
    arrays.py \
    assembler.py \
    vm.py

include ../examples.mk
