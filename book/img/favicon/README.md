# Favicon

A favicon version of the cover

## To compile

To compile the LaTeX document:

    $ latexmk --xelatex main.tex

To convert `main.pdf` to `png`:

    $ convert -resize x32 -gravity center -crop 32x32+0+0 main.pdf -flatten -colors 256 -background transparent favicon.ico
