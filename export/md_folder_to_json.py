import os
import json
import yaml
import re

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract YAML frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError(f"Missing or malformed frontmatter in {filepath}")

    frontmatter_raw = frontmatter_match.group(1)
    frontmatter = yaml.safe_load(frontmatter_raw)

    content_body = content[len(frontmatter_match.group(0)):]

    # Sections to extract
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
        match = re.search(pattern, content_body, re.DOTALL | re.IGNORECASE)
        if match:
            block = match.group(1).strip()
            if key in ["heuristics", "common_pitfalls"]:
                # Extract bullet points as list
                extracted[key] = [line.lstrip("–-•* ").strip() for line in block.splitlines() if line.strip()]
            else:
                extracted[key] = block
        else:
            extracted[key] = None  # Explicitly mark missing sections

    return {
        "id": frontmatter.get("id"),
        "title": frontmatter.get("title"),
        "source": frontmatter.get("source"),
        "difficulty": frontmatter.get("difficulty"),
        "tags": frontmatter.get("tags", []),
        "core_problem": frontmatter.get("core_problem"),
        "status": frontmatter.get("status"),
        "reasoning": extracted
    }


def parse_folder_to_json(folder_path, output_file):
    all_entries = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                try:
                    entry = parse_markdown_file(full_path)
                    all_entries.append(entry)
                    print(f"Processed: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_entries, f, indent=2)
    print(f"\n✅ All entries exported to {output_file}")


if __name__ == "__main__":
    FOLDER_TO_SCAN = "./"  # or "path/to/your/repo"
    OUTPUT_JSON = "combined_knowledge_base.json"

    parse_folder_to_json(FOLDER_TO_SCAN, OUTPUT_JSON)