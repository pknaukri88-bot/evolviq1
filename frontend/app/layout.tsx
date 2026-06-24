export const metadata = {
  title: "EvolvIQ",
  description: "AI-Native Intelligence Workspace",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
