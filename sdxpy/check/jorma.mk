# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := check
PY_FILES := \
    attrs.py \
    catalog.py \
    check.py \
    contains.py \
    ex_flatten.py \
    parse.py \
    visitor.py

include ../examples.mk
