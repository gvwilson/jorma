# Shared rules for jorma variable-role analysis.
# Each jorma.mk must define THIS_DIR, LESSON, and PY_FILES before including
# this file.

JORMA      := uv run jorma

.PHONY: all
all: index.md

index.md: $(PY_FILES)
	@{ \
	    printf '# Variable Role Analysis: %s\n\n' "$(LESSON)"; \
	    for f in $(PY_FILES); do \
	        printf '## %s\n\n' "$$f"; \
	        $(JORMA) --format markdown "$(THIS_DIR)$$f" 2>&1 || true; \
	        printf '\n'; \
	    done; \
	} > $@

.PHONY: clean
clean:
	rm -f index.md
