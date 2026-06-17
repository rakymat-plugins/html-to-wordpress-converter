from html.parser import HTMLParser
from pathlib import Path


class SectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sections: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"section", "header", "footer", "main", "nav"}:
            return
        data = {key: value or "" for key, value in attrs}
        self.sections.append({
            "tag": tag,
            "id": data.get("id", ""),
            "class": data.get("class", ""),
        })


def analyze_html_sections(file_path: Path) -> list[dict[str, str]]:
    parser = SectionParser()
    parser.feed(file_path.read_text(encoding="utf-8", errors="ignore"))
    return parser.sections

