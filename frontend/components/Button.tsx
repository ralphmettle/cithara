import Link from "next/link";
import React from "react";

export default function Button({
  label,
  link,
  icon,
  func,
}: {
  label?: string;
  link?: string;
  icon?: React.ReactNode;
  func?: CallableFunction;
}) {
  return link ? (
    <Link href={`${link}`}>
      <div className="flex w-fit items-center justify-center p-2 hover:bg-cithara-border-light rounded-lg border border-cithara-border-light ring-cithara-bg ring-1 hover:border-white/20 shadow-md select-none cursor-pointer gap-2 transition-all">
        {(icon || label) && <ButtonInner icon={icon} label={label} />}
      </div>
    </Link>
  ) : (
    <div className="flex w-fit items-center justify-center p-2 hover:bg-cithara-border-light rounded-lg border border-cithara-border-light ring-cithara-bg ring-1 hover:border-white/20 shadow-md select-none cursor-pointer transition-all">
      {(icon || label) && <ButtonInner icon={icon} label={label} />}
    </div>
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
    <>
      {icon && <span className="">{icon}</span>}
      {label && <span className="">{label}</span>}
    </>
  );
}
