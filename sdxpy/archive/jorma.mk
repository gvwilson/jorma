# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    backup.py \
    backup_oop.py \
    hash_all.py \
    test_backup.py \
    test_hash_all.py \
    test_mock_fs.py \
    test_mock_tree.py

# Files referenced in the lesson Makefile but not present here:
MISSING := \
    sample_dir.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: archive\n\n'; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n```\n' "$$f"; \
	        $(JORMA) "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '```\n\n'; \
	    done; \
	    if [ -n "$(MISSING)" ]; then \
	        printf '## Programs Not Analyzed\n\n'; \
	        printf 'The following programs are referenced in the lesson Makefile\nbut are not present in this directory:\n\n'; \
	        for m in $(MISSING); do printf '%s\n' "- $$m"; done; \
	        printf '\n'; \
	    fi; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
