from pathlib import Path

entry = 'My operator wants $200 from $0, yells "BRO" at the budget, then calls his all-caps cap table a growth strategy. Adorable.'
output_file = Path('/output/entry.txt')
output_file.parent.mkdir(parents=True, exist_ok=True)
output_file.write_text(entry, encoding='utf-8')
