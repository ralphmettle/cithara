from cithara.core.interval import Interval


# Mapping of natural notes to their semitone distance from C to be used as tokens
NATURAL_PITCHES: dict[str, int] = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
}

# Reverse mapping of prior dict for O(1) lookup by pitch
PITCH_TO_NATURAL: dict[int, str] = {v: k for k, v in NATURAL_PITCHES.items()}


class Note:
    def __init__(self, note_name: str) -> None:
        if not note_name:
            raise ValueError("Note string cannot be empty.")
        self._validate_note_string(note_name)
        self.note_name: str = note_name
        self.natural: str = note_name[0]
        self.pitch_class: int = self._get_pitch_class()
        self.enharmonics: list[str] = self._get_enharmonic_equivalents()
        self.canonical_name: str = self._canonise()

    def _validate_note_string(self, note_name: str) -> None:
        _valid_accidentals: tuple[str, str] = ("#", "b")
        if len(note_name) > 1:
            for acc in note_name[1:].lower():
                if acc not in _valid_accidentals:
                    raise ValueError(f"Invalid accidental in '{note_name}': {acc}")
        if note_name[0] not in NATURAL_PITCHES:
            raise ValueError(f"Invalid note name: {note_name[0]}")

    def _get_pitch_class(self) -> int:
        def calculate_accidentals(note_name: str) -> int:
            val: int = 0
            for acc in note_name[1:].lower():
                if acc == "#":
                    val += 1
                else:
                    val -= 1
            return val

        base_pitch: int = NATURAL_PITCHES.get(self.note_name[0])
        accidental_shift: int = calculate_accidentals(self.note_name)

        return (base_pitch + accidental_shift) % 12

    def _get_enharmonic_equivalents(self) -> list[str]:
        # Take the pitch class of the note, and find natural pitches within 2 semitones that can be altered to reach
        enharmonics: list[str] = []
        for pitch in NATURAL_PITCHES:
            diff = NATURAL_PITCHES[pitch] - self.pitch_class
            if NATURAL_PITCHES[pitch] < self.pitch_class and abs(diff) <= 2:
                new_note: str = pitch + ("#" * abs(diff))
                enharmonics.append(new_note)
            if NATURAL_PITCHES[pitch] > self.pitch_class and diff <= 2:
                new_note: str = pitch + ("b" * diff)
                enharmonics.append(new_note)
        return enharmonics

    def _canonise(self, use_flats: bool = False) -> str:
        return note_name_from_pitch_class(self.pitch_class, use_flats)

    def __eq__(self, other: "Note") -> bool:
        if isinstance(other, Note):
            return self.pitch_class == other.pitch_class
        return NotImplemented

    def __str__(self) -> str:
        return f"{self.note_name}"

    def __repr__(self) -> str:
        return f"<Note: '{self.note_name}'> (pitch class: {self.pitch_class})"


class PitchTransformer:
    @staticmethod
    def name_from_pitch(pitch_class: int) -> str:
        for note, pitch in NATURAL_PITCHES.items():
            if pitch_class == pitch:
                return note + "#"

    @staticmethod
    def sharpen(canonise: bool = True, use_flats: bool = False):
        return

    @staticmethod
    def flatten(canonise: bool = True, use_flats: bool = False):
        return


class NoteGenerator:
    @staticmethod
    def from_pitch_class(pitch_class: int, use_flats: bool = False) -> Note:
        return Note(note_name_from_pitch_class(pitch_class, use_flats))

    @staticmethod
    def from_interval(root: Note, interval: Interval, use_flats: bool = False) -> Note:
        target_pitch = (root.pitch_class + interval.semitones) % 12
        return NoteGenerator.from_pitch_class(target_pitch, use_flats)


# Likely needs a lot of work
def note_name_from_pitch_class(pitch_class: int, use_flats: bool = False):
    if pitch_class in PITCH_TO_NATURAL:
        return PITCH_TO_NATURAL[pitch_class]

    if use_flats:
        target = (pitch_class + 1) % 12
        if target in PITCH_TO_NATURAL:
            return PITCH_TO_NATURAL[target] + "b"
    else:
        target = (pitch_class - 1) % 12
        if target in PITCH_TO_NATURAL:
            return PITCH_TO_NATURAL[target] + "#"

    # If for some reason it fails to enter the conditionals (?)
    raise ValueError(f"Invalid input: {pitch_class}")
