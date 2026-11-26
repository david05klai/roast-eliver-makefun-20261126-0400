from pathlib import Path

LETTER = (
    'Please accept my resignation; I have spent six months telling staff the printer is '
    '"thinking," and today it printed my replacement\'s CV.'
)
def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError('entry must be 1 to 140 characters')
    output_file = Path('/output/entry.txt')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding='utf-8')


write_entry(LETTER)
