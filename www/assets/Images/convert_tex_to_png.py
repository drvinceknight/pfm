#!/usr/bin/env python
from sys import argv
from os import system

system("pdflatex %s" % (argv[1]))
system("convert -density 300 %s.pdf %s.png" % (argv[1][:-4], argv[1][:-4]))
