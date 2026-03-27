all:
	@echo "#" $$(basename $$(pwd)) > index.md
	@echo "" >> index.md
	@for filename in $(FILES); \
	do \
		echo "##" $$(basename $$filename) >> index.md; \
		echo "" >> index.md; \
		jorma --run --suppress $$filename >> index.md; \
		echo "" >> index.md; \
	done
