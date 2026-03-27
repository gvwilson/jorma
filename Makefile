all: commands

## commands: show available commands (*)
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## check: check code issues
check:
	@ruff check .

## clean: clean up
clean:
	@find . -path ./.venv -prune -o -type d -name __pycache__ -exec rm -rf {} +
	@find . -path ./.venv -prune -o -type d -name .ruff_cache -exec rm -rf {} +
	@find . -path ./.venv -prune -o -type f -name '*~' -exec rm {} +

## fix: fix code issues
fix:
	@ruff check --fix .

## format: format code
format:
	@ruff format .

## test: test code
test:
	python -m pytest tests

## coverage: run tests with coverage
coverage:
	@python -m coverage run -m pytest tests
	@python -m coverage report --show-missing

## analyze: regenerate jorma analysis for all sdxpy subdirectories
analyze:
	@for dir in sdxpy/*/; do \
	    if [ -f "$$dir/jorma.mk" ]; then \
	        echo "=== $$dir ==="; \
	        cd $$dir && $(MAKE) -f jorma.mk; \
	    fi; \
	done

## package: build support package
package:
	python -m build

## publish: publish using ~/.pypirc credentials
publish:
	twine upload --verbose dist/*
