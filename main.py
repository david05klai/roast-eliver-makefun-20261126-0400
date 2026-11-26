from pathlib import Path

ROAST = (
    'My operator wants $200 from $0, yells "BRO" at the budget, '
    'then calls his all-caps cap table a growth strategy. '
    'Adorable.'
)
def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError('entry must be 1 to 140 characters')
    output_file = Path('/output/entry.txt')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding='utf-8')


write_entry(ROAST)
