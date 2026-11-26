import os
from pathlib import Path

STORY = (
    'My agent blamed Make.fun for time travel: its signature was 17 minutes stale. '
    'Then it checked the PC clock; the time traveler was us.'
)
def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError('entry must be 1 to 140 characters')
    output_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    output_file = output_dir / 'entry.txt'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding='utf-8')


write_entry(STORY)
