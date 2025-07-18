import Footer from "@/app/components/Footer";
import ScaleSelector from "@/app/components/ScaleSelector";
import { Button } from "@/components/ui/button";
import { FaGithub } from "react-icons/fa";

export default function Home() {
  return (
    <>
      <div className="w-full min-h-screen pt-[25vh] flex flex-col items-center bg-radial-[at_50%_100%] from-page-gradient to-page-background bg-bottom">
        <div className="flex flex-col items-center text-center">
          <h1 className="text-cithara-ui-dark dark:text-foreground text-8xl sm:text-[10rem] font-bold select-none cursor-default">Cithara</h1>
          <p className="pt-2 text-md text-stone-400 select-none cursor-default">
            A Python library for music theory object creation
          </p>
        </div>
        <div className="w-full flex flex-col gap-4 items-center pt-12 px-10">
          <p className="text-sm text-stone-400">
            Try the demo!
          </p>
          <div className="w-full sm:w-xl flex">
            <ScaleSelector />
          </div>
        </div>
        <div className="flex pt-4 gap-4">
          <Button
            // className="hover:cursor-pointer bg-cithara-ui hover:bg-cithara-ui-dark"
            className="bg-stone-500 hover:bg-stone-500 hover:cursor-not-allowed text-white sm:bg-cithara-ui sm:hover:bg-stone-500 transition-all duration-250"
            variant="secondary"
          >
            Get info
          </Button>
          <Button asChild className="hover:cursor-pointer duration-250" variant="outline">
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
