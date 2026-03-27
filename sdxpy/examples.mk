# The including file must define a variable TARGETS with the names of everything
# to be created.
all: ${TARGETS}

# Show the targets defined by the including file.
targets:
	@echo ${TARGETS}

# Create HTML or text from a shell script that runs some Python.
# Normally used when there are parameters to the Python file but no extra
# dependencies.
%.html: %.sh %.py
	bash $< 2>&1 > $@
%.out: %.sh %.py
	bash $< 2>&1 > $@

# Create HTML or text when there is only a shell script.
# Normally used when the output depends on multiple .py files, in which case the
# including file must define dependencies.
%.html: %.sh
	bash $< 2>&1 > $@
%.out: %.sh
	bash $< 2>&1 > $@

# Create HTML or text by running Python without parameters.
%.html: %.py
	python $< 2>&1 > $@
%.out: %.py
	python $< 2>&1 > $@

# Get rid of all generated files.
erase:
	rm -f ${TARGETS}
