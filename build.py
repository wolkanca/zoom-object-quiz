from pathlib import Path
import json

root = Path(__file__).parent
items = json.loads((root / "objects.json").read_text(encoding="utf-8"))
assert len(items) >= 10
assert len({item["id"] for item in items}) == len(items)
for item in items:
    assert item["answer"] in item["options"] and len(item["options"]) == 4
    assert len(item["anchor"]) == 2

template = (root / "index.template.html").read_text(encoding="utf-8")
assert template.count("__EMBED_DATA__") == 1
payload = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
(root / "index.html").write_text(template.replace("__EMBED_DATA__", payload), encoding="utf-8")
print(f"Generated index.html with {len(items)} questions")
