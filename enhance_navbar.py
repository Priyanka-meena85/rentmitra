# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the header and nav block with ultra-enhanced, non-wrapping, luxury navbar
old_nav_block = """  <!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-4 left-0 right-0 z-40 px-4 pointer-events-auto">
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
      <div class="hidden md:flex items-center gap-1 bg-amber-100/60 p-1 rounded-full border border-amber-200/60">
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
          <span id="agentBtnText"><span class="hidden sm:inline">Agent Portal (Sharma Ji)</span><span class="sm:hidden">Agent</span></span>
        </button>

        <!-- Mobile Hamburger Menu Button -->
        <button onclick="toggleMobileNav()" class="md:hidden w-9 h-9 rounded-full bg-amber-100 text-charcoal-900 flex items-center justify-center hover:bg-amber-200 transition-colors border border-amber-300 shadow-sm" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>"""

new_nav_block = """  <!-- ==================== TOP FLOATING PILL NAVBAR ==================== -->
  <header class="fixed top-3 sm:top-4 left-0 right-0 z-40 px-3 sm:px-6 pointer-events-auto">
    <nav class="max-w-7xl mx-auto glass-pill rounded-full px-4 sm:px-6 py-2.5 sm:py-3 flex items-center justify-between shadow-warm-card pointer-events-auto border border-amber-200/90 transition-all duration-300">
      
      <!-- Brand Logo -->
      <a href="javascript:void(0)" onclick="navTo('home')" class="flex items-center gap-2.5 sm:gap-3 group cursor-pointer flex-shrink-0" title="RentWala Home">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-gradient-to-tr from-terracotta-700 to-terracotta-500 text-white flex items-center justify-center shadow-md group-hover:scale-105 transition-transform flex-shrink-0">
          <i class="fa-solid fa-house-chimney text-base sm:text-lg"></i>
        </div>
        <div class="flex-shrink-0">
          <div class="flex items-center gap-1.5">
            <span class="font-serif text-lg sm:text-xl font-bold tracking-tight text-charcoal-900 whitespace-nowrap">RentWala</span>
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

      <!-- Right CTAs (Server Live, Phone, Agent Portal) -->
      <div class="flex items-center gap-2 sm:gap-2.5 flex-shrink-0">
        
        <!-- Live Server Status Pill -->
        <div id="backendStatusBadge" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800 border border-olive-300 shadow-sm whitespace-nowrap flex-shrink-0">
          <span class="w-2 h-2 rounded-full bg-olive-600 animate-ping"></span>
          <span id="backendStatusText" class="whitespace-nowrap">Node.js Server LIVE</span>
        </div>

        <!-- Phone Direct Call Button -->
        <a href="tel:+919876543210" class="hidden md:inline-flex items-center gap-1.5 text-xs font-bold text-stone-700 hover:text-terracotta-700 px-3 py-1.5 rounded-full hover:bg-amber-100/70 transition-colors whitespace-nowrap flex-shrink-0">
          <i class="fa-solid fa-phone text-terracotta-700 text-xs"></i>
          <span class="whitespace-nowrap">98765 43210</span>
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

if old_nav_block in c:
    c = c.replace(old_nav_block, new_nav_block)
    print("Replaced old_nav_block with new_nav_block")
else:
    print("Could not find exact old_nav_block, trying fuzzy search")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
