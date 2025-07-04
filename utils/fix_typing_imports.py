import os
import re

TYPING_NAMES = {"List", "Optional", "Dict", "Set", "Tuple", "Union", "Any", "Callable"}
IMPORT_LINE = "from typing import "


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    content = "".join(lines)

    used = {name for name in TYPING_NAMES if re.search(rf"\b{name}\b", content)}
    if not used:
        return  # Nothing to import

    already_imported = set()
    for line in lines:
        if line.strip().startswith(IMPORT_LINE):
            already_imported.update(map(str.strip, line[len(IMPORT_LINE):].split(",")))

    missing = used - already_imported
    if not missing:
        return  # All good

    # Insert import
    insert_line = f"{IMPORT_LINE}{', '.join(sorted(missing))}\n"
    for i, line in enumerate(lines):
        if line.strip() and not line.strip().startswith("#"):
            lines.insert(i, insert_line)
            break

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"✅ Fixed imports in {filepath}")


def run_on_dir(root):
    for folder, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py"):
                fix_file(os.path.join(folder, file))


if __name__ == "__main__":
    run_on_dir(".")
