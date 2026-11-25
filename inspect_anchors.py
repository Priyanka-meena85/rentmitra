import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

hrefs = re.findall(r'href="#([^"]*)"', html)
print('Total hash hrefs:', len(hrefs))
missing = []
for h in set(hrefs):
    if h and h != '' and f'id="{h}"' not in html:
        missing.append(h)

print('Missing anchor targets:', missing)
