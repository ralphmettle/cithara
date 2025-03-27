import React from "react";
import Button from "./Button";
import ModalButton from "./ModalButton";
import SettingsModal from "./SettingsModal";
import { FaGithub } from "react-icons/fa";
import { FaUser } from "react-icons/fa6";
import { VscSettings } from "react-icons/vsc";

export default function NavbarFooter() {
  return (
    <div className="flex flex-row items-center justify-between w-full">
      <Button
        icon={<FaGithub className="w-6 h-6" />}
        externalLink="https://www.github.com/ralphmettle/cithara"
      />
      <ModalButton icon={<FaUser className="w-4 h-4" />} label="Account">
        Account Modal
      </ModalButton>
      <ModalButton icon={<VscSettings className="w-6 h-6" />}>
        <SettingsModal />
      </ModalButton>
    </div>
  );
}
