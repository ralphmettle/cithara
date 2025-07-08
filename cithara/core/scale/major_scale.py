from cithara.core.note import Note
from cithara.core.scale.base import Scale, ScaleBuilder, SCALE_FORMULAS

class MajorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root)
        self.type = "major"
        self.formula: list[int] = SCALE_FORMULAS.get(self.type)
        self.notes = ScaleBuilder.build(self.root, self.formula)
