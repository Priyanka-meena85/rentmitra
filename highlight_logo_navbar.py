# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_nav_section = """  <!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-3 sm:top-4 left-0 right-0 z-40 px-3 sm:px-6 pointer-events-auto">
    <nav class="max-w-7xl mx-auto glass-pill rounded-full px-4 sm:px-6 py-2.5 sm:py-3 flex items-center justify-between shadow-warm-card pointer-events-auto border border-amber-200/90 transition-all duration-300">
      
      <!-- Brand Logo -->
      <a href="javascript:void(0)" onclick="navTo('home')" class="flex items-center gap-2.5 sm:gap-3 group cursor-pointer flex-shrink-0" title="RentMitraa Home">
        <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-white p-1 border border-amber-300 shadow-sm group-hover:scale-105 transition-transform flex-shrink-0 overflow-hidden flex items-center justify-center">
          <img src="/logo.jpg" alt="RentMitraa Logo" class="w-full h-full object-contain" />
        </div>
        <div class="flex-shrink-0">
          <div class="flex items-center gap-1.5">
            <span class="font-serif text-lg sm:text-xl font-bold tracking-tight text-charcoal-900 whitespace-nowrap">RentMitraa</span>
            <span class="inline-flex items-center px-1.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-semibold bg-olive-100 text-olive-800 border border-olive-600/30 whitespace-nowrap">
              <i class="fa-solid fa-circle-check text-[9px] mr-1 text-olive-700"></i>Verified
            </span>
          </div>
          <p class="text-[9px] sm:text-[10px] font-bold text-stone-500 -mt-0.5 tracking-wider uppercase whitespace-nowrap">Sharma Rentals</p>
        </div>
      </a>

      <!-- Middle Navigation Links (Desktop: Always Single Line whitespace-nowrap) -->
      <div class="hidden lg:flex items-center gap-1 bg-cream-200/70 p-1 rounded-full border border-amber-300/60 shadow-inner flex-shrink-0">
        <button id="navBtn-home" onclick="navTo('home')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">Home</button>
        <button id="navBtn-properties" onclick="navTo('properties')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">Ghar Dhoondo</button>
        <button id="navBtn-howItWorks" onclick="navTo('howItWorks')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">Kaise Kaam Karta Hai</button>
        <button id="navBtn-reviews" onclick="navTo('reviews')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 hover:bg-white/90 transition-all whitespace-nowrap flex-shrink-0">Review & Vishwas</button>
        <button id="navBtn-tenantPortal" onclick="navTo('tenantPortal')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-bold text-terracotta-800 bg-terracotta-100/90 hover:bg-terracotta-200 transition-all flex items-center gap-1.5 shadow-sm whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-user-shield text-[11px]"></i> <span>Tenant Portal</span>
        </button>
      </div>

      <!-- Right CTAs (Phone Icon Only, Agent Portal) -->
      <div class="flex items-center gap-2 sm:gap-2.5 flex-shrink-0">
        
        <!-- Phone Direct Call Button (Icon Only) -->
        <a href="tel:+919876543210" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-amber-100/80 hover:bg-amber-200 text-terracotta-700 hover:text-terracotta-800 border border-amber-300/80 flex items-center justify-center shadow-xs transition-all hover:scale-105 active:scale-95 flex-shrink-0" title="Call Sharma Ji: 98765 43210" aria-label="Call Sharma Ji">
          <i class="fa-solid fa-phone text-xs sm:text-sm"></i>
        </a>

        <!-- Agent Portal Toggle Button -->
        <button id="agentPortalToggleBtn" onclick="toggleAgentPortal()" class="pill-btn px-4 py-2 rounded-full text-xs font-bold bg-charcoal-900 hover:bg-terracotta-700 text-white shadow-pill flex items-center gap-2 transition-all hover:scale-105 active:scale-95 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-key text-amber-300 text-xs"></i>
          <span id="agentBtnText" class="whitespace-nowrap"><span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span></span>
        </button>

        <!-- Mobile Hamburger Menu Button -->
        <button onclick="toggleMobileNav()" class="lg:hidden w-9 h-9 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm flex-shrink-0" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>"""

new_nav_section = """  <!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-3 sm:top-4 left-0 right-0 z-40 px-3 sm:px-6 pointer-events-auto">
    <nav class="max-w-7xl mx-auto glass-pill rounded-full px-4 sm:px-6 py-2 sm:py-2.5 flex items-center justify-between shadow-[0_12px_36px_-6px_rgba(194,65,12,0.15),0_4px_12px_rgba(0,0,0,0.05)] pointer-events-auto border-2 border-amber-300/85 transition-all duration-300">
      
      <!-- Brand Logo & Identity (Prominently Highlighted) -->
      <a href="javascript:void(0)" onclick="navTo('home')" class="flex items-center gap-3 sm:gap-3.5 group cursor-pointer flex-shrink-0" title="RentMitraa Home">
        
        <!-- Highlighted High-Res Logo Badge -->
        <div class="relative flex-shrink-0">
          <div class="w-12 h-12 sm:w-13 sm:h-13 rounded-2xl bg-white p-1 border-2 border-amber-400 shadow-[0_4px_14px_rgba(194,65,12,0.2)] group-hover:scale-105 group-hover:border-terracotta-600 transition-all duration-300 flex items-center justify-center overflow-hidden">
            <img src="/logo.jpg" alt="RentMitraa Official Logo" class="w-full h-full object-contain filter contrast-105" />
          </div>
          <span class="absolute -bottom-1 -right-1 w-3.5 h-3.5 bg-olive-600 border-2 border-white rounded-full"></span>
        </div>

        <div class="flex-shrink-0">
          <div class="flex items-center gap-2">
            <span class="font-serif text-xl sm:text-2xl font-black tracking-tight text-charcoal-900 whitespace-nowrap">Rent<span class="text-terracotta-700">Mitraa</span></span>
            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-olive-100 text-olive-800 border border-olive-400/50 shadow-xs whitespace-nowrap">
              <i class="fa-solid fa-circle-check text-[9px] mr-1 text-olive-700"></i>Verified
            </span>
          </div>
          <p class="text-[10px] sm:text-[11px] font-bold text-amber-800/80 -mt-0.5 tracking-wider uppercase whitespace-nowrap">Sharma Rentals • Delhi-NCR</p>
        </div>
      </a>

      <!-- Middle Navigation Dock (Ultra-Sleek Glass Dock) -->
      <div class="hidden lg:flex items-center gap-1.5 bg-amber-100/70 backdrop-blur-md p-1.5 rounded-full border border-amber-300/80 shadow-inner flex-shrink-0">
        <button id="navBtn-home" onclick="navTo('home')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-bold text-stone-700 hover:text-terracotta-700 hover:bg-white transition-all flex items-center gap-1.5 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-house-chimney text-[11px] text-terracotta-600"></i>
          <span>Home</span>
        </button>
        <button id="navBtn-properties" onclick="navTo('properties')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-bold text-stone-700 hover:text-terracotta-700 hover:bg-white transition-all flex items-center gap-1.5 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-magnifying-glass text-[11px] text-terracotta-600"></i>
          <span>Ghar Dhoondo</span>
        </button>
        <button id="navBtn-howItWorks" onclick="navTo('howItWorks')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-bold text-stone-700 hover:text-terracotta-700 hover:bg-white transition-all flex items-center gap-1.5 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-list-check text-[11px] text-terracotta-600"></i>
          <span>Kaise Kaam Karta Hai</span>
        </button>
        <button id="navBtn-reviews" onclick="navTo('reviews')" class="nav-link px-3.5 py-1.5 rounded-full text-xs font-bold text-stone-700 hover:text-terracotta-700 hover:bg-white transition-all flex items-center gap-1.5 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-star text-[11px] text-amber-500"></i>
          <span>Review & Vishwas</span>
        </button>
        <button id="navBtn-tenantPortal" onclick="navTo('tenantPortal')" class="nav-link px-4 py-1.5 rounded-full text-xs font-extrabold text-terracotta-800 bg-gradient-to-r from-amber-200/90 to-amber-100 hover:from-terracotta-100 hover:to-amber-200 transition-all flex items-center gap-1.5 shadow-sm border border-amber-300/80 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-user-shield text-[11px] text-terracotta-700"></i>
          <span>Tenant Portal</span>
        </button>
      </div>

      <!-- Right CTAs (Circular Call Pill & Obsidian Gold Agent Portal) -->
      <div class="flex items-center gap-2.5 sm:gap-3 flex-shrink-0">
        
        <!-- Phone Direct Call Button (Icon Only with Warm Ring) -->
        <a href="tel:+919876543210" class="w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-gradient-to-tr from-amber-100 to-amber-50 hover:from-amber-200 hover:to-amber-100 text-terracotta-700 hover:text-terracotta-800 border-2 border-amber-300/90 shadow-sm flex items-center justify-center transition-all hover:scale-105 active:scale-95 flex-shrink-0" title="Call Sharma Ji: 98765 43210" aria-label="Call Sharma Ji">
          <i class="fa-solid fa-phone text-xs sm:text-sm"></i>
        </a>

        <!-- Agent Portal Toggle Button -->
        <button id="agentPortalToggleBtn" onclick="toggleAgentPortal()" class="pill-btn px-4 sm:px-5 py-2.5 rounded-full text-xs font-extrabold bg-gradient-to-r from-charcoal-950 via-charcoal-900 to-charcoal-950 hover:from-terracotta-800 hover:to-terracotta-700 text-white shadow-pill flex items-center gap-2 border border-amber-400/40 transition-all hover:scale-105 active:scale-95 whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-key text-amber-300 text-xs"></i>
          <span id="agentBtnText" class="whitespace-nowrap"><span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span></span>
        </button>

        <!-- Mobile Hamburger Menu Button -->
        <button onclick="toggleMobileNav()" class="lg:hidden w-10 h-10 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm flex-shrink-0" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>"""

if old_nav_section in c:
    c = c.replace(old_nav_section, new_nav_section)
    print("Replaced with highlighted logo navbar!")
else:
    print("Could not match exact old_nav_section, performing replace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
