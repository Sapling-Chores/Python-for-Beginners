# 🔸 Special Notes


---

# README — Overview of Advanced Math Functions in Python

This script demonstrates advanced mathematical operations using Python's built-in `math` module, beyond basic arithmetic and operator precedence.

---

## Key Highlights

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



### Constants

* `math.pi`: π (3.14159...) — ratio of circle circumference to diameter.
* `math.e`: Euler’s number (2.71828...) — base of natural logarithms.

### Rounding Functions

* `ceil(x)`: Round up to nearest integer.
* `floor(x)`: Round down to nearest integer.
* `trunc(x)`: Truncate decimal part (no rounding).

### Powers & Roots

* `sqrt(x)`: Square root.
* `pow(x, y)`: x raised to power y (returns float).
* `exp(x)`: e^x (exponential function).

### Logarithms

* `log(x, base)`: Logarithm with optional base (default: e).
* `log10(x)`: Base-10 logarithm.

### Trigonometry & Angle Conversion

* `sin(x)`, `cos(x)`, `tan(x)`: Trig functions in radians.
* `radians(deg)`: Degrees → radians.
* `degrees(rad)`: Radians → degrees.

### Number Theory

* `gcd(a, b)`: Greatest common divisor.
* `lcm(*args)`: Least common multiple of multiple numbers.
* `isqrt(x)`: Integer square root (floor of sqrt).

### Notes

* `tan(90°)` approaches infinity — watch for this in calculations.
* Exponentiation is **right-associative** (`2 ** 3 ** 2 = 512`).

---

This code is useful for anyone needing precise math operations, scientific calculations, or learning Python’s math module features.

---

