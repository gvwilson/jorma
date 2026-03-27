# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    dump_ast.py \
    ex_redundant.py \
    find_duplicate_keys.py \
    find_unused_variables.py \
    function_keys.py \
    has_duplicate_keys.py \
    has_unused_variables.py \
    simple.py \
    walk_ast.py

# Files referenced in the lesson Makefile but not present here:
# double.py — used as input to dump_ast.py and walk_ast.py, not copied here.
# dump_ast_double.py, dump_ast_simple.py — lesson builds these targets by running
# dump_ast.py on double.py/simple.py via shell scripts; no standalone .py files.
MISSING := \
    double.py \
    dump_ast_double.py \
    dump_ast_simple.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: lint\n\n'; \
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
