import './globals.css';
import { Typography } from '@/components/ui/Typography';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body className="bg-surface-background text-brand-primary">
        <nav className="p-6 border-b border-slate-200 flex justify-between items-center bg-white">
          <Typography variant="h3" className="font-bold text-brand-accent">DATASYS</Typography>
          <div className="space-x-8">
            {['About', 'Solutions', 'Portfolio', 'Contact'].map((item) => (
              <a key={item} href={`/${item.toLowerCase()}`} className="text-sm font-medium hover:text-brand-accent transition-colors">
                {item}
              </a>
            ))}
          </div>
        </nav>
        <main className="min-h-screen">{children}</main>
        <footer className="p-10 border-t border-slate-200 text-center text-sm text-brand-secondary">
          © 2026 DATASYS. All rights reserved.
        </footer>
      </body>
    </html>
  );
}