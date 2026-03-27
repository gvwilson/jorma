# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := glob
PY_FILES := \
    glob_any.py \
    glob_either.py \
    glob_lit.py \
    glob_null.py \
    test_glob_any.py \
    test_glob_either.py \
    test_glob_lit.py \
    test_glob_problem.py

include ../examples.mk
