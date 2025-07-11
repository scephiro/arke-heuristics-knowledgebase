---
id: "CS50-W2-003"
title: "Substitution Cipher"
source: "CS50"
difficulty: "Medium"
tags: ["encryption", "strings", "validation", "mapping"]
core_problem: "Implement a substitution cipher that encrypts text by mapping each letter to a corresponding letter in a user-provided key"
status: "complete"
---

## 🧩 Problem Summary 

Create a program that takes a **26-character key** representing a substitution cipher mapping, then encrypts plaintext by replacing each alphabetical character with its corresponding character in the key.

Example:  
- Key: `QWERTYUIOPLKJHGFDSAZXCVBNM`  
- Plaintext: `HELLO`  
- Ciphertext: `ITSSG`

Key requirements:  
- Must contain 26 unique alphabetical characters  
- Case-insensitive but preserve case in output

---

## 🚧 Initial Approach

- Assume key is valid without checking  
- For each character in plaintext, convert to uppercase or lowercase and replace by position in key  
- Ignore key validation and duplicates  
- Directly substitute without preserving case or validating input

Drawbacks:  
❌ Potential for invalid keys causing unpredictable output  
❌ Case handling issues  
❌ No error messaging or user feedback on invalid keys

---

## ✅ Optimal Strategy

- Validate key length is exactly 26  
- Verify all characters are alphabetical and unique (no duplicates)  
- For each plaintext character:  
  - Identify if uppercase or lowercase  
  - Find its alphabetical index (`A` or `a` offset)  
  - Replace with corresponding character from key preserving case  
- Reject invalid keys with meaningful error messages before encryption

Benefits:  
✅ Robust input validation  
✅ Proper case preservation  
✅ Predictable, secure substitutions

---

## 🧠 Heuristics & Insights

- **Input validation is critical** — cryptographic security depends on key integrity  
- Use data structures (e.g., boolean arrays or hash sets) to check duplicates efficiently  
- Case preservation maintains readability and usability  
- Modularize code into validation and encryption functions for clarity and testing

---

## ⚠️ Common Pitfalls

- Not checking for duplicate letters in the key  
- Misaligning substitution due to off-by-one indexing  
- Overwriting characters without preserving case  
- Accepting keys with non-alphabetic characters

---

## 🧭 Meta Insight

This problem introduces practical **mapping-based encryption** beyond simple shifts.

It illustrates:  
- The importance of validating assumptions  
- The role of substitution in cryptography  
- Modular design for input validation and transformation

---

## 🗃️ Notes

- Substitution ciphers are vulnerable but great for learning mapping logic  
- Lays groundwork for understanding more complex symmetric encryption schemes

---

## 🔍 References

- CS50 PSet 2: Substitution — https://cs50.harvard.edu/x/2023/psets/2/substitution/
- Substitution cipher (Wikipedia) — https://en.wikipedia.org/wiki/Substitution_cipher