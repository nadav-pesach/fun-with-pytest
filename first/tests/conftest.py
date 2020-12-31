from pathlib import Path

import pytest

from highlight import highlight_below


@pytest.fixture
def highlight(scope="session"):
    myfile_path = Path(Path.cwd(), 'myhtml.html')
    return highlight_below(myfile_path)
