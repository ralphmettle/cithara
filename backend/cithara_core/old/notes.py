_PITCH_CLASSES = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


class Note:
    """
    Represents a musical note, including its base note name (e.g., "C") and any accidentals
    (positive for sharps, negative for flats). Provides methods to calculate properties like
    normalized pitch, generate enharmonic equivalents, and display note names.

    Attributes:
        `note (str)`: Base note name (must be one of "C", "D", "E", ...) without any accidentals.
        `accidentals (int)`: Number of accidentals applied (positive = sharps, negative = flats).

    Methods:
        `name() -> str`:
            Returns the note's name.
        `enharmonic_equivalents() -> list[str]`:
            Generates a list of valid enharmonic equivalents.
        `__eq__(other: Note) -> bool`:
            Compares two notes for equality based on normalized pitch.
    """

    SEMITONES_PER_OCTAVE = 12

    def __init__(self, note: str, accidentals: int = 0):
        """
        Initializes a new Note object.

        Args:
            `note (str)`: Base note name (e.g., "C", "D", "E").
            `accidentals (int, optional)`: Accidentals to apply (default is 0).

        Raises:
            ValueError: If the note is invalid.
        """
        note = note.upper()
        if note not in _PITCH_CLASSES:
            raise ValueError(f"Invalid note: {note}")

        self.note = note
        self.accidentals = accidentals
        self.base_pitch = _PITCH_CLASSES[self.note]

    @property
    def pitch_class(self) -> int:
        """Calculates the normalized pitch class of the note."""
        return (self.base_pitch + self.accidentals) % self.SEMITONES_PER_OCTAVE

    def name(self) -> str:
        """Returns the note's name, including accidentals."""
        accidental_symbol = (
            "#" * self.accidentals
            if self.accidentals > 0
            else "b" * abs(self.accidentals)
        )
        return f"{self.note}{accidental_symbol}"

    @classmethod
    def from_pitch_class(cls, pitch_class: int, prefer_flat: bool = False) -> "Note":
        """Creates a Note object from a pitch class value (0-11)."""
        closest_note = None
        smallest_accidentals = float("inf")

        for base_name, base_pitch in _PITCH_CLASSES.items():
            accidentals = (pitch_class - base_pitch) % cls.SEMITONES_PER_OCTAVE

            if prefer_flat and accidentals > 0:
                accidentals -= cls.SEMITONES_PER_OCTAVE
            elif not prefer_flat and accidentals > 6:
                accidentals -= cls.SEMITONES_PER_OCTAVE

            if abs(accidentals) <= 2:
                candidate = cls(base_name, accidentals)
                if abs(accidentals) < smallest_accidentals:
                    closest_note = candidate
                    smallest_accidentals = abs(accidentals)

        if closest_note:
            return closest_note
        raise ValueError(f"No valid note found for pitch class {pitch_class}")

    @property
    def enharmonic_equivalents(self) -> list[str]:
        """
        Generates a list of valid enharmonic equivalents for the `Note`.
        Only includes equivalents that can be represented with accidentals of at most ±1 (e.g., "C#", "Db").
        """
        equivalents = []

        # Iterate over all possible base notes
        for base_note, base_pitch in _PITCH_CLASSES.items():
            # Calculate the accidentals required to match the current pitch
            accidental_shift = (self.pitch_class - base_pitch) % 12

            # Normalize accidental_shift to the range [-11, 11]
            if accidental_shift > 6:  # Prefer flats when ambiguous
                accidental_shift -= 12

            # Add to equivalents only if accidental shift is valid (-1, 0, +1)
            if abs(accidental_shift) <= 1:
                equivalents.append(Note(base_note, accidental_shift))

        return equivalents

    def __str__(self):
        """Returns the note's name as a string."""
        return self.name()

    def __repr__(self):
        """Returns a detailed string representation for debugging."""
        return f"<Note: {self.name()}>"

    def __eq__(self, other):
        """Compares two notes for equality based on their pitch class."""
        return self.pitch_class == other.pitch_class


class PitchTransform:
    """
    Provides methods for transforming `Note` objects by altering their pitch.
    Methods return new `Note` objects with the transformed pitch.

    Methods:
        - `sharpen(note: Note) -> Note`:
            Increases to the next natural `Note`.
        - `flatten(note: Note) -> Note`:
            Decreases to the previous natural `Note`.
        - `augment(note: Note) -> Note`:
            Adds a sharp to the current `Note` object.
        - `diminish(note: Note) -> Note`:
            Adds a flat to the current `Note` object.
    """

    @staticmethod
    def sharpen(note: Note) -> Note:
        """Increases to the next natural `Note`."""
        new_pitch_class = (note.pitch_class + 1) % Note.SEMITONES_PER_OCTAVE
        return Note.from_pitch_class(new_pitch_class)

    @staticmethod
    def flatten(note: Note) -> Note:
        """Decreases to the previous natural `Note`."""
        new_pitch_class = (note.pitch_class - 1) % Note.SEMITONES_PER_OCTAVE
        return Note.from_pitch_class(new_pitch_class)

    @staticmethod
    def augment(note: Note) -> Note:
        """Adds a sharp to the current `Note` object."""
        return Note(note.note, note.accidentals + 1)

    @staticmethod
    def diminish(note: Note) -> Note:
        """Adds a flat to the current `Note` object."""
        return Note(note.note, note.accidentals - 1)
