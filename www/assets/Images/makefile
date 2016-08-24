tex  = $(wildcard *.tex)
pngs = $(tex:%.tex=%.png)

all: $(pngs) 

%.png: %.tex
	./convert_tex_to_png.py $<

clean:
	rm *.aux
	rm *.log
	rm *.pdf
