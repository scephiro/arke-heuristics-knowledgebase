---
id: "CS50-W1-002"
title: "Credit Card Validator"
source: "CS50"
difficulty: "Easy"
tags: ["validation", "math", "greedy", "modulo", "Luhn"]
core_problem: "Determine whether a credit card number is valid using Luhn's Algorithm and identify the card type"
status: "complete"
---

## 🧩 Problem Summary 

You’re given a number representing a credit card. You need to:
1. Check if it’s valid using **Luhn’s Algorithm** (a checksum validation formula)
2. Determine if it's an **AMEX**, **MASTERCARD**, or **VISA** based on the starting digits and length

---

## 🚧 Initial Approach

- Convert the number to a string
- Use string slicing to:
  - Get prefixes
  - Count length
  - Traverse digits in reverse for Luhn’s Algorithm
- Hardcode rules for valid card types

Example logic:
```
- AMEX starts with 34 or 37 and has 15 digits
- MASTERCARD starts with 51–55 and has 16 digits
- VISA starts with 4 and has 13 or 16 digits
```

❌ Relies too much on string manipulation  
❌ Not memory- or type-safe in C  
❌ No separation between validation and classification logic

---

## ✅ Optimal Strategy

- Treat the number as a long integer (`long`)
- Use **modulus arithmetic** to isolate digits from the end:
  - `% 10` to get last digit
  - `/ 10` to shift
- Use two separate loops:
  - One to apply Luhn’s checksum rule
  - One to extract prefix (first 1–2 digits) and count length
- Store intermediate results: `sum`, `length`, `first_two_digits`, etc.

Benefits:
✅ Works without string conversion  
✅ Respects C's type system  
✅ Logical separation of tasks (validation vs classification)

---

## 🧠 Heuristics & Insights

- If you need to process individual digits **in reverse**, modulus and division are the cleanest tools.
- **Checksums** like Luhn’s often use a pattern of alternating multipliers (e.g., every other digit * 2), followed by digit-sum reductions (e.g., 12 → 1 + 2).
- For input classification (e.g., card type):
  → Extract leading values and length, then apply rule-matching.
- Luhn-like problems reward clean logic separation:
  - `is_valid = validate_luhn(n)`
  - `type = detect_card_type(n)`

---

## ⚠️ Common Pitfalls

- Starting Luhn’s algorithm from the wrong side (it goes **right to left**)
- Failing to split two-digit results in Luhn (e.g. 12 → 1 + 2)
- Misidentifying prefixes due to leading zeros (e.g. using string parsing)
- Forgetting to validate *both* the checksum **and** the type constraints

---

## 🧭 Meta Insight

This problem teaches you to **simulate real-world systems using pure logic**, which is a central theme in both algorithm design and systems programming.

You’re not just learning loops — you’re learning how to encode policy (e.g. card issuer rules) and validate data without external APIs.

---

## 🗃️ Notes

This is one of the earliest CS50 problems to require both:
- A **validation algorithm** (Luhn)
- A **classification engine** (type detection)

It also introduces the idea of **data-driven logic** — a decision tree where values flow through rule gates.

Highly transferable to:
- Input validation
- Data parsing
- Real-world simulations

---

## 🔍 References

- CS50 PSet 1: Credit — https://cs50.harvard.edu/x/2023/psets/1/credit/
- Luhn Algorithm (Wikipedia) — https://en.wikipedia.org/wiki/Luhn_algorithm