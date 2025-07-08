from cithara.core.note import Note, NoteGenerator
from cithara.core.interval import Interval
from cithara.core.scale.scale_degree import ScaleDegree

# Mapping of scale varieties to their interval patterns from the root
# NOTE: modes are handled internally by scales (hence "minor" not being included here)
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

        # 0-indexed method of getting a specifc scale degree
        @classmethod
        def get_degree(self, degree: int):
            # How do I want to represent the degree?
            # Should I allow for "extended degrees" i.e. mod(7) operation?
            # Do I expect the user to only pass in a number 1-7?
            pass


class ScaleBuilder:
    @staticmethod
    def build(
        root: Note, formula: list[int], use_flats: bool = False
    ) -> list[ScaleDegree]:
        scale = []
        degree = 0
        for interval in formula:
            if interval == 0:
                scale.append(
                    ScaleDegree(
                        note=root, root=root, degree=degree, interval=Interval(interval)
                    )
                )
            else:
                scale.append(
                    ScaleDegree(
                        note=NoteGenerator.from_interval(
                            root=root,
                            interval=Interval(interval),
                            use_flats=use_flats,
                        ),
                        root=root,
                        degree=degree,
                        interval=Interval(interval),
                    )
                )
            degree += 1

        return scale
