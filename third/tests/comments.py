from pathlib import Path

import re


def comments_finder(my_file):
    try:
        with open(my_file, 'r', encoding='utf-8') as f:
            mytext = f.read()
    except FileNotFoundError as err:
        print(err)
    else:
        pattern = re.compile(
            r"(?<=\'{3})[^\']*(?=\'{3})"
            r'|'
            r"(?<=\"{3})[^\"]*(?=\"{3})"
        )
        resulte = pattern.findall(mytext)
        print(resulte)
        return resulte


if __name__ == "__main__":
    my_file = Path(Path.cwd(), 'test.py')
    comments_finder(my_file)
