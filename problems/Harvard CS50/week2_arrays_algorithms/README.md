# Week 2 – Arrays & Algorithms

**Focus:** Fundamental data structures (strings, arrays) and basic algorithmic techniques — including frequency analysis, iteration over characters, and classic encryption.

This week transitions from *how to code* to *how to think algorithmically*. The problems introduce:
- String and array manipulation in C
- ASCII character encoding
- Cipher-based transformations
- Early steps in frequency analysis and algorithm design

## 🧠 Heuristics to Extract

Each problem builds pattern recognition in:
- Input sanitization and validation
- Transforming data structures (strings to arrays, characters to indexes)
- Mapping input through deterministic rules (e.g., Caesar shift)
- Thinking in terms of **O(n)** loops, character class filtering, and ASCII arithmetic

These skills transfer directly into fields like:
- Natural language processing
- Data parsing and transformation
- Lightweight encryption and input normalization

## 📂 Problems Covered

- `001-readability.md`: Analyze a block of text to determine its reading level using the Coleman–Liau index — involves counting words, letters, and sentences.
- `002-caesar.md`: Implement a classic Caesar cipher using modular arithmetic and ASCII manipulation.
- `003-substitution.md`: Extend the Caesar cipher into a key-driven substitution cipher — testing more advanced input validation and array-based lookup logic.

## 🗃️ Notes

This is your first exposure to **string-based data modeling**:
- Letters → numbers  
- Sentences → feature counts  
- Plaintext → encrypted text

From here on, you'll be regularly asked to:
- Design transformations  
- Build validations  
- Enforce constraints  
- Model the "flow" of data through controlled operations

## 📎 Resources

- [CS50 Week 2 Lecture](https://cs50.harvard.edu/x/2023/weeks/2/)
- [Readability](https://cs50.harvard.edu/x/2023/psets/2/readability/)
- [Caesar](https://cs50.harvard.edu/x/2023/psets/2/caesar/)
- [Substitution](https://cs50.harvard.edu/x/2023/psets/2/substitution/)