import re
from flask import Flask, render_template, render_template_string
from utils.bulid_doc import parse_markdown_from_dir
from utils.process_html import extract_toc_from_html
from utils.db import save_html_to_sqlite, get_doc_from_sqlite

app = Flask(__name__)


@app.route('/')
def index():
    # get doc name dict
    doc_dict = parse_markdown_from_dir("./markdown")

    # get doc name list
    doc_list = [key for key in doc_dict]

    # save to sqlite
    save_html_to_sqlite(doc_dict)

    return render_template("index.html", **locals())


@app.route('/documents/<doc_name>')
def show_doc(doc_name):
    doc = get_doc_from_sqlite(doc_name)
    toc_dict = extract_toc_from_html(doc)
    with open(f"templates/show_doc.html", "r") as f:
        text = "".join(f.readlines())
        need_replace = re.search("<div id='write' class=''>(\n.*)</div>", text, re.S).group(1)
        html = text.replace(need_replace, doc)

    return render_template_string(html, **locals())


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
