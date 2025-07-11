---
id: "LC-001"
title: "Two Sum"
source: "LeetCode"
difficulty: "Easy"
tags: ["array", "hash map", "complements"]
core_problem: "Find two indices in an array whose values sum to a given target"
status: "complete"
---

## 🧩 Problem Summary

Given a list of integers and a target number, find the **indices** of two numbers that add up to the target.  
Only one valid pair exists. The array is not sorted, and each input has exactly one solution.

---

## 🚧 Initial Approach

Try every possible pair of elements using a nested loop.  
Check if the sum of each pair equals the target.

```
for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    if nums[i] + nums[j] == target:
      return [i, j]
```

❌ Time complexity: O(n²)  
❌ Doesn’t scale with large inputs  
❌ Redundant checks and brute-force mindset

---

## ✅ Optimal Strategy

Use a **hash map** to store numbers as you iterate:
- For each number, compute the **complement** (`target - current number`)
- If the complement is already in the map, return the index pair
- Otherwise, store the current number and its index in the map

This allows you to find the pair in a single pass with constant-time lookups.

✅ Time complexity: O(n)  
✅ Space complexity: O(n)  
✅ Efficient, clean, and reusable pattern

---

## 🧠 Heuristics & Insights

- If a problem involves finding a **pair that matches a sum or condition**, try:  
  → "Can I use a hash map to track complements?"

- For **single-pass problems** where **order matters**, think:  
  → "Can I store previous values in a way that speeds up future checks?"

- This is a classic case of:  
  → 🧠 **Memory tradeoff**: Extra space → faster runtime

- Recognizing that the problem is about **lookup**, not brute enumeration, is the turning point.

---

## ⚠️ Common Pitfalls

- Returning **values** instead of **indices**
- Forgetting to check if the complement exists **before** inserting the current number
- Trying to sort the array and use two pointers (breaks index requirement)
- Not accounting for duplicate numbers properly

---

## 🧭 Meta Insight

This problem teaches a **core decision-making upgrade**:  
→ Start with brute-force — but always ask:  
→ "Can I use a map or set to shortcut lookup?"

It also appears as a **building block** in:
- 3Sum / 4Sum variations
- Subarray sum problems
- XOR pair problems
- Dynamic programming optimizations

---

## 🗃️ Notes

This is one of the most famous “aha” problems.  
It appears simple, but it trains you to make a fundamental shift from **iteration to lookup** — a pattern that appears across hundreds of real-world problems.
