# Run: make -f jorma.mk   Output: index.md
# Note: double_linear_dep.out is built via a shell script + JSON config,
# not from a standalone Python program; no double_linear_dep.py exists.
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := build
PY_FILES := \
    build_better.py \
    build_simple.py \
    build_time.py \
    test_build_better.py \
    test_build_time.py

include ../examples.mk
