import Link from "next/link";

export default function NavLink({
  link,
  title,
}: {
  link: string;
  title: string;
}) {
  return (
    <Link href={`/${link}`}>
      <div className="text-stone-700 dark:text-stone-500 hover:text-foreground dark:hover:text-stone-200 hover:cursor-pointer transition-all duration-250 select-none">
        <p>{title}</p>
      </div>
    </Link>
  );
}
