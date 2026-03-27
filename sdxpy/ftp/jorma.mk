# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := ftp
PY_FILES := \
    client_all.py \
    client_chunk.py \
    logging_handler.py \
    server_chunk.py \
    server_lib.py \
    server_raw.py \
    test_server.py

include ../examples.mk
