# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update <title>
c = c.replace('<title>RentWala', '<title>RentMitraa')

# 2. Update Navbar Logo Icon with new Image logo and RentMitraa text
old_nav_logo = """      <!-- Brand Logo -->
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
      </a>"""

new_nav_logo = """      <!-- Brand Logo -->
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
      </a>"""

if old_nav_logo in c:
    c = c.replace(old_nav_logo, new_nav_logo)
    print("Replaced Navbar Logo")

# 3. Update Footer Logo Icon
old_footer_logo = """          <!-- Column 1: Brand & Credentials -->
          <div class="space-y-4 lg:col-span-1">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-terracotta-700 to-terracotta-500 text-white flex items-center justify-center shadow-md">
                <i class="fa-solid fa-house-chimney text-sm"></i>
              </div>
              <div>
                <span class="font-serif text-2xl font-bold text-white tracking-tight block">RentWala</span>
                <span class="text-[10px] text-amber-400 font-bold uppercase tracking-widest block -mt-1">Sharma Rentals</span>
              </div>
            </div>"""

new_footer_logo = """          <!-- Column 1: Brand & Credentials -->
          <div class="space-y-4 lg:col-span-1">
            <div class="flex items-center gap-3">
              <div class="w-11 h-11 rounded-2xl bg-white p-1 border border-amber-400 shadow-md overflow-hidden flex items-center justify-center">
                <img src="/logo.jpg" alt="RentMitraa Logo" class="w-full h-full object-contain" />
              </div>
              <div>
                <span class="font-serif text-2xl font-bold text-white tracking-tight block">RentMitraa</span>
                <span class="text-[10px] text-amber-400 font-bold uppercase tracking-widest block -mt-1">Sharma Rentals</span>
              </div>
            </div>"""

if old_footer_logo in c:
    c = c.replace(old_footer_logo, new_footer_logo)
    print("Replaced Footer Logo")

# 4. Replace other brand text occurrences
c = c.replace('RentWala - Sharma Rentals', 'RentMitraa - Sharma Rentals')
c = c.replace('RentWala Platform', 'RentMitraa Platform')
c = c.replace('RentWala App', 'RentMitraa App')
c = c.replace('care@rentwala.in', 'care@rentmitraa.in')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied RentMitraa brand and logo to index.html")

# 5. Also update manifest.json
with open('manifest.json', 'r', encoding='utf-8') as f:
    m = f.read()

m = m.replace('RentWala - Sharma Rentals', 'RentMitraa - Sharma Rentals')
m = m.replace('"short_name": "RentWala"', '"short_name": "RentMitraa"')
m = m.replace('https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=192&q=80', '/logo.jpg')
m = m.replace('https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=512&q=80', '/logo.jpg')

with open('manifest.json', 'w', encoding='utf-8') as f:
    f.write(m)

print("Updated manifest.json")
