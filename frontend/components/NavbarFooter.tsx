import React from "react";
import Button from "./Button";
import { FaGithub } from "react-icons/fa";
import { FaUser } from "react-icons/fa6";
import { IoChevronBackOutline } from "react-icons/io5";
import { VscSettings } from "react-icons/vsc";

export default function NavbarFooter() {
  return (
    <div className="flex flex-row items-center justify-between w-full">
      <Button icon={<FaGithub className="w-6 h-6" />} link="https://www.github.com/ralphmettle/cithara" />
      <Button icon={<FaUser className="w-4 h-4 mr-3" />} label="Account" />
      <Button icon={<VscSettings className="w-6 h-6" />} />
    </div>
  );
}
