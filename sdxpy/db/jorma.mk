# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    blocked.py \
    blocked_file.py \
    cleanup.py \
    file_backed.py \
    interface.py \
    interface_original.py \
    just_dict_original.py \
    just_dict_refactored.py \
    record.py \
    record_original.py \
    show_packed_records.py \
    test_db_original.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: db\n\n'; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n```\n' "$$f"; \
	        $(JORMA) "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '```\n\n'; \
	    done; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
