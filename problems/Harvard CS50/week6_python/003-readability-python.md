---
id: "CS50-W6-003"
title: "Readability (Python)"
source: "CS50"
difficulty: "Medium"
tags: ["python", "string processing", "text analysis", "loops", "conditionals"]
core_problem: "Calculate the Coleman-Liau index to determine the readability grade level of a text"
status: "complete"
---

## 🧩 Problem Summary

Implement the Coleman-Liau readability formula in Python to estimate the grade level of a given text.

Steps:
- Count letters, words, and sentences in the text
- Compute averages per 100 words:
  - L = average number of letters per 100 words
  - S = average number of sentences per 100 words
- Apply formula:
  
  `index = 0.0588 * L - 0.296 * S - 15.8`

- Round the result to the nearest whole number and print the grade level.

---

## 🔄 Initial Approach

- Iterate through each character in the text
- Use conditions to count letters (alphabetic), words (spaces +1), sentences (`.`, `!`, `?`)
- Calculate L and S based on total counts
- Compute the index using the formula
- Output grade level with appropriate message (e.g., "Grade 16+", "Before Grade 1")

---

## ✅ Optimal Strategy

Python’s string methods and built-in functions simplify counting:

- Use `str.isalpha()` to identify letters
- Use `.split()` to count words efficiently
- Use a loop or list comprehension to count sentences
- Use `round()` for final index

Input validation is minimal since you’re processing arbitrary text.

---

## 🧠 Heuristics & Insights

- Breaking text analysis into **count letters, count words, count sentences** modularizes the problem  
- Use Python’s string capabilities to simplify checks instead of manual ASCII code ranges  
- Remember that splitting on whitespace counts words accurately for most inputs  
- Rounding rules affect output — test edge cases carefully

---

## ⚠️ Common Pitfalls

- Counting non-alphabetic characters as letters  
- Incorrect word count due to punctuation or multiple spaces  
- Forgetting to convert counts to float for averages  
- Misapplying formula order of operations  
- Not handling edge cases (empty input, very short texts)

---

## 🧭 Meta Insight

This problem bridges string processing and applied math, demonstrating how simple algorithms can model complex concepts like readability.

It shows the power of Python for text analysis tasks that would be verbose in lower-level languages.

---

## 🔍 References

- CS50 PSet 6: Readability — https://cs50.harvard.edu/x/2023/psets/6/readability/
- Coleman-Liau index (Wikipedia) — https://en.wikipedia.org/wiki/Coleman–Liau_index
- Python string methods — https://docs.python.org/3/library/stdtypes.html#string-methods