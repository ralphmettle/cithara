from abc import ABC
from cithara.core.interval import Interval
from cithara.core.note import Note

# Representation of chord tones as intervals from root
CHORD_FORMULA: dict[str, list[int]] = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
}


class Chord(ABC):
    def __init__(self, root: Note, type: str, ext: int = 0) -> None:
        self.root: Note = root
        self.type: str
        self.notes: list[str]
        self.formula: list[int] = []
        # Number of notes/tones in the chord
        self.form: int


class MajorChord(Chord):
    def __init__(self, root: Note, use_flats: bool = True):
        super().__init__(root=root)
        self.type = "major"
        self.formula = CHORD_FORMULA.get(self.type)
        self.notes = ChordBuilder.build(root=self.root, use_flats=use_flats)
        self.tones = [note.note_name for note in self.notes]


class MinorChord:
    pass


class DominantChord:
    pass


class DiminishedChord:
    pass


class AugmentedChord:
    pass


class ChordBuilder:
    @staticmethod
    def build() -> list[Note]:
        pass
