from abc import ABC
from cithara.core.contextualised_note import ChordTone
from cithara.core.interval import Interval
from cithara.core.note import Note, NoteGenerator

# Representation of chord tones as intervals from root
CHORD_FORMULA: dict[str, list[int]] = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8],
}


class Chord(ABC):
    def __init__(self, root: Note, type: str, use_flats: bool = True) -> None:
        self.root: Note = root
        self.type: str = type
        self.formula: list[int] = CHORD_FORMULA.get(self.type, [])
        self.notes: list[ChordTone] = ChordBuilder.build(root=self.root, formula=self.formula, use_flats=use_flats)
        self.tones = [note.note.note_name for note in self.notes]
        # i.e. triad, 4 note, etc.
        self.form: int = len(self.notes)


class MajorChord(Chord):
    def __init__(self, root: Note, use_flats: bool = True):
        super().__init__(root=root, type="major", use_flats=use_flats)
        

class MinorChord(Chord):
    def __init__(self, root: Note, use_flats: bool = True):
        super().__init__(root=root, type="minor", use_flats=use_flats)


class DiminishedChord(Chord):
    def __init__(self, root: Note, use_flats: bool = True):
        super().__init__(root=root, type="diminished", use_flats=use_flats)


class AugmentedChord(Chord):
    def __init__(self, root: Note, use_flats: bool = True):
        super().__init__(root=root, type="augmented", use_flats=use_flats)


class ChordBuilder:
    @staticmethod
    def build(
        root: Note, formula: list[int], use_flats: bool = True
    ) -> list[ChordTone]:
        chord = []
        tone = 0
        for tone in formula:
            if tone == 0:
                chord.append(
                    ChordTone(
                        note=root, root=root, tone=tone, interval=Interval(tone)
                    )
                )
            else:
                chord.append(
                    ChordTone(
                        note=NoteGenerator.from_interval(
                            root=root,
                            interval=Interval(tone),
                            use_flats=use_flats,
                        ),
                        root=root,
                        tone=tone,
                        interval=Interval(tone),
                    )
                )
        
        return chord

