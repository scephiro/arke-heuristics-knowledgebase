---
id: "CS50-W1-001"
title: "Mario Pyramid"
source: "CS50"
difficulty: "Easy"
tags: ["loops", "nested iteration", "alignment", "simulation"]
core_problem: "Recreate a pyramid-shaped pattern based on user input using loops and alignment"
status: "complete"
---

## 🧩 Problem Summary

You're asked to print a **pyramid of bricks** (`#`) of a given height (between 1 and 8), aligned to the right — similar to the structure seen in *Super Mario Bros*. You prompt the user for the height, then output rows of increasing brick length.

Example (height = 4):
```
   #
  ##
 ###
####
```

---

## 🚧 Initial Approach

- Prompt the user and use `scanf` to get height
- Use nested loops:
  - Outer loop for each row
  - Inner loop to:
    - Print spaces first
    - Then print hashes
- Hardcode the bounds of loops or use excessive conditionals

Issues with this:
❌ Inefficient or redundant inner loops  
❌ Manual tracking of row/column indices can become error-prone  
❌ Doesn’t scale if asked to change dimensions (e.g. double-sided pyramids)

---

## ✅ Optimal Strategy

Use two nested loops where:
- The **outer loop** iterates from `1` to `height`
- The **inner loop** prints:
  1. `height - row` spaces
  2. `row` hashes (`#`)

This allows you to:
✅ Cleanly simulate the shape row-by-row  
✅ Decouple logic from specific row numbers  
✅ Easily adapt to other variations (e.g. two-sided pyramids)

---

## 🧠 Heuristics & Insights

- Any time you're **building a shape in the console**, visualize each row as a **sequence of character groups** (spaces, symbols, etc.)
- **Inverted logic** helps: Instead of thinking “how many bricks should I add?”, ask “how many spaces do I need to fill to shift it?”
- Pattern construction = nested loops + math mapping

Example translation:
```c
for (int row = 1; row <= height; row++) {
    print (height - row) spaces
    print (row) hashes
}
```

This maps neatly to:
- **Increasing substructure** (row-wise progression)
- **Decreasing space-to-content ratio**

---

## ⚠️ Common Pitfalls

- Off-by-one errors: loop starting from 0 instead of 1
- Forgetting to print a newline at the end of each row
- Using magic numbers instead of variables
- Mixing logic: printing space and hashes in one loop without clarity

---

## 🧭 Meta Insight

This problem isn’t about printing bricks — it’s about **thinking procedurally**.

It teaches:
- Loop-based layout design  
- Basic condition mapping (how X affects Y)  
- Control flow tied to visual structure  

It’s your first taste of **simulating a system with deterministic logic**, which is the foundation of more complex algorithms.

---

## 🗃️ Notes

Though simple, Mario's pyramid introduces key thinking patterns:
- Coordinate reasoning (space vs brick)
- Control flow by iteration
- Translating real-world patterns into procedural steps

Later, this mindset will extend to:
- Graph traversal  
- Grid algorithms (e.g. image processing)  
- Game logic

---

## 🔍 References

- CS50 PSet 1: Mario — https://cs50.harvard.edu/x/2023/psets/1/mario/