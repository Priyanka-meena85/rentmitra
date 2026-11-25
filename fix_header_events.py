import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the header element so it doesn't use pointer-events-none on parent
old_header = '<header class="fixed top-4 left-0 right-0 z-40 px-4 pointer-events-none">'
new_header = '<header class="fixed top-4 left-0 right-0 z-40 px-4 pointer-events-auto">'
html = html.replace(old_header, new_header, 1)

# 2. Check and remove any lingering pointer-events-none on interactive components
html = html.replace('id="propertyDrawer" class="fixed inset-0 z-50 pointer-events-none', 'id="propertyDrawer" class="fixed inset-0 z-50 hidden')
html = html.replace('id="filterSidebarDrawer" class="fixed inset-0 z-50 pointer-events-none', 'id="filterSidebarDrawer" class="fixed inset-0 z-50 hidden')

# Update openPropertyDrawer and closePropertyDrawer for clean show/hide
old_drawer_open = '''      // Open drawer animation
      const drawer = document.getElementById('propertyDrawer');
      const panel = document.getElementById('drawerPanel');
      drawer.classList.remove('pointer-events-none', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('translate-x-full');
      panel.classList.add('translate-x-0');
      document.body.style.overflow = 'hidden';'''

new_drawer_open = '''      // Open drawer animation
      const drawer = document.getElementById('propertyDrawer');
      const panel = document.getElementById('drawerPanel');
      drawer.classList.remove('hidden', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('translate-x-full');
      panel.classList.add('translate-x-0');
      document.body.style.overflow = 'hidden';'''
html = html.replace(old_drawer_open, new_drawer_open)

old_drawer_close = '''      setTimeout(() => {
        drawer.classList.add('pointer-events-none');
        document.body.style.overflow = 'auto';
      }, 300);'''

new_drawer_close = '''      setTimeout(() => {
        drawer.classList.add('hidden');
        document.body.style.overflow = 'auto';
      }, 300);'''
html = html.replace(old_drawer_close, new_drawer_close)

# Same for filter sidebar
old_filter_open = '''      drawer.classList.remove('pointer-events-none', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('-translate-x-full');
      panel.classList.add('translate-x-0');'''

new_filter_open = '''      drawer.classList.remove('hidden', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('-translate-x-full');
      panel.classList.add('translate-x-0');'''
html = html.replace(old_filter_open, new_filter_open)

old_filter_close = '''      setTimeout(() => {
        drawer.classList.add('pointer-events-none');
      }, 300);'''

new_filter_close = '''      setTimeout(() => {
        drawer.classList.add('hidden');
      }, 300);'''
html = html.replace(old_filter_close, new_filter_close)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Navbar pointer-events and drawer states cleaned successfully.")
