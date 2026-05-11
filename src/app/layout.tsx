import type { Metadata } from "next";
import { Noto_Sans_KR } from "next/font/google";
import "./globals.css";

const notoSansKR = Noto_Sans_KR({
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  variable: "--font-noto-sans-kr",
  display: "swap",
});

export const metadata: Metadata = {
  title: "부엉이 누수 탐지 | 빠르고 정확한 누수 해결",
  description: "최신 열화상 카메라와 가스 탐지기로 숨은 누수까지 확실하게 잡아냅니다. 미해결 시 0원. 지금 바로 긴급 상담받으세요.",
  keywords: ["누수", "누수탐지", "부엉이누수", "배관공사", "방수공사", "누수전문가"],
  openGraph: {
    title: "부엉이 누수 탐지 | 확실한 누수 해결",
    description: "최신 탐지 장비 도입! 미해결 시 0원. 우리 집 누수 고민, 부엉이 누수가 완벽하게 해결해 드립니다.",
    url: "https://owl-leak.example.com",
    siteName: "부엉이 누수",
    images: [
      {
        url: "/logo.png",
        width: 800,
        height: 600,
        alt: "부엉이 누수 탐지 로고",
      },
    ],
    locale: "ko_KR",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko" className={notoSansKR.variable}>
      <body>
        {children}
      </body>
    </html>
  );
}
