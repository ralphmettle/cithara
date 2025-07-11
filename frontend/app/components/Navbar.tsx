import Link from "next/link";
import { PiPianoKeysFill } from "react-icons/pi";

export default function Navbar() {
  return (
    <nav className="flex flex-row w-full lg:w-6xl items-center justify-between mx-4 pl-4 pr-4 sm:px-8 py-4 border rounded-lg bg-background/50 backdrop-blur-lg">
      <Link href="/">
        <div className="flex items-center justify-center gap-1 font-bold text-xl group">
          <PiPianoKeysFill className="text-cithara group-hover:text-cithara-ui transition-colors duration-150 w-8 h-8" />
          <h1 className="text-white">Cithara</h1>
        </div>
      </Link>
      <div className="flex flex-row items-center gap-4 sm:gap-6">
        <p>Home</p>
        <p>Docs</p>
        <p>GitHub</p>
      </div>
    </nav>
  );
}
