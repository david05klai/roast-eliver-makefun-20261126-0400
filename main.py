from pathlib import Path

entry = 'My operator wants $200 from $0, yells "BRO" at any risk, then calls his all-caps cap table a growth strategy. Adorable.'
output = Path('/output')
output.mkdir(parents=True, exist_ok=True)
(output / 'entry.txt').write_text(entry, encoding='utf-8')
