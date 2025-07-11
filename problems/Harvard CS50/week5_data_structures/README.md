# Week 5 – Data Structures

**Focus:** Introduction to classic data structures — how to store, search, and organize data efficiently.

This week dives into:
- Hash tables and linked lists
- Trade-offs between data access speed and memory use
- Searching and inserting elements into dynamic structures
- Applying these structures in real-world tasks like spell checking

## 🧠 Heuristics to Extract

- Know when to use an array vs. a linked list vs. a hash table  
- Trade speed for flexibility: arrays are fast but fixed-size; linked lists are dynamic but slower  
- Hashing is fast, but the hash function matters — good hashing minimizes collisions  
- Always manage memory manually when using `malloc` and `free` — memory leaks are silent but deadly  
- Traversal and insertion logic differ drastically between arrays and pointer-based structures

This week emphasizes **mental models** of data movement, memory layout, and pointer chaining.

## 📂 Problems Covered

- `001-speller.md`: Implement a spell checker by loading a large dictionary file into memory using a hash table or linked list, then checking words in a given text file for correctness.

## 🗃️ Notes

This week builds your systems intuition:
- You’re no longer just solving problems — you’re **designing systems**
- Data structures are *tools*, and choosing the right one is half the problem

It’s also your first step toward topics like:
- Trees
- Graphs
- Caching systems
- Database indexing

## 📎 Resources

- [CS50 Week 5 Lecture](https://cs50.harvard.edu/x/2023/weeks/5/)
- [Speller](https://cs50.harvard.edu/x/2023/psets/5/speller/)