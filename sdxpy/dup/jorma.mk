# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := dup
PY_FILES := \
    brute_force_2.py \
    dup.py \
    grouped.py \
    naive_hash.py \
    using_sha256.py

include ../examples.mk
