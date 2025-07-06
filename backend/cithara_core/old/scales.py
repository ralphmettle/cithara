from intervals import Interval, IntervalDefinition, Transposer
from notes import Note


class Scale:
    """
    Represents a musical scale with a root note and scale type.
    Generates properly spelled scale notes with correct accidentals.
    """

    SCALE_PATTERNS = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "natural_minor": [0, 2, 3, 5, 7, 8, 10],
        "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
        "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
    }

    NOTE_SEQUENCE = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "D": ["D", "E", "F", "G", "A", "B", "C"],
        "E": ["E", "F", "G", "A", "B", "C", "D"],
        "F": ["F", "G", "A", "B", "C", "D", "E"],
        "G": ["G", "A", "B", "C", "D", "E", "F"],
        "A": ["A", "B", "C", "D", "E", "F", "G"],
        "B": ["B", "C", "D", "E", "F", "G", "A"],
    }

    def __init__(self, root: Note, scale_type: str = "major"):
        """
        Initialize a new scale.

        Args:
            root (Note): The root note of the scale
            scale_type (str): The type of scale (major, natural_minor, etc.)
        """

        if scale_type not in self.SCALE_PATTERNS:
            raise ValueError(
                f'Invalid scale type. Supported types: {", ".join(self.SCALE_PATTERNS.keys())}'
            )

        self.root = root
        self.scale_type = scale_type
        self.notes = self._generate_notes()

    def _get_note_sequence(self) -> list[str]:
        """Get the sequence of note names starting from the root note."""
        base_note = self.root.note
        return self.NOTE_SEQUENCE[base_note]

    def _calculate_accidental(self, target_index: int, base_note: str) -> int:
        """
        Calculate the required accidental count to reach the target index from a base note.
        Positive numbers represent sharps, negative numbers represent flats.
        """
        base_note_obj = Note(base_note)
        base_index = base_note_obj.pitch_class
        raw_diff = (target_index - base_index) % 12

        if raw_diff > 6:
            return -(12 - raw_diff)  # Use flats
        elif raw_diff <= 6:
            return raw_diff  # Use sharps
        return 0

    def _generate_notes(self) -> list[Note]:
        """Generate the scale notes with proper spelling."""
        notes = []
        note_sequence = self._get_note_sequence()
        intervals = self.SCALE_PATTERNS[self.scale_type]

        for i, interval in enumerate(intervals):
            target_index = (self.root.pitch_class + interval) % 12

            if i == 0:
                notes.append(self.root)
            else:
                base_note = note_sequence[i]
                accidental = self._calculate_accidental(target_index, base_note)
                notes.append(Note(base_note, accidental))

        return notes

    def contains_note(self, note: Note) -> bool:
        """Check if a note is in the scale."""
        return any(
            scale_note.pitch_class == note.pitch_class for scale_note in self.notes
        )

    def get_scale_degree(self, note: Note) -> int:
        """Get the scale degree (1-7) of a note, or -1 if not in scale."""
        for i, scale_note in enumerate(self.notes, 1):
            if scale_note.pitch_class == note.pitch_class:
                return i
        return -1

    def get_note(self, index: int) -> Note:
        """Get the note at a specific scale degree (0-6)."""
        if 0 <= index <= 6:
            return self.notes[index]
        raise ValueError(f"Index out of range. Must be a value between 0-6.")

    def __str__(self):
        return f"{self.root} {self.scale_type.replace('_', ' ').title()} Scale: {' '.join(note.name() for note in self.notes)}"

    def __repr__(self):
        return f"<Scale: {self}>"
