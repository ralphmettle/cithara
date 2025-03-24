import React from "react";
import NavButton from "./NavButton";
import Link from "next/link";
import NavbarFooter from "./NavbarFooter";

import { TbPiano } from "react-icons/tb";

export default function Navbar() {
  return (
    <div className="flex flex-col grow items-center h-full w-xs p-4 mx-2 rounded-2xl bg-cithara-primary border border-cithara-border-light shadow-2xl z-10">
      <Link href="/" className="flex w-full items-center justify-center">
        <button className="flex gap-2 font-extrabold font-funnel-display text-4xl justify-center items-center text-center select-none cursor-pointer transition-all border border-cithara-border-light ring-cithara-bg ring-1 hover:bg-cithara-border-light hover:border-white/20 shadow-md p-4 py-6 w-full h-full rounded-xl">
          <TbPiano className="w-10 h-10"/>
          <h1>Cithara</h1>
        </button>
      </Link>
      <div className="flex flex-col h-full gap-3 p-4 w-full my-6 rounded-xl shadow-md border border-cithara-border-light ring-cithara-bg ring-1 ">
        <NavButton label="Chord List" link="chords" />
        <NavButton label="Notes" link="#" />
        <NavButton label="Favourites" link="#" />
        <NavButton label="Repository" link="#" />
      </div>
      <div className="flex items-end w-full">
        <NavbarFooter />
      </div>
    </div>
  );
}
