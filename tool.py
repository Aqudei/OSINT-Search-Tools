from argparse import ArgumentParser
import os
import re


def change_title(newtitle):
    re_title = re.compile(r'<title>.+</title>')

    for item in os.listdir("."):
        _, ext = os.path.splitext(item)
        if not '.html' in ext.lower():
            continue

        with open("./" + item, 'rt', encoding='utf8') as infile:
            html = infile.read()
            title = re_title.search(html)
            if title:
                newtitle_html = f"<title>{newtitle}</title>"
                newhtml = html.replace(title.group(0), newtitle_html)
                with open("./" + item, 'wt', encoding='utf8') as outfile:
                    outfile.write(newhtml)


def replace_text(origninal, replacement):
    for item in os.listdir("."):
        _, ext = os.path.splitext(item)
        if not '.html' in ext.lower():
            continue

        with open("./" + item, 'rt', encoding='utf8') as infile:
            html = infile.read()
            newhtml = html.replace(origninal, replacement)
            with open("./" + item, 'wt', encoding='utf8') as outfile:
                outfile.write(newhtml)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--change-title")
    args = parser.parse_args()
    if args.change_title:
        
        change_title(args.change_title)
