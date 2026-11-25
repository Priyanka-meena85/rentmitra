import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navbar so buttons are visible on tablets and mobile menu has all routes
old_nav_classes = '<div class="hidden lg:flex items-center gap-1 bg-amber-100/60 p-1 rounded-full border border-amber-200/60">'
new_nav_classes = '<div class="hidden md:flex items-center gap-1 bg-amber-100/60 p-1 rounded-full border border-amber-200/60">'
html = html.replace(old_nav_classes, new_nav_classes, 1)

old_burger = '<button onclick="toggleMobileNav()" class="lg:hidden w-9 h-9 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm" aria-label="Toggle Menu">'
new_burger = '<button onclick="toggleMobileNav()" class="md:hidden w-9 h-9 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm" aria-label="Toggle Menu">'
html = html.replace(old_burger, new_burger, 1)

# 2. Add assignMistriModal before the script tag
assign_modal_html = '''
  <!-- ==================== MODAL 14: ASSIGN MISTRI (MAINTENANCE) ==================== -->
  <div id="assignMistriModal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4">
    <div onclick="closeAssignMistriModal()" class="fixed inset-0 bg-charcoal-950/60 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl max-w-sm w-full p-6 border border-amber-200 shadow-2xl z-10 animate-fade-in text-xs">
      <div class="flex items-center justify-between mb-4 pb-2 border-b border-amber-100">
        <div>
          <h3 class="font-serif text-lg font-bold text-charcoal-900">Assign Mistri</h3>
          <p class="text-[11px] text-stone-500">Ticket ID: <span id="assignModalTicketId" class="font-mono font-bold text-terracotta-700"></span></p>
        </div>
        <button onclick="closeAssignMistriModal()" class="w-8 h-8 rounded-full bg-cream-100 hover:bg-stone-200 flex items-center justify-center text-stone-600">
          <i class="fa-solid fa-xmark text-xs"></i>
        </button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="block font-bold text-stone-700 mb-1">Mistri Name & Contact</label>
          <select id="assignMistriSelect" class="w-full p-2.5 rounded-xl border border-amber-300 bg-cream-50 font-semibold text-xs">
            <option value="Raju Plumber (+91 98765 11223)">Raju Plumber (+91 98765 11223)</option>
            <option value="Mohan Electrician (+91 98765 33445)">Mohan Electrician (+91 98765 33445)</option>
            <option value="Aslam Carpenter (+91 98765 55667)">Aslam Carpenter (+91 98765 55667)</option>
            <option value="Vinod AC Specialist (+91 98765 77889)">Vinod AC Specialist (+91 98765 77889)</option>
          </select>
        </div>
        <button onclick="confirmAssignMistri()" class="w-full py-2.5 rounded-full bg-terracotta-700 hover:bg-terracotta-800 text-white font-bold shadow-sm transition-all mt-2">
          Confirm Assignment
        </button>
      </div>
    </div>
  </div>
'''

html = html.replace('  <!-- ==================== JAVASCRIPT LOGIC', assign_modal_html + '\n  <!-- ==================== JAVASCRIPT LOGIC', 1)

# 3. Enhance navTo function to support section navigation with perfect visibility
new_nav_to = '''    // ================= CENTRAL SPA NAVIGATION ROUTER =================
    function navTo(section) {
      const publicView = document.getElementById('publicView');
      const agentDashboardView = document.getElementById('agentDashboardView');
      const tenantPortalPage = document.getElementById('tenantPortalPageSection');
      const homeSection = document.getElementById('home');
      const propertiesSection = document.getElementById('properties-section');
      const howItWorksSection = document.getElementById('how-it-works');
      const testimonialsSection = document.getElementById('testimonials');
      const footerSection = document.querySelector('footer');

      // Hide agent dashboard
      if (agentDashboardView) agentDashboardView.classList.add('hidden');
      if (publicView) publicView.classList.remove('hidden');

      const agentBtnText = document.getElementById('agentBtnText');
      if (agentBtnText) agentBtnText.innerText = "Agent Portal (Sharma Ji)";

      // Reset desktop active nav indicators
      document.querySelectorAll('.nav-link').forEach(btn => {
        btn.classList.remove('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
      });

      if (section === 'tenantPortal') {
        // Show dedicated tenant portal interface
        if (tenantPortalPage) tenantPortalPage.classList.remove('hidden');
        if (homeSection) homeSection.classList.add('hidden');
        if (propertiesSection) propertiesSection.classList.add('hidden');
        if (howItWorksSection) howItWorksSection.classList.add('hidden');
        if (testimonialsSection) testimonialsSection.classList.add('hidden');
        if (footerSection) footerSection.classList.add('hidden');

        const activeBtn = document.getElementById('navBtn-tenantPortal');
        if (activeBtn) activeBtn.classList.add('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showToast("Tenant Portal khul gaya hai!", "info");
      } else {
        // Show regular public site sections
        if (tenantPortalPage) tenantPortalPage.classList.add('hidden');
        if (homeSection) homeSection.classList.remove('hidden');
        if (propertiesSection) propertiesSection.classList.remove('hidden');
        if (howItWorksSection) howItWorksSection.classList.remove('hidden');
        if (testimonialsSection) testimonialsSection.classList.remove('hidden');
        if (footerSection) footerSection.classList.remove('hidden');

        if (section === 'home') {
          const activeBtn = document.getElementById('navBtn-home');
          if (activeBtn) activeBtn.classList.add('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
          window.scrollTo({ top: 0, behavior: 'smooth' });
        } else if (section === 'properties') {
          const activeBtn = document.getElementById('navBtn-properties');
          if (activeBtn) activeBtn.classList.add('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
          if (propertiesSection) propertiesSection.scrollIntoView({ behavior: 'smooth' });
        } else if (section === 'howItWorks') {
          const activeBtn = document.getElementById('navBtn-howItWorks');
          if (activeBtn) activeBtn.classList.add('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
          if (howItWorksSection) howItWorksSection.scrollIntoView({ behavior: 'smooth' });
        } else if (section === 'reviews') {
          const activeBtn = document.getElementById('navBtn-reviews');
          if (activeBtn) activeBtn.classList.add('bg-white', 'text-terracotta-700', 'shadow-sm', 'font-bold');
          if (testimonialsSection) testimonialsSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    }'''

html = re.sub(r'    // ================= CENTRAL SPA NAVIGATION ROUTER =================.*?function toggleMobileNav\(\)', new_nav_to + '\n\n    function toggleMobileNav()', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html fixed successfully.")
