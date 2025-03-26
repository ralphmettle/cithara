import React from "react";
import Button from "./Button";

export default function SettingsModal() {
  return (
    <div className="flex absolute z-1000 justify-center items-center w-full h-full">
      <div className="flex items-center justify-center bg-cithara-bg/30 w-full h-full backdrop-blur-md">
        <div className="flex flex-col p-10 items-center justify-center w-md bg-cithara-panel border border-cithara-panel-border shadow-2xl rounded-2xl">
          SettingsModal
          <Button label="test" />
        </div>
      </div>
    </div>
  );
}
