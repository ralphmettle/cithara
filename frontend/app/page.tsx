import { RMLogo } from "@/components/RMLogo";
import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col h-full grow items-center justify-center">
      <h1 className="font-bold text-6xl">WELCOME!</h1>
      <div className="flex flex-col pt-10 text-lg items-center justify-center gap-1">
        <p>Thank you for your interest in Cithara!</p>
        <p>Please note that this project is under construction.</p>
        <p>
          You can track the progress/status of the project (this site & Cithara API) at the repo on the
          bottom left.
        </p>
        <p>Hope to see you soon!</p>
        {/* <p className="mt-6">- Ralph</p> */}
        <RMLogo color="a41d1b" width={75} className="pt-12 invert"/>
      </div>
    </div>
  );
}
