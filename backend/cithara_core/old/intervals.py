from notes import Note


class Interval:
    """
    Represents the musical distance between two notes.
    Handles interval identification, creation, and manipulation.
    """

    def __init__(self, start_note: Note, end_note: Note = None, semitones: int = None):
        """
        Initialize an interval. If only start_note is provided, creates a Perfect Unison.

        Args:
            `start_note` (Note): The starting note.
            `end_note` (Note, optional): The ending note.
            `semitones` (int, optional): Number of semitones for the interval.
            Semitones greater than 12 will wrap around to their value mod 12 (e.g. 13 -> 1).
        """
        self.start_note = start_note
        if end_note and semitones is not None:
            raise ValueError("Provide either `end_note` or `semitones`, not both.")
        elif end_note:
            self.end_note = end_note
            self.semitones = self._calculate_semitones()
        elif semitones is not None:
            self.semitones = semitones % 12
            self.end_note = self._calculate_end_note()
        else:
            self.semitones = 0
            self.end_note = start_note

    def _calculate_semitones(self) -> int:
        """Calculate semitones between start and end notes using pitch class."""
        return (self.end_note.pitch_class - self.start_note.pitch_class) % 12

    def _calculate_end_note(self) -> Note:
        """Calculate the end note based on semitones from the start note."""
        return Transposer.transpose(self.start_note, self.semitones)

    def invert(self) -> "Interval":
        """Get the inverted interval (e.g. Perfect Fifth -> Perfect Fourth)."""
        return Interval(self.start_note, semitones=(12 - self.semitones) % 12)

    @property
    def name(self) -> str:
        """Provides the name of the current Interval based on semitones."""
        if self.semitones == 12:
            return IntervalDefinition.INTERVAL_NAMES.get(self.semitones)
        return IntervalDefinition.INTERVAL_NAMES.get(
            self.semitones % 12, "Unknown interval."
        )

    def __str__(self):
        return f"{self.start_note} -> {self.end_note} : {self.name} ({self.semitones} semitones)"

    def __repr__(self):
        return f"<Interval: {self.start_note} to {self.end_note} ({self.name})>"


class IntervalDefinition:
    INTERVAL_NAMES = {
        0: "Perfect Unison",
        1: "Minor Second",
        2: "Major Second",
        3: "Minor Third",
        4: "Major Third",
        5: "Perfect Fourth",
        6: "Tritone",
        7: "Perfect Fifth",
        8: "Minor Sixth",
        9: "Major Sixth",
        10: "Minor Seventh",
        11: "Major Seventh",
    }

    @classmethod
    def interval_names(cls) -> list:
        """Returns a list of interval names for reference."""
        return list(cls.INTERVAL_NAMES.values())

    @classmethod
    def from_name(
        cls, start_note: Note, interval_name: str, prefer_flat: bool = False
    ) -> "Interval":
        """
        Create an Interval from a start_note and interval name.

        Args:
            start_note (Note): The starting note
            interval_name (str): Name of the interval
            prefer_flats (bool): If True, uses flats instead of sharps for accidentals
        """
        for semitones, name in cls.INTERVAL_NAMES.items():
            if name.lower() == interval_name.lower():
                target_index = (start_note.pitch_class + semitones) % 12
                end_note = Note.from_pitch_class(target_index, prefer_flat=prefer_flat)
                return Interval(start_note, end_note)

        raise ValueError(f"Unknown interval name: {interval_name}")


class Transposer:
    @staticmethod
    def transpose(note: Note, semitones: int) -> Note:
        """Transpose a note by a specified number of semitones."""
        target_index = (note.pitch_class + semitones) % 12
        return Note.from_pitch_class(target_index)

    @staticmethod
    def transpose_by_interval(note: Note, interval: Interval) -> Note:
        """Transpose a note by the interval's semitone count."""
        return Transposer.transpose(note, interval.semitones)


class IntervalQuality:
    PERFECT_INTERVALS = [0, 5, 7]
    MAJOR_INTERVALS = [2, 4, 9, 11]
    MINOR_INTERVALS = [1, 3, 8, 10]

    @staticmethod
    def is_perfect(interval: Interval) -> bool:
        """Check if an `Interval's` semitone count corresponds to a perfect interval."""
        return interval.semitones % 12 in IntervalQuality.PERFECT_INTERVALS

    @staticmethod
    def is_major(interval: Interval) -> bool:
        """Check if an `Interval's` semitone count corresponds to a major interval."""
        return interval.semitones % 12 in IntervalQuality.MAJOR_INTERVALS

    @staticmethod
    def is_minor(interval: Interval) -> bool:
        """Check if an `Interval's` semitone count corresponds to a minor interval."""
        return interval.semitones % 12 in IntervalQuality.MINOR_INTERVALS
