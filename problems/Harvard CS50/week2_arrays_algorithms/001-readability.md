---
id: "CS50-W2-001"
title: "Readability"
source: "CS50"
difficulty: "Medium"
tags: ["text analysis", "strings", "iteration", "heuristics"]
core_problem: "Calculate the reading grade level of a given text using the Coleman–Liau index"
status: "complete"
---

## 🧩 Problem Summary

Given a block of text, analyze it to estimate the **reading grade level** by counting:
- Letters
- Words
- Sentences

Then apply the **Coleman–Liau index formula** to output a grade level (e.g., Grade 8, Grade 12).

---

## 🚧 Initial Approach

- Read the entire text into a string
- Iterate character-by-character
- Count letters by checking if a character is alphabetic
- Count words by counting spaces + 1
- Count sentences by looking for punctuation marks like `.`, `!`, `?`

This works but may have pitfalls:
❌ Assuming words only split by spaces (ignores tabs, newlines)  
❌ Counting non-alphabetic characters as letters if not careful  
❌ Hardcoding sentence terminators, missing edge cases

---

## ✅ Optimal Strategy

- Use robust checks for letters using `isalpha()` or equivalent  
- Count words by tracking transitions from non-space to space characters, or use a state machine  
- Sentences recognized by `.` `!` `?` with context awareness  
- Calculate averages per 100 words as required by Coleman–Liau:
  - `L = (letters / words) * 100`
  - `S = (sentences / words) * 100`
- Compute index = `0.0588 * L - 0.296 * S - 15.8`

Benefits:
✅ More accurate counting  
✅ Clear formula application  
✅ Easily adaptable to other indices or languages

---

## 🧠 Heuristics & Insights

- When parsing natural text, use **library helpers** to avoid edge cases (`isalpha()`, `isspace()`)
- Use a **stateful approach** to track word boundaries rather than simple counters  
- Normalize data (convert all to lowercase if needed) before counting  
- Carefully validate inputs to handle empty strings or unusual punctuation  
- Separate counting logic from output formatting

---

## ⚠️ Common Pitfalls

- Off-by-one errors in word counting  
- Counting punctuation as letters  
- Miscalculating averages due to integer division  
- Forgetting to handle edge cases like empty input or strings with no punctuation

---

## 🧭 Meta Insight

This problem is a great example of **data-driven heuristics** in text processing.

It shows how to:
- Extract features from raw data  
- Apply domain-specific formulas  
- Translate human language concepts into computational logic

---

## 🗃️ Notes

- The Coleman–Liau index is one of many readability formulas; the approach generalizes well  
- Counting patterns in text is fundamental to NLP, search engines, and automated editing tools

---

## 🔍 References

- CS50 PSet 2: Readability — https://cs50.harvard.edu/x/2023/psets/2/readability/
- Coleman–Liau index (Wikipedia) — https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index