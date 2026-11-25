# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

popular_neighborhoods_html = """
    <!-- ==================== EXPLORE POPULAR NEIGHBORHOODS (DELHI-NCR) ==================== -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-3 mb-8">
        <div>
          <span class="text-xs font-bold uppercase tracking-wider text-terracotta-700 flex items-center gap-1.5">
            <i class="fa-solid fa-compass"></i> Prime Residential Corridors
          </span>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold text-charcoal-900 mt-1">
            Delhi-NCR Ke Chahite Neighborhoods
          </h2>
          <p class="text-xs sm:text-sm text-stone-500 mt-0.5">Sharma Ji ki field-verified properties in top residential & IT corridors</p>
        </div>
        <span class="text-xs font-semibold text-stone-500">Tap card to explore</span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Neighborhood 1: Indirapuram -->
        <div onclick="filterByLocation('Indirapuram')" class="group relative rounded-3xl overflow-hidden aspect-[4/5] cursor-pointer shadow-warm-soft hover:shadow-warm-card border border-amber-200/80 transition-all duration-300 transform hover:-translate-y-1.5">
          <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=600&q=80" alt="Indirapuram Ghaziabad" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-gradient-to-t from-charcoal-950 via-charcoal-900/40 to-transparent"></div>
          <div class="absolute top-3 left-3 bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] font-bold text-charcoal-900 border border-amber-200 shadow-sm">
            15+ Flats Available
          </div>
          <div class="absolute bottom-4 left-4 right-4 text-white space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">Ghaziabad Prime</span>
            <h3 class="font-serif text-xl font-bold">Indirapuram</h3>
            <p class="text-[11px] text-stone-300">Vaibhav, Ahinsa & Shipra Khand • Direct NH-24</p>
            <div class="pt-2 flex items-center justify-between text-xs border-t border-white/20">
              <span class="font-bold text-amber-300">Starts ₹10,000/mo</span>
              <span class="text-[11px] font-bold group-hover:translate-x-1 transition-transform">Explore →</span>
            </div>
          </div>
        </div>

        <!-- Neighborhood 2: Noida Sector 62 & 76 -->
        <div onclick="filterByLocation('Noida Sector 62')" class="group relative rounded-3xl overflow-hidden aspect-[4/5] cursor-pointer shadow-warm-soft hover:shadow-warm-card border border-amber-200/80 transition-all duration-300 transform hover:-translate-y-1.5">
          <img src="https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=600&q=80" alt="Noida Sector 62" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-gradient-to-t from-charcoal-950 via-charcoal-900/40 to-transparent"></div>
          <div class="absolute top-3 left-3 bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] font-bold text-charcoal-900 border border-amber-200 shadow-sm">
            18+ Flats Available
          </div>
          <div class="absolute bottom-4 left-4 right-4 text-white space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">IT & Metro Belt</span>
            <h3 class="font-serif text-xl font-bold">Noida Sector 62 & 76</h3>
            <p class="text-[11px] text-stone-300">Blue Line Metro Corridor • Gated Societies</p>
            <div class="pt-2 flex items-center justify-between text-xs border-t border-white/20">
              <span class="font-bold text-amber-300">Starts ₹12,000/mo</span>
              <span class="text-[11px] font-bold group-hover:translate-x-1 transition-transform">Explore →</span>
            </div>
          </div>
        </div>

        <!-- Neighborhood 3: Gurgaon DLF Phase 5 -->
        <div onclick="filterByLocation('Gurgaon DLF Phase 5')" class="group relative rounded-3xl overflow-hidden aspect-[4/5] cursor-pointer shadow-warm-soft hover:shadow-warm-card border border-amber-200/80 transition-all duration-300 transform hover:-translate-y-1.5">
          <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" alt="Gurgaon DLF Phase 5" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-gradient-to-t from-charcoal-950 via-charcoal-900/40 to-transparent"></div>
          <div class="absolute top-3 left-3 bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] font-bold text-charcoal-900 border border-amber-200 shadow-sm">
            8+ Studios & PGs
          </div>
          <div class="absolute bottom-4 left-4 right-4 text-white space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">Cyber City Prime</span>
            <h3 class="font-serif text-xl font-bold">Gurgaon DLF Phase 5</h3>
            <p class="text-[11px] text-stone-300">Golf Course Road • Rapid Metro Access</p>
            <div class="pt-2 flex items-center justify-between text-xs border-t border-white/20">
              <span class="font-bold text-amber-300">Starts ₹9,500/mo</span>
              <span class="text-[11px] font-bold group-hover:translate-x-1 transition-transform">Explore →</span>
            </div>
          </div>
        </div>

        <!-- Neighborhood 4: South Delhi Lajpat Nagar -->
        <div onclick="filterByLocation('Lajpat Nagar')" class="group relative rounded-3xl overflow-hidden aspect-[4/5] cursor-pointer shadow-warm-soft hover:shadow-warm-card border border-amber-200/80 transition-all duration-300 transform hover:-translate-y-1.5">
          <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=600&q=80" alt="South Delhi Lajpat Nagar" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-gradient-to-t from-charcoal-950 via-charcoal-900/40 to-transparent"></div>
          <div class="absolute top-3 left-3 bg-white/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[10px] font-bold text-charcoal-900 border border-amber-200 shadow-sm">
            6+ Builder Floors
          </div>
          <div class="absolute bottom-4 left-4 right-4 text-white space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">South Delhi Central</span>
            <h3 class="font-serif text-xl font-bold">Lajpat Nagar</h3>
            <p class="text-[11px] text-stone-300">Pink & Violet Line Metro • Central Market</p>
            <div class="pt-2 flex items-center justify-between text-xs border-t border-white/20">
              <span class="font-bold text-amber-300">Starts ₹20,000/mo</span>
              <span class="text-[11px] font-bold group-hover:translate-x-1 transition-transform">Explore →</span>
            </div>
          </div>
        </div>

      </div>
    </section>
"""

target_loc = """        <div class="p-2 border-l border-amber-200">
          <p class="font-serif text-3xl md:text-4xl font-extrabold text-terracotta-800">24 Ghante</p>
          <p class="text-xs md:text-sm font-semibold text-stone-600 mt-1">Visit Se Shift Tak</p>
        </div>
      </div>
    </section>"""

if target_loc in html and 'Prime Residential Corridors' not in html:
    html = html.replace(target_loc, target_loc + '\n' + popular_neighborhoods_html)
    print("Injected Popular Neighborhoods section successfully!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
