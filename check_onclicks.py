import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all onclicks
onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', html)
print(f"Total onclick attributes in HTML: {len(onclicks)}")

unique_calls = set()
for oc in onclicks:
    # get fn name
    for part in oc.split(';'):
        part = part.strip()
        if part:
            fn = part.split('(')[0].strip()
            if fn and not fn.startswith('//'):
                unique_calls.add(fn)

print(f"Unique functions called: {len(unique_calls)}")

missing = []
for fn in sorted(unique_calls):
    pattern1 = rf'function\s+{re.escape(fn)}\b'
    pattern2 = rf'\b{re.escape(fn)}\s*=\s*(function|\()'
    pattern3 = rf'window\.{re.escape(fn)}\s*='
    if not (re.search(pattern1, html) or re.search(pattern2, html) or re.search(pattern3, html)):
        missing.append(fn)

print(f"Missing functions ({len(missing)}): {missing}")
