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


class Note:
    def __init__(self, note_string: str) -> None:
        if not note_string:
            raise ValueError("Note string cannot be empty.")
        self._validate_note_string(note_string)
        self.note_string: str = note_string
        self.natural: str = note_string[0]
        self.pitch_class: int = self._get_pitch_class()
        self.enharmonics: list[str] = self._get_enharmonic_equivalents()
        self.canonical_name: str = self._canonise()

    def _validate_note_string(self, note_string: str) -> None:
        _valid_accidentals: tuple[str, str] = ("#", "b")
        if len(note_string) > 1:
            for acc in note_string[1:].lower():
                if acc not in _valid_accidentals:
                    raise ValueError(f"Invalid accidental in '{note_string}': {acc}")
        if note_string[0] not in NATURAL_PITCHES:
            raise ValueError(f"Invalid note name: {note_string[0]}")

    def _get_pitch_class(self) -> int:
        def calculate_accidentals(note_string: str) -> int:
            val: int = 0
            for acc in note_string[1:].lower():
                if acc == "#":
                    val += 1
                else:
                    val -= 1
            return val

        base_pitch: int = NATURAL_PITCHES.get(self.note_string[0])
        accidental_shift: int = calculate_accidentals(self.note_string)

        return (base_pitch + accidental_shift) % 12

    def _get_enharmonic_equivalents(self) -> list[str]:
        # Take the pitch class of the note, and find natural pitches within reasonable range that can be altered to reach
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
        if self.pitch_class in NATURAL_PITCHES.values():
            # return PitchTransformer.name_from_pitch(self.pitch_class)
            pass
        
        if self.note_string in NATURAL_PITCHES:
            return self.note_string
        
        if use_flats and self.pitch_class + 1 in NATURAL_PITCHES.values():
            for note, pitch in NATURAL_PITCHES.items():
                if self.pitch_class + 1 == pitch:
                    return note + "b"
        elif not use_flats and self.pitch_class - 1 in NATURAL_PITCHES.values():
            for note, pitch in NATURAL_PITCHES.items():
                if self.pitch_class - 1 == pitch:
                    return note + "#"
        # If for some reason it fails to enter the conditionals (?)
        return self.note_string

        
    def __eq__(self, other: "Note") -> bool:
        if isinstance(other, Note):
            return self.pitch_class == other.pitch_class
        return NotImplemented
    
    def __str__(self) -> str:
        return f"{self.note_string}"

    def __repr__(self) -> str:
        return f"<Note: '{self.note_string}'> (pitch class: {self.pitch_class})"

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
        return
