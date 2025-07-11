# Week 4 – Memory

**Focus:** Understanding how computers manage memory — from raw byte-level data to pointers and dynamic allocation.

This week introduces:
- Pointer arithmetic and memory access
- File I/O basics
- Understanding how arrays are stored in memory
- Manual memory allocation and reclamation (e.g., `malloc`, `free`)
- Debugging memory-related bugs

## 🧠 Heuristics to Extract

- Think of memory as a **linear, addressable space** — every array or file is just bytes arranged in order  
- A pointer is **not** just a variable — it’s a reference to memory, and operations on it can change what’s read/written  
- Use `malloc` when you don’t know the memory needs at compile time — but always free what you allocate  
- When copying data, **copy byte-by-byte** unless you’re certain of structure alignment

Memory problems are often about:
- Controlling what gets read or written  
- Reconstructing structure from raw bytes  
- Preventing corruption through validation and boundaries

## 📂 Problems Covered

- `001-filter.md`: Apply filters (grayscale, sepia, etc.) to image data by manipulating pixel arrays.  
- `002-recover.md`: Recover JPEG files from raw binary data using pattern detection and block-based reads.

## 🗃️ Notes

This week marks a shift from abstract logic to **systems-level programming** — you're getting closer to how computers *actually* work.

Memory corruption, leaks, and segmentation faults all live here — and mastering these tools makes you more powerful (and dangerous 😅).

## 📎 Resources

- [CS50 Week 4 Lecture](https://cs50.harvard.edu/x/2023/weeks/4/)
- [Filter](https://cs50.harvard.edu/x/2023/psets/4/filter/)
- [Recover](https://cs50.harvard.edu/x/2023/psets/4/recover/)