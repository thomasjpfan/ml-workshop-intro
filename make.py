import argparse
from jinja2 import Template
from livereload import Server
from pathlib import Path


def build():
    print("building index.html")

    assets = Path("assets")

    with (assets / "index.html.jinja").open('r') as f:
        template = Template(f.read())

    with open("slides.md", 'r') as f:
        slides = f.readlines()

    # get metadata up to the first title
    valid_metadata_keys = set(['title', 'use_katex'])
    metadata = {}
    for line in slides:

        # first title
        if line.startswith("#") or len(metadata) == len(valid_metadata_keys):
            break
        line_split = line.split(":", maxsplit=1)
        if len(line_split) != 2:
            continue

        key = line_split[0]
        if key not in valid_metadata_keys:
            continue

        value = line_split[1].strip()
        metadata[key] = value

    if len(metadata) != 2:
        raise ValueError("Be sure to include title: and use_katex as metadata "
                         "in slides.md file")

    output = template.render(title=metadata['title'],
                             use_katex=metadata['use_katex'] == 'True',
                             slides="".join(slides))

    with open("index.html", 'w') as f:
        f.write(output)


def live():
    print("Serving index.html")
    cur_dir = Path('.')

    server = Server()
    server.watch("slides.md", build)
    server.watch(str(cur_dir / 'assets' / "style.css"))
    server.serve(open_url_delay=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Building slides")
    parser.add_argument("action", choices=['build', 'live'])

    args = parser.parse_args()

    if args.action == 'build':
        build()
    else:
        live()
