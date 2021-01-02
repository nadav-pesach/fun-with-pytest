
from pathlib import Path

from comments import comments_finder

import pytest


@pytest.fixture
def comment(scope="session"):
    my_file = Path(Path.cwd(), 'test.py')
    return comments_finder(my_file)
