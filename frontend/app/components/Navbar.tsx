export default function Navbar() {
  return (
    <nav className="flex flex-row w-full lg:w-6xl items-center justify-between mx-4 px-8 py-4 border rounded-lg bg-background/50 backdrop-blur-lg">
      <p className="font-bold text-xl">Cithara</p>
      <div className="flex flex-row items-center gap-6">
        <p>Home</p>
        <p>Docs</p>
        <p>GitHub</p>
      </div>
    </nav>
  );
}
