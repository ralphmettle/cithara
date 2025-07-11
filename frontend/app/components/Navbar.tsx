import Link from "next/link";
import { PiPianoKeysFill } from "react-icons/pi";

export default function Navbar() {
  return (
    <nav className="flex flex-row w-full lg:w-6xl items-center justify-between mx-4 px-8 py-4 border rounded-lg bg-background/50 backdrop-blur-lg">
      <Link href="/">
        <div className="flex items-center justify-center gap-1 font-bold text-xl">
          <PiPianoKeysFill className="text-cithara w-8 h-8" />
          <h1>Cithara</h1>
        </div>
      </Link>
      <div className="flex flex-row items-center gap-6">
        <p>Home</p>
        <p>Docs</p>
        <p>GitHub</p>
      </div>
    </nav>
  );
}
