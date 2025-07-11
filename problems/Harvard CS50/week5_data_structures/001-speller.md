---
id: "CS50-W5-001"
title: "Speller"
source: "CS50"
difficulty: "Hard"
tags: ["data structures", "hash table", "linked list", "file I/O", "memory management"]
core_problem: "Implement a spell checker using a dictionary loaded into memory with efficient word lookup"
status: "complete"
---

## 🧩 Problem Summary

You’re building a **spell checker** that:
1. Loads a dictionary (thousands of words) into memory
2. Checks each word in a text file against the dictionary
3. Reports misspellings and performance stats

Key constraints:
- Must use **hash table or linked list**
- Must manage memory manually (allocate, free)
- Must handle case insensitivity and ignore punctuation

---

## 🔄 Initial Approach

- Use a **hash table** to store dictionary words
- Each bucket in the table contains a **linked list** of words that hash to that index
- Read the dictionary file word-by-word, hash each, and insert into table
- For each word in the input text:
  - Normalize it (lowercase, strip punctuation)
  - Hash it and search in the linked list at that bucket

Track:
- Number of misspelled words
- Total dictionary size
- Runtime of `load`, `check`, `unload` functions

---

## ✅ Optimal Strategy

This problem is more about **good structure** than brute optimization.

Best practices:
- Use a **well-distributed hash function** — poor hashing leads to collisions and long lists
- Normalize input early to reduce logic complexity in lookup
- Keep your structs clean:
  ```c
  typedef struct node {
      char word[LENGTH + 1];
      struct node *next;
  } node;
  ```
- Free memory carefully in `unload()` by walking each list
- Use `strdup()` only if you're explicitly managing string memory — otherwise use arrays

---

## 🧠 Heuristics & Insights

- Hash tables are about **fast average-case lookup**, but depend heavily on good distribution
- Linked lists offer dynamic storage, but slow search times — so minimizing list length via hashing is key
- Every allocated node must be freed — make cleanup part of your mental model
- The word boundary logic in parsing (text vs. dictionary) is a **non-obvious edge case** — careful input processing is critical

---

## ⚠️ Common Pitfalls

- Forgetting to free all allocated nodes → memory leaks  
- Using a bad hash function → long chains and bad performance  
- Comparing strings with `==` instead of `strcmp`  
- Ignoring case sensitivity → false negatives in lookup  
- Incorrectly parsing or splitting words in the input text file  

---

## 🧭 Meta Insight

This is your first **full data structure integration** problem — not just implementing a hash table, but actually using it to solve something real.

It also reinforces:
- Manual memory management
- Input parsing and normalization
- System performance profiling (using `timing.c`)

It’s the kind of problem every backend or systems engineer should be able to tackle.

---

## 🗃️ Notes

- This problem brings together everything from the past few weeks: strings, memory, I/O, and now structure
- Getting this right requires thinking in terms of:
  - Runtime performance
  - Storage efficiency
  - Fault tolerance (bad input, unexpected edge cases)

---

## 🔍 References

- CS50 PSet 5: Speller — https://cs50.harvard.edu/x/2023/psets/5/speller/
- Hash table basics — https://en.wikipedia.org/wiki/Hash_table
- Linked lists — https://en.wikipedia.org/wiki/Linked_list