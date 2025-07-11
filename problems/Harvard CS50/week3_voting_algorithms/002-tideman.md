---
id: "CS50-W3-002"
title: "Tideman Voting"
source: "CS50"
difficulty: "Hard"
tags: ["voting", "graph theory", "ranking", "cycle detection", "adjacency matrix"]
core_problem: "Implement the Tideman voting system to determine a winner based on ranked preferences without creating cycles"
status: "complete"
---

## 🧩 Problem Summary 

You're simulating the **Tideman (Ranked Pairs)** voting system.

Voters rank candidates. Based on those rankings, you:
1. Build a graph of candidate preferences (who is preferred over whom)
2. Sort winning pairs by margin of victory
3. Lock in the strongest pairs, ensuring **no cycles** are created
4. The source of the resulting graph (no edges pointing to them) is the winner

---

## 🔄 Initial Approach

- Record individual voter preferences in a 2D matrix  
- Count how many voters prefer candidate A over B for all A/B pairs  
- Store all winning pairs and compute their victory margins  
- Sort pairs in descending order of victory margin  
- Lock pairs one by one unless locking would create a cycle  
- Print the candidate who has no incoming edges

This involves:
- A preference matrix `preferences[i][j]` where `i` is preferred over `j`  
- A `locked[i][j]` matrix to represent the directed acyclic graph (DAG)

---

## ✅ Optimal Strategy

Because this problem is logic-heavy, optimization is about:
- Clear **separation of phases**:
  - Recording preferences
  - Pair generation
  - Sorting
  - Cycle-safe locking
  - Winner determination
- Efficient **cycle detection** using recursion/DFS-style traversal
- Careful **edge direction tracking** in the locked graph

Best practices:
- Build small helper functions: `record_preferences()`, `add_pairs()`, `sort_pairs()`, `lock_pairs()`, `print_winner()`  
- Use a recursive `creates_cycle()` function to avoid invalid edge insertions  
- Keep everything deterministic and predictable

---

## 🧠 Heuristics & Insights

- Any time you're dealing with **ranking**, look for ways to **translate rankings into pairwise preferences**
- Sorting + locking = **greedy algorithm**  
- When building graphs, especially directed ones, **cycle detection is non-negotiable**
- To prevent cycles:
  - Use DFS-style recursion
  - Track visited nodes
  - Think of the locked graph as a growing tree — avoid making loops

---

## ⚠️ Common Pitfalls

- Not properly detecting cycles → incorrect or unfair graph  
- Forgetting that `preferences[i][j]` ≠ `preferences[j][i]`  
- Off-by-one errors in array indexing  
- Locking pairs blindly without checking for cycles  
- Assuming ties don’t affect the outcome (they might)

---

## 🧭 Meta Insight

Tideman is a perfect example of:
- **Graph-based thinking**
- Combining **voter intent modeling** with **mathematical fairness**
- Applying a **greedy algorithm** safely within logical constraints

It blends data structures (matrices, recursion) with high-level modeling (ranking → winner) and is one of the first truly algorithm-heavy problems in CS50.

---

## 🗃️ Notes

- The underlying structure here is a **DAG** (directed acyclic graph)  
- The source node (no incoming edges) represents the winner — this is a **classic graph traversal insight**

Tideman builds critical intuition for:
- Sorting algorithms  
- Cycle detection  
- Decision-tree logic  
- Real-world voting fairness models

---

## 🔍 References

- CS50 PSet 3: Tideman — https://cs50.harvard.edu/x/2023/psets/3/tideman/
- Tideman method (Wikipedia) — https://en.wikipedia.org/wiki/Ranked_pairs