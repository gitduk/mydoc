import os
import re
from flask import Flask, render_template, render_template_string
from utils.bulid_doc import parse_markdown_from_dir, markdown_to_html
from utils.process_html import extract_toc_from_html
from utils.db import save_html_to_sqlite, get_doc_from_sqlite

app = Flask(__name__)


@app.route('/')
def index():
    # set title
    title = "Kaige Documents"

    # get doc name list
    dir_path = "markdown/"
    file_name_list = os.listdir(dir_path)

    doc_list_generator = (key.replace(".md", "") for key in file_name_list)

    return render_template("index.html", **locals())


@app.route('/documents/<doc_name>')
def show_doc(doc_name):
    # set title
    title = f"Document - {doc_name}"

    # get doc content
    file_path = f"markdown/{doc_name}.md"
    doc = markdown_to_html(file_path)

    # extract toc from doc
    toc_dict = extract_toc_from_html(doc)

    # build child html
    with open(f"templates/show_doc.html", "r") as f:
        text = "".join(f.readlines())
        need_replace = re.search("<div id='write' class=''>(\n.*)</div>", text, re.S).group(1)
        html = text.replace(need_replace, doc)

    return render_template_string(html, **locals())


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
