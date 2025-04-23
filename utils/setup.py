# setup_leetcode_repo.py
"""
Script to set up a folder structure for LeetCode solutions.
Generates README.md and subfolders for easy/medium/hard problems.
"""

import os

BASE_DIR = "."
SUBFOLDERS = ["easy", "medium", "hard", "utils"]
README_CONTENT = """# LeetCode Solutions

This repository contains my solutions to LeetCode problems, categorized by difficulty (Easy, Medium, Hard). Each solution is implemented in Python.

## Structure

- `easy/` – Easy-level problems
- `medium/` – Medium-level problems
- `hard/` – Hard-level problems
- Each file is named after the problem (e.g., `two_sum.py`)

## Example

```bash
python easy/two_sum.py
```

## Notes

- Solutions may include comments for clarity.
- All code is written with readability and simplicity in mind.
- Some files might include brute-force + optimized solutions.

## License

MIT – feel free to use any code here.
"""

def create_structure():
    os.makedirs(BASE_DIR, exist_ok=True)
    for folder in SUBFOLDERS:
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w") as f:
        f.write(README_CONTENT)

    print(f"LeetCode repo structure created at: ./{BASE_DIR}/")

if __name__ == "__main__":
    create_structure()
