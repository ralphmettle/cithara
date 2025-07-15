"use client";

import { useState, useEffect } from "react";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const notes = [
  { value: "C", label: "C", hasAlternative: false, use_flats: false },
  {
    value: "C#/Db",
    label: "C#/Db",
    hasAlternative: true,
    sharp: "C#",
    flat: "Db",
    use_flats: true,
  },
  { value: "D", label: "D", hasAlternative: false, use_flats: false },
  {
    value: "D#/Eb",
    label: "D#/Eb",
    hasAlternative: true,
    sharp: "D#",
    flat: "Eb",
    use_flats: true,
  },
  { value: "E", label: "E", hasAlternative: false, use_flats: false },
  { value: "F", label: "F", hasAlternative: false, use_flats: true },
  {
    value: "F#/Gb",
    label: "F#/Gb",
    hasAlternative: true,
    sharp: "F#",
    flat: "Gb",
    use_flats: true,
  },
  { value: "G", label: "G", hasAlternative: false, use_flats: false },
  {
    value: "G#/Ab",
    label: "G#/Ab",
    hasAlternative: true,
    sharp: "G#",
    flat: "Ab",
    use_flats: true,
  },
  { value: "A", label: "A", hasAlternative: false, use_flats: false },
  {
    value: "A#/Bb",
    label: "A#/Bb",
    hasAlternative: true,
    sharp: "A#",
    flat: "Bb",
    use_flats: true,
  },
  { value: "B", label: "B", hasAlternative: false, use_flats: false },
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
  const [scaleResult, setScaleResult] = useState<string[]>([]);

  const selectedNoteData = notes.find((note) => note.value === selectedNote);
  const isAccidentalEnabled = selectedNoteData?.hasAlternative || false;

  const handleNoteChange = (value: string) => {
    setSelectedNote(value);
    setSelectedAccidental("");
  };

  useEffect(() => {
    if (!selectedNote || !selectedScale) return;

    const useFlats = selectedNoteData?.use_flats ? "true" : "false";

    const params = new URLSearchParams({
      note: selectedNoteData?.sharp || selectedNote,
      type: selectedScale,
      use_flats: useFlats,
    });

    fetch(`http://localhost:8000/api/get_scale/?${params.toString()}`)
      .then((res) => res.json())
      .then((data) => {
        setScaleResult(data.scale || []);
      })
      .catch((err) => {
        console.error("Failed to fetch scale:", err);
        setScaleResult([]);
      });
  }, [selectedNote, selectedAccidental, selectedScale]);

  return (
    <div className="w-full mx-auto space-y-6">
      <div className="bg-background/75 backdrop-blur-md flex border rounded-md overflow-hidden">
        <Select value={selectedNote} onValueChange={handleNoteChange}>
          <SelectTrigger className="flex border-0 border-r rounded-none hover:bg-muted/50 active:bg-muted/70 transition-colors duration-150">
            <SelectValue placeholder="Root Note" />
          </SelectTrigger>
          <SelectContent>
            {notes.map((note) => (
              <SelectItem key={note.value} value={note.value}>
                {note.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>

        {isAccidentalEnabled && (
          <Select
            value={selectedAccidental}
            onValueChange={setSelectedAccidental}
          >
            <SelectTrigger className="flex border-0 border-r rounded-none hover:bg-muted/50 active:bg-muted/70 transition-colors duration-150">
              <SelectValue placeholder="#/b" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="sharp">
                Sharp ({selectedNoteData?.sharp})
              </SelectItem>
              <SelectItem value="flat">
                Flat ({selectedNoteData?.flat})
              </SelectItem>
            </SelectContent>
          </Select>
        )}

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

      <div className="flex bg-neutral-200/65 dark:bg-muted/20 p-6 rounded-md min-h-[100px] border border-border items-center justify-center">
        {scaleResult.length > 0 ? (
          <div className="space-y-4">
            <h2 className="text-2xl sm:text-3xl font-bold text-center text-foreground ">
              {selectedNote} {selectedScale.charAt(0).toUpperCase() + selectedScale.slice(1)} Scale
            </h2>
            <div className="flex flex-wrap justify-center gap-4 items-end">
              {scaleResult.map((note, index) => {
                const romanNumerals = ["I", "II", "III", "IV", "V", "VI", "VII"];
                return (
                  <div key={index} className="flex flex-col items-center">
                    <span className="text-xs text-stone-400">{romanNumerals[index] || ""}</span>
                    <span className="px-3 py-2 bg-background dark:bg-background/30 text-primary font-medium rounded-md text-base border border-border hover:shadow-lg hover:brightness-150 transition-all select-none cursor-default">
                      {note}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
        ) : (
          <p className="text-muted-foreground text-sm">
            Select options to view a scale (this isn&apos;t working fully yet!)
          </p>
        )}
      </div>
    </div>
  );
}
