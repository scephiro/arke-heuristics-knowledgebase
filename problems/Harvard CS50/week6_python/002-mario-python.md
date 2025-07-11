---
id: "CS50-W6-002"
title: "Mario Pyramid (Python)"
source: "CS50"
difficulty: "Easy"
tags: ["python", "loops", "strings", "conditionals"]
core_problem: "Recreate the half-pyramid pattern from CS50 using Python’s loops and string manipulation"
status: "complete"
---

## 🧩 Problem Summary

Reimplement the classic Mario half-pyramid from CS50, but using Python.

Given a user input height `n` (between 1 and 8), print a right-aligned pyramid of hashes (`#`) of height `n`.

Example for `n = 4`:
```
   #
  ##
 ###
####
```

---

## 🔄 Initial Approach

- Prompt user for height between 1 and 8
- Use a `for` loop to iterate over each row
- For each row:
  - Print spaces (`" "`) to right-align the pyramid
  - Print hashes (`"#"`) for the current row count

Example logic:
```python
for i in range(1, n + 1):
    print(" " * (n - i) + "#" * i)
```

---

## ✅ Optimal Strategy

The initial approach is already simple and efficient.

Tips:
- Use string multiplication for cleaner code  
- Validate user input before proceeding  
- Use built-in `input()` and `int()` conversion carefully to avoid exceptions

---

## 🧠 Heuristics & Insights

- Python string multiplication (`" " * count`) is a powerful tool for text patterns  
- Loop ranges in Python are exclusive on the upper bound — `range(1, n+1)` includes `n`  
- Breaking problems into smaller parts (spaces, hashes) simplifies logic  
- Input validation is crucial to avoid runtime errors

---

## ⚠️ Common Pitfalls

- Off-by-one errors in loops  
- Forgetting to convert input strings to integers  
- Using `print` incorrectly (missing commas or concatenation)  
- Ignoring input constraints (height must be between 1 and 8)

---

## 🧭 Meta Insight

This problem demonstrates Python’s elegance for text-based algorithms, emphasizing readable, concise code for classic exercises.

It’s a bridge from manual loops to idiomatic Python constructs.

---

## 🔍 References

- CS50 Week 6 Lecture — https://cs50.harvard.edu/x/2023/weeks/6/
- Python string multiplication — https://docs.python.org/3/library/stdtypes.html#common-sequence-operations