def build_child_html(father, extend_dict):
    html = "{% " + f"extends '{father}'" + " %}"
    for key, value in extend_dict.items():
        html = html + "\n" + "{% " + f"block {key}" + " %}" + "\n" + value + "{% endblock %}" + "\n"

    return html
