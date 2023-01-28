from argparse import ArgumentParser
import os
import re

re_title = re.compile(r'<title>.+</title>')

if __name__ == "__main__":
    parser = ArgumentParser()

    # Set title to Jeff

    for item in os.listdir("."):
        _, ext = os.path.splitext(item)
        if not '.html' in ext.lower():
            continue

        with open("./" + item, 'rt', encoding='utf8') as infile:
            html = infile.read()
            title = re_title.search(html)
            if title:
                newtitle = title.group(0).replace("HOPain", "D7")
                newhtml = html.replace(title.group(0), newtitle)
                with open("./" + item, 'wt', encoding='utf8') as outfile:
                    outfile.write(newhtml)
