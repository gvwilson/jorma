# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := lint
PY_FILES := \
    dump_ast.py \
    ex_redundant.py \
    find_duplicate_keys.py \
    find_unused_variables.py \
    function_keys.py \
    has_duplicate_keys.py \
    has_unused_variables.py \
    simple.py \
    walk_ast.py

include ../examples.mk
