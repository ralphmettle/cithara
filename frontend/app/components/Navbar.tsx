import Link from "next/link";
import NavLink from "@/app/components/NavLink";
import { FaGithub } from "react-icons/fa";
import { PiPianoKeysFill } from "react-icons/pi";
import { ModeToggle } from "./ModeToggle";

export default function Navbar() {
  return (
    <nav className="flex flex-row w-full lg:w-6xl items-center justify-between mx-4 px-4 py-3 pr-5 sm:px-8 sm:py-4 border rounded-lg bg-background/25 backdrop-blur-lg">
      <Link href="/">
        <div className="flex items-center justify-center gap-1 font-bold text-xl group hover:shadow-cithara hover:drop-shadow-cithara transition-all duration-200 select-none">
          <PiPianoKeysFill className="text-cithara group-hover:text-cithara-ui-active transition-colors duration-250 w-8 h-8" />
          <h1 className="">Cithara</h1>
        </div>
      </Link>
      <div className="flex flex-row items-center gap-4 sm:gap-12">
        <NavLink link="" title="Home" />
        <NavLink link="docs" title="Docs" />
        <a
          target="_blank"
          rel="noopener noreferrer"
          href="https://github.com/ralphmettle/cithara"
        >
          <div className="flex flex-row items-center justify-center text-stone-700 dark:text-stone-500 hover:text-foreground hover:cursor-pointer transition-all duration-250 select-none">
            <FaGithub className="h-6 w-6" />
          </div>
        </a>
        <div className="sm:flex sm:-ml-2 hidden">
          <ModeToggle />
        </div>
      </div>
    </nav>
  );
}
