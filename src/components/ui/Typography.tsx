import React from 'react';

interface TypographyProps {
  variant?: 'h1' | 'h2' | 'h3' | 'p' | 'span';
  children: React.ReactNode;
  className?: string;
}

export const Typography = ({ variant = 'p', children, className = '' }: TypographyProps) => {
  const Tag = variant as any;
  const baseStyles = "text-brand-secondary leading-relaxed";
  const variants = {
    h1: "text-4xl font-bold text-brand-primary font-display",
    h2: "text-2xl font-semibold text-brand-primary",
    h3: "text-xl font-medium text-brand-secondary",
    p: baseStyles,
    span: "text-sm",
  };

  return <Tag className={`${variants[variant]} ${className}`}>{children}</Tag>;
};