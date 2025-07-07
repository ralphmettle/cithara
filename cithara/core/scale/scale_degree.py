from core.note import Note
from core.interval import Interval


class ScaleDegree:
    def __init__(self, note: Note, root: Note, degree: int, interval: Interval):
        self.note: Note = note
        self.root: Note = root
        self.degree: int = degree
        self.interval: Interval = interval  # Distance from the tonic

    def __str__(self):
        return f"{self.note.note_name} (root: {self.root.note_name}, degree: {self.degree})"

    def __repr__(self):
        return f"<ScaleDegree degree={self.degree}, note='{self.note.note_name}', root='{self.root.note_name}', interval='{self.interval.interval_name}'>"


scale_degree = ScaleDegree(
    note=Note("C"), root=Note("A"), degree=3, interval=Interval(3)
)
