from cithara.core.note import Note
from cithara.core.interval import Interval


class ScaleDegree:
    def __init__(self, note: Note, root: Note, degree: int, interval: Interval):
        self.note: Note = note
        self.root: Note = root
        # 0-indexed (0 - 6)
        self.degree: int = degree
        self.interval: Interval = interval

    def __str__(self):
        return f"{self.note.note_name} (root: {self.root.note_name}, degree: {self.degree})"

    def __repr__(self):
        return f"<ScaleDegree degree={self.degree}, note='{self.note.note_name}', root='{self.root.note_name}', interval='{self.interval.interval_name}'>"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ScaleDegree):
            return NotImplemented
        return (
            self.note == other.note and
            self.root == other.root and
            self.degree == other.degree and
            self.interval == other.interval
        )

