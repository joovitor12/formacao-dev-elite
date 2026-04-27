import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Barbearia do Seu Ze",
  description:
    "Tradição, estilo e atendimento de primeira no coração do bairro.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
