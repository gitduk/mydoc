import os
import re
from flask import Flask, render_template
from utils.bulid_doc import build_child_html

app = Flask(__name__)


@app.route('/')
def index():
    doc_file_name_list = os.listdir(r"./templates/documents")
    doc_list = [file_name.replace('.html', '') for file_name in doc_file_name_list]

    doc_file_name_list = os.listdir(r"./templates/documents")
    html_doc_list = [file_name for file_name in doc_file_name_list]
    doc_list = []
    root = "templates/documents/"
    for doc_name in html_doc_list:
        with open(root + doc_name, "r") as f:
            lines = f.readlines()
            text = "".join(lines)
            drop = re.search("<style .*</style>", text, re.S).group()
            doc = text.replace(drop, "")

        doc_list.append(doc_name.replace(".html", ""))

        toc = "{% for name, level in toc_dict.items() %}\n<a href='#{{ name }}'>{{ name }}</a>\n{% endfor %}\n"
        with open("templates/docs/" + doc_name, "w") as f:
            block_dict = {
                "show_doc": doc,
                "TOC": toc
            }
            html = build_child_html(extends='index.html', block_dict=block_dict)
            f.write(html)

    return render_template("index.html", **locals())


@app.route('/documents/<doc_name>')
def doc(doc_name):
    file_path = f"./templates/docs/{doc_name}.html"
    with open(file_path, "r") as f:
        lines = f.readlines()
        html = "".join(lines)
        h_tags = re.findall("<h\d>.*?</h\d>", html)
        toc_dict = {}
        for h in h_tags:
            level = h[2]
            name = re.search("name=\"(.*?)\"", h).group(1)
            toc_dict[name] = level
    return render_template(f"docs/{doc_name}.html", **locals())


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
