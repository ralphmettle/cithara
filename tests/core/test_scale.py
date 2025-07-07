import pytest
from cithara.core.note import Note
from cithara.core.scale.scale import Scale, MajorScale


def test_initialise_scale():
    major_scale = MajorScale(root=Note("C"))
