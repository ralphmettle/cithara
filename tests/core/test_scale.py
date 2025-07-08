import pytest
from cithara.core.interval import Interval
from cithara.core.note import Note
from cithara.core.scale.scale import MajorScale
from cithara.core.scale.scale_degree import ScaleDegree


def test_initialise_major_scale():
    major_scale = MajorScale(root=Note("C"))
    assert major_scale.root == Note("C")
    assert major_scale.type == "major"
    assert isinstance(major_scale.notes[0], ScaleDegree)
    assert major_scale.notes == [
        ScaleDegree(note=Note("C"), root=Note("C"), degree=0, interval=Interval(0)),
        ScaleDegree(note=Note("D"), root=Note("C"), degree=1, interval=Interval(2)),
        ScaleDegree(note=Note("E"), root=Note("C"), degree=2, interval=Interval(4)),
        ScaleDegree(note=Note("F"), root=Note("C"), degree=3, interval=Interval(5)),
        ScaleDegree(note=Note("G"), root=Note("C"), degree=4, interval=Interval(7)),
        ScaleDegree(note=Note("A"), root=Note("C"), degree=5, interval=Interval(9)),
        ScaleDegree(note=Note("B"), root=Note("C"), degree=6, interval=Interval(11)),
    ]
    # assert major_scale.get_degree(1) == ScaleDegree(Note("C"))
