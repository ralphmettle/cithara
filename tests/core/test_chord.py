import pytest
from cithara.core.chord.base import (
    Chord,
    MajorChord,
    MinorChord,
    DiminishedChord,
    AugmentedChord,
    ChordBuilder,
)
from cithara.core.note import Note
from cithara.core.scale.major_scale import MajorScale


def test_major_chord_initialisation_from_note():
    chord = MajorChord(root=Note("C"))
    assert chord.tones == ["C", "E", "G"]


def test_minor_chord_initialisation_from_note():
    chord = MinorChord(root=Note("C"))
    assert chord.tones == ["C", "Eb", "G"]


def test_diminished_chord_initialisation_from_note():
    chord = DiminishedChord(root=Note("C"))
    assert chord.tones == ["C", "Eb", "Gb"]

def test_augmented_chord_initialisation_from_note():
    chord = AugmentedChord(root=Note("C"), use_flats=False)
    assert chord.tones == ["C", "E", "G#"]
