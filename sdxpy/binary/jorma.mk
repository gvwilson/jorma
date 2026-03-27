# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := binary
PY_FILES := \
    binary_notation.py \
    bit_mask.py \
    calcsize.py \
    ex_dynamic_format.py \
    pack_count.py \
    pack_unpack.py \
    variable_packing.py \
    variable_unpacking.py

include ../examples.mk
