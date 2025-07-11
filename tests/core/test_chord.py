import pytest
from cithara.core.chord.base import Chord, MajorChord, ChordBuilder
from cithara.core.note import Note
from cithara.core.scale.major_scale import MajorScale


def test_major_chord_initialisation_from_note():
    chord = MajorChord(root=Note("C"))
    assert chord.tones == ["C", "E", "G"]
    assert chord.tone(0).note_name == "C"
