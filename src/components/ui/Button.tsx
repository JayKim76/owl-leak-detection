import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'outline' | 'ghost';
}

export const Button = ({ variant = 'primary', className = '', ...props }: ButtonProps) => {
  const baseStyles = "px-6 py-3 rounded-brand font-medium transition-all duration-200 active:scale-95";
  const variants = {
    primary: "bg-brand-accent text-white hover:bg-cyan-600 shadow-lg shadow-cyan-500/20",
    outline: "border-2 border-brand-accent text-brand-accent hover:bg-cyan-50",
    ghost: "text-brand-secondary hover:bg-slate-100",
  };

  return (
    <button className={`${baseStyles} ${variants[variant]} ${className}`} {...props} />
  );
};