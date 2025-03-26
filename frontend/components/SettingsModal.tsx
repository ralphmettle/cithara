import React from "react";

import DestructiveButton from "./DestructiveButton";
import ModalButton from "./ModalButton";

import { BiSolidPalette } from "react-icons/bi";
import { FaTrashAlt } from "react-icons/fa";
import { VscSettings } from "react-icons/vsc";

export default function SettingsModal() {
  return (
    <div className="flex flex-col justify-center items-center w-full h-full gap-6 mt-6 select-none cursor-default">
      <h1 className="flex font-funnel-display items-center justify-center font-bold w-full text-center gap-2 text-4xl bg-cithara-button border border-cithara-border-inner ring-cithara-border-outer ring-1 shadow-md py-6 rounded-xl">
        <VscSettings className="w-10 h-10" />
        Settings
      </h1>
      <div className="flex justify-center items-center rounded-xl p-6 w-full bg-cithara-button border border-cithara-border-inner ring-cithara-border-outer ring-1 shadow-md">
        <ul className="flex w-full items-center flex-col gap-4">
          {Array.from({ length: 5 }).map((_, index) => (
            <li
              key={index}
              className="text-center py-3 w-full rounded-md hover:bg-cithara-bg/50 cursor-pointer select-none transition-all"
            >
              SettingPlaceholder{index + 1}
            </li>
          ))}
        </ul>
      </div>
      <div className="flex row w-full justify-between">
        <DestructiveButton
          icon={<FaTrashAlt className="w-5 h-5" />}
          label="Clear Cache"
        />
        <ModalButton
          icon={<BiSolidPalette className="w-6 h-6" />}
          label="Themes"
        />
      </div>
    </div>
  );
}
