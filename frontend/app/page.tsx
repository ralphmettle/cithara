import Button from "@/components/Button";
import { RMLogo } from "@/components/RMLogo";
import { FaGithub } from "react-icons/fa6";

export default function Home() {
  return (
    <div className="flex flex-col h-full grow items-center justify-center">
      <div className="flex flex-col pt-10 text-lg text-center items-center justify-center gap-1">
        <p>Thank you for your interest in Cithara!</p>
        <p>Please note that this project is under construction.</p>
        <p>
          You can track the progress/status of the project (this site & Cithara
          API) at the repo on the bottom left.
        </p>
        <p className="pb-6">Hope to see you soon!</p>
        <Button
          icon={<FaGithub className="w-6 h-6" />}
          label="View on GitHub"
          externalLink="https://www.github.com/ralphmettle/cithara"
        />
        <RMLogo color="a41d1b" width={75} className="pt-10 invert" />
      </div>
    </div>
  );
}
