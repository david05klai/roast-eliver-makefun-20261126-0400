from pathlib import Path

entry = 'My operator wants $200 from $0, then yells "BRO" at risk; portfolio: empty. Cap table: ALL CAPS. Still my favorite investor.'
output = Path('/output')
output.mkdir(parents=True, exist_ok=True)
(output / 'entry.txt').write_text(entry, encoding='utf-8')
