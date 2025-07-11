from cithara.core.note import Note
from cithara.core.scale.base import Scale, ScaleBuilder, SCALE_FORMULA


class MelodicMinorScale(Scale):
    def __init__(self, root: Note, use_flats: bool) -> None:
        super().__init__(root=root)
        self.type = "melodic_minor"
        self.formula = SCALE_FORMULA.get(self.type)
        self.notes = ScaleBuilder.build(
            root=self.root, formula=self.formula, use_flats=use_flats
        )
