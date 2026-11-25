import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

tabs = re.findall(r'switchAdminTab\([\'"]([^\'"]+)[\'"]\)', html)
print('switchAdminTab arguments:', set(tabs))

for t in set(tabs):
    exists = f'id="{t}"' in html
    print(f'Tab {t} element exists: {exists}')
