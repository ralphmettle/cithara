"use client";

import { useState } from "react";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const notes = [
  { value: "C", label: "C", hasAlternative: false },
  {
    value: "C#/Db",
    label: "C#/Db",
    hasAlternative: true,
    sharp: "C#",
    flat: "Db",
  },
  { value: "D", label: "D", hasAlternative: false },
  {
    value: "D#/Eb",
    label: "D#/Eb",
    hasAlternative: true,
    sharp: "D#",
    flat: "Eb",
  },
  { value: "E", label: "E", hasAlternative: false },
  { value: "F", label: "F", hasAlternative: false },
  {
    value: "F#/Gb",
    label: "F#/Gb",
    hasAlternative: true,
    sharp: "F#",
    flat: "Gb",
  },
  { value: "G", label: "G", hasAlternative: false },
  {
    value: "G#/Ab",
    label: "G#/Ab",
    hasAlternative: true,
    sharp: "G#",
    flat: "Ab",
  },
  { value: "A", label: "A", hasAlternative: false },
  {
    value: "A#/Bb",
    label: "A#/Bb",
    hasAlternative: true,
    sharp: "A#",
    flat: "Bb",
  },
  { value: "B", label: "B", hasAlternative: false },
];

const scaleTypes = [
  { value: "major", label: "Major" },
  { value: "minor", label: "Minor" },
  { value: "diminished", label: "Diminished" },
  { value: "augmented", label: "Augmented" },
];

export default function MusicSelector() {
  const [selectedNote, setSelectedNote] = useState<string>("");
  const [selectedAccidental, setSelectedAccidental] = useState<string>("");
  const [selectedScale, setSelectedScale] = useState<string>("");

  const selectedNoteData = notes.find((note) => note.value === selectedNote);
  const isAccidentalEnabled = selectedNoteData?.hasAlternative || false;

  const handleNoteChange = (value: string) => {
    setSelectedNote(value);
    // Reset accidental selection when note changes
    setSelectedAccidental("");
  };

  return (
    <div className="w-full mx-auto">
      <div className="flex border rounded-md overflow-hidden">
        {/* Note Selection */}
        <Select value={selectedNote} onValueChange={handleNoteChange}>
          <SelectTrigger className="flex border-0 border-r rounded-none hover:bg-muted/50 active:bg-muted/70 transition-colors duration-150">
            <SelectValue placeholder="Root Note" />
          </SelectTrigger>
          <SelectContent className="flex items-center">
            {notes.map((note) => (
              <SelectItem key={note.value} value={note.value}>
                {note.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>

        {/* Accidental Preference - Only show when needed */}
        {isAccidentalEnabled && (
          <Select
            value={selectedAccidental}
            onValueChange={setSelectedAccidental}
          >
            <SelectTrigger className="flex border-0 border-r rounded-none hover:bg-muted/50 active:bg-muted/70 transition-colors duration-150">
              <SelectValue placeholder="#/b" />
            </SelectTrigger>
            <SelectContent className="flex items-center">
              <SelectItem className="" value="sharp">
                Sharp ({selectedNoteData?.sharp})
              </SelectItem>
              <SelectItem className="" value="flat">
                Flat ({selectedNoteData?.flat})
              </SelectItem>
            </SelectContent>
          </Select>
        )}

        {/* Scale/Chord Type */}
        <Select value={selectedScale} onValueChange={setSelectedScale}>
          <SelectTrigger className="flex-1 border-0 rounded-none hover:bg-muted/50 active:bg-muted/70 transition-colors duration-150">
            <SelectValue placeholder="Chord Type" />
          </SelectTrigger>
          <SelectContent>
            {scaleTypes.map((scale) => (
              <SelectItem key={scale.value} value={scale.value}>
                {scale.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}
