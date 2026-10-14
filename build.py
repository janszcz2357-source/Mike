"""Wrap src/page.html (a body fragment with its own <title>, <link> and <style>)
into a complete, standalone index.html.

Usage: python3 build.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).parent
fragment = (ROOT / "src" / "page.html").read_text(encoding="utf-8")

# Everything before the first visible element belongs in <head>.
split = fragment.index('<a class="skip"')
head, body = fragment[:split].strip(), fragment[split:].strip()
head = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", head)

description = (
    "Unofficial, sourced career file on British racing driver Mike Wilds: "
    "Formula One 1974-76, Le Mans, historic racing, titles and his memoir."
)
favicon = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Ccircle cx='16' cy='16' r='15' fill='%23F5C400' stroke='%23121108' stroke-width='2'/%3E"
    "%3Cpath d='M16 6 21 16 16 26 11 16Z' fill='%23121108'/%3E%3C/svg%3E"
)

page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{description}">
<meta property="og:title" content="Mike Wilds Career File">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta name="theme-color" content="#F5C400">
<link rel="icon" href="{favicon}">
{head}
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"wrote index.html ({len(page):,} bytes)")
