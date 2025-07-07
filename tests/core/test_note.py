import pytest
from cithara.core.interval import Interval
from cithara.core.note import Note, PitchTransformer, NoteGenerator

def test_note_initialisation():
    note = Note("C#")
    assert note.note_name == "C#"
    assert note.natural == "C"
    assert note.pitch_class == 1

def test_invalid_note_raises():
    with pytest.raises(ValueError):
        Note("H")

    with pytest.raises(ValueError):
        Note("C$")

    with pytest.raises(ValueError):
        Note("")

def test_pitch_class_calculation():
    assert Note("C").pitch_class == 0
    assert Note("B#").pitch_class == 0
    assert Note("D#").pitch_class == 3
    assert Note("Eb").pitch_class == 3
    assert Note("F##").pitch_class == 7
    assert Note("Gbb").pitch_class == 5

def test_enharmonic_equivalents():
    enharmonics_of_eb = Note("Eb").enharmonics
    enharmonics_of_d_sharp = Note("D#").enharmonics
    assert "D#" in enharmonics_of_eb or "Eb" in enharmonics_of_d_sharp

def test_note_equality():
    assert Note("D#") == Note("Eb")
    assert Note("C") != Note("C#")

def test_str_and_repr():
    note = Note("F#")
    assert str(note) == "F#"
    assert repr(note) == "<Note: 'F#'> (pitch class: 6)"

def test_canonise_method():
    assert Note("C#")._canonise() == "C#"
    canonised = Note("Eb")._canonise(use_flats=True)
    assert canonised in {"D#", "Eb"}  # Allow for both options if ambiguous

def test_name_from_pitch():
    assert PitchTransformer.name_from_pitch(0) == "C#"
    assert PitchTransformer.name_from_pitch(2) == "D#"

def test_generate_from_pitch_class():
    assert NoteGenerator.from_pitch_class(pitch_class=0, use_flats=False).note_name == Note("C").note_name
    assert NoteGenerator.from_pitch_class(pitch_class=1, use_flats=True).note_name == Note("Db").note_name
    assert NoteGenerator.from_pitch_class(pitch_class=3, use_flats=False).note_name == Note("D#").note_name

def test_generate_from_interval():
    assert NoteGenerator.from_interval(root=Note("C"), interval=Interval(4)).note_name == Note("E").note_name
    assert NoteGenerator.from_interval(root=Note("C"), interval=Interval(3)).note_name == Note("D#").note_name
    assert NoteGenerator.from_interval(root=Note("C"), interval=Interval(3), use_flats=True).note_name == Note("Eb").note_name

