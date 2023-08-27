# Build the book for Taylor and Francis.
#
# Note that this does not work as intended: all steps are recompiled 
# regardless of whether or not the source files are modified.
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
RAW_LATEX:=$(ROOT_DIR)/taylor-and-francis/_build/latex/book.tex
CLEAN_LATEX:=$(ROOT_DIR)/taylor-and-francis/_build/latex/main.tex
MYST_SOURCE_FILES:=$(shell find $(ROOT_DIR)/book -type f)
CLEAN_SCRIPT:=$(ROOT_DIR)/taylor-and-francis/_build/latex/clean.py

$(ROOT_DIR)/taylor-and-francis/main.pdf: CLEAN_LATEX
	@echo "Compiling final latex file"
	@cd $(ROOT_DIR)/taylor-and-francis; latexmk --xelatex main.tex > $(ROOT_DIR)/taf.make.log 2>&1 

CLEAN_LATEX: RAW_LATEX $(CLEAN_SCRIPT)
	@echo "Cleaning generated latex file"
	@cd $(ROOT_DIR)/taylor-and-francis/_build/latex; python clean.py > $(ROOT_DIR)/clean-tex.make.log 2>&1

RAW_LATEX: $(MYST_SOURCE_FILES)
	@echo "Generating latex file from myst source files"
	@jb build book --builder latex --path-output $(ROOT_DIR)/taylor-and-francis > $(ROOT_DIR)/.generate-tex.make.log 2>&1
