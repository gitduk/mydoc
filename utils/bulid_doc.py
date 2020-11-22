import os
import mistune
from mistune import escape
from mistune.plugins import plugin_table, plugin_strikethrough, plugin_footnotes
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


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

    def block_code(self, code, info=None):
        if not info:
            return f'\n<pre><code>{mistune.escape(code)}</code></pre>\n'

        lexer = get_lexer_by_name(info, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


def markdown_to_html(file_path):
    file = open(file_path, "r")
    content = "".join(file.readlines())

    # use customized renderer
    plugins = [plugin_table, plugin_strikethrough, plugin_footnotes]
    markdown = mistune.create_markdown(renderer=PandaRenderer(), plugins=plugins)
    doc = markdown(content)

    file.close()
    return doc


def build_child_html(extends, block_dict):
    child_html = "{% " + f"extends '{extends}'" + " %}"
    for key, value in block_dict.items():
        child_html = child_html + "\n" + "{% " + f"block {key}" + " %}" + "\n" + value + "\n{% endblock %}" + "\n"

    return child_html


def parse_markdown_from_dir(file_dir):
    # get markdown file name list
    file_name_list = os.listdir(file_dir)

    # get markdown content
    doc_dict = {}
    for name in file_name_list:
        file_path = f"{file_dir}/{name}"

        # translate markdown to html
        doc = markdown_to_html(file_path)

        doc_dict[name.replace(".md", "")] = doc

    return doc_dict
