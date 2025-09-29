from cithara.core.note import Note
from cithara.core.scale.base import Scale, ScaleBuilder, SCALE_FORMULA


class HarmonicMinorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root=root, type="harmonic_minor")
