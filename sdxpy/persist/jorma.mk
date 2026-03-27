# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := persist
PY_FILES := \
    aliasing.py \
    aliasing_wrong.py \
    attr.py \
    builtin.py \
    ex_aliasing.py \
    ex_circular.py \
    objects.py \
    save_aliasing.py \
    save_builtin.py \
    test_aliasing_wrong.py \
    test_builtin.py

include ../examples.mk
