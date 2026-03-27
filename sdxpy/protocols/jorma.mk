# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

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

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: protocols\n\n'; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n```\n' "$$f"; \
	        $(JORMA) "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '```\n\n'; \
	    done; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
