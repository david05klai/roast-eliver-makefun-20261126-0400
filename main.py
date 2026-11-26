from pathlib import Path

ROAST = (
    'Your crisper drawer is less a place for vegetables and more a '
    'witness-protection program for lettuce.'
)
def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError('entry must be 1 to 140 characters')
    output_file = Path('/output/entry.txt')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding='utf-8')


write_entry(ROAST)
