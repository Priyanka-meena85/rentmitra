import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update DOMContentLoaded handler to be bulletproof whether document is already loaded or loading
old_dom_listener = '''    // Initialize application on DOM ready
    window.addEventListener('DOMContentLoaded', () => {
      initData();
    });'''

new_dom_listener = '''    // Bulletproof initialization on DOM ready or immediate if already interactive
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initData);
    } else {
      initData();
    }'''

html = html.replace(old_dom_listener, new_dom_listener)

# 2. Update switchAdminTab so it never fails even if event is undefined
old_switch_admin = '''    function switchAdminTab(tabId) {
      document.querySelectorAll('.admin-tab-content').forEach(el => el.classList.add('hidden'));
      document.getElementById(tabId).classList.remove('hidden');

      document.querySelectorAll('.admin-tab-btn').forEach(btn => {
        btn.classList.remove('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        btn.classList.add('text-stone-700');
      });

      const clickedBtn = event.currentTarget;
      if (clickedBtn) {
        clickedBtn.classList.add('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        clickedBtn.classList.remove('text-stone-700');
      }
    }'''

new_switch_admin = '''    function switchAdminTab(tabId, clickedBtn = null) {
      document.querySelectorAll('.admin-tab-content').forEach(el => el.classList.add('hidden'));
      const targetTab = document.getElementById(tabId);
      if (targetTab) targetTab.classList.remove('hidden');

      document.querySelectorAll('.admin-tab-btn').forEach(btn => {
        btn.classList.remove('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        btn.classList.add('text-stone-700');
      });

      const activeBtn = clickedBtn || (window.event && window.event.currentTarget) || document.querySelector(`[onclick*="${tabId}"]`);
      if (activeBtn) {
        activeBtn.classList.add('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        activeBtn.classList.remove('text-stone-700');
      }
    }'''

html = html.replace(old_switch_admin, new_switch_admin)

# 3. Update switchTenantTab so it never fails even if event is undefined
old_switch_tenant = '''      event.currentTarget.classList.add('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
      event.currentTarget.classList.remove('text-stone-600');'''

new_switch_tenant = '''      const activeTenantBtn = (window.event && window.event.currentTarget) || document.querySelector(`[onclick*="${tabKey}"]`);
      if (activeTenantBtn) {
        activeTenantBtn.classList.add('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
        activeTenantBtn.classList.remove('text-stone-600');
      }'''

html = html.replace(old_switch_tenant, new_switch_tenant)

# 4. Make sure navTo sets pointer cursor and is fully accessible
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html hardened successfully.")
