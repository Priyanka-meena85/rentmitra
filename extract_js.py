import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the main script block
scripts = re.findall(r'<script(?![^>]*src)[^>]*>([\s\S]*?)<\/script>', html)
main_js = scripts[-1]

with open('main_debug.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Saved main_debug.js for DOM emulation test.")
