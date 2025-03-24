import type { Metadata } from "next";
import { Funnel_Display, Funnel_Sans } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const funnelDisplay = Funnel_Display({
  variable: "--font-funnel-display",
  subsets: ["latin"],
});

const funnelSans = Funnel_Sans({
  variable: "--font-funnel-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Cithara",
  description: "Music theory repository",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${funnelSans.variable} ${funnelDisplay.variable} antialiased`}
      >
        <div className="flex flex-row justify-center items-center h-screen w-full py-2">
          <Navbar />
          <div className="flex grow justify-center h-full w-full p-2 mr-2 rounded-2xl bg-cithara-primary border border-cithara-border-light shadow-2xl">
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
