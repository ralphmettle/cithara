import type { Metadata } from "next";
import { Funnel_Display, Funnel_Sans } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/utils/theme-provider";

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
  description: "Python music theory library, visualise relationships in music!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head />
      <body
        className={`${funnelSans.variable} ${funnelDisplay.variable} antialiased`}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
