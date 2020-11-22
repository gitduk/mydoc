import os
import mistune
from mistune import escape

from utils.process_html import save_html_to_dir


class PandaRenderer(mistune.HTMLRenderer):
    def codespan(self, text):
        if text.startswith('$') and text.endswith('$'):
            return '<span class="math">' + escape(text) + '</span>'
        return '<code>' + escape(text) + '</code>'

    def link(self, link, text=None, title=None):
        element = f'<a href={link} title={title}><span>{text}</span></a>'
        return element

    def image(self, src, alt="", title=None):
        element = f'<img src={src} referrerpolicy="no-referrer" alt={alt} title={title}>'
        return element

    def heading(self, text, level):
        element = f'<h{level}><a name="{text}" class="md-header-anchor" style="position: relative;top: -40px;"></a><span>{text}</span></h{level}>'
        return element


def markdown_to_html(file_path):
    file = open(file_path, "r")
    content = "".join(file.readlines())

    # use customized renderer
    markdown = mistune.create_markdown(renderer=PandaRenderer())
    html = markdown(content)

    file.close()
    return html


def build_child_html(extends, block_dict):
    html = "{% " + f"extends '{extends}'" + " %}"
    for key, value in block_dict.items():
        html = html + "\n" + "{% " + f"block {key}" + " %}" + "\n" + value + "\n{% endblock %}" + "\n"

    return html


def parse_markdown_from_dir(file_dir):
    # get markdown file name list
    file_name_list = os.listdir(file_dir)

    # get markdown content
    doc_dict = {}
    for name in file_name_list:
        file_path = f"{file_dir}/{name}"

        # translate markdown to html
        html = markdown_to_html(file_path)

        doc_dict[name.replace(".md", "")] = html

    return doc_dict
