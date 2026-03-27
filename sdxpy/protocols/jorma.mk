# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := protocols
PY_FILES := \
    alternative_design.py \
    better_iterator.py \
    callable.py \
    decorator_param.py \
    decorator_simple.py \
    ex_timer.py \
    ex_with.py \
    mock_context.py \
    mock_object.py \
    mock_time.py \
    naive_iterator.py \
    test_naive_iterator.py \
    wrap_capture.py \
    wrap_infinite.py \
    wrap_param.py

include ../examples.mk
