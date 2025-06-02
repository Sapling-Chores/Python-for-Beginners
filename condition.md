

---

# 🔸 Conditions, Tuples, and Truthy/Falsy in Python

This file explains essential Python control flow, data types, and how Python evaluates expressions in conditional contexts.

---

## ✅ Conditions in Python

Conditions use boolean logic to control program flow. Python evaluates expressions using:

* `if`, `elif`, `else` blocks
* comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
* logical operators: `and`, `or`, `not`

### Syntax Example

```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

## 🔁 Logical Operators

| Operator | Meaning             | Example            |
| -------- | ------------------- | ------------------ |
| `and`    | True if both True   | `x > 5 and x < 20` |
| `or`     | True if either True | `x < 5 or x > 100` |
| `not`    | Inverts boolean     | `not (x > 10)`     |

---

## ✅ Truthy and Falsy Values

Python evaluates some values as `False` in conditional contexts.

### Falsy Values

These always evaluate to `False`:

* `False`
* `None`
* `0`, `0.0`
* `''`, `""` (empty strings)
* `[]` (empty list)
* `{}`, `set()`, `()` (empty dict, set, tuple)

Everything else is considered **truthy**.

```python
if []:
    print("This won't print")
if "hello":
    print("This will print")
```

---

## 📦 Tuples

Tuples are immutable, ordered sequences. Similar to lists, but **cannot be changed** after creation.

### Creating Tuples

```python
a = (1, 2, 3)
b = 1, 2, 3       # also valid
c = (42,)         # single-element tuple (comma is required)
```

### Access & Unpacking

```python
print(a[0])       # → 1
x, y, z = a       # unpacking
```

### Properties

* Immutable: can’t be changed
* Supports slicing, indexing
* Faster than lists for read-only data

---

## ✅ Tuple Use Cases

* Return multiple values from a function
* Use as dictionary keys
* Represent fixed collections (like coordinates, RGB colors)

---

This guide gives you all you need to start working with conditionals and tuples effectively in Python.


