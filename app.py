import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    doc_file_name_list = os.listdir(r"./templates/documents")
    doc_list = [file_name.replace('.html', '') for file_name in doc_file_name_list]
    return render_template("index.html", **locals())


@app.route('/documents/<doc_name>')
def doc(doc_name):
    return render_template(f"documents/{doc_name}.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
