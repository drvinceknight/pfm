# Build commands for the book
#
MYST_SOURCE_FILES:=$(shell find book -type f)

all: tex html

tex: taylor-and-francis/_build/latex/book.tex

tex: $(MYST_SOURCE_FILES)
	@echo "Generating latex file from myst source files"
	@jb build book --builder latex --path-output taylor-and-francis > .generate-tex.make.log 2>&1

html: _build/html/index.html

_build/html/index.html: $(MYST_SOURCE_FILES)
	@echo "Generating html files"
	@jb build book --path-output  . > .html.make.log 2>&1 
