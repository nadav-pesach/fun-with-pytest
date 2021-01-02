import pytest


def test_disassemble_dict(disassemble):
    assert isinstance(disassemble, dict)


words = [
    'folder',
    'name',
    'extension'
]


@pytest.mark.parametrize('word', words)
def test_disassemble_keys(disassemble, word):
    assert word in disassemble.keys()
