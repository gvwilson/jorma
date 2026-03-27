# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := cache
PY_FILES := \
    cache_base.py \
    cache_filesystem.py \
    cache_io.py \
    cache_limited.py \
    index_base.py \
    index_csv.py \
    test_cache_filesystem.py \
    test_cache_limited.py \
    test_index_csv.py

include ../examples.mk
