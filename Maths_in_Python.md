# 🔸 Special Notes

- `/` always returns a **float**, even if the division is perfectly divisible.  
  Example: `4 / 2` → `2.0`

- `//` returns an **int** if both operands are integers; otherwise, it returns a **float**.  
  Example: `4 // 2` → `2`, but `4.0 // 2` → `2.0`

- `%` (modulo) is useful for checking even/odd numbers and creating cycles or patterns.  
  Example: `5 % 2` → `1`, so 5 is odd.

- `**` is **right-associative**. This means it evaluates from the right side.  
  Example: `2 ** 3 ** 2` → `2 ** (3 ** 2)` = `2 ** 9` = `512`


# Python Operator Precedence Table

This document outlines the levels of operator precedence in Python, from highest to lowest.

| Precedence Level | Operators                                     |
| ---------------- | --------------------------------------------- |
| 1 (Highest)      | `()` – Parentheses                            |
| 2                | `**` – Exponentiation                         |
| 3                | `+x`, `-x`, `~x` – Unary plus/minus           |
| 4                | `*`, `/`, `//`, `%` – Multiplicative          |
| 5                | `+`, `-` – Additive                           |
| 6                | Comparisons: `<`, `<=`, `>`, `>=`, `==`, `!=` |
| 7                | `not`                                         |
| 8                | `and`                                         |
| 9 (Lowest)       | `or`                                          |
