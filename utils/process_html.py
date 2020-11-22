import re


def extract_toc_from_html(html):
    h_tags = re.findall("<h\d>.*?</h\d>", str(html))
    toc_dict = {}
    for h in h_tags:
        level = h[2]
        # name = re.search("name=\"(.*?)\"", h).group(1)
        name = re.search("name=\"(.*?)\"", h).group(1)
        toc_dict[name] = int(level)

    return toc_dict


def save_html_to_dir(html, dir_path):
    with open(dir_path, "w") as f:
        f.write(html)
