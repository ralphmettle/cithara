import Image from "next/image";

export default function DocsPage() {
  return (
    <div className="w-full min-h-screen flex flex-col pt-[8vh] items-center justify-center bg-radial-[at_50%_100%] from-page-gradient to-page-background bg-bottom gap-4">
      <h1 className="text-5xl font-bold"> This page is under construction!</h1>
      <p className="text-muted-foreground">
        Please look forward to Cithara's release for documentation
      </p>
      <Image
        className="mt-8"
        src="/bongo-cat-transparent.gif"
        height={200}
        width={200}
        alt="Bongo cat!"
      />
    </div>
  );
}
