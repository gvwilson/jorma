# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := http
PY_FILES := \
    basic_server.py \
    file_server.py \
    mock_handler.py \
    requests_example.py \
    test_testable_server.py \
    testable_server.py

include ../examples.mk
