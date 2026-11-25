import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Target the floating navbar header
old_nav_pattern = r'<!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->.*?<!-- ==================== NOTIFICATION TOAST ==================== -->'

new_nav = '''<!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-4 left-0 right-0 z-40 px-4 pointer-events-none">
    <nav class="max-w-6xl mx-auto glass-pill rounded-full px-4 sm:px-6 py-2.5 sm:py-3 flex items-center justify-between shadow-warm-soft pointer-events-auto border border-amber-200/80 transition-all duration-300">
      
      <!-- Brand Logo -->
      <a href="javascript:void(0)" onclick="navTo('home')" class="flex items-center gap-2.5 sm:gap-3 group cursor-pointer" title="RentWala Home">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-gradient-to-tr from-terracotta-700 to-terracotta-500 text-white flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-house-chimney text-base sm:text-lg"></i>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-serif text-lg sm:text-xl font-bold tracking-tight text-charcoal-900">RentWala</span>
            <span class="inline-flex items-center px-1.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-semibold bg-olive-100 text-olive-800 border border-olive-600/30">
              <i class="fa-solid fa-circle-check text-[9px] mr-1 text-olive-700"></i>Verified
            </span>
          </div>
          <p class="text-[10px] sm:text-[11px] font-medium text-stone-500 -mt-1 tracking-wider uppercase">Sharma Rentals</p>
        </div>
      </a>

      <!-- Middle Navigation Links (Desktop) -->
      <div class="hidden lg:flex items-center gap-1 bg-amber-100/60 p-1 rounded-full border border-amber-200/60">
        <button id="navBtn-home" onclick="navTo('home')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/80 transition-all">Home</button>
        <button id="navBtn-properties" onclick="navTo('properties')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/80 transition-all">Ghar Dhoondo</button>
        <button id="navBtn-howItWorks" onclick="navTo('howItWorks')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/80 transition-all">Kaise Kaam Karta Hai</button>
        <button id="navBtn-reviews" onclick="navTo('reviews')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/80 transition-all">Review & Vishwas</button>
        <button id="navBtn-tenantPortal" onclick="navTo('tenantPortal')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-terracotta-800 bg-terracotta-100 hover:bg-terracotta-200 transition-all flex items-center gap-1.5 shadow-sm">
          <i class="fa-solid fa-user-shield text-[11px]"></i> Tenant Portal
        </button>
      </div>

      <!-- Right CTAs -->
      <div class="flex items-center gap-2">
        <!-- Live Full-Stack API Status Pill -->
        <div id="backendStatusBadge" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800 border border-olive-300 shadow-sm">
          <span class="w-2 h-2 rounded-full bg-olive-600 animate-ping"></span>
          <span id="backendStatusText">Node.js Server LIVE</span>
        </div>

        <a href="tel:+919876543210" class="hidden md:inline-flex items-center gap-1.5 text-xs font-bold text-stone-700 hover:text-terracotta-700 px-3 py-2 rounded-full hover:bg-amber-100/60 transition-colors">
          <i class="fa-solid fa-phone text-terracotta-700"></i>
          <span>98765 43210</span>
        </a>

        <!-- Agent Portal Pill Toggle Button -->
        <button id="agentPortalToggleBtn" onclick="toggleAgentPortal()" class="pill-btn px-3.5 sm:px-4 py-2 rounded-full text-xs font-bold bg-charcoal-900 hover:bg-terracotta-700 text-white shadow-pill flex items-center gap-2 transition-all hover:scale-105 active:scale-95">
          <i class="fa-solid fa-key text-amber-300"></i>
          <span id="agentBtnText">Agent Portal (Sharma Ji)</span>
        </button>

        <!-- Mobile Hamburger Menu Button -->
        <button onclick="toggleMobileNav()" class="lg:hidden w-9 h-9 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>

    <!-- Mobile Dropdown Navigation Drawer -->
    <div id="mobileNavMenu" class="hidden max-w-6xl mx-auto mt-2 pointer-events-auto transition-all duration-300">
      <div class="glass-pill rounded-3xl p-4 border border-amber-200/80 shadow-warm-card flex flex-col gap-2 bg-[#FFFBF5]/95 backdrop-blur-md">
        <button onclick="navTo('home'); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-house text-terracotta-700 w-4"></i> Home
        </button>
        <button onclick="navTo('properties'); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-magnifying-glass text-terracotta-700 w-4"></i> Ghar Dhoondo (Flats & Shops)
        </button>
        <button onclick="navTo('howItWorks'); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-list-check text-terracotta-700 w-4"></i> Kaise Kaam Karta Hai
        </button>
        <button onclick="navTo('reviews'); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-star text-terracotta-700 w-4"></i> Review & Vishwas
        </button>
        <button onclick="navTo('tenantPortal'); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-terracotta-800 bg-amber-100/80 hover:bg-amber-200/80 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-user-shield text-terracotta-700 w-4"></i> Tenant Self-Service Portal
        </button>
        <a href="tel:+919876543210" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-phone text-terracotta-700 w-4"></i> Call Sharma Ji: 98765 43210
        </a>
      </div>
    </div>
  </header>

  <!-- ==================== NOTIFICATION TOAST ==================== -->'''

content, count = re.subn(old_nav_pattern, new_nav, content, flags=re.DOTALL)
print(f"Replaced navbar: {count}")

# 2. Add dedicated Tenant Portal Full Page View right before </main>
tenant_page_view = '''    <!-- DEDICATED FULL-PAGE INTERFACE: TENANT PORTAL PAGE -->
    <section id="tenantPortalPageSection" class="hidden max-w-5xl mx-auto px-4 sm:px-6 mb-20">
      <div class="bg-white rounded-3xl p-6 sm:p-8 border border-amber-200/90 shadow-warm-card">
        
        <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 mb-6 border-b border-amber-100 gap-4">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-2xl bg-terracotta-100 text-terracotta-700 flex items-center justify-center font-bold text-xl">
              <i class="fa-solid fa-user-shield"></i>
            </div>
            <div>
              <h2 class="font-serif text-2xl font-bold text-charcoal-900">Tenant Self-Service Portal</h2>
              <p class="text-xs text-stone-500">Rent Receipts, Live Visits, Digital Agreement aur Complaint Management</p>
            </div>
          </div>
          <button onclick="navTo('home')" class="px-4 py-2 rounded-full bg-cream-100 hover:bg-cream-200 text-stone-700 text-xs font-bold self-start sm:self-auto flex items-center gap-1.5 transition-colors">
            <i class="fa-solid fa-arrow-left"></i> Wapas Website Par Jayein
          </button>
        </div>

        <!-- Tenant Login Card -->
        <div id="tenantPageLoginCard" class="max-w-md mx-auto py-8">
          <div class="p-6 rounded-3xl bg-cream-50 border border-amber-200 shadow-sm space-y-4">
            <div class="text-center">
              <h3 class="font-serif text-lg font-bold text-charcoal-900">Tenant Login</h3>
              <p class="text-xs text-stone-600 mt-1">Apna registered mobile number enter karke OTP se login karein</p>
            </div>

            <div>
              <label class="block text-xs font-bold text-stone-700 mb-1">Registered Mobile Number</label>
              <input id="tenantPageLoginPhone" type="tel" value="9811122334" class="w-full text-xs p-3 rounded-2xl border border-amber-200 bg-white focus:outline-none focus:border-terracotta-600">
            </div>

            <div id="tenantPageOtpContainer" class="hidden">
              <label class="block text-xs font-bold text-stone-700 mb-1">Enter 4-Digit OTP (Demo: 1234)</label>
              <input id="tenantPageLoginOtp" type="text" maxlength="4" value="1234" class="w-full text-center tracking-widest text-base font-bold p-3 rounded-2xl border border-amber-200 bg-white focus:outline-none focus:border-terracotta-600">
            </div>

            <button id="tenantPageLoginBtn" onclick="sendTenantPageOtp()" class="w-full py-3 rounded-full bg-terracotta-700 hover:bg-terracotta-800 text-white font-bold text-xs uppercase tracking-wider transition-colors shadow-pill">
              Send OTP on SMS
            </button>
          </div>
        </div>

        <!-- Logged In Tenant Full Interface -->
        <div id="tenantPageDashboardSection" class="hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between bg-cream-100 p-4 rounded-2xl border border-amber-200 gap-3">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-olive-100 text-olive-800 flex items-center justify-center font-bold">
                <i class="fa-solid fa-user-check"></i>
              </div>
              <div>
                <p class="text-sm font-bold text-charcoal-900">Namaste, Rahul Verma Ji</p>
                <p class="text-xs text-stone-600">Flat 204, Royal Palm Residency • Allotted Tenant</p>
              </div>
            </div>
            <button onclick="logoutTenantPage()" class="text-xs font-bold text-maroon-700 hover:underline px-3 py-1.5 rounded-full bg-white border border-maroon-200 shadow-sm self-start sm:self-auto">
              <i class="fa-solid fa-right-from-bracket mr-1"></i> Logout
            </button>
          </div>

          <!-- Quick Tenant Stat Pills -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div class="p-3.5 bg-cream-50 rounded-2xl border border-amber-200">
              <p class="text-[10px] uppercase font-bold text-stone-500">Monthly Rent</p>
              <p class="text-lg font-serif font-black text-charcoal-900 mt-1">₹14,000</p>
            </div>
            <div class="p-3.5 bg-olive-50 rounded-2xl border border-olive-200">
              <p class="text-[10px] uppercase font-bold text-olive-800">Payment Status</p>
              <p class="text-lg font-serif font-black text-olive-700 mt-1">Cleared</p>
            </div>
            <div class="p-3.5 bg-cream-50 rounded-2xl border border-amber-200">
              <p class="text-[10px] uppercase font-bold text-stone-500">Agreement End</p>
              <p class="text-lg font-serif font-black text-charcoal-900 mt-1">31 Oct 2027</p>
            </div>
            <div class="p-3.5 bg-cream-50 rounded-2xl border border-amber-200">
              <p class="text-[10px] uppercase font-bold text-stone-500">Tenant Rating</p>
              <p class="text-lg font-serif font-black text-terracotta-700 mt-1">4.8 / 5.0</p>
            </div>
          </div>

          <!-- Dedicated Tenant Tabs -->
          <div class="flex gap-2 border-b border-amber-200 pb-2 overflow-x-auto no-scrollbar text-xs">
            <button onclick="switchTenantPageTab('visits')" class="tenant-page-tab font-bold text-terracotta-700 border-b-2 border-terracotta-700 px-4 py-2 whitespace-nowrap">My Scheduled Visits</button>
            <button onclick="switchTenantPageTab('agreement')" class="tenant-page-tab text-stone-600 px-4 py-2 hover:text-terracotta-700 whitespace-nowrap">My Agreement</button>
            <button onclick="switchTenantPageTab('rentHistory')" class="tenant-page-tab text-stone-600 px-4 py-2 hover:text-terracotta-700 whitespace-nowrap">Rent Ledger</button>
            <button onclick="switchTenantPageTab('receipts')" class="tenant-page-tab text-stone-600 px-4 py-2 hover:text-terracotta-700 whitespace-nowrap">Download Receipts</button>
            <button onclick="switchTenantPageTab('maintenance')" class="tenant-page-tab text-stone-600 px-4 py-2 hover:text-terracotta-700 whitespace-nowrap">Maintenance Complaint</button>
          </div>

          <!-- Page Subtab 1: Visits -->
          <div id="tenantPagePane-visits" class="tenant-page-pane block space-y-4">
            <div class="p-4 bg-cream-50 rounded-2xl border border-amber-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800">Confirmed Visit</span>
                <h4 class="font-bold text-charcoal-900 text-sm mt-1">Flat 204 - Royal Palm Residency</h4>
                <p class="text-xs text-stone-500">Tomorrow • 11:00 AM • Assigned Agent: Raju Sharma (98765 43210)</p>
              </div>
              <div class="flex gap-2">
                <button onclick="openRescheduleModal('VISIT-1024')" class="px-3 py-1.5 rounded-full bg-cream-200 text-charcoal-900 text-xs font-bold hover:bg-cream-300">Reschedule</button>
                <button onclick="openCancelModal('VISIT-1024')" class="px-3 py-1.5 rounded-full bg-red-100 text-red-800 text-xs font-bold hover:bg-red-200">Cancel</button>
              </div>
            </div>
          </div>

          <!-- Page Subtab 2: Agreement -->
          <div id="tenantPagePane-agreement" class="tenant-page-pane hidden space-y-4">
            <div class="p-5 bg-cream-50 rounded-2xl border border-amber-200 space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="font-bold text-charcoal-900 text-sm">Rent Agreement #AGR-2026-881</h4>
                  <p class="text-xs text-stone-500">Flat 204 • 11 Months Tenure (1 Nov 2026 to 31 Oct 2027)</p>
                </div>
                <button onclick="printOfficialAgreement()" class="px-4 py-2 rounded-full bg-terracotta-700 text-white font-bold text-xs flex items-center gap-1.5 hover:bg-terracotta-800">
                  <i class="fa-solid fa-download"></i> PDF Download
                </button>
              </div>
              <div class="p-3 bg-white rounded-xl text-xs text-stone-600 border border-amber-200">
                Aadhaar verified digital agreement duly executed between Owner and Rahul Verma under Sharma Rentals supervision.
              </div>
            </div>
          </div>

          <!-- Page Subtab 3: Rent Ledger -->
          <div id="tenantPagePane-rentHistory" class="tenant-page-pane hidden space-y-4">
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left">
                <thead class="bg-cream-100 text-stone-700 border-b border-amber-200 font-bold">
                  <tr>
                    <th class="p-3">Month</th>
                    <th class="p-3">Amount</th>
                    <th class="p-3">Paid Date</th>
                    <th class="p-3">Mode</th>
                    <th class="p-3">Receipt</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-amber-100">
                  <tr>
                    <td class="p-3 font-bold">November 2026</td>
                    <td class="p-3">₹14,000</td>
                    <td class="p-3 text-stone-500">03 Nov 2026</td>
                    <td class="p-3"><span class="px-2 py-0.5 rounded-full bg-olive-100 text-olive-800 font-bold text-[10px]">UPI</span></td>
                    <td class="p-3"><button onclick="generateReceipt('RCP-1101')" class="text-terracotta-700 font-bold hover:underline">View Receipt</button></td>
                  </tr>
                  <tr>
                    <td class="p-3 font-bold">October 2026</td>
                    <td class="p-3">₹14,000</td>
                    <td class="p-3 text-stone-500">02 Oct 2026</td>
                    <td class="p-3"><span class="px-2 py-0.5 rounded-full bg-olive-100 text-olive-800 font-bold text-[10px]">NetBanking</span></td>
                    <td class="p-3"><button onclick="generateReceipt('RCP-1001')" class="text-terracotta-700 font-bold hover:underline">View Receipt</button></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Page Subtab 4: Receipts -->
          <div id="tenantPagePane-receipts" class="tenant-page-pane hidden space-y-3">
            <div class="p-4 bg-cream-50 rounded-2xl border border-amber-200 flex items-center justify-between">
              <div>
                <p class="font-bold text-charcoal-900 text-xs">Official Rent Receipt - Nov 2026</p>
                <p class="text-[11px] text-stone-500">Receipt ID: RCP-1101 • ₹14,000</p>
              </div>
              <button onclick="generateReceipt('RCP-1101')" class="px-3 py-1.5 rounded-full bg-terracotta-700 text-white font-bold text-xs hover:bg-terracotta-800">
                <i class="fa-solid fa-receipt mr-1"></i> Open Receipt
              </button>
            </div>
          </div>

          <!-- Page Subtab 5: Maintenance -->
          <div id="tenantPagePane-maintenance" class="tenant-page-pane hidden space-y-4">
            <div class="p-4 bg-cream-50 rounded-2xl border border-amber-200 space-y-3">
              <h4 class="font-bold text-charcoal-900 text-xs">Nayi Complaint Darj Karein</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div>
                  <label class="block font-bold text-stone-700 mb-1">Issue Category</label>
                  <select id="tenantPageIssueCat" class="w-full p-2.5 rounded-xl border border-amber-300 bg-white">
                    <option>Plumbing (Nal / Leakage)</option>
                    <option>Electrical (Switch / Fan)</option>
                    <option>Woodwork (Door / Lock)</option>
                    <option>Seepage / Paint</option>
                  </select>
                </div>
                <div>
                  <label class="block font-bold text-stone-700 mb-1">Severity</label>
                  <select id="tenantPageIssueSev" class="w-full p-2.5 rounded-xl border border-amber-300 bg-white">
                    <option>High (24 Ghante me theek)</option>
                    <option>Medium</option>
                    <option>Low</option>
                  </select>
                </div>
              </div>
              <div>
                <label class="block font-bold text-stone-700 mb-1 text-xs">Problem Description</label>
                <textarea id="tenantPageIssueDesc" rows="2" placeholder="Bathroom tap leak ho raha hai..." class="w-full p-2.5 rounded-xl border border-amber-300 bg-white text-xs"></textarea>
              </div>
              <button type="button" onclick="submitTenantPageComplaint()" class="px-5 py-2.5 rounded-full bg-terracotta-700 text-white font-bold text-xs hover:bg-terracotta-800">
                Submit Complaint to Sharma Ji
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>
'''

content = content.replace('  </main>', tenant_page_view + '\n  </main>')

# 3. Add JavaScript navigation controller functions right before showPublicSite()
js_nav_router = '''    // ================= CENTRAL SPA NAVIGATION ROUTER =================
    function navTo(section) {
      const publicView = document.getElementById('publicView');
      const agentDashboardView = document.getElementById('agentDashboardView');
      const tenantPortalPage = document.getElementById('tenantPortalPageSection');
      const homeSection = document.getElementById('home');
      const propertiesSection = document.getElementById('properties-section');
      const howItWorksSection = document.getElementById('how-it-works');
      const testimonialsSection = document.getElementById('testimonials');

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
    }

    function toggleMobileNav() {
      const menu = document.getElementById('mobileNavMenu');
      if (menu) {
        menu.classList.toggle('hidden');
      }
    }

    function sendTenantPageOtp() {
      const otpContainer = document.getElementById('tenantPageOtpContainer');
      const btn = document.getElementById('tenantPageLoginBtn');
      if (otpContainer.classList.contains('hidden')) {
        otpContainer.classList.remove('hidden');
        btn.innerText = "Verify OTP & Open Portal";
        showToast("Demo OTP bhej diya: 1234", "info");
      } else {
        const otpVal = document.getElementById('tenantPageLoginOtp').value;
        if (otpVal === "1234") {
          document.getElementById('tenantPageLoginCard').classList.add('hidden');
          document.getElementById('tenantPageDashboardSection').classList.remove('hidden');
          showToast("Tenant Portal me Login Ho Gaye!", "success");
        } else {
          showToast("Galat OTP! Demo OTP hai: 1234", "error");
        }
      }
    }

    function logoutTenantPage() {
      document.getElementById('tenantPageDashboardSection').classList.add('hidden');
      document.getElementById('tenantPageLoginCard').classList.remove('hidden');
      document.getElementById('tenantPageOtpContainer').classList.add('hidden');
      document.getElementById('tenantPageLoginBtn').innerText = "Send OTP on SMS";
      showToast("Logged out successfully", "info");
    }

    function switchTenantPageTab(tabKey) {
      document.querySelectorAll('.tenant-page-pane').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tenant-page-tab').forEach(btn => {
        btn.classList.remove('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
        btn.classList.add('text-stone-600');
      });

      const pane = document.getElementById('tenantPagePane-' + tabKey);
      if (pane) pane.classList.remove('hidden');

      if (window.event && window.event.currentTarget) {
        window.event.currentTarget.classList.add('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
        window.event.currentTarget.classList.remove('text-stone-600');
      }
    }

    function submitTenantPageComplaint() {
      const cat = document.getElementById('tenantPageIssueCat').value;
      const desc = document.getElementById('tenantPageIssueDesc').value || "No details provided";
      showToast("Aapki complaint (#CMP-" + Math.floor(1000 + Math.random()*9000) + ") darj ho gayi!", "success");
      document.getElementById('tenantPageIssueDesc').value = "";
    }
'''

content = content.replace('    function showPublicSite() {', js_nav_router + '\n    function showPublicSite() {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
