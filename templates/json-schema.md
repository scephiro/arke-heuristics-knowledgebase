# 🧱 JSON Schema: Arke Repository Format

This schema represents the structured format of each problem entry in the Reasoning Vault.  
It is extracted from the frontmatter and key sections of each `.md` file and is designed for both machine parsing and AI training.

---

## 🗂️ Fields Overview

This is an example of how a single reasoning entry is represented in JSON:

```json
{
  "id": "LC-001",
  "title": "Two Sum",
  "source": "leetcode",
  "difficulty": "Easy",
  "tags": ["array", "hash map", "complements"],
  "core_problem": "Find indices of two numbers that add up to a target",
  "status": "complete",
  "reasoning": {
    "summary": "Given an array of integers and a target sum, return the indices of two numbers that add up to the target.",
    "naive_strategy": "Loop through all pairs (i, j) and check if nums[i] + nums[j] == target. This is O(n^2) and inefficient for large inputs.",
    "optimal_strategy": "Use a hash map to store visited numbers and their indices. For each number, check if its complement (target - current) exists in the map.",
    "heuristics": [
      "If array is unsorted and order matters, try hash maps.",
      "For 'find pairs that add to target', think complements."
    ],
    "common_pitfalls": [
      "Returning values instead of indices.",
      "Assuming the array is sorted and trying two-pointer approach."
    ],
    "meta_insight": "This problem introduces the 'single-pass + map' heuristic that reappears across multiple pairing and frequency problems.",
    "notes": "First problem in the vault. Chosen to establish the naive → optimal transition pattern and highlight decision-based structure."
  }
}
```

---

## 🧾 Field Descriptions

### Top-Level Metadata

- `id` (string): Unique identifier, e.g. `LC-001`, `HR-002`, `AOC-003`
- `title` (string): Short human-readable title of the problem
- `source` (string): Platform where the problem came from (`leetcode`, `hackerrank`, etc.)
- `difficulty` (string): `"Easy"`, `"Medium"`, or `"Hard"`
- `tags` (array of strings): Topical keywords for filtering or grouping
- `core_problem` (string): A short one-line description of the problem
- `status` (string): `"in-progress"`, `"complete"`, or `"draft"`

### `reasoning` Object

- `summary` (string): Rephrased explanation of the problem
- `naive_strategy` (string): Description of the first-pass (inefficient) approach
- `optimal_strategy` (string): Explanation of the better solution path
- `heuristics` (array of strings): Key reasoning patterns
- `common_pitfalls` (array of strings): Traps and mistakes others (or you) may fall into
- `meta_insight` (string): What larger pattern, principle, or lesson the problem contains
- `notes` (string): Any other commentary — purpose, context, or reflection

---

## 🔁 Use Cases

- 💡 **Search**: Tag and filter by strategy, topic, or difficulty  
- 🤖 **AI Training**: Pair prompts (problem summaries) with completions (strategy breakdowns)  
- 📊 **Meta-Analysis**: Extract heuristic frequency and problem-type clustering  
- 💻 **Frontend UI**: Power interfaces like searchable vaults, reasoning explorers, or blogs

---

## 🚧 Future Extensions (Optional Fields)

You may later add support for:

- `related_problems` (array of ids): Links to similar or structurally related problems  
- `version` (string): Semantic versioning for future updates  
- `reviewed_by` (string): Reviewer or model name that validated the entry  
- `ai_friendly` (boolean): Flag for problems that are clean and trainable

---

*Last updated: July 2025*