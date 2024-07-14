import re
from typing import Optional


def filter_files_names(files: list[str]) -> list[str]:
    filtered_names = []
    for file in files:
        match = re.match(r'^[1-2][0-9][0-9][0-9]_(BoysNames|GirlsNames)\.txt$', file)
        if match:
            filtered_names.append(file)
    return filtered_names


def parse_names_from_lines(line: str) -> Optional[tuple[str, int]]:
    line = line.strip()
    match = re.match(r'^[A-Z][a-z]+\s[0-9]+$', line)
    if match:
        name, qty = match.group(0).split()
        return name, int(qty)
    return None
