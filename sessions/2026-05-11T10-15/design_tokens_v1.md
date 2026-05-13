# 🎨 데이터시스 디자인 토큰 시스템 (Design Tokens v1.0)

## 💡 목표
이 문서는 데이터시스 브랜드의 모든 시각적 요소를 제어하는 원자적(Atomic) 변수 집합을 정의합니다. 모든 컴포넌트는 이 토큰을 참조해야 하며, 디자인 일관성을 100% 보장하는 것이 목표입니다.

## 🌈 1. 색상 토큰 (Color Tokens)

색상은 단순한 HEX 코드가 아닌, 사용 목적(Semantic)에 따라 정의되어야 합니다.

| 토큰 이름 | 용도 (Semantic) | 값 (HEX) | 설명 |
| :--- | :--- | :--- | :--- |
| `$color-primary-500` | **브랜드 메인 액션** (버튼, 강조) | `#1A73E8` | 데이터시스의 주력 액션 색상. 신뢰와 기술력을 상징. |
| `$color-primary-600` | **호버/활성화 상태** | `#1565C0` | 마우스 오버 또는 활성화된 주 액션 색상. |
| `$color-secondary-400` | **보조 정보/강조** (데이터 포인트) | `#FF9800` | 보조적인 중요 정보나 그래프의 포인트 색상. |
| `$color-success` | **성공/완료 상태** | `#4CAF50` | 성공적인 결과, 완료된 단계 표시. |
| `$color-warning` | **주의/경고 상태** | `#FFC107` | 주의가 필요한 정보, 검토 필요 항목 표시. |
| `$color-error` | **오류/실패 상태** | `#FF1744` | 오류 발생, 실패 단계 표시 (가장 높은 시각적 경고). |
| `$color-background-default` | **기본 배경** | `#FFFFFF` | 페이지의 기본 배경색. |
| `$color-background-card` | **요소 배경** | `#F8F9FA` | 카드, 모달 등 콘텐츠를 담는 영역의 배경색. |
| `$color-text-default` | **본문 텍스트** | `#333333` | 일반적인 본문 텍스트 색상. |
| `$color-text-secondary` | **보조 텍스트** | `#6C757D` | 날짜, 출처, 캡션 등 보조적인 텍스트 색상. |
| `$color-border-default` | **기본 경계선** | `#E0E0E0` | 입력 필드, 섹션 구분선 등 일반적인 경계선. |

## 🖋️ 2. 타이포그래피 토큰 (Typography Tokens)

| 토큰 이름 | 용도 (Semantic) | 값 | 설명 |
| :--- | :--- | :--- | :--- |
| `$font-family-primary` | **주요 폰트** | `Pretendard, sans-serif` | 제목, 핵심 메시지 등 가장 강조되어야 할 텍스트. |
| `$font-family-secondary` | **보조 폰트** | `Noto Sans KR, sans-serif` | 데이터, 코드, 캡션 등 기술적 내용을 담는 텍스트. |
| `$font-size-h1` | **메인 제목** | `2.5rem` | 페이지의 주제를 나타내는 가장 큰 제목. |
| `$font-size-h2` | **섹션 제목** | `2.0rem` | 섹션의 주제를 나타내는 큰 제목. |
| `$font-size-body-lg` | **본문 (강조)** | `1.125rem` | 일반적인 본문에서 강조가 필요한 문단. |
| `$font-size-body-base` | **본문 (표준)** | `1.0rem` | 가장 일반적이고 표준적인 본문 텍스트 크기. |
| `$font-size-caption` | **캡션/메타 정보** | `0.875rem` | 날짜, 작은 설명 등 크기가 작아야 하는 텍스트. |

## 📏 3. 간격/크기 토큰 (Spacing & Size Tokens)

간격은 8px 그리드 시스템을 기반으로 정의하여, 모든 여백과 크기가 일관성을 갖도록 강제합니다.

| 토큰 이름 | 값 (px) | 용도 |
| :--- | :--- | :--- |
| `$spacing-xs` | `4px` | 작은 구분자, 아이콘 간격 등 최소 간격. |
| `$spacing-sm` | `8px` | 버튼 패딩, 작은 요소 간의 간격. |
| `$spacing-md` | `16px` | 섹션 내부 요소 간의 일반적인 간격. |
| `$spacing-lg` | `24px` | 컴포넌트 간의 주요 간격, 여백. |
| `$spacing-xl` | `32px` | 큰 여백, 섹션의 수직적 분리 간격. |
| `$size-border-radius-md` | `8px` | 모서리 둥글기 (기본 컴포넌트). |

---

## 🧩 4. Core Component 재정의 원칙 (Phase 2 가이드)

위 토큰을 기반으로, 향후 모든 컴포넌트는 다음 원칙을 준수해야 합니다.

1.  **Button Component**:
    *   **Primary**: 배경: `$color-primary-500`, 텍스트: `$color-background-default`, 패딩: `($spacing-sm)`
    *   **Secondary**: 배경: `$color-background-card`, 테두리: `$color-border-default`, 텍스트: `$color-primary-500`
2.  **Card Component**:
    *   **배경**: `$color-background-card`
    *   **테두리**: `1px solid $color-border-default`
    *   **패딩**: `$spacing-lg`
3.  **Input Field Component**:
    *   **테두리**: `1px solid $color-border-default`
    *   **Focus (포커스)**: 테두리 색상 변경을 `$color-primary-500`으로 적용. (사용자 피드백 강화)