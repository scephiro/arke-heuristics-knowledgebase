---
id: "LC-003"
title: "Maximum Subarray"
source: "LeetCode"
difficulty: "Medium"
tags: ["array", "dynamic programming", "greedy", "prefix sum"]
core_problem: "Find the contiguous subarray with the largest sum"
status: "complete"
---

## 🧩 Problem Summary

Given an array of integers (which may include negatives), return the **maximum sum** of any contiguous subarray.  
The subarray must contain at least one number.

---

## 🚧 Naive Strategy

Try every possible subarray using two nested loops:

- For each index `i`, try every end index `j >= i`
- Sum the subarray from `i` to `j`
- Track the max sum encountered

Example logic:

```
max_sum = float('-inf')
for i in range(len(nums)):
    for j in range(i, len(nums)):
        total = sum(nums[i:j+1])
        max_sum = max(max_sum, total)
```

❌ Time complexity: O(n²) or worse  
❌ Recalculates the same sums repeatedly  
❌ No memory of previous work

---

## ✅ Optimal Strategy

Use **Kadane’s Algorithm** — a dynamic programming technique optimized for linear time.

Track:
- `current_sum`: best sum ending at the current position
- `max_sum`: best overall sum seen so far

At each step:
- Either extend the previous subarray: `current_sum + num`  
- Or start fresh from `num`  
→ Pick the better option

```
current_sum = max(num, current_sum + num)
max_sum = max(max_sum, current_sum)
```

✅ Time complexity: O(n)  
✅ Space complexity: O(1)  
✅ Clean, elegant, fast

---

## 🧠 Heuristics & Insights

- This is a **running state** problem:  
  → "Should I carry forward or reset?"

- When dealing with **maximum/minimum of a contiguous range**, always check:  
  → "Can I track local max and global max?"

- Greedy logic works when:
  - Local decision leads toward a global optimum
  - You can make an isolated choice at each index

- Dynamic programming doesn’t always need arrays or tables — sometimes it's just smart variables.

---

## ⚠️ Common Pitfalls

- Forgetting to initialize `max_sum` with `float('-inf')`
- Incorrectly updating `max_sum` before updating `current_sum`
- Not handling all-negative arrays (max may be a single element)
- Mistaking this for a prefix sum problem

---

## 🧭 Meta Insight

Kadane’s Algorithm is a mental model for **local improvement under constraints**.  
It’s a prime example of reducing a complex search space to a few tracked variables — and making confident decisions at every step.

Also useful for:
- Stock trading profit problems  
- Streaming window optimizations  
- Local maximums in signal analysis

---

## 🗃️ Notes

This is often people’s first exposure to greedy dynamic programming.  
It rewards intuition and clean implementation — and teaches you to **trust local decisions when the math works out**.
