# Galton board

A diagram showing the state space of a Galton board

## To compile

To compile the LaTeX document:

    $ latexmk --xelatex main.tex

To convert `main.pdf` to `png`:

    $ convert -density 300 main.pdf -quality 90 main.png
