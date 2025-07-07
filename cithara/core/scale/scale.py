from cithara.core.note import Note
from cithara.core.interval import Interval
from cithara.core.scale.scale_degree import ScaleDegree

# Mapping of 
SCALE_FORMULAS = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
}

class Scale:
    def __init__(self, root: Note) -> None:
        self.root: Note = root
        self.type: str
        self.notes: list[ScaleDegree] = []
        # The interval distance of each scale degree by semitone from the root
        self.formula: list[int] = []


class MajorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root)
        self.type = "major"
        self.formula: list[int] = SCALE_FORMULAS.get(self.type)


class HarmonicMinorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root)


class MelodicMinorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root)


class ScaleBuilder:
    @staticmethod
    def build(self, root: Note, formula: list[int]) -> list[Note]:
        return
