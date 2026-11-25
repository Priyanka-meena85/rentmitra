# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_footer = """    <!-- FOOTER -->
    <footer class="bg-charcoal-950 text-stone-300 pt-16 pb-12 border-t border-amber-900/30">
      <div class="max-w-6xl mx-auto px-4 sm:px-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          
          <div class="md:col-span-2 space-y-4">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 rounded-full bg-terracotta-700 text-white flex items-center justify-center">
                <i class="fa-solid fa-house-chimney text-xs"></i>
              </div>
              <span class="font-serif text-2xl font-bold text-white tracking-tight">RentWala</span>
              <span class="text-xs text-amber-400 font-serif">- Sharma Rentals</span>
            </div>
            <p class="text-sm text-stone-400 max-w-sm">
              Delhi-NCR ka sabse transparent aur bharosemand rental network. Verified property, fixed rent aur zero dispute agreement.
            </p>
            <div class="text-xs text-stone-400 space-y-1">
              <p><i class="fa-solid fa-location-dot text-terracotta-500 mr-2"></i> Shop 14, Main Market, Indirapuram, Ghaziabad (UP)</p>
              <p><i class="fa-solid fa-phone text-terracotta-500 mr-2"></i> +91 98765 43210 (Sharma Ji)</p>
            </div>
          </div>

          <div>
            <h4 class="font-serif text-base font-bold text-white mb-3">Popular Localities</h4>
            <ul class="text-xs space-y-2 text-stone-400">
              <li><a href="#properties-section" onclick="filterByLocation('Indirapuram')" class="hover:text-terracotta-400">Indirapuram Flats</a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Noida Sector 62')" class="hover:text-terracotta-400">Noida Sector 62 / 76</a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Gurgaon DLF Phase 5')" class="hover:text-terracotta-400">Gurgaon Cyber City</a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Lajpat Nagar')" class="hover:text-terracotta-400">South Delhi Lajpat Nagar</a></li>
            </ul>
          </div>

          <div>
            <h4 class="font-serif text-base font-bold text-white mb-3">Important Links</h4>
            <ul class="text-xs space-y-2 text-stone-400">
              <li><button onclick="openTenantPortalModal()" class="hover:text-terracotta-400">Tenant Login & Receipts</button></li>
              <li><button onclick="toggleAgentPortal()" class="hover:text-terracotta-400">Sharma Ji Admin Dashboard</button></li>
              <li><a href="https://wa.me/919876543210?text=Namaste%20Sharma%20Ji,%20mujhe%20rent%20pe%20flat%20chahiye" target="_blank" class="hover:text-terracotta-400">Direct WhatsApp Chat</a></li>
              <li><button onclick="resetDemoData()" class="text-stone-500 hover:text-amber-400">Reset Demo Data</button></li>
            </ul>
          </div>

        </div>

        <div class="pt-8 border-t border-stone-800 text-center text-xs text-stone-500 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p>© 2026 RentWala - Sharma Rentals. All rights reserved.</p>
          <p class="flex items-center gap-1">Designed with <i class="fa-solid fa-heart text-terracotta-600"></i> for Indian Renters & Landlords</p>
        </div>
      </div>
    </footer>"""

new_footer = """    <!-- ==================== PREMIUM LUXURY FOOTER ==================== -->
    <footer class="bg-charcoal-950 text-stone-300 pt-16 pb-12 border-t-2 border-amber-900/40 relative overflow-hidden">
      
      <!-- Subtle Ambient Glow in Footer -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-24 bg-gradient-to-b from-amber-600/10 via-terracotta-700/5 to-transparent blur-3xl pointer-events-none"></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-14">
        
        <!-- PRE-FOOTER LUXURY CALLOUT BANNER FOR LANDLORDS / OWNERS -->
        <div class="relative rounded-3xl p-6 sm:p-10 bg-gradient-to-r from-[#241E1A] via-[#1C1917] to-[#291F1A] border border-amber-500/30 shadow-2xl overflow-hidden flex flex-col lg:flex-row items-center justify-between gap-6">
          <div class="space-y-2 max-w-2xl text-center lg:text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-terracotta-900/60 border border-amber-500/30 text-amber-300 text-xs font-bold">
              <i class="fa-solid fa-key text-amber-400"></i>
              <span>Makan Malik Special • 0% Listing Fee</span>
            </div>
            <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white tracking-tight">
              Apna Flat ya Shop <span class="text-terracotta-400 underline decoration-amber-400 decoration-wavy decoration-1">7 Din Me Rent Pe Lagayein</span>
            </h3>
            <p class="text-xs sm:text-sm text-stone-400 leading-relaxed">
              Sharma Ji khud karenge background check, official police verification, aur doorstep 11-month agreement. Direct har mahine bank me rent guaranteed.
            </p>
          </div>

          <div class="flex flex-wrap items-center justify-center gap-3 shrink-0">
            <a href="tel:+919876543210" class="px-5 py-3 rounded-full bg-gradient-to-r from-terracotta-700 to-terracotta-600 hover:from-terracotta-800 text-white font-bold text-xs tracking-wider uppercase shadow-pill flex items-center gap-2.5 transition-transform hover:scale-105 active:scale-95">
              <i class="fa-solid fa-phone"></i>
              <span>Call Sharma Ji</span>
            </a>
            <a href="https://wa.me/919876543210?text=Namaste%20Sharma%20Ji,%20meri%20property%20rent%20pe%20lagani%20hai" target="_blank" class="px-5 py-3 rounded-full bg-olive-700 hover:bg-olive-800 text-white font-bold text-xs tracking-wider uppercase shadow-sm flex items-center gap-2 transition-transform hover:scale-105 active:scale-95">
              <i class="fa-brands fa-whatsapp text-sm"></i>
              <span>WhatsApp Details</span>
            </a>
          </div>
        </div>

        <!-- MAIN FOOTER MULTI-COLUMN GRID -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 lg:gap-10 pb-8 border-b border-stone-800">
          
          <!-- Column 1: Brand & Credentials -->
          <div class="space-y-4 lg:col-span-1">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-terracotta-700 to-terracotta-500 text-white flex items-center justify-center shadow-md">
                <i class="fa-solid fa-house-chimney text-sm"></i>
              </div>
              <div>
                <span class="font-serif text-2xl font-bold text-white tracking-tight block">RentWala</span>
                <span class="text-[10px] text-amber-400 font-bold uppercase tracking-widest block -mt-1">Sharma Rentals</span>
              </div>
            </div>
            
            <p class="text-xs text-stone-400 leading-relaxed">
              Delhi-NCR ka sabse transparent aur bharosemand rental network. Verified property, fixed rent aur zero dispute agreement.
            </p>

            <div class="space-y-2 text-[11px] text-stone-400">
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-shield-halved text-olive-500 text-xs"></i>
                <span>Govt RERA Broker Reg #AGY-2026-NCR</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-file-contract text-amber-500 text-xs"></i>
                <span>100% Legal E-Stamp Agreements</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-clock text-terracotta-500 text-xs"></i>
                <span>Office: Mon-Sun (10:00 AM - 8:30 PM)</span>
              </div>
            </div>
          </div>

          <!-- Column 2: Popular Delhi-NCR Localities -->
          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-location-dot text-terracotta-500"></i> Popular Hubs
            </h4>
            <ul class="text-xs space-y-2 text-stone-400">
              <li><a href="#properties-section" onclick="filterByLocation('Indirapuram')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>Indirapuram (Vaibhav/Ahinsa)</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Noida Sector 62')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>Noida Sector 62 & 76</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Gurgaon DLF Phase 5')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>Gurgaon DLF Phase 5</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Lajpat Nagar')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>South Delhi Lajpat Nagar</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Vaishali')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>Vaishali Metro Station Area</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
              <li><a href="#properties-section" onclick="filterByLocation('Gaur City')" class="hover:text-amber-300 transition-colors flex items-center justify-between"><span>Gaur City 1 & 2 Noida Ext.</span> <i class="fa-solid fa-chevron-right text-[9px] text-stone-600"></i></a></li>
            </ul>
          </div>

          <!-- Column 3: Configuration & Budget -->
          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-couch text-terracotta-500"></i> Flat Types
            </h4>
            <ul class="text-xs space-y-2 text-stone-400">
              <li><a href="#properties-section" onclick="setFilter('1BHK')" class="hover:text-amber-300 transition-colors">1 BHK Affordable Flats</a></li>
              <li><a href="#properties-section" onclick="setFilter('2BHK')" class="hover:text-amber-300 transition-colors">2 BHK Gated Society Family Homes</a></li>
              <li><a href="#properties-section" onclick="setFilter('3BHK')" class="hover:text-amber-300 transition-colors">3 BHK Luxury Penthouses with Club</a></li>
              <li><a href="#properties-section" onclick="setFilter('PG')" class="hover:text-amber-300 transition-colors">Corporate Studio & PG (Bachelors)</a></li>
              <li><a href="#properties-section" onclick="setFilter('Shop')" class="hover:text-amber-300 transition-colors">Commercial Shops & Main Road Offices</a></li>
              <li><a href="#properties-section" onclick="switchListingView('map')" class="hover:text-amber-300 transition-colors text-amber-400 font-semibold"><i class="fa-solid fa-map-location-dot mr-1"></i> Interactive Map View</a></li>
            </ul>
          </div>

          <!-- Column 4: Tenant & Agent Services -->
          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-bolt text-terracotta-500"></i> Quick Portals
            </h4>
            <ul class="text-xs space-y-2 text-stone-400">
              <li><button onclick="navTo('tenantPortal')" class="hover:text-amber-300 transition-colors text-left flex items-center gap-1.5"><i class="fa-solid fa-user-shield text-[10px] text-amber-500"></i> Tenant Self-Service Portal</button></li>
              <li><button onclick="openCompareModal()" class="hover:text-amber-300 transition-colors text-left flex items-center gap-1.5"><i class="fa-solid fa-code-compare text-[10px] text-amber-500"></i> Side-by-Side Property Comparison</button></li>
              <li><button onclick="toggleAgentPortal()" class="hover:text-amber-300 transition-colors text-left flex items-center gap-1.5"><i class="fa-solid fa-key text-[10px] text-amber-500"></i> Sharma Ji Admin Dashboard</button></li>
              <li><button onclick="switchAdminTab('policeVerificationTab'); toggleAgentPortal();" class="hover:text-amber-300 transition-colors text-left flex items-center gap-1.5"><i class="fa-solid fa-building-shield text-[10px] text-amber-500"></i> Police Verification Form Auto-Fill</button></li>
              <li><button onclick="switchAdminTab('ownerPayoutTab'); toggleAgentPortal();" class="hover:text-amber-300 transition-colors text-left flex items-center gap-1.5"><i class="fa-solid fa-money-bill-transfer text-[10px] text-amber-500"></i> Owner Rent Split & Payouts</button></li>
              <li><button onclick="resetDemoData()" class="text-stone-500 hover:text-amber-400 text-left transition-colors"><i class="fa-solid fa-rotate-left mr-1"></i> Reset Demo Database</button></li>
            </ul>
          </div>

          <!-- Column 5: Direct Office & Connect -->
          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-headset text-terracotta-500"></i> Office & Contact
            </h4>
            
            <div class="text-xs text-stone-400 space-y-2.5">
              <div class="flex items-start gap-2">
                <i class="fa-solid fa-store text-terracotta-500 text-xs mt-0.5 shrink-0"></i>
                <span>Shop 14, Main Market, Indirapuram, Ghaziabad (UP) 201014</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-phone text-terracotta-500 text-xs shrink-0"></i>
                <a href="tel:+919876543210" class="hover:text-amber-300 font-bold text-stone-200">+91 98765 43210 (Sharma Ji)</a>
              </div>
              <div class="flex items-center gap-2">
                <i class="fa-brands fa-whatsapp text-olive-500 text-xs shrink-0"></i>
                <a href="https://wa.me/919876543210" target="_blank" class="hover:text-olive-400 font-semibold">24x7 WhatsApp Enquiry</a>
              </div>
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-envelope text-amber-500 text-xs shrink-0"></i>
                <a href="mailto:care@rentwala.in" class="hover:text-amber-300">care@rentwala.in</a>
              </div>
            </div>

            <!-- Install PWA Mobile Badge -->
            <div class="pt-2">
              <div class="p-2.5 rounded-xl bg-stone-900 border border-stone-800 text-[11px] flex items-center justify-between">
                <div>
                  <span class="text-white font-bold block">Mobile App Ready</span>
                  <span class="text-stone-500 text-[10px]">Add to Home Screen (PWA)</span>
                </div>
                <div class="w-7 h-7 rounded-lg bg-terracotta-700 text-white flex items-center justify-center">
                  <i class="fa-solid fa-mobile-screen-button text-xs"></i>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- FOOTER BOTTOM COPYRIGHT & TRUST BAR -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-stone-500">
          <div class="space-y-1 text-center sm:text-left">
            <p>© 2026 RentWala - Sharma Rentals. All rights reserved. RERA Broker License #AGY-2026-DLH-NCR.</p>
            <p class="text-[11px] text-stone-600">Privacy Protected • 100% Verified Owners • Fixed Rate Guarantee • Doorstep Agreement</p>
          </div>

          <div class="flex items-center gap-4 text-stone-400 text-xs">
            <button onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" class="hover:text-amber-300 flex items-center gap-1 transition-colors">
              <span>Back to Top</span>
              <i class="fa-solid fa-arrow-up text-[10px]"></i>
            </button>
          </div>
        </div>

      </div>
    </footer>"""

if old_footer in html:
    html = html.replace(old_footer, new_footer)
    print("Replaced old footer with new luxury footer!")
else:
    print("Could not find exact old_footer, searching for <footer> tag")
    import re
    html = re.sub(r'<!-- FOOTER -->.*?</footer>', new_footer, html, flags=re.DOTALL)
    print("Replaced via regex!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
