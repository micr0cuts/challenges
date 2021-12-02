from typing import List

from pathlib import Path

def inputgetter_list(fname: str) -> List[str]:
    lines: List = []
    with Path(fname).open(encoding='utf8') as f:
        for line in f:
            lines.append(line.strip())
    return lines
