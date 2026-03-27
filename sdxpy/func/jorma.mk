# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := func
PY_FILES := \
    closure.py \
    counter_fail.py \
    counter_succeed.py \
    ex_dict_zip.py \
    example_def.py \
    func.py \
    inner.py \
    oop.py

include ../examples.mk
