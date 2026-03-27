# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := test
PY_FILES := \
    callable.py \
    ex_loop_globals_2.py \
    find_test_funcs.py \
    func_list.py \
    globals.py \
    globals_plus.py \
    locals.py \
    manual.py \
    runner.py \
    signature.py \
    type_func.py \
    type_int.py \
    type_len.py

include ../examples.mk
