# Standalone Makefile for variable role analysis using jorma.
# Run: make -f jorma.mk   Output: index.md

THIS_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
JORMA_ROOT := $(realpath $(THIS_DIR)../..)
JORMA      := uv run --directory $(JORMA_ROOT) jorma

PY_FILES := \
    client_all.py \
    client_chunk.py \
    logging_handler.py \
    server_chunk.py \
    server_lib.py \
    server_raw.py \
    test_server.py

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: ftp\n\n'; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n```\n' "$$f"; \
	        $(JORMA) "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '```\n\n'; \
	    done; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
