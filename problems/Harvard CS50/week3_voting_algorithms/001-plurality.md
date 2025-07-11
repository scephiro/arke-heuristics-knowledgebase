---
id: "CS50-W3-001"
title: "Plurality Voting"
source: "CS50"
difficulty: "Medium"
tags: ["voting", "data structures", "counting", "input processing"]
core_problem: "Implement a voting system where the candidate with the most votes wins"
status: "complete"
---

## 🧩 Problem Summary 

You're building a voting system using the **plurality rule**, where each voter votes for one candidate, and the candidate with the most votes wins. In the event of a tie, all candidates with the highest number of votes are declared winners.

---

## 🔄 Initial Approach

- Store each candidate’s name in an array of structs
- Track each candidate’s vote count using an integer field
- Loop through each vote:
  - Compare the voter's input to the candidate list
  - Increment vote count if there's a match
- After collecting all votes:
  - Find the highest vote count
  - Print all candidates who match that count

Basic logic:
```c
typedef struct {
    string name;
    int votes;
} candidate;
```

This works well for small fixed-size inputs.

---

## ✅ Optimal Strategy

The initial approach is already efficient given the constraints:
- Max 9 candidates
- Vote count is linear in number of voters

What makes it optimal is:
- Validating input before processing (check if candidate exists)
- Encapsulating vote logic in a function like `vote(string name)`
- Separating vote tallying from result printing

Further optimization isn’t necessary unless scaling the system or handling dynamic input.

---

## 🧠 Heuristics & Insights

- When simulating real-world processes, **identify the actors** (candidates, voters) and their interactions (votes)  
- A **struct** is perfect for grouping related data (e.g. name and vote count)  
- When processing untrusted input (like user votes), **validation comes first**  
- Always **decouple computation from display logic** — tally, then print

---

## ⚠️ Common Pitfalls

- Not checking for invalid candidate names  
- Overwriting the vote count instead of incrementing  
- Failing to print all winners in a tie  
- Using the wrong comparison function for strings (e.g., `==` instead of `strcmp` in C)

---

## 🧭 Meta Insight

This problem introduces **data modeling through structs**, and simulates real-world processes using control structures.

It’s a foundational example of:
- Mapping input to structured data  
- Aggregating and comparing values  
- Implementing fair decision-making logic

---

## 🗃️ Notes

Plurality voting is simple but widely used — and also widely criticized for not representing voter preferences well. This sets up the need for **ranked** or **pairwise** systems like Tideman.

---

## 🔍 References

- CS50 PSet 3: Plurality — https://cs50.harvard.edu/x/2023/psets/3/plurality/
- Plurality voting (Wikipedia) — https://en.wikipedia.org/wiki/Plurality_voting