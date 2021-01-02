
from disassemble import disassemble_paths

import pytest


@pytest.fixture
def disassemble(scope="session"):
    path = r'C:\Berries Sherries\Music\Axis of Awesome\4 Chords.tar.gz'
    return disassemble_paths(path)
