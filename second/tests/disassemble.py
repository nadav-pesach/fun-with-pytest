import re


def disassemble_paths(path):
    pattern = re.compile(
        r'(?P<folder>[^\\]+)'
        r'\\'
        r'(?P<name>[^\\]+)'
        r'\.'
        r'(?P<extension>[^\.]+)$'
    )
    path_de = pattern.search(path)
    for item in path_de.groupdict():
        print(type(item), item)
    return path_de.groupdict()


if __name__ == "__main__":
    path = r'C:\Berries Sherries\Music\Axis of Awesome\4 Chords.tar.gz'
    disassemble_paths(path)
