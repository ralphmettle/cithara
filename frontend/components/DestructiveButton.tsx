import Link from "next/link";
import React from "react";

export default function DestructiveButton({
  onClick,
  label,
  link,
  icon,
}: {
  onClick?: () => void;
  label?: string;
  link?: string;
  icon?: React.ReactNode;
}) {
  return link ? (
    <Link href={`${link}`} className="w-fit h-fit">
      <DestructiveButtonInner onClick={onClick} icon={icon} label={label} />
    </Link>
  ) : (
    <DestructiveButtonInner onClick={onClick} icon={icon} label={label} />
  );
}

function DestructiveButtonInner({
  onClick,
  icon,
  label,
}: {
  onClick?: () => void;
  icon?: React.ReactNode;
  label?: string;
}) {
  return (
    <div
      onClick={onClick}
      className="flex w-fit h-fit items-center justify-center p-2 gap-2 bg-red-600 hover:bg-red-500 rounded-lg border border-red-500 ring-red-800 ring-1 hover:border-red-400 shadow-md select-none cursor-pointer transition-all"
    >
      {(icon || label) && <DestructiveButtonLabel icon={icon} label={label} />}
    </div>
  );
}

function DestructiveButtonLabel({
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
