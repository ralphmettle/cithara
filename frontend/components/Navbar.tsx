import React from "react";
import NavButton from "./NavButton";
import Link from "next/link";

export default function Navbar() {
  return (
    <div className="flex flex-col items-center h-screen w-xs p-2 m-2 px-4 mx-4 rounded-xl bg-cithara-primary border border-[#e96354] shadow-lg">
      <Link href="/">
        <h1 className="font-extrabold font-funnel-display m-4 text-5xl text-left hover:text-cithara-bg select-none cursor-pointer transition-all">
          Cithara
        </h1>
      </Link>
      <div className="pt-4 p-2 place-self-start w-full">
        <NavButton label="Chord List" link="chords" />
        <NavButton label="Notes" link="" />
        <NavButton label="Favourites" link="" />
        <NavButton label="Repository" link="" />
      </div>
    </div>
  );
}
