# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    callable.py \
    ex_loop_globals_2.py \
    find_test_funcs.py \
    func_list.py \
    globals.py \
    globals_plus.py \
    locals.py \
    manual.py \
    runner.py \
    signature.py \
    type_func.py \
    type_int.py \
    type_len.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: test\n\n'; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n```\n' "$$f"; \
	        $(JORMA) "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '```\n\n'; \
	    done; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
