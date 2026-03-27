all:
	@echo "#" $$(basename $$(pwd)) > index.md
	@for filename in $(FILES); \
	do \
		jorma --suppress $$filename >> index.md; \
	done
