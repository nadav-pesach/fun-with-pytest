
import pytest


def test_highlight_list(highlight):
    assert isinstance(highlight, list)
    
def test_item_tuple(highlight):
    assert all(isinstance(item,tuple) for item in highlight)