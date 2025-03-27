import "./globals.css";

import type { Metadata } from "next";
import { Funnel_Display, Funnel_Sans } from "next/font/google";

import { IoIosArrowBack } from "react-icons/io";

import Navbar from "@/components/Navbar";
import Button from "@/components/Button";

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
          <div className="flex grow h-full w-full p-4 mx-2 rounded-2xl bg-cithara-primary border border-cithara-panel-border shadow-2xl">
            <div className="absolute w-fit h-fit z-10">
              <Button icon={<IoIosArrowBack className="w-4 h-4" />} />
            </div>
            <div className="z-0 relative w-full h-full">{children}</div>
          </div>
        </div>
      </body>
    </html>
  );
}
