# Knowledge versus technique

A diagram showing the difference between technique and knowledge.

## To compile

To compile the LaTeX document:

    $ latexmk --xelatex main.tex

To convert `main.pdf` to `png`:

    $ convert -density 300 main.pdf -quality 90 main.png
