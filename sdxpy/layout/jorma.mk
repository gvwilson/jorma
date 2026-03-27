# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := layout
PY_FILES := \
    easy_mode.py \
    placed.py \
    render.py \
    rendered.py \
    test_easy_mode.py \
    test_placed.py \
    test_rendered.py \
    test_wrapped.py \
    wrapped.py

include ../examples.mk
