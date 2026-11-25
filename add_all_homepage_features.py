# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Live Keyword Input in Hero Search Card
old_search_card_header = """          <!-- Search Bar in Floating Warm Card with 3 Pill Tabs -->
          <div class="bg-white/95 backdrop-blur-md rounded-[28px] p-3 sm:p-4 border border-amber-200 shadow-warm-card max-w-2xl">
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 pb-2">"""

new_search_card_header = """          <!-- Search Bar in Floating Warm Card with Live Keyword Input + 3 Pill Tabs -->
          <div class="bg-white/95 backdrop-blur-md rounded-[28px] p-3 sm:p-4 border border-amber-200 shadow-warm-card max-w-2xl">
            
            <!-- Live Society / Landmark Keyword Search Input -->
            <div class="mb-2.5">
              <div class="flex items-center gap-2.5 bg-cream-100/90 hover:bg-cream-200/60 focus-within:bg-white focus-within:border-terracotta-600 rounded-2xl px-3.5 py-2.5 border border-amber-200/80 transition-all shadow-xs">
                <i class="fa-solid fa-magnifying-glass text-terracotta-700 text-sm"></i>
                <input 
                  type="text" 
                  id="heroKeywordInput" 
                  oninput="applyHeroSearch()" 
                  placeholder="Society, Sector, ya Landmark search karein (e.g. Royal Palm, Sector 62, Indirapuram)..." 
                  class="w-full bg-transparent text-xs sm:text-sm font-semibold text-charcoal-900 placeholder:text-stone-400 focus:outline-none"
                />
                <button type="button" onclick="clearHeroKeyword()" class="text-stone-400 hover:text-stone-700 text-xs px-1" title="Clear">
                  <i class="fa-solid fa-xmark"></i>
                </button>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 pb-2">"""

if old_search_card_header in html:
    html = html.replace(old_search_card_header, new_search_card_header)
    print("Step 1: Added Live Keyword input to Hero search card")

# 2. Add "Explore Popular Neighborhoods" section right after stats row
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
        <span class="text-xs font-semibold text-stone-500">Tap to filter flats</span>
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

# Place after stats section (before properties-section)
target_stats_end = """        <div class="p-2">
          <p class="font-serif text-3xl sm:text-4xl font-extrabold text-terracotta-700">0</p>
          <p class="text-xs text-stone-500 font-semibold mt-1">Dispute Record</p>
        </div>
      </div>
    </section>"""

if target_stats_end in html and 'id="properties-section"' in html:
    html = html.replace(target_stats_end, target_stats_end + '\n' + popular_neighborhoods_html)
    print("Step 2: Added Explore Neighborhoods visual section")

# 3. Add "Why RentMitraa vs Local Brokers" Section (after How It Works / before Testimonials)
why_rentmitraa_html = """
    <!-- ==================== WHY RENTMITRAA VS LOCAL BROKERS ==================== -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 mb-20">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-wider text-terracotta-700 flex items-center justify-center gap-1.5">
          <i class="fa-solid fa-scale-balanced"></i> Farq Saaf Hai
        </span>
        <h2 class="font-serif text-2xl sm:text-3xl font-bold text-charcoal-900 mt-1">
          Local Broker Ke Jhatke vs RentMitraa Ka Bharosa
        </h2>
        <p class="text-xs sm:text-sm text-stone-500 mt-1">Dekhein kaise Sharma Ji ka system tenants ke hazaron rupaye aur samay bachata hai</p>
      </div>

      <div class="bg-white rounded-3xl border border-amber-200 shadow-warm-card overflow-hidden">
        <div class="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-amber-200">
          
          <!-- Column 1: Aam Local Broker (Red) -->
          <div class="p-6 sm:p-8 bg-red-50/40 space-y-5">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-red-100 text-maroon-700 flex items-center justify-center text-base font-bold shrink-0">
                <i class="fa-solid fa-xmark"></i>
              </div>
              <div>
                <h3 class="font-serif text-lg font-bold text-maroon-900">Aam Local Broker</h3>
                <p class="text-xs text-stone-500">Purana aur risky tarika</p>
              </div>
            </div>

            <ul class="space-y-3.5 text-xs text-stone-700">
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-xmark text-maroon-600 mt-0.5 text-sm shrink-0"></i>
                <span><b>Fake & Purani Photos:</b> Online kuch aur dikhate hain, visit par bekar flat nikalta hai.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-xmark text-maroon-600 mt-0.5 text-sm shrink-0"></i>
                <span><b>Hidden Brokerage Jhatka:</b> Aakhiri samay par 1-2 mahine ka mota brokerage maangte hain.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-xmark text-maroon-600 mt-0.5 text-sm shrink-0"></i>
                <span><b>Zubani Vaada, Zero Guarantee:</b> Agar kisi aur ne ₹500 zyada diye toh aapka flat doosre ko de dete hain.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-xmark text-maroon-600 mt-0.5 text-sm shrink-0"></i>
                <span><b>No Post-Shift Support:</b> Chabi dene ke baad agar nal ya switch kharab ho, toh phone uthana band.</span>
              </li>
            </ul>
          </div>

          <!-- Column 2: RentMitraa Sharma Rentals (Green/Olive) -->
          <div class="p-6 sm:p-8 bg-olive-50/40 space-y-5">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-olive-100 text-olive-800 flex items-center justify-center text-base font-bold shrink-0">
                <i class="fa-solid fa-check"></i>
              </div>
              <div>
                <h3 class="font-serif text-lg font-bold text-olive-950">RentMitraa (Sharma Rentals)</h3>
                <p class="text-xs text-olive-700 font-semibold">100% Transparent aur Legal</p>
              </div>
            </div>

            <ul class="space-y-3.5 text-xs text-stone-800">
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-check text-olive-700 mt-0.5 text-sm shrink-0"></i>
                <span><b>100% Real Field Photos & Video Tour:</b> Jo screen par dikhega, flat wahi hoga. Guarantee.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-check text-olive-700 mt-0.5 text-sm shrink-0"></i>
                <span><b>Fixed & Transparent Rates:</b> Har flat ka rent, deposit aur terms pehle se website par saaf likha hai.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-check text-olive-700 mt-0.5 text-sm shrink-0"></i>
                <span><b>₹2,000 Instant Token Lock:</b> Pay karte hi flat locked ho jata hai with official printable PDF receipt.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i class="fa-solid fa-circle-check text-olive-700 mt-0.5 text-sm shrink-0"></i>
                <span><b>Doorstep Agreement & Mistri Support:</b> 24h legal agreement plus complaint aane par verified mistri doorstep par.</span>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </section>
"""

# Place after #how-it-works
if 'id="how-it-works"' in html:
    html = html.replace('<!-- TESTIMONIALS -->', why_rentmitraa_html + '\n    <!-- TESTIMONIALS -->')
    print("Step 3: Added Why RentMitraa vs Local Brokers section")

# 4. Add Tenant FAQ Accordion Section (before Footer)
faq_section_html = """
    <!-- ==================== FREQUENTLY ASKED QUESTIONS (FAQS) ==================== -->
    <section class="max-w-4xl mx-auto px-4 sm:px-6 mb-20">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold uppercase tracking-wider text-terracotta-700 flex items-center justify-center gap-1.5">
          <i class="fa-solid fa-circle-question"></i> Aapke Sawal, Hamare Jawab
        </span>
        <h2 class="font-serif text-2xl sm:text-3xl font-bold text-charcoal-900 mt-1">
          Aam Taur Par Puche Jaane Wale Sawal
        </h2>
        <p class="text-xs sm:text-sm text-stone-500 mt-1">Rent par ghar lene se pehle tenants ke har sawal ka saaf aur sidha jawab</p>
      </div>

      <div class="space-y-3" id="faqAccordionContainer">
        
        <!-- FAQ 1 -->
        <div class="faq-item bg-white rounded-2xl border border-amber-200 overflow-hidden shadow-xs">
          <button onclick="toggleFaq(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 font-serif font-bold text-sm sm:text-base text-charcoal-900 hover:text-terracotta-700 transition-colors">
            <span>1. Kya RentMitraa par flat visit karne ke koi charges hain?</span>
            <i class="fa-solid fa-chevron-down text-xs text-stone-400 transition-transform duration-200 faq-icon"></i>
          </button>
          <div class="faq-content hidden px-4 sm:px-5 pb-4 sm:pb-5 text-xs text-stone-600 leading-relaxed border-t border-amber-100 pt-3">
            Bilkul nahi! Site visit bilkul 100% Free hai. Aap apni pasand ke time slot (11:00 AM, 02:00 PM, ya 05:00 PM) par aakar aaram se flat physically check kar sakte hain.
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="faq-item bg-white rounded-2xl border border-amber-200 overflow-hidden shadow-xs">
          <button onclick="toggleFaq(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 font-serif font-bold text-sm sm:text-base text-charcoal-900 hover:text-terracotta-700 transition-colors">
            <span>2. ₹2,000 Token Payment karne par flat doosre ko toh nahi dikhega?</span>
            <i class="fa-solid fa-chevron-down text-xs text-stone-400 transition-transform duration-200 faq-icon"></i>
          </button>
          <div class="faq-content hidden px-4 sm:px-5 pb-4 sm:pb-5 text-xs text-stone-600 leading-relaxed border-t border-amber-100 pt-3">
            Jaise hi aap UPI se ₹2,000 token pay karte hain, property ka status turant 'BOOKED' ho jata hai aur wo doosre kisi bhi tenant ke liye lock ho jati hai. Sath hi aapko official PDF receipt mil jati hai.
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="faq-item bg-white rounded-2xl border border-amber-200 overflow-hidden shadow-xs">
          <button onclick="toggleFaq(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 font-serif font-bold text-sm sm:text-base text-charcoal-900 hover:text-terracotta-700 transition-colors">
            <span>3. Digital Legal Agreement banne me kitna samay lagta hai?</span>
            <i class="fa-solid fa-chevron-down text-xs text-stone-400 transition-transform duration-200 faq-icon"></i>
          </button>
          <div class="faq-content hidden px-4 sm:px-5 pb-4 sm:pb-5 text-xs text-stone-600 leading-relaxed border-t border-amber-100 pt-3">
            Token lene ke baad 24 ghante ke andar 11-month registered stamp paper agreement draft ho jata hai. Owner aur Tenant ke digital signature ke sath PDF aapke portal par download ke liye uplabdh hoti hai.
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="faq-item bg-white rounded-2xl border border-amber-200 overflow-hidden shadow-xs">
          <button onclick="toggleFaq(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 font-serif font-bold text-sm sm:text-base text-charcoal-900 hover:text-terracotta-700 transition-colors">
            <span>4. Kya bachelors ya pets allowed hote hain?</span>
            <i class="fa-solid fa-chevron-down text-xs text-stone-400 transition-transform duration-200 faq-icon"></i>
          </button>
          <div class="faq-content hidden px-4 sm:px-5 pb-4 sm:pb-5 text-xs text-stone-600 leading-relaxed border-t border-amber-100 pt-3">
            Hamare har property card par saaf badge laga hota hai — 'Family Only', 'Bachelors Allowed', ya 'Girls Only'. Aap filter sidebar se sirf bachelors ya pet-friendly flats chunte hain.
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="faq-item bg-white rounded-2xl border border-amber-200 overflow-hidden shadow-xs">
          <button onclick="toggleFaq(this)" class="w-full p-4 sm:p-5 text-left flex items-center justify-between gap-4 font-serif font-bold text-sm sm:text-base text-charcoal-900 hover:text-terracotta-700 transition-colors">
            <span>5. Shift hone ke baad nal ya bijli kharab ho jaye toh kya karein?</span>
            <i class="fa-solid fa-chevron-down text-xs text-stone-400 transition-transform duration-200 faq-icon"></i>
          </button>
          <div class="faq-content hidden px-4 sm:px-5 pb-4 sm:pb-5 text-xs text-stone-600 leading-relaxed border-t border-amber-100 pt-3">
            Aap Tenant Portal me jakar 'Maintenance Complaint' tab me photo ke sath request daal sakte hain. Sharma Ji 24 ghante ke andar in-house verified plumber ya electrician assign karte hain.
          </div>
        </div>

      </div>
    </section>
"""

# Place before footer
target_footer_comment = '<!-- ==================== PREMIUM LUXURY FOOTER ==================== -->'
if target_footer_comment in html:
    html = html.replace(target_footer_comment, faq_section_html + '\n    ' + target_footer_comment)
    print("Step 4: Added Tenant FAQ Accordion Section")

# 5. Add Wishlist Trigger in Navbar + Wishlist Modal
wishlist_nav_btn = """        <!-- Wishlist Saved Flats Button -->
        <button onclick="openWishlistModal()" class="w-10 h-10 rounded-full bg-cream-200/70 hover:bg-cream-300/80 text-terracotta-700 hover:text-terracotta-800 border border-amber-300 flex items-center justify-center relative shadow-xs transition-all hover:scale-105 active:scale-95 flex-shrink-0" title="Saved Wishlist Flats">
          <i class="fa-solid fa-heart text-xs"></i>
          <span id="wishlistCountBadge" class="hidden absolute -top-1 -right-1 w-4 h-4 bg-terracotta-700 text-white rounded-full text-[9px] font-bold flex items-center justify-center">0</span>
        </button>"""

if 'id="wishlistCountBadge"' not in html:
    html = html.replace(
        '<!-- Phone Direct Call Button (Icon Only Circle) -->',
        wishlist_nav_btn + '\n\n        <!-- Phone Direct Call Button (Icon Only Circle) -->'
    )

wishlist_modal_html = """
  <!-- ==================== WISHLIST / SAVED FLATS MODAL ==================== -->
  <div id="wishlistModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6">
    <div class="bg-[#FFFBF5] rounded-3xl border border-amber-200 shadow-2xl max-w-2xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-5 border-b border-amber-200 flex items-center justify-between bg-cream-100">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-full bg-terracotta-700 text-white flex items-center justify-center">
            <i class="fa-solid fa-heart text-sm"></i>
          </div>
          <div>
            <h3 class="font-serif text-lg font-bold text-charcoal-900">Aapki Saved Properties</h3>
            <p class="text-xs text-stone-500">Shortlisted flats jinhe aapne pasand kiya hai</p>
          </div>
        </div>
        <button onclick="closeWishlistModal()" class="w-8 h-8 rounded-full bg-amber-200/80 hover:bg-amber-300 text-charcoal-900 flex items-center justify-center transition-colors">
          <i class="fa-solid fa-xmark text-sm"></i>
        </button>
      </div>

      <div id="wishlistModalBody" class="p-5 overflow-y-auto space-y-3">
        <!-- Injected via renderWishlistModal() -->
      </div>

      <div class="p-4 border-t border-amber-200 bg-cream-50 flex items-center justify-between text-xs text-stone-600">
        <span>Direct Visit Book Karein ya Token Lock Karein</span>
        <button onclick="closeWishlistModal()" class="px-4 py-2 rounded-full bg-stone-200 hover:bg-stone-300 text-stone-800 font-bold transition-colors">
          Band Karein
        </button>
      </div>
    </div>
  </div>
"""

if 'id="wishlistModal"' not in html:
    html = html.replace('<!-- ==================== NOTIFICATION TOAST ==================== -->', wishlist_modal_html + '\n  <!-- ==================== NOTIFICATION TOAST ==================== -->')

# 6. Add JavaScript functions for FAQ Accordion, Keyword Clear, and Wishlist Management
new_js_logic = """
    // ================= FAQ ACCORDION LOGIC =================
    function toggleFaq(btn) {
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isHidden = content.classList.contains('hidden');

      // Close all other FAQs
      document.querySelectorAll('.faq-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.faq-icon').forEach(ic => ic.style.transform = 'rotate(0deg)');

      if (isHidden) {
        content.classList.remove('hidden');
        if (icon) icon.style.transform = 'rotate(180deg)';
      }
    }

    // ================= HERO KEYWORD SEARCH LOGIC =================
    function clearHeroKeyword() {
      const input = document.getElementById('heroKeywordInput');
      if (input) input.value = '';
      applyHeroSearch();
    }

    // ================= WISHLIST / SAVED FLATS MANAGEMENT =================
    let userWishlist = JSON.parse(localStorage.getItem('rentwala_wishlist')) || [];

    function toggleWishlist(propId, btnEl) {
      const idx = userWishlist.indexOf(propId);
      if (idx > -1) {
        userWishlist.splice(idx, 1);
        showToast("Property Saved list se hata di gayi", "info");
      } else {
        userWishlist.push(propId);
        showToast("Property Saved list me add ho gayi!", "success");
      }
      localStorage.setItem('rentwala_wishlist', JSON.stringify(userWishlist));
      updateWishlistUI();
      renderPublicPropertyList();
    }

    function updateWishlistUI() {
      const badge = document.getElementById('wishlistCountBadge');
      if (badge) {
        if (userWishlist.length > 0) {
          badge.classList.remove('hidden');
          badge.innerText = userWishlist.length;
        } else {
          badge.classList.add('hidden');
        }
      }
    }

    function openWishlistModal() {
      const modal = document.getElementById('wishlistModal');
      const body = document.getElementById('wishlistModalBody');
      if (!modal || !body) return;

      const savedProps = properties.filter(p => userWishlist.includes(p.id));

      if (savedProps.length === 0) {
        body.innerHTML = `
          <div class="text-center py-10 space-y-3">
            <div class="w-14 h-14 rounded-full bg-cream-200 text-terracotta-700 flex items-center justify-center mx-auto text-xl">
              <i class="fa-regular fa-heart"></i>
            </div>
            <h4 class="font-serif font-bold text-base text-charcoal-900">Koi Property Saved Nahi Hai</h4>
            <p class="text-xs text-stone-500 max-w-sm mx-auto">Kisi bhi flat ke dil (heart) icon par click karke aap use yahan save kar sakte hain.</p>
            <button onclick="closeWishlistModal(); document.getElementById('properties-section').scrollIntoView({ behavior: 'smooth' });" class="px-4 py-2 rounded-full bg-terracotta-700 text-white font-bold text-xs">
              Properties Dekhein
            </button>
          </div>
        `;
      } else {
        body.innerHTML = savedProps.map(p => `
          <div class="p-3 bg-white rounded-2xl border border-amber-200 flex items-center justify-between gap-3 shadow-xs">
            <div class="flex items-center gap-3">
              <img src="${p.images[0]}" alt="${p.title}" class="w-16 h-16 rounded-xl object-cover shrink-0" />
              <div>
                <h5 class="font-serif font-bold text-xs sm:text-sm text-charcoal-900">${p.title}</h5>
                <p class="text-[11px] text-stone-500">${p.locality} • ${p.bhk}</p>
                <span class="font-serif font-extrabold text-terracotta-700 text-xs">₹${p.rent.toLocaleString('en-IN')}/mo</span>
              </div>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <button onclick="closeWishlistModal(); openPropertyDrawer('${p.id}');" class="px-3 py-1.5 rounded-full bg-charcoal-900 text-white text-[11px] font-bold">
                Details
              </button>
              <button onclick="toggleWishlist('${p.id}'); openWishlistModal();" class="text-stone-400 hover:text-red-500 p-1.5" title="Hatao">
                <i class="fa-solid fa-trash-can text-xs"></i>
              </button>
            </div>
          </div>
        `).join('');
      }

      modal.classList.remove('hidden');
    }

    function closeWishlistModal() {
      const modal = document.getElementById('wishlistModal');
      if (modal) modal.classList.add('hidden');
    }
"""

if '// ================= FAQ ACCORDION LOGIC =================' not in html:
    html = html.replace(
        '// ================= SUPER FEATURE 1: PROPERTY COMPARISON TOOL =================',
        new_js_logic + '\n\n    // ================= SUPER FEATURE 1: PROPERTY COMPARISON TOOL ================='
    )

# Update applyHeroSearch() to include keyword search filter
old_hero_search_fn = """    function applyHeroSearch() {
      const loc = document.getElementById('heroLocationSelect').value;
      const budget = document.getElementById('heroBudgetSelect').value;
      const type = document.getElementById('heroTypeSelect').value;

      let list = [...properties];"""

new_hero_search_fn = """    function applyHeroSearch() {
      const loc = document.getElementById('heroLocationSelect').value;
      const budget = document.getElementById('heroBudgetSelect').value;
      const type = document.getElementById('heroTypeSelect').value;
      const keywordEl = document.getElementById('heroKeywordInput');
      const keyword = keywordEl ? keywordEl.value.trim().toLowerCase() : '';

      let list = [...properties];

      if (keyword) {
        list = list.filter(p => 
          p.title.toLowerCase().includes(keyword) || 
          p.locality.toLowerCase().includes(keyword) || 
          p.fullAddress.toLowerCase().includes(keyword) ||
          p.bhk.toLowerCase().includes(keyword)
        );
      }"""

if old_hero_search_fn in html:
    html = html.replace(old_hero_search_fn, new_hero_search_fn)
    print("Updated applyHeroSearch() to support live keyword typing!")

# Ensure initData calls updateWishlistUI()
if 'updateWishlistUI();' not in html:
    html = html.replace(
        'populatePoliceDropdowns();',
        'populatePoliceDropdowns();\n      updateWishlistUI();'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 5: Successfully injected all new Homepage features into index.html!")
