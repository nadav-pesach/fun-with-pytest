import pytest


def test_comment_list(comment):
    assert isinstance(comment, list)


words = [
    '\n',
]


@pytest.mark.parametrize('word', words)
def test_comment_multi_line(comment, word):
    assert all(word in item for item in comment)
