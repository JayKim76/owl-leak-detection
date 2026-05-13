/**
 * @file tokens.ts
 * @description Designer 에이전트가 정의한 Design Tokens (v2.0)
 */

export const tokens = {
  colors: {
    primary: '#007AFF',    // iOS/Instagram Blue
    accent: '#FF2D55',     // Instagram Pink/Red
    surface: '#FFFFFF',    // Main Background
    background: '#F2F2F7', // System Background
    text: {
      main: '#1C1C1E',
      secondary: '#8E8E93',
      subtle: '#C7C7CC'
    },
    border: '#E5E5EA'
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px'
  },
  borderRadius: {
    sm: '4px',
    md: '12px',
    lg: '20px',
    full: '9999px'
  },
  typography: {
    h1: { fontSize: '32px', fontWeight: '700' },
    h2: { fontSize: '24px', fontWeight: '600' },
    body: { fontSize: '16px', fontWeight: '400' },
    caption: { fontSize: '12px', fontWeight: '400' }
  }
};