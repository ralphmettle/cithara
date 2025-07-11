import Navbar from "@/app/components/Navbar";
import ScaleSelector from "@/app/components/ScaleSelector";
import { Button } from "@/components/ui/button";
import { FaGithub } from "react-icons/fa";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <>
      <div className="flex fixed w-full pt-6 items-center justify-center">
        <Navbar />
      </div>
      <div className="w-full min-h-screen pt-[30vh] flex flex-col items-center pb-40">
        <div className="flex flex-col items-center text-center">
          <h1 className="text-8xl sm:text-[10rem] font-bold">Cithara</h1>
          <p className="pt-2 text-md text-stone-400">
            A Python library for music theory object creation
          </p>
        </div>
        <div className="w-full flex flex-col gap-4 items-center pt-12 px-10">
          <p className="text-sm text-stone-400">
            Try a demo! (this isn&apos;t working yet lol)
          </p>
          <div className="w-full sm:w-xl flex">
            <ScaleSelector />
          </div>
        </div>
        <div className="flex pt-4 gap-4">
          <Button
            className="hover:cursor-not-allowed bg-cithara-ui hover:bg-cithara-ui-dark"
            variant="secondary"
          >
            Get info
          </Button>
          <Button asChild className="hover:cursor-pointer" variant="outline">
            <a
              target="_blank"
              rel="noopener noreferrer"
              href="https://github.com/ralphmettle/cithara"
            >
              <FaGithub /> Check it out on GitHub
            </a>
          </Button>
        </div>
        {/* <div className="w-full h-120 bg-neutral-200 rounded-md shadow-inner mt-6" /> */}
        {/* <div className="h-120" /> */}
      </div>
      <Footer />
    </>
  );
}
