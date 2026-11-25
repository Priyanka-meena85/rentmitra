# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the entire <header> ... </header> block
old_header_start = '<!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->'
old_header_end = '</header>'

idx_start = c.find(old_header_start)
idx_end = c.find(old_header_end, idx_start)

if idx_start != -1 and idx_end != -1:
    idx_end += len(old_header_end)
    
    clean_header = """<!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-3 sm:top-4 left-0 right-0 z-40 px-3 sm:px-6 pointer-events-auto">
    <nav class="max-w-7xl mx-auto bg-[#FFFDF9]/95 backdrop-blur-xl rounded-full px-4 sm:px-6 py-2 sm:py-2.5 flex items-center justify-between shadow-[0_10px_30px_-5px_rgba(28,25,23,0.08),0_2px_8px_rgba(0,0,0,0.03)] pointer-events-auto border border-amber-200/90 transition-all duration-300">
      
      <!-- Brand Logo & Identity (Clean Organic Logo Display) -->
      <a href="javascript:void(0)" onclick="navTo('home')" class="flex items-center gap-2.5 sm:gap-3 group cursor-pointer flex-shrink-0" title="RentMitraa Home">
        <div class="h-10 sm:h-11 w-auto flex-shrink-0 flex items-center justify-center transition-transform group-hover:scale-105 duration-200">
          <img src="/logo.png" alt="RentMitraa Logo" class="h-9 sm:h-10 w-auto object-contain filter drop-shadow-xs" />
        </div>
        <div class="flex-shrink-0">
          <div class="flex items-center gap-1.5">
            <span class="font-serif text-xl sm:text-2xl font-bold tracking-tight text-charcoal-900 leading-none whitespace-nowrap">
              Rent<span class="text-terracotta-700">Mitraa</span>
            </span>
            <span class="inline-flex items-center px-1.5 py-0.5 rounded-full text-[9px] font-bold bg-olive-100 text-olive-800 border border-olive-500/30 whitespace-nowrap">
              <i class="fa-solid fa-circle-check text-[9px] mr-1 text-olive-700"></i>Verified
            </span>
          </div>
          <p class="text-[9px] sm:text-[10px] font-bold text-stone-500 tracking-wider uppercase mt-0.5 whitespace-nowrap">Sharma Rentals</p>
        </div>
      </a>

      <!-- Middle Navigation Links (Desktop: Spacious, Elegant Single-Line Menu) -->
      <div class="hidden lg:flex items-center gap-1 bg-cream-100/90 p-1 rounded-full border border-amber-200/70 shadow-inner flex-shrink-0">
        <button id="navBtn-home" onclick="navTo('home')" class="nav-link px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">
          Home
        </button>
        <button id="navBtn-properties" onclick="navTo('properties')" class="nav-link px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">
          Ghar Dhoondo
        </button>
        <button id="navBtn-howItWorks" onclick="navTo('howItWorks')" class="nav-link px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">
          Kaise Kaam Karta Hai
        </button>
        <button id="navBtn-reviews" onclick="navTo('reviews')" class="nav-link px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">
          Review & Vishwas
        </button>
        <button id="navBtn-tenantPortal" onclick="navTo('tenantPortal')" class="nav-link px-4 py-2 rounded-full text-xs font-bold text-terracotta-800 bg-terracotta-100/90 hover:bg-terracotta-200 transition-all flex items-center gap-1.5 shadow-xs whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-user-shield text-[11px] text-terracotta-700"></i>
          <span>Tenant Portal</span>
        </button>
      </div>

      <!-- Right CTAs (Phone Call Button, Agent Portal Toggle Button, Mobile Menu) -->
      <div class="flex items-center gap-2.5 sm:gap-3 flex-shrink-0">
        
        <!-- Phone Direct Call Button (Icon Only Circle) -->
        <a href="tel:+919876543210" class="w-10 h-10 rounded-full bg-cream-200/70 hover:bg-cream-300/80 text-terracotta-700 hover:text-terracotta-800 border border-amber-300 flex items-center justify-center shadow-xs transition-all hover:scale-105 active:scale-95 flex-shrink-0" title="Call Sharma Ji: 98765 43210" aria-label="Call Sharma Ji">
          <i class="fa-solid fa-phone text-xs"></i>
        </a>

        <!-- Agent Portal Toggle Button (Luxury Charcoal Pill) -->
        <button id="agentPortalToggleBtn" onclick="toggleAgentPortal()" class="pill-btn px-4 sm:px-5 py-2.5 rounded-full text-xs font-bold bg-charcoal-900 hover:bg-terracotta-700 text-white shadow-pill flex items-center gap-2 transition-all hover:scale-105 active:scale-95 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-key text-amber-300 text-xs"></i>
          <span id="agentBtnText" class="whitespace-nowrap"><span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span></span>
        </button>

        <!-- Mobile Hamburger Menu Button -->
        <button onclick="toggleMobileNav()" class="lg:hidden w-10 h-10 rounded-full bg-cream-200/70 text-charcoal-900 flex items-center justify-center hover:bg-cream-300 transition-colors border border-amber-300 shadow-xs flex-shrink-0" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>

    <!-- Mobile Dropdown Navigation Drawer -->
    <div id="mobileNavMenu" class="hidden max-w-7xl mx-auto mt-2 pointer-events-auto transition-all duration-300">
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
        <button onclick="toggleAgentPortal(); toggleMobileNav();" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-white bg-charcoal-900 hover:bg-terracotta-700 flex items-center gap-2.5 transition-colors shadow-sm">
          <i class="fa-solid fa-key text-amber-300 w-4"></i> Agent Portal (Sharma Ji Admin)
        </button>
        <a href="tel:+919876543210" class="text-left px-4 py-2.5 rounded-2xl text-xs font-bold text-stone-800 hover:bg-amber-100/70 flex items-center gap-2.5 transition-colors">
          <i class="fa-solid fa-phone text-terracotta-700 w-4"></i> Call Sharma Ji: 98765 43210
        </a>
      </div>
    </div>
  </header>"""
    
    c = c[:idx_start] + clean_header + c[idx_end:]
    print("Replaced Header with clean luxury design!")

# Also update footer logo to use logo.png
c = c.replace('src="/logo.jpg"', 'src="/logo.png"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
