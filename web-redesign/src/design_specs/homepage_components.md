# 🌌 Homepage Component Specification: DataSys Redesign

## 🎯 1. 디자인 목표 및 적용 원칙
*   **목표:** 사용자가 페이지에 진입했을 때, '데이터시스'가 단순 컨설팅 회사가 아닌, **미래 기술을 선도하는 자동화 솔루션 기업**이라는 인상을 받도록 합니다.
*   **원칙:**
    1.  **고대비(High Contrast):** 어두운 배경(Deep Space Black)에 밝은 네온 컬러(Neon Blue)를 사용하여 정보의 중요도를 강조합니다.
    2.  **정보 밀도(Data Density):** 텍스트와 시각 요소가 공존하되, 여백(Whitespace)을 충분히 활용하여 복잡함을 방지합니다.
    3.  **흐름(Flow):** 스크롤을 내릴 때마다 '문제 제기 $\rightarrow$ 솔루션 제시 $\rightarrow$ 증거 제시(Case Study)'의 논리적 흐름을 유지합니다.

---

## 🛠️ 2. 핵심 컴포넌트 스펙 (Component Specs)

### A. [Hero Section] - (Above the Fold)
*   **역할:** 방문자의 시선을 사로잡고, 회사와 서비스의 핵심 가치를 3초 내에 전달.
*   **레이아웃:** 2단 구성 (좌: 텍스트/CTA, 우: 인터랙티브 비주얼).
*   **배경:** Deep Space Black (`#050505`). 미세한 노이즈 텍스처(Noise Texture) 오버레이 적용.
*   **텍스트 (H1):**
    *   **내용:** AI 기반 기업 자동화 솔루션 컨설팅. 비즈니스의 미래를 재정의하다.
    *   **스타일:** 타이포그래피는 산세리프(Sans-serif) 계열 중 기술적인 느낌의 폰트 (예: Inter 또는 Orbitron 계열). 'AI 기반', '솔루션 컨설팅' 등 핵심 키워드에 **Neon Blue** 컬러 적용.
    *   **크기:** 매우 크게 (H1), 시각적 위압감을 주어 전문성 강조.
*   **CTA 버튼:**
    *   **Primary Button:** "무료 진단 받기"
    *   **스타일:** Neon Blue 배경, Deep Space Black 텍스트. 마우스 오버 시 미세한 글로우(Glow) 효과와 함께 배경색이 Cyber Purple로 전환되는 애니메이션 적용.
*   **우측 비주얼:**
    *   **요소:** 데이터 흐름 다이어그램 (Flow Diagram) 또는 인터랙티브 대시보드 목업.
    *   **스타일:** 다양한 색상의 점(Dot)들이 복잡하게 연결되어 움직이는(Animation) 형태. Neon Blue와 Cyber Purple 라인이 주를 이루며, 데이터가 흐르는 느낌을 시각적으로 구현. (실제 데이터 대신 추상적인 '연결성'을 보여주는 것이 핵심).

### B. [Service Overview Section] - (문제 제기 및 솔루션 제시)
*   **역할:** 고객의 Pain Point를 언급하며, 데이터시스의 서비스가 왜 필요한지 논리적으로 설득.
*   **레이아웃:** 3분할 구조 (Column 1, Column 2, Column 3).
*   **배경:** Surface Dark (`#0F0F0F`).
*   **헤드라인 (H2):**
    *   **내용:** 기업이 직면한 자동화의 3가지 핵심 과제.
    *   **스타일:** 중앙 정렬, Neon Blue 하이라이트.
*   **3개 컬럼 (Card Components):**
    *   각 카드는 모서리가 약간 둥근(Border-radius: 8px) 어두운 카드 배경을 가집니다.
    *   **구성:** 아이콘 (Icon) $\rightarrow$ 제목 (H3) $\rightarrow$ 설명 (P) $\rightarrow$ CTA (Optional)
    *   **아이콘:** 각 문제 영역을 상징하는 테크니컬하고 간결한 라인 아이콘 (예: 톱니바퀴, 그래프, 클라우드). 아이콘은 Neon Blue로 처리.
    *   **예시 1 (문제):** '수작업 기반의 비효율적인 업무 프로세스'
    *   **예시 2 (솔루션):** '데이터 사일로로 인한 정보 분산 및 활용 저하'
    *   **예시 3 (결과):** '수동 보고서 작성에 소요되는 막대한 시간 비용'

---

## 🚀 3. Developer Action Item
1.  **컴포넌트 분리:** 위 스펙을 바탕으로 `HeroSection.jsx`, `ServiceOverview.jsx` 등의 재사용 가능한 컴포넌트 구조를 구축합니다.
2.  **애니메이션 적용:** Hero Section의 데이터 흐름 다이어그램과 CTA 버튼의 인터랙션에 최소한의 CSS 애니메이션(Transition, Keyframes)을 적용하여 Cyberpunk 느낌을 극대화합니다.
3.  **반응형 최적화:** 모든 컴포넌트는 모바일 환경에서도 정보가 명확하게 전달되도록 반응형 디자인을 우선 적용합니다.