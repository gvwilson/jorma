# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := interp
PY_FILES := \
    add_example.py \
    ex_assign_expr.py \
    expr.py \
    vars.py \
    vars_reflect.py \
    vars_table.py

include ../examples.mk
