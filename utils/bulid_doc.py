def build_child_html(extends, block_dict):
    html = "{% " + f"extends '{extends}'" + " %}"
    for key, value in block_dict.items():
        html = html + "\n" + "{% " + f"block {key}" + " %}" + "\n" + value + "\n{% endblock %}" + "\n"

    return html
