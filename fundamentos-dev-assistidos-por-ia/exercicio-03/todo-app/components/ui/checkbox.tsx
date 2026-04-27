import * as React from "react"

export interface CheckboxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  checked: boolean
  onCheckedChange: () => void
}

export function Checkbox({ checked, onCheckedChange, ...props }: CheckboxProps) {
  return (
    <input
      type="checkbox"
      checked={checked}
      onChange={onCheckedChange}
      className="h-5 w-5 accent-primary rounded border border-input focus:ring-2 focus:ring-ring"
      {...props}
    />
  )
}
