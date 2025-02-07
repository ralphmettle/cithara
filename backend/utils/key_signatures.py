from notes import Note, FIFTHS

MAJOR = {
    note: num
    for num, note in enumerate(
        [f"{note}b" for note in FIFTHS[1::]]
        + FIFTHS
        + [f"{note}#" for note in FIFTHS[0:2]],
        start=-7,
    )
}

MINOR = {
    note: num
    for num, note in enumerate(
        [f"{note}b" for note in FIFTHS[-3:]]
        + FIFTHS
        + [f"{note}#" for note in FIFTHS[:5]],
        start=-7,
    )
}


class KeySignature:
    def __init__(self, tonic: Note, tonality: str = "major"):
        if isinstance(tonic, Note):
            self.tonic = tonic
        elif isinstance(key, str):
            self.tonic = Note(tonic)
        else:
            raise ValueError("Key must be a Note object or string.")

        if tonality not in ["major", "minor"]:
            raise ValueError(
                f"Invalid tonality: {
                             tonality}. Valid tonalities are 'major' and 'minor'."
            )

        self.tonality = tonality

        # Define which dictionary to check based on tonality
        if self.tonality == "major" and self.tonic.normalise().note_string not in MAJOR:
            raise ValueError(
                f"Invalid key signature: {
                             self.tonic.note_string}"
            )
        elif (
            self.tonality == "minor" and self.tonic.normalise().note_string not in MINOR
        ):
            raise ValueError(
                f"Invalid key signature: {
                             self.tonic.note_string}"
            )

        self.key_dict = MAJOR if tonality == "major" else MINOR

        # Check if the normalised tonic is in the circle of fifths
        if self.tonic.note_string not in self.key_dict:
            normalised_note = self.tonic.normalise(False)
            if normalised_note.note_string in self.key_dict:
                self.tonic = normalised_note
            else:
                normalised_flat = self.tonic.normalise(True)
                if normalised_flat.note_string in self.key_dict:
                    self.tonic = normalised_flat
                else:
                    raise ValueError(
                        f"Invalid key signature: {
                                     self.tonic.note_string}"
                    )

    @property
    def accidentals(self) -> int:
        return self.key_dict.get(self.tonic.note_string)

    @property
    def altered_notes(self) -> list[str]:
        notes_list = []
        accidental = "#" if self.accidentals > 0 else "b"
        fifths_list = FIFTHS if self.accidentals > 0 else list(reversed(FIFTHS))

        for i in range(abs(self.accidentals)):
            notes_list.append(fifths_list[i] + accidental)

        return notes_list

    @property
    def notes(self) -> list[str]:
        notes_list = self.altered_notes
        fifths_list = FIFTHS if self.accidentals > 0 else list(reversed(FIFTHS))

        for i in range(abs(self.accidentals), len(fifths_list)):
            notes_list.append(fifths_list[i])

        return notes_list

    def relative(self, tonality: str = "minor") -> str:
        if tonality == "minor":
            return [k for k, v in MINOR.items() if v == self.accidentals][0]
        elif tonality == "major":
            return [k for k, v in MAJOR.items() if v == self.accidentals][0]
        else:
            raise ValueError(f"Not a valid relative tonality: {tonality}")
