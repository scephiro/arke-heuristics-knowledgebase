---
id: "CS50-W2-002"
title: "Caesar Cipher"
source: "CS50"
difficulty: "Medium"
tags: ["encryption", "strings", "modular arithmetic", "ASCII"]
core_problem: "Implement a classic Caesar cipher that shifts letters by a user-specified key"
status: "complete"
---

## 🧩 Problem Summary 

Implement a program that takes a plaintext string and a numeric key, then outputs the ciphertext by shifting each alphabetical character forward by the key amount, wrapping around the alphabet if needed.

Example:
- Plaintext: `HELLO`
- Key: `1`
- Ciphertext: `IFMMP`

Non-alphabetical characters remain unchanged.

---

## 🚧 Initial Approach

- Iterate over each character in the string
- For letters, add the key directly to the ASCII value
- Wrap around by resetting if it goes past `Z` or `z`
- Leave non-letters as-is

Issues:
❌ Might not properly handle wrap-around  
❌ Doesn’t distinguish uppercase and lowercase clearly  
❌ Could produce invalid characters if wrap logic is off

---

## ✅ Optimal Strategy

- Check if character is uppercase (`A`–`Z`) or lowercase (`a`–`z`)
- Normalize the character’s ASCII code by subtracting `A` or `a` to get a zero-based index (0–25)
- Apply the shift with modular arithmetic: `(index + key) % 26`
- Convert back to ASCII by adding `A` or `a`
- Keep non-alphabetical characters unchanged

Benefits:
✅ Cleanly handles wrap-around  
✅ Preserves case  
✅ Modular arithmetic simplifies logic

---

## 🧠 Heuristics & Insights

- Modular arithmetic is key to cyclic shifts  
- Always preserve character case when encrypting  
- Non-alphabetical characters should remain unaltered to maintain message readability  
- Separating logic for uppercase and lowercase avoids complexity

---

## ⚠️ Common Pitfalls

- Forgetting to reset the shift when exceeding `Z` or `z`  
- Applying the key to non-alphabetical characters  
- Mixing uppercase and lowercase transformations  
- Using incorrect ASCII offsets

---

## 🧭 Meta Insight

The Caesar cipher is a foundational encryption technique that introduces:
- Character encoding concepts  
- Modular arithmetic applications  
- Importance of case preservation in data transformations

---

## 🗃️ Notes

- This problem teaches modular arithmetic in a practical context  
- A good stepping stone towards more complex ciphers and cryptographic algorithms

---

## 🔍 References

- CS50 PSet 2: Caesar — https://cs50.harvard.edu/x/2023/psets/2/caesar/
- Caesar cipher (Wikipedia) — https://en.wikipedia.org/wiki/Caesar_cipher