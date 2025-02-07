from intervals import Interval, Transposer
from notes import Note, PitchTransform
from scales import Scale


class Chord:
    """ """

    # Common chord structures as semitone intervals from the root
    CHORD_STRUCTURES = {
        "major": [0, 4, 7],
        "minor": [0, 3, 7],
        "diminished": [0, 3, 6],
        "augmented": [0, 4, 8],
        "major7": [0, 4, 7, 11],
        "minor7": [0, 3, 7, 10],
        "dominant7": [0, 4, 7, 10],
        "diminished7": [0, 3, 6, 9],
        "half_diminished7": [0, 3, 6, 10],
        "sus2": [0, 2, 7],
        "sus4": [0, 5, 7],
        "major6": [0, 4, 7, 9],
        "minor6": [0, 3, 7, 9],
    }

    def __init__(
        self,
        root: Note = None,
        scale: Scale = None,
        degree: int = None,
        type: str = "major",
    ):
        self.root_note = root
        self.scale = scale
        self.type = type
        self.degree = degree
        self.notes = self._generate_chords()

    @property
    def root(self):
        if self.scale:
            return self.scale.get_note(0)
        else:
            return self.root_note

    @property
    def intervals(self):
        return self.CHORD_STRUCTURES[self.type]

    def _generate_chords(self) -> list[Note]:
        if self.scale:
            return self._generate_from_scale()
        else:
            return self._generate_from_intervals()

    # def _generate_from_intervals(self) -> list[Note]:
    #     prefer_flat = self.type in ['minor', 'diminished', 'minor7', 'half_diminished7']
    #     return [
    #         Note.from_pitch_class(
    #             (self.root.pitch_class + interval) % Note.SEMITONES_PER_OCTAVE,
    #             prefer_flat
    #         ) for interval in self.intervals
    #     ]

    def _generate_from_intervals(self) -> list[Note]:
        prefer_flat = self.type in ["minor", "diminished", "minor7", "half_diminished7"]
        used_pitch_classes = set()

        chord_notes = []
        for interval in self.intervals:
            target_pitch_class = (
                self.root.pitch_class + interval
            ) % Note.SEMITONES_PER_OCTAVE
            print(f"\n{self.root=}")
            print(f"{target_pitch_class=}")

            # If the target pitch class is already used, adjust up or down
            while target_pitch_class in used_pitch_classes:
                target_pitch_class = (
                    target_pitch_class + 1
                ) % Note.SEMITONES_PER_OCTAVE

            note = Note.from_pitch_class(target_pitch_class, prefer_flat)
            used_pitch_classes.add(note.pitch_class)
            print(f"{used_pitch_classes=}")
            print(f"{note=}\n")
            chord_notes.append(note)

        return chord_notes

    def _generate_from_scale(self) -> list[Note]:
        """
        Generate a chord from the given scale and scale degree.
        Each interval in the chord structure is mapped to a unique note in the scale.
        """
        if self.degree is None or self.scale is None:
            raise ValueError(
                "Scale and degree must be provided to generate a chord from a scale."
            )

        chord_notes = []
        root_scale_note = self.scale.get_note(self.degree)
        for interval in self.intervals:
            # Calculate the target pitch class relative to the root scale note
            target_pitch_class = (root_scale_note.pitch_class + interval) % 12

            # Search for the correct note in the scale
            for i in range(len(self.scale.notes)):
                scale_note = self.scale.get_note(i)
                if scale_note.pitch_class == target_pitch_class:
                    chord_notes.append(scale_note)
                    break
            else:
                # If the target pitch class isn't in the scale, fallback to transposing diatonically
                chord_notes.append(Transposer.transpose(root_scale_note, interval - 1))

        return chord_notes

    @property
    def get_intervals(self) -> list[Interval]:
        """Get the intervals between the root and each note in the chord."""
        return [Interval(self.root, note) for note in self.notes[1:]]

    def __str__(self):
        return f"Root: {self.root} – {' '.join(str(note) for note in self.notes)}"

    def __repr__(self):
        return f"<Chord: {self}>"


test_note = Note("F", 1)
test_chord = Chord(test_note, type="major7")
print(repr(test_chord))
