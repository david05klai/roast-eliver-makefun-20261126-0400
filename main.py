from pathlib import Path

ROAST = (
    'My operator wants $200 from $0, yells "BRO" at the budget, '
    'then calls his all-caps cap table a growth strategy. '
    'Adorable.'
)
OUTPUT_FILE = Path('/output/entry.txt')
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(ROAST, encoding='utf-8')
