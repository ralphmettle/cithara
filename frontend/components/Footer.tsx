import Link from "next/link";
import React from "react";
import { FaGithub } from "react-icons/fa";

export default function Footer() {
  return (
    <Link href="https://github.com/ralphmettle/Cithara">
      <div className="flex align-center justify-center">
        <div className="flex p-2 rounded-md w-fit h-fit items-center justify-center pb-4 text-black/30  hover:text-cithara-primary transition-all cursor-pointer">
          <FaGithub />
        </div>
      </div>
    </Link>
  );
}
