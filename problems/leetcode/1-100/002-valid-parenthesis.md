---
id: "LC-002"
title: "Valid Parentheses"
source: "LeetCode"
difficulty: "Easy"
tags: ["stack", "string", "balanced symbols"]
core_problem: "Check if a string of brackets is properly closed and nested"
status: "complete"
---

## 🧩 Problem Summary

Given a string containing just parentheses (`()`, `{}`, `[]`), determine if the string is **valid** — meaning all brackets are closed and properly nested in the correct order.

---

## 🚧 Initial Approach

Scan the string and try to cancel out matching pairs as they appear.  
Attempting to replace or remove matched characters in-place without structure.

Example logic:

- If you see `(`, look ahead for a `)`
- Remove them if found
- Repeat until empty

❌ Falls apart quickly for nested input (e.g. `"([)]"`)  
❌ Can’t reliably track order  
❌ Time complexity is inefficient due to repeated string manipulation  
❌ No understanding of **structure** — just reaction

---

## ✅ Optimal Strategy

Use a **stack** to track expected closing brackets:

- For every opening bracket (`(`, `{`, `[`), push the **corresponding closing bracket** to the stack
- For every closing bracket, check if it matches the **top of the stack**
- If it doesn’t match or the stack is empty — invalid
- If the stack is empty at the end — valid

✅ Time complexity: O(n)  
✅ Space complexity: O(n) in worst case  
✅ Correctly handles nesting, order, and balance

---

## 🧠 Heuristics & Insights

- If a problem involves **opening/closing patterns**, especially nested, think:  
  → **"Use a stack to track expectations"**

- Push **what you expect**, not what you saw.  
  (Push `)` when you see `(` — not `(` itself)

- In parsing problems:  
  → Stack = **Last In, First Out = Nested State Tracking**

- This problem is often your **first encounter with a parser mindset**

---

## ⚠️ Common Pitfalls

- Checking if brackets are “the same type” without considering order  
- Forgetting to check if the stack is empty before popping  
- Not verifying the stack is **empty at the end** (e.g. `"((("` passes mid-loop checks)

---

## 🧭 Meta Insight

This is a structural validation problem — your job is to model **what should happen**, not just scan for characters.  
It’s an introduction to the **"push what you expect"** strategy that applies to:

- Expression parsing  
- Syntax checking  
- Tree traversal with backtracking  
- Custom DSL or compiler construction

It’s also a building block for:
- Harder stack problems (min-stack, decode string)
- Recursion-free backtracking techniques

---

## 🗃️ Notes

This problem is often underestimated because it’s short and labeled “easy.”  
But it introduces **stateful parsing**, **stack-based validation**, and one of the most powerful general-purpose tools in programming: **expectation tracking**.
