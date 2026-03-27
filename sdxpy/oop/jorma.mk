# Run: make -f jorma.mk   Output: index.md
THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

LESSON   := oop
PY_FILES := \
    func_obj.py \
    inherit_class.py \
    inherit_constructor.py \
    inherit_original.py \
    larger.py \
    shapes_class.py \
    shapes_dict.py \
    shapes_original.py \
    spread.py \
    varargs.py

include ../examples.mk
