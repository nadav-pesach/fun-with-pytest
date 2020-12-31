
from pathlib import Path

import re


def highlight_below(myfile_path):
    with open(myfile_path, 'r', encoding='utf-8') as f:
        mytext = f.read()
        pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
        match = re.findall(pattern, mytext)
        return [(item[0], item[1]) for item in match]


if __name__ == "__main__":
    myfile_path = Path(Path.cwd(), 'myhtml.html')
    highlight_below(myfile_path)
