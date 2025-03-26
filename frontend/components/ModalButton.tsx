"use client";

import React, { useState } from "react";
import Button from "./Button";
import { IoClose } from "react-icons/io5";

export default function ModalButton({
  children,
  icon,
  label,
}: {
  children?: React.ReactNode;
  icon?: React.ReactNode;
  label?: string;
}) {
  const [isOpen, setIsOpen] = useState(false);
  const toggleModal = () => setIsOpen((prev) => !prev);

  return (
    <>
      <ModalButtonInner onClick={toggleModal} icon={icon} label={label} />
      {isOpen && children && (
        <ModalDisplay onClose={toggleModal}>{children}</ModalDisplay>
      )}
    </>
  );
}

function ModalButtonInner({
  onClick,
  icon,
  label,
}: {
  onClick: () => void;
  icon?: React.ReactNode;
  label?: string;
}) {
  return (
    <div
      onClick={onClick}
      className="flex w-fit h-fit items-center justify-center p-2 bg-cithara-button hover:bg-cithara-border-inner rounded-lg border border-cithara-border-inner ring-cithara-border-outer ring-1 hover:border-white/20 shadow-md select-none cursor-pointer transition-all"
    >
      {(icon || label) && <ModalButtonLabel icon={icon} label={label} />}
    </div>
  );
}

function ModalButtonLabel({
  icon,
  label,
}: {
  icon?: React.ReactNode;
  label?: string;
}) {
  return (
    <>
      {icon && <span className="">{icon}</span>}
      {label && <span className="">{label}</span>}
    </>
  );
}

function ModalDisplay({
  children,
  onClose,
}: {
  children: React.ReactNode;
  onClose: () => void;
}) {
  return (
    <div
      onClick={onClose}
      className="fixed flex items-center justify-center inset-0 bg-cithara-bg/80 backdrop-blur-md w-full h-full"
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className="relative flex flex-col p-10 items-center justify-center w-md bg-cithara-panel border border-cithara-panel-border shadow-2xl rounded-2xl"
      >
        <div className="absolute top-4 left-4">
          <Button onClick={onClose} icon={<IoClose className="w-5 h-5"/>} />
        </div>
        {children}
      </div>
    </div>
  );
}
