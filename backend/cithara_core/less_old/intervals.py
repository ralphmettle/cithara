from notes import Note


class Interval:
    # Interval names and their corresponding semitone distances
    _interval_names = {
        0: "Unison",
        1: "Minor Second",
        2: "Major Second",
        3: "Minor Third",
        4: "Major Third",
        5: "Perfect fourth",
        6: "Tritone",
        7: "Perfect Fifth",
        8: "Minor Sixth",
        9: "Major Sixth",
        10: "Minor Seventh",
        11: "Major Seventh",
    }

    def __init__(self, start_note: Note, end_note: Note):
        self.start_note = start_note
        self.end_note = end_note

    @property
    def semitones(self) -> int:
        return (self.end_note.pitch - self.start_note.pitch) % 12

    @property
    def name(self) -> str:
        return self._interval_names.get(self.semitones, "Unknown interval")

    def __str__(self):
        return f"{self.start_note} -> {self.end_note} | {self.name} ({self.semitones} semitones)"
