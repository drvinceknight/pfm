import collections
import itertools
import jinja2
import json
import nbformat
import pathlib
import shutil
import sys
import tempfile
import tqdm

from nbconvert import HTMLExporter, PDFExporter

ROOT = "cfm"
TITLE = "Computing for mathematics"
TITLE_CY = "Cyfrifiadureg ar gyfer mathemateg"
DESCRIPTION = "An undergraduate course introducing programming, through Python, to mathematicians."
DESCRIPTION_CY = "Cwrs israddedig yn cyflwyno rhaglennu, trwy defnyddio Python, i mathemategwyr."
KEYWORDS = "python, mathematics, jupyter, mathemateg"
AUTHOR = "Vince Knight"


def get_id(path):
    """
    Return the id of a file
    """
    stem = path.stem
    try:
        return stem[: stem.index("-")]
    except ValueError:
        stem = stem.lower()
        stem = stem.replace(" ", "-")
        stem = stem.replace(",", "")
        return stem


def get_name(path):
    """
    Return the name of a file
    """
    stem = path.stem
    try:
        return stem[stem.index("-") :].replace("-", " ").lstrip()
    except ValueError:
        return stem


def convert_html(nb_path, tags_to_ignore=["solution"]):
    """
    Convert a notebook to html
    """
    contents = nb_path.read_text()
    nb = json.loads(contents)

    cells = []
    for cell in nb["cells"]:
        if "tags" not in cell["metadata"] or all(
            tag not in cell["metadata"]["tags"] for tag in tags_to_ignore
        ):
            cells.append(cell)
    nb["cells"] = cells

    temporary_nb = tempfile.NamedTemporaryFile()
    with open(temporary_nb.name, "w") as f:
        f.write(json.dumps(nb))

    html_exporter = HTMLExporter()
    html_exporter.template_file = "basic"
    return html_exporter.from_file(temporary_nb)


def render_template(template_file, template_vars, searchpath="./templates/"):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    return template.render(template_vars)


def make_dir(
    path, directory, previous_url=None, next_url=None, chapters=None,
    suffix=None, **kwargs
):
    """
    Create a directory for the name of the file
    """
    path_id = get_id(path)
    p = pathlib.Path(f"./{directory}/{path_id}")
    if suffix is not None:
        p = p / pathlib.Path(suffix)
    p.mkdir(exist_ok=True)
    nb, _ = convert_html(path)
    nb = nb.replace("{{root}}", ROOT)
    if suffix is not None:
        searchpath = "./templates/cy/"
    else:
        searchpath = "./templates/"
    html = render_template(
        "content.html",
        {
            "nb": nb,
            "root": ROOT,
            "id": path_id,
            "previous_url": previous_url,
            "next_url": next_url,
            "chapters": chapters,
            **kwargs,
        },
        searchpath=searchpath,
    )
    (p / "index.html").write_text(html)


def make_collection(
    paths,
    directory,
    make_previous_url=True,
    make_next_url=True,
    chapters=None,
    **kwargs,
):

    number_of_paths = len(paths)
    for index, filename in enumerate(paths):
        previous_path = paths[(index - 1) % number_of_paths]
        previous_id = get_id(previous_path)

        next_path = paths[(index + 1) % number_of_paths]
        next_id = get_id(next_path)

        make_dir(
            pathlib.Path(filename),
            directory=directory,
            previous_url=previous_id,
            next_url=next_id,
            chapters=chapters,
            **kwargs,
        )


Chapter = collections.namedtuple("chapter", ["dir", "title", "nb"])

if __name__ == "__main__":

    nb_dir = pathlib.Path("nbs")
    chapter_paths = sorted(nb_dir.glob("./chapters/*ipynb"))
    chapter_paths_cy = sorted(nb_dir.glob("./cy/chapters/*ipynb"))
    other_paths = list(nb_dir.glob("./other/*ipynb"))
    other_paths_cy = list(nb_dir.glob("./cy/other/*ipynb"))

    chapters = []
    chapters_cy = []
    for path, path_cy in tqdm.tqdm(zip(chapter_paths, chapter_paths_cy)):
        chapters_cy.append(Chapter(f"{get_id(path_cy)}/cy", get_name(path_cy),
            str(path_cy)))
        chapters.append(Chapter(f"{get_id(path)}", get_name(path), str(path)))


    for paths, directory, suffix, title, list_of_chapters, description in [
        (chapter_paths, "chapters", None, TITLE, chapters, DESCRIPTION),
        (chapter_paths_cy, "chapters", "cy", TITLE_CY, chapters_cy, DESCRIPTION_CY),
        (other_paths, "other", None, TITLE, chapters, DESCRIPTION),
        (other_paths_cy, "other", "cy", TITLE_CY, chapters_cy, DESCRIPTION_CY),
    ]:
        make_collection(
            paths=paths,
            directory=directory,
            chapters=list_of_chapters,
            title=title,
            description=description,
            keywords=KEYWORDS,
            author=AUTHOR,
            suffix=suffix,
        )

    html = render_template(
        "home.html",
        {
            "chapters": chapters,
            "root": ROOT,
            "title": TITLE,
            "description": DESCRIPTION,
            "keywords": KEYWORDS,
            "author": AUTHOR,
        },
    )
    with open("index.html", "w") as f:
        f.write(html)

    html_cy = render_template(
        "home.html",
        {
            "chapters": chapters_cy,
            "root": ROOT,
            "title": TITLE_CY,
            "description": DESCRIPTION_CY,
            "keywords": KEYWORDS,
            "author": AUTHOR,
        },
        searchpath="./templates/cy/"
    )
    with open("cy/index.html", "w") as f:
        f.write(html_cy)
