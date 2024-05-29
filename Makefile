# Build the book.
#
# Note that this does not work as intended: all steps are recompiled 
# regardless of whether or not the source files are modified.
RAW_LATEX:=taylor-and-francis/_build/latex/book.tex
CLEAN_LATEX:=taylor-and-francis/_build/latex/main.tex
MYST_SOURCE_FILES:=$(shell find book -type f)
CLEAN_SCRIPT:=taylor-and-francis/_build/latex/clean.py

all: taf html

taf: taylor-and-francis/main.pdf

taylor-and-francis/main.pdf: CLEAN_LATEX
	@echo "Compiling final latex file"
	@cd taylor-and-francis; latexmk -c; latexmk --xelatex main.tex > .taf.make.log 2>&1 

CLEAN_LATEX: RAW_LATEX $(CLEAN_SCRIPT)
	@echo "Cleaning generated latex file"
	@cd taylor-and-francis/_build/latex; python clean.py > .clean-tex.make.log 2>&1

RAW_LATEX: $(MYST_SOURCE_FILES)
	@echo "Generating latex file from myst source files"
	@jb build book --builder latex --path-output taylor-and-francis > .generate-tex.make.log 2>&1

html: _build/html/index.html

_build/html/index.html: $(MYST_SOURCE_FILES)
	@echo "Generating html files"
	@jb build book --path-output  . > .html.make.log 2>&1 
