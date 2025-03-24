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
      <div className="flex text-lg items-center justify-left p-2 px-3 rounded-lg hover:bg-cithara-bg transition-all cursor-pointer select-none my-2">
        {label}
      </div>
    </Link>
  );
}
