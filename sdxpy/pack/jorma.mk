# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    exhaustive.py \
    incremental.py \
    manual.py \
    z3_complete.py \
    z3_equal.py \
    z3_part_equal.py \
    z3_setup.py \
    z3_triple.py \
    z3_unequal.py

# Files referenced in the lesson Makefile but not present here:
# incremental_reverse.py — does not exist in the original lesson directory either.
MISSING := \
    incremental_reverse.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: pack\n\n'; \
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
