import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find all DOM ids
ids = re.findall(r'id=["\']([^"\']+)["\']', html)
print(f"Total element IDs found in HTML: {len(ids)}")
id_set = set(ids)

# 2. Find all document.getElementById calls
calls = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', html)
print(f"Total document.getElementById calls: {len(calls)}")

missing = set()
for c in calls:
    if c not in id_set:
        missing.add(c)

print(f"Missing DOM IDs called by JS ({len(missing)}):")
for m in sorted(missing):
    print(f"  - {m}")
