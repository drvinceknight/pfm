"""
Script to clean the base LaTeX file.
"""
import pathlib
import re

regex_patterns = {
    re.compile(r"{{(.*?)}.png}"): r"{./_build/latex/\1.png}",
    re.compile(r"\\\(\\LaTeX\\\)"): r"\\LaTeX",
}


def read_book(p):
    tex = p.read_text()
    for pattern, replacement in regex_patterns.items():
        tex = re.sub(pattern, replacement, tex)
    return tex


if __name__ == "__main__":
    starting_text = "\part{Overview}"
    ending_text = r"\renewcommand{\indexname}{Index}"
    book_path = pathlib.Path("./book.tex")
    tex = read_book(book_path)
    index_of_end_of_preamble = tex.index(starting_text)
    index_of_end_of_book = tex.index(ending_text)
    out_path = pathlib.Path("./main.tex")
    out_path.write_text(
        tex[index_of_end_of_preamble + len(starting_text) : index_of_end_of_book]
    )
