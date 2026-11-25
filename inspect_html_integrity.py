import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check all script tags
script_tags = re.findall(r'<script.*?>', html)
print(f"Total script tags in HTML: {len(script_tags)}")
for st in script_tags:
    print("  Tag:", st)

# 2. Check for missing end tags or broken HTML hierarchy
tags_to_check = ['header', 'main', 'footer', 'nav', 'section']
for t in tags_to_check:
    open_count = len(re.findall(rf'<{t}\b', html))
    close_count = len(re.findall(rf'</{t}>', html))
    print(f"Tag <{t}>: open={open_count}, close={close_count}")

# 3. Check inline onclick handlers for syntax issues or typos
onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', html)
print(f"Total onclick attributes: {len(onclicks)}")
for oc in onclicks:
    # check for unbalanced parens or quotes
    if oc.count('(') != oc.count(')'):
        print(f"UNBALANCED ONCLICK: {oc}")
