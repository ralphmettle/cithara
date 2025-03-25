import Link from "next/link";
import React from "react";

export default function Button({
  label,
  link,
  icon,
  // func,
}: {
  label?: string;
  link?: string;
  icon?: React.ReactNode;
  // func?: CallableFunction;
}) {
  return link ? (
    <Link href={`${link}`} className="w-fit h-fit">
      <ButtonInner icon={icon} label={label} />
    </Link>
  ) : (
    <ButtonInner icon={icon} label={label} />
  );
}

function ButtonInner({
  icon,
  label,
}: {
  icon?: React.ReactNode;
  label?: string;
}) {
  return (
    <div className="flex w-fit h-fit items-center justify-center p-2 bg-cithara-primary hover:bg-cithara-border-light rounded-lg border border-cithara-border-light ring-cithara-bg ring-1 hover:border-white/20 shadow-md select-none cursor-pointer transition-all">
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
