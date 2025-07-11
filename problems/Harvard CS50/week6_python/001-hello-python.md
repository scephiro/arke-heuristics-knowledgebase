---
id: "CS50-W6-001"
title: "Hello, Python"
source: "CS50"
difficulty: "Easy"
tags: ["python basics", "syntax", "print", "variables"]
core_problem: "Learn and apply basic Python syntax and structure to print a greeting"
status: "complete"
---

## 🧩 Problem Summary

Write a program in Python that prints `"hello, <name>"` after prompting the user for input.

This is a warm-up problem designed to help you get comfortable with Python syntax, I/O, and conventions — replacing C-style code with more concise, expressive statements.

---

## 🔄 Initial Approach

- Use the built-in `input()` function to get user input
- Use string interpolation or concatenation to construct the greeting
- Use the `print()` function to output the result

Example:
```python
name = input("What's your name? ")
print(f"hello, {name}")
```

---

## ✅ Optimal Strategy

This problem is already optimal using basic Python syntax. The key is to avoid overcomplicating it with unnecessary constructs.

Best practices:
- Use f-strings (`f"..."`) for cleaner and faster string formatting
- Avoid manual string concatenation (`+`) unless required

---

## 🧠 Heuristics & Insights

- In Python, **simple is better than complex** — avoid verbose constructs
- The `input()` function always returns a string — no need to manually cast here
- `print()` in Python adds a newline by default; use `end=""` to suppress if needed
- `f"{var}"` is the most Pythonic way to include variables in strings

---

## ⚠️ Common Pitfalls

- Forgetting that `input()` returns a string (casting isn’t needed here)  
- Using older formatting styles like `.format()` or `%s` (less clean)  
- Confusing indentation rules — Python uses indentation *not* braces `{}` to define blocks  

---

## 🧭 Meta Insight

This problem is symbolic — it marks your transition from low-level C into expressive, high-level Python.

It teaches:
- Simplicity
- Readability
- Trust in the language's built-ins

---

## 🔍 References

- CS50 Week 6 Lecture — https://cs50.harvard.edu/x/2023/weeks/6/
- Python `input()` — https://docs.python.org/3/library/functions.html#input
- Python f-strings — https://realpython.com/python-f-strings/