import Link from "next/link";
import React from "react";

export default function Button({
  label,
  link,
}: {
  label: string;
  link: string;
}) {
  return (
    <Link href={`/${link}`}>
      <div className="flex w-fit items-center justify-center p-2 hover:bg-cithara-bg rounded-lg border border-cithara-bg select-none cursor-pointer transition-all">
        {label}
      </div>
    </Link>
  );
}
