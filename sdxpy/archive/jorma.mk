# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := archive
PY_FILES := \
    backup.py \
    backup_oop.py \
    hash_all.py \
    test_backup.py \
    test_hash_all.py \
    test_mock_fs.py \
    test_mock_tree.py

include ../examples.mk
