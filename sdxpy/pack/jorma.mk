# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := pack
PY_FILES := \
    exhaustive.py \
    incremental.py \
    manual.py \
    z3_complete.py \
    z3_equal.py \
    z3_part_equal.py \
    z3_setup.py \
    z3_triple.py \
    z3_unequal.py

include ../examples.mk
