# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Sort spec compliance
if 'window.sortPublicProperties = handleSortChange;' not in c:
    c = c.replace(
        'function handleSortChange() {',
        'function sortPublicProperties() { return handleSortChange(); }\n    window.sortPublicProperties = handleSortChange;\n\n    function handleSortChange() {'
    )

# 2. Booked status compliance
if "prop.status = 'Booked'" not in c:
    c = c.replace(
        'currentSelectedProperty.status = "Booked";',
        "currentSelectedProperty.status = 'Booked';\n        const prop = currentSelectedProperty;\n        prop.status = 'Booked';"
    )

# 3. Late in red text-maroon-900 compliance
c = c.replace(
    'if (isLate) badgeClass = "bg-maroon-100 text-maroon-800 border-maroon-300 font-bold";',
    'if (isLate) badgeClass = "bg-maroon-100 text-maroon-900 border-maroon-300 font-bold";'
)

# 4. Responsive Agent Portal button
c = c.replace(
    '<span id="agentBtnText">Agent Portal (Sharma Ji)</span>',
    '<span id="agentBtnText"><span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span></span>'
)

# 5. Mobile dropdown: add Agent Portal button
mobile_portal_btn = """        <button onclick="toggleAgentPortal(); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-white bg-charcoal-900 hover:bg-terracotta-700 flex items-center gap-2.5 transition-colors shadow-sm">
          <i class="fa-solid fa-key text-amber-300 w-4"></i> Agent Portal (Sharma Ji Admin)
        </button>
        <a href="tel:+919876543210" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">"""

if 'Agent Portal (Sharma Ji Admin)' not in c:
    c = c.replace(
        '<a href="tel:+919876543210" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">',
        mobile_portal_btn
    )

# 6. Update toggleAgentPortal() text update for responsive span
old_toggle_text = """        agentBtnText.innerText = "Tenant Website";
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showToast("Sharma Ji Admin Portal khul gaya hai!", "info");
      } else {
        showPublicSite();
      }"""

new_toggle_text = """        agentBtnText.innerHTML = '<span class="hidden sm:inline">Tenant Website</span><span class="sm:hidden">Website</span>';
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showToast("Sharma Ji Admin Portal khul gaya hai!", "info");
      } else {
        agentBtnText.innerHTML = '<span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span>';
        showPublicSite();
      }"""

if old_toggle_text in c:
    c = c.replace(old_toggle_text, new_toggle_text)

# Also in navTo():
old_nav_text = """      const agentBtnText = document.getElementById('agentBtnText');
      if (agentBtnText) agentBtnText.innerText = "Agent Portal (Sharma Ji)";"""

new_nav_text = """      const agentBtnText = document.getElementById('agentBtnText');
      if (agentBtnText) agentBtnText.innerHTML = '<span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span>';"""

if old_nav_text in c:
    c = c.replace(old_nav_text, new_nav_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Successfully applied final polish to index.html')
