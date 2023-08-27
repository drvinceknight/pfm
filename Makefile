ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

taf:  clean-tex 
	@echo "Compiling final latex file"
	@cd taylor-and-francis; latexmk --xelatex main.tex > log/taf.log 2>&1 

clean-tex: generate-tex log
	@echo "Cleaning generated latex file"
	@cd taylor-and-francis/_build/latex; python clean.py > $(ROOT_DIR)/log/clean-tex.log 2>&1

generate-tex: log
	@echo "Generating latex file from myst source files"
	@jb build book --builder latex --path-output taylor-and-francis > $(ROOT_DIR)/log/generate-tex.log 2>&1

log:
	@echo "Making log directory"
	@mkdir $(ROOT_DIR)/log
