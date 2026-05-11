import styles from "./page.module.css";

import Image from "next/image";

export default function Home() {
  const dummyPhone = "010-6265-8464";

  return (
    <div className={styles.container}>
      {/* Header */}
      <header className={styles.header}>
        <div className={styles.logo}>
          <Image src="/images/logo.jpg" alt="부엉이 누수 탐지 로고" width={50} height={50} style={{ objectFit: 'contain' }} priority unoptimized />
          <span style={{ marginLeft: '10px' }}>부엉이 누수</span>
        </div>
        <a href={`tel:${dummyPhone}`}>
          <button className={styles.contactBtn}>📞 전화 상담</button>
        </a>
      </header>

      <main className={styles.main}>
        {/* Hero Section */}
        <section className={styles.hero}>
          <div className={`${styles.heroContent} animate-fade-in`}>
            <div className={styles.badge}>미해결 시 0원 보장</div>
            <h1 className={styles.title}>
              우리 집 숨은 누수,<br />
              <span className={styles.highlight}>부엉이처럼 정확하게</span><br />
              잡아냅니다.
            </h1>
            <p className={styles.subtitle}>
              최신 열화상 카메라와 정밀 가스 탐지기 도입으로<br className={styles.desktopOnly} />
              타 업체가 포기한 누수도 완벽하게 해결해 드립니다.
            </p>
            <div className={styles.ctaGroup}>
              <a href={`tel:${dummyPhone}`} className={styles.ctaPrimary}>
                긴급 누수 출동 요청
              </a>
              <a href="#process" className={styles.ctaSecondary}>
                작업 과정 보기
              </a>
            </div>
          </div>
        </section>

        {/* Features / Why Us */}
        <section className={styles.features}>
          <h2 className={styles.sectionTitle}>왜 부엉이 누수인가요?</h2>
          <p className={styles.sectionSubtitle}>
            어둠 속에서도 먹이를 놓치지 않는 부엉이처럼,<br className={styles.desktopOnly} />
            숨어있는 누수 포인트를 끝까지 찾아냅니다.
          </p>

          <div className={styles.grid}>
            <div className={`${styles.card} animate-fade-in delay-100`}>
              <div className={styles.cardIcon}>🔍</div>
              <h3 className={styles.cardTitle}>최첨단 탐지 장비</h3>
              <p className={styles.cardText}>
                고성능 열화상 카메라, 청음식 탐지기, 혼합 가스 탐지기 등
                최고급 장비를 총동원하여 오차 없는 탐지를 진행합니다.
              </p>
            </div>

            <div className={`${styles.card} animate-fade-in delay-200`}>
              <div className={styles.cardIcon}>💯</div>
              <h3 className={styles.cardTitle}>미해결 시 0원</h3>
              <p className={styles.cardText}>
                누수 원인을 찾지 못한다면 비용을 받지 않습니다.
                그만큼 실력에 대한 강한 자신감과 책임감을 가지고 있습니다.
              </p>
            </div>

            <div className={`${styles.card} animate-fade-in delay-300`}>
              <div className={styles.cardIcon}>🛠️</div>
              <h3 className={styles.cardTitle}>당일 시공 및 마감</h3>
              <p className={styles.cardText}>
                불필요한 파괴를 최소화하며, 정확한 포인트만 굴착합니다.
                탐지부터 배관 교체, 미장 및 타일 마감까지 하루에 끝냅니다.
              </p>
            </div>
          </div>
        </section>

        {/* Process Section */}
        <section id="process" className={styles.process}>
          <h2 className={styles.sectionTitle}>체계적인 탐지 프로세스</h2>
          <p className={styles.sectionSubtitle}>투명하고 정확한 절차로 안심하고 맡기실 수 있습니다.</p>

          <div className={styles.processSteps}>
            <div className={styles.step}>
              <div className={styles.stepNumber}>01</div>
              <div className={styles.stepContent}>
                <h3>전화 상담 및 현장 방문</h3>
                <p>누수 증상을 상세히 상담한 후, 고객님이 편한 시간에 신속하게 현장으로 출동합니다.</p>
              </div>
            </div>

            <div className={styles.step}>
              <div className={styles.stepNumber}>02</div>
              <div className={styles.stepContent}>
                <h3>기초 검사 및 장비 탐지</h3>
                <p>공압 검사를 통해 배관의 압력 손실을 확인하고, 청음/가스 탐지기로 정확한 누수 포인트를 짚어냅니다.</p>
              </div>
            </div>

            <div className={styles.step}>
              <div className={styles.stepNumber}>03</div>
              <div className={styles.stepContent}>
                <h3>부분 굴착 및 원인 확인</h3>
                <p>탐지된 포인트를 최소한으로 굴착하여, 고객님과 함께 누수 지점과 배관의 파손 상태를 직접 확인합니다.</p>
              </div>
            </div>

            <div className={styles.step}>
              <div className={styles.stepNumber}>04</div>
              <div className={styles.stepContent}>
                <h3>배관 보수 및 원상복구 마감</h3>
                <p>문제가 된 배관을 새 부속으로 견고하게 교체하고, 재압력 검사 후 미장 및 타일을 꼼꼼하게 복구합니다.</p>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className={styles.footer}>
        <div className={styles.footerContent}>
          <div className={styles.footerCol}>
            <div style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center' }}>
              <Image src="/images/logo.jpg" alt="부엉이 누수 탐지 로고" width={40} height={40} style={{ objectFit: 'contain' }} unoptimized className={styles.footerLogo} />
              <span style={{ marginLeft: '10px', fontSize: '1.2rem', fontWeight: 'bold' }}>부엉이 누수 탐지</span>
            </div>
            <p>언제나 빠르고 정확하게 누수를 해결합니다.</p>
            <p><strong>고객센터:</strong> {dummyPhone}</p>
            <p><strong>운영시간:</strong> 연중무휴 24시간 긴급 출동</p>
          </div>
          <div className={styles.footerCol}>
            <h4>서비스 지역</h4>
            <p>서울 / 경기 / 인천 전 지역 출장 가능</p>
            <p>아파트, 빌라, 상가, 주택, 공장 누수 전문</p>
          </div>
        </div>
        <div className={styles.footerBottom}>
          <p>© {new Date().getFullYear()} 부엉이 누수 탐지. All rights reserved.</p>
        </div>
      </footer>

      {/* FAB (Floating Action Button) */}
      <a href={`tel:${dummyPhone}`} className={styles.fab} aria-label="전화 걸기">
        📞
      </a>
    </div>
  );
}
