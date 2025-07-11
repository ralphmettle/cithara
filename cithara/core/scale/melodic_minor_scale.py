from cithara.core.note import Note
from cithara.core.scale.base import Scale, ScaleBuilder, SCALE_FORMULA


class MelodicMinorScale(Scale):
    def __init__(self, root: Note, use_flats: bool = True) -> None:
        super().__init__(root=root, type="melodic_minor", use_flats=use_flats)
