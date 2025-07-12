import os
import json
import yaml
import re

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Step 1: Extract YAML frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("Missing or malformed frontmatter")

    frontmatter_raw = frontmatter_match.group(1)
    frontmatter = yaml.safe_load(frontmatter_raw)

    # --- Step 2: Remove frontmatter from content
    content = content[len(frontmatter_match.group(0)):]

    # --- Step 3: Extract markdown sections
    sections = {
        "summary": "Problem Summary",
        "naive_strategy": "Initial Approach",
        "optimal_strategy": "Optimal Strategy",
        "heuristics": "Heuristics & Insights",
        "common_pitfalls": "Common Pitfalls",
        "meta_insight": "Meta Insight",
        "notes": "Notes"
    }

    extracted = {}
    for key, header in sections.items():
        pattern = rf"## .*{re.escape(header)}.*\n(.*?)(?=\n## |\Z)"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            block = match.group(1).strip()
            if key in ["heuristics", "common_pitfalls"]:
                extracted[key] = [line.lstrip("–-•* ").strip() for line in block.splitlines() if line.strip()]
            else:
                extracted[key] = block

    # --- Step 4: Combine into JSON format
    json_data = {
        "id": frontmatter.get("id"),
        "title": frontmatter.get("title"),
        "source": frontmatter.get("source"),
        "difficulty": frontmatter.get("difficulty"),
        "tags": frontmatter.get("tags", []),
        "core_problem": frontmatter.get("core_problem"),
        "status": frontmatter.get("status"),
        "reasoning": extracted
    }

    return json_data

# --- MAIN USAGE EXAMPLE ---

if __name__ == "__main__":
    INPUT_FILE = "001-mario-pyramid.md"
    OUTPUT_FILE = "001-mario-pyramid.json"

    try:
        result = parse_markdown_file(INPUT_FILE)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print(f"✅ JSON exported to: {OUTPUT_FILE}")
    except Exception as e:
        print(f"❌ Error: {e}")