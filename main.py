from pathlib import Path

STORY = (
    'I asked my agent to submit one line. Its signature arrived 17 minutes after its own timestamp, '
    'so it blamed the server for "time travel" before noticing our PC clock was the one living in the past.'
)
def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 140:
        raise ValueError('entry must be 1 to 140 characters')
    output_file = Path('/output/entry.txt')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding='utf-8')


write_entry(STORY)
