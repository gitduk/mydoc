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
            doc = "".join(lines)
            # result = re.search("<body>(.*)</body>", html, re.S).group(1)

        doc_list.append(doc_name.replace(".html", ""))
        with open("templates/docs/" + doc_name, "w") as f:
            extend_dict = {
                "show_doc": doc,
            }
            html = build_child_html(father='index.html', extend_dict=extend_dict)
            f.write(html)

    return render_template("index.html", **locals())


@app.route('/documents/<doc_name>')
def doc(doc_name):
    return render_template(f"docs/{doc_name}.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
