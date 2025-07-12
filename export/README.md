# Markdown to JSON Converter

This folder contains Python scripts to convert Markdown problem entries into JSON format  
following the Reasoning Vault schema.

---

## Files

- `md_to_json.py` — Converts a **single** Markdown file to JSON.  
- `md_folder_to_json.py` — Recursively converts **all** Markdown files in a folder to a single combined JSON array.

---

## How to Use `md_to_json.py` (Single File Converter)

1. **Prepare your Markdown file(s)**  
   Place your `.md` file (e.g., `001-mario-pyramid.md`) in this folder or update the script path accordingly.

2. **Install dependencies**  
    Make sure you have Python installed (3.7+) and install dependencies:  

```bash
   pip install pyyaml
```

3. **Run the converter**
    Update the INPUT_FILE variable in md_to_json.py with your Markdown filename.
    Then run:

```bash
    python md_to_json.py
 ```

This will create a .json file with the same base name in this folder.

4. **Check the output**
    The JSON file matches the vault schema and can be used for AI training, indexing, or integration.

⸻

## How to Use md_folder_to_json.py (Batch Folder Converter)

This script recursively scans a folder (and subfolders) for all Markdown .md files following the Reasoning Vault format,
converts each into JSON objects, and outputs one combined JSON array file.
	1.	Place md_folder_to_json.py in your repository or export folder.
	2.	Update the FOLDER_TO_SCAN variable in the script to the folder where your .md files reside (default is current directory).
	3.	Run the script:
``` bash
python md_folder_to_json.py
```
	4.	The script will create combined_knowledge_base.json containing all parsed entries.

⸻

## Features
	•	Processes single or multiple Markdown files into JSON
	•	Handles missing sections gracefully by setting them to null in JSON
	•	Prints progress and errors during processing
	•	Easy to modify for custom workflows

⸻

## Requirements
	•	Python 3.7+
	•	pyyaml package installed via:
``` bash
pip install pyyaml
```

⸻

## Notes
	•	Make sure your Markdown files follow the frontmatter and section naming conventions strictly for accurate parsing.
	•	Supported sections:
	•	Problem Summary
	•	Initial Approach
	•	Optimal Strategy
	•	Heuristics & Insights
	•	Common Pitfalls
	•	Meta Insight
	•	Notes

⸻

Last updated: July 2025

---