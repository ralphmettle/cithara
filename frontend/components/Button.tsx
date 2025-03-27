import Link from "next/Link";
import React from "react";

export default function Button({
  onClick,
  label,
  externalLink,
  internalLink,
  icon,
}: {
  onClick?: () => void;
  label?: string;
    externalLink?: string;
    internalLink?: string;
  icon?: React.ReactNode;
}) {
  return internalLink ? (
    <Link href={`${internalLink}`} className="w-fit h-fit">
      <ButtonInner onClick={onClick} icon={icon} label={label} />
    </Link>
  ) : externalLink ? (
    <a href={`${externalLink}`} target="_blank" rel="noopener noreferrer" className="w-fit h-fit">
      <ButtonInner onClick={onClick} icon={icon} label={label} />
    </a>
  ) : (
    <ButtonInner onClick={onClick} icon={icon} label={label} />
  );
}

function ButtonInner({
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
      className="flex w-fit h-fit items-center justify-center p-2 gap-2 bg-cithara-button hover:bg-cithara-border-inner rounded-lg border border-cithara-border-inner ring-cithara-border-outer ring-1 hover:border-white/20 shadow-md select-none cursor-pointer transition-all"
    >
      {(icon || label) && <ButtonLabel icon={icon} label={label} />}
    </div>
  );
}

function ButtonLabel({
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
