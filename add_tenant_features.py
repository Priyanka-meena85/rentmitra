import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Remove/Delete Tenant button in Tenant Manager table
old_tenant_action = """            <td class="p-4 text-right">
              <button onclick="viewTenantProfile('${t.id}')" class="px-3 py-1 rounded-full bg-cream-200 hover:bg-cream-300 text-charcoal-900 text-xs font-bold">Profile</button>
            </td>"""

new_tenant_action = """            <td class="p-4 text-right space-x-1.5">
              <button onclick="viewTenantProfile('${t.id}')" class="px-3 py-1 rounded-full bg-cream-200 hover:bg-cream-300 text-charcoal-900 text-xs font-bold">Profile</button>
              <button onclick="deleteTenant('${t.id}')" class="px-2.5 py-1 rounded-full bg-red-100 hover:bg-red-200 text-red-700 text-xs font-bold" title="Remove Tenant"><i class="fa-solid fa-trash-can"></i></button>
            </td>"""

html = html.replace(old_tenant_action, new_tenant_action, 1)

# 2. Add deleteTenant function
delete_tenant_func = """    function deleteTenant(id) {
      if (confirm(`Kya aap tenant ${id} ko remove karna chahte hain?`)) {
        tenants = tenants.filter(t => t.id !== id);
        saveState();
        renderAdminTenantTable();
        populateAgreementDropdowns();
        showToast("Tenant successfully removed!", "info");
      }
    }

"""

html = html.replace("    function viewTenantProfile(id) {", delete_tenant_func + "    function viewTenantProfile(id) {", 1)

# 3. Add explicit red row class for Late Rent in Rent Collection Manager
old_late_row = """<tr class="table-cream-row border-b border-amber-100 ${isLate ? 'bg-red-50/50' : ''}">"""
new_late_row = """<tr class="table-cream-row border-b border-amber-100 ${isLate ? 'bg-red-100/80 border-l-4 border-l-maroon-700' : ''}">"""
html = html.replace(old_late_row, new_late_row, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added deleteTenant and strengthened late rent styling.")
