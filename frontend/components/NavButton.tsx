import React from "react";
import Link from "next/link";

export default function NavButton({
  label,
  link,
}: {
  label: string;
  link: string;
}) {
  return (
    <Link href={`/${link}`}>
      <div className="flex text-lg items-center justify-center p-2 px-3 rounded-lg hover:bg-cithara-bg/70 transition-all cursor-pointer select-none">
        {label}
      </div>
    </Link>
  );
}
