PITCHES = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
FIFTHS = ["F", "C", "G", "D", "A", "E", "B"]


class Note:
    def __init__(self, note_string: str):
        self.note_string = note_string[0].upper() + note_string[1:].lower()
        self.natural = note_string[0]
        self.natural_pitch = PITCHES.get(note_string[0])

        _valid_accidentals = ["#", "b"]
        for acc in self.note_string[1:].lower():
            if acc not in _valid_accidentals:
                raise ValueError(f"Invalid accidental: {acc}")

        if self.natural_pitch is None:
            raise ValueError(f"Invalid note: {note_string}")

    @property
    def pitch(self) -> int:
        note_accidentals = self.note_string[1:].lower()
        shift = 0

        for acc in note_accidentals:
            if acc == "#":
                shift += 1
            elif acc == "b":
                shift -= 1

        return (self.natural_pitch + shift) % 12

    def _note_from_pitch(self, value) -> str:
        return next((key for key, val in PITCHES.items() if val == value), None)

    def normalise(self, prefer_flat: bool = False) -> "Note":
        if self.pitch in PITCHES.values():
            return Note(self._note_from_pitch(self.pitch))

        if prefer_flat:
            return Note(self._note_from_pitch(self.pitch + 1) + "b")
        else:
            return Note(self._note_from_pitch(self.pitch - 1) + "#")

    def is_enharmonic(self, other_note) -> bool:
        return self.pitch == other_note.pitch

    def __str__(self):
        return self.note_string

    def __repr__(self):
        return f"<Note: {self.note_string}>"


class PitchTransform:
    @staticmethod
    def sharpen(note: Note) -> Note:
        if note.note_string[-1] == "b":
            return Note(note.note_string[:-1])
        else:
            return Note(note.note_string + "#")

    @staticmethod
    def flatten(note: Note) -> Note:
        if note.note_string[-1] == "#":
            return Note(note.note_string[:-1])
        else:
            return Note(note.note_string + "b")
