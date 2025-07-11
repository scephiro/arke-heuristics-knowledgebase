---
id: "CS50-W4-002"
title: "Recover"
source: "CS50"
difficulty: "Medium-Hard"
tags: ["file I/O", "memory", "binary data", "forensics", "pattern recognition"]
core_problem: "Recover JPEG files from a raw binary memory card image by identifying signature byte patterns"
status: "complete"
---

## 🧩 Problem Summary

You're given a raw memory dump (binary file) from a camera's memory card. Your job is to **recover JPEG images** by scanning the file block-by-block and extracting sequences that represent valid JPEGs.

Key idea:
- JPEG files start with a specific **signature** — a series of bytes that can be detected in binary data:
  - Starts with: `0xff 0xd8 0xff` followed by `0xe0` to `0xef`

---

## 🔄 Initial Approach

- Read the file in 512-byte chunks (blocks) — this is a standard block size for FAT file systems
- Check each block for the **JPEG header signature**
- When a signature is found:
  - If a file is already open, close it
  - Start a new file and begin writing
- If not a header, and you're already writing, append the block to the current file

This approach avoids having to buffer entire files in memory, which is critical when working with raw data.

---

## ✅ Optimal Strategy

The initial method is pretty close to optimal given the nature of the problem.

Best practices include:
- Use `fread()` with care: always check return value to avoid overreading
- Use a `BYTE` buffer (e.g., `typedef uint8_t BYTE;`) to represent raw blocks
- Use formatted filenames like `###.jpg` to name each recovered image
- Handle edge cases like:
  - Multiple JPEGs found in succession
  - No JPEGs found at all
  - Corrupted headers

---

## 🧠 Heuristics & Insights

- When recovering structured data from binary:
  - Look for **byte-level signatures or magic numbers**
  - Process in **block-sized chunks** that match the file system layout
- File carving doesn’t require knowing the full structure — just the start and end boundaries
- Keep state:
  - Are we inside a file?
  - Do we need to close the previous one?
- Reuse small buffers and avoid dynamic memory where possible — it keeps things simple

---

## ⚠️ Common Pitfalls

- Not checking all 4 bytes of the JPEG signature properly  
- Forgetting to close the last image file  
- Appending to a file that was never opened  
- Writing the first block of a new JPEG to the wrong file  
- Confusing file pointers vs block buffers

---

## 🧭 Meta Insight

This problem simulates **real digital forensics** — recovering data from damaged drives or deleted storage.

It introduces:
- Reading raw binary data
- Pattern detection at the byte level
- Simple but powerful file carving techniques

It’s a bridge between **memory-level programming** and **real-world recovery tools** like PhotoRec.

---

## 🗃️ Notes

- This is your first low-level data recovery tool  
- You’re operating below the OS — treating files as pure memory

This kind of thinking is foundational for:
- Security engineering  
- Malware analysis  
- File systems and OS development

---

## 🔍 References

- CS50 PSet 4: Recover — https://cs50.harvard.edu/x/2023/psets/4/recover/
- JPEG file format — https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format
- File carving — https://en.wikipedia.org/wiki/File_carving