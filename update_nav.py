# Python script to upgrade index.html with:
# 1. Responsive Navbar with active indicators and Mobile Drawer Menu
# 2. navTo('home' | 'properties' | 'howItWorks' | 'reviews' | 'tenantPortal' | 'agentPortal')
# 3. Full-page dedicated Tenant Portal View (id="tenantPortalView")
# 4. Global navigation sync

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect the exact lines to replace
print("Original size:", len(content))
