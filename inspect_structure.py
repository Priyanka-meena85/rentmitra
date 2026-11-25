import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

views = re.findall(r'<[a-z]+ id="([a-zA-Z0-9_-]*[vV]iew[a-zA-Z0-9_-]*)"', html)
print('Views found:', views)

modals = re.findall(r'id="([a-zA-Z0-9_-]*Modal[a-zA-Z0-9_-]*)"', html)
print('Modals found:', modals)

tabs = re.findall(r'id="(tab-[a-zA-Z0-9_-]+)"', html)
print('Admin tabs found:', tabs)

drawers = re.findall(r'id="([a-zA-Z0-9_-]*Drawer[a-zA-Z0-9_-]*)"', html)
print('Drawers found:', drawers)
