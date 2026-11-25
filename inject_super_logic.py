# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update DEFAULT_PROPERTIES with localityScore and coords
old_prop_101 = """        id: "FLAT-101",
        title: "Royal Palm Residency, Garden Facing",
        locality: "Indirapuram",
        fullAddress: "Flat 204, Tower B, Royal Palm, Vaibhav Khand, Indirapuram, Ghaziabad",
        rent: 14500,
        deposit: 29000,
        bhk: "2BHK",
        area: 1150,
        furnishing: "Full Furnished",
        allowed: "Family / Bachelor Both",
        status: "Available",
        vacantDays: 4,
        owner: "Sunil Gupta",
        availableFrom: "Ready to Move",
        badge: "Verified Owner",
        images: [
          "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Lift", "Car Parking", "24h Water", "Power Backup", "WiFi", "Gym"]"""

new_prop_101 = """        id: "FLAT-101",
        title: "Royal Palm Residency, Garden Facing",
        locality: "Indirapuram",
        fullAddress: "Flat 204, Tower B, Royal Palm, Vaibhav Khand, Indirapuram, Ghaziabad",
        rent: 14500,
        deposit: 29000,
        bhk: "2BHK",
        area: 1150,
        furnishing: "Full Furnished",
        allowed: "Family / Bachelor Both",
        status: "Available",
        vacantDays: 4,
        owner: "Sunil Gupta",
        availableFrom: "Ready to Move",
        badge: "Verified Owner",
        coords: [28.6415, 77.3714],
        localityScore: {
          water: "24h Ganga Jal + Submersible",
          power: "Zero Power Cut (100% DG Backup)",
          nightSafety: "9.4 / 10 Gated",
          metroWalk: "6 min walk (Blue Line)",
          deliverySpeed: "8 mins (Blinkit / Swiggy)"
        },
        images: [
          "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Lift", "Car Parking", "24h Water", "Power Backup", "WiFi", "Gym"]"""

if old_prop_101 in html:
    html = html.replace(old_prop_101, new_prop_101)

# Also enrich other default properties
old_prop_102 = """        id: "FLAT-102",
        title: "Gaur City Luxury Flat, Near Metro",
        locality: "Noida Sector 62",
        fullAddress: "Flat 302, Gaur City Center, Sector 62, Noida (Near Metro)",
        rent: 12000,
        deposit: 24000,
        bhk: "1BHK",
        area: 720,
        furnishing: "Full Furnished",
        allowed: "Bachelors Allowed",
        status: "Available",
        vacantDays: 15, // Causes ₹6,000 vacant loss!
        owner: "Harish Chandra",
        availableFrom: "Immediate",
        badge: "Urgent Deal","""

new_prop_102 = """        id: "FLAT-102",
        title: "Gaur City Luxury Flat, Near Metro",
        locality: "Noida Sector 62",
        fullAddress: "Flat 302, Gaur City Center, Sector 62, Noida (Near Metro)",
        rent: 12000,
        deposit: 24000,
        bhk: "1BHK",
        area: 720,
        furnishing: "Full Furnished",
        allowed: "Bachelors Allowed",
        status: "Available",
        vacantDays: 15, // Causes ₹6,000 vacant loss!
        owner: "Harish Chandra",
        availableFrom: "Immediate",
        badge: "Urgent Deal",
        coords: [28.6280, 77.3649],
        localityScore: {
          water: "24h Treated Supply",
          power: "Zero Power Cut",
          nightSafety: "9.2 / 10 CCTV",
          metroWalk: "3 min walk (Sec 62 Metro)",
          deliverySpeed: "6 mins (Zepto Live)"
        },"""

if old_prop_102 in html:
    html = html.replace(old_prop_102, new_prop_102)

old_prop_103 = """        id: "FLAT-103",
        title: "ATS Pristine 3BHK Penthouse with Balcony",
        locality: "Noida Sector 76",
        fullAddress: "Tower 4, ATS Pristine, Sector 76, Central Noida",
        rent: 28000,
        deposit: 56000,
        bhk: "3BHK",
        area: 1750,
        furnishing: "Semi Furnished",
        allowed: "Family Only",
        status: "Rented",
        vacantDays: 0,
        owner: "Col. Rajesh Tyagi",
        availableFrom: "15 Dec 2026",
        badge: "Premium Luxury","""

new_prop_103 = """        id: "FLAT-103",
        title: "ATS Pristine 3BHK Penthouse with Balcony",
        locality: "Noida Sector 76",
        fullAddress: "Tower 4, ATS Pristine, Sector 76, Central Noida",
        rent: 28000,
        deposit: 56000,
        bhk: "3BHK",
        area: 1750,
        furnishing: "Semi Furnished",
        allowed: "Family Only",
        status: "Rented",
        vacantDays: 0,
        owner: "Col. Rajesh Tyagi",
        availableFrom: "15 Dec 2026",
        badge: "Premium Luxury",
        coords: [28.5672, 77.3850],
        localityScore: {
          water: "24h Ganga Jal Supply",
          power: "100% Dual DG Backup",
          nightSafety: "9.8 / 10 3-Tier Security",
          metroWalk: "5 min walk (Sec 76 Metro)",
          deliverySpeed: "7 mins (Blinkit Hub)"
        },"""

if old_prop_103 in html:
    html = html.replace(old_prop_103, new_prop_103)

old_prop_104 = """        id: "FLAT-104",
        title: "DLF Phase 5 Corporate Studio / PG",
        locality: "Gurgaon DLF Phase 5",
        fullAddress: "Studio Suite 12, Golf Course Road, DLF Phase 5, Gurgaon",
        rent: 9500,
        deposit: 19000,
        bhk: "PG",
        area: 450,
        furnishing: "Full Furnished",
        allowed: "Bachelors Allowed",
        status: "Available",
        vacantDays: 2,
        owner: "Vikram Malhotra",
        availableFrom: "Immediate",
        badge: "Under ₹10k Budget","""

new_prop_104 = """        id: "FLAT-104",
        title: "DLF Phase 5 Corporate Studio / PG",
        locality: "Gurgaon DLF Phase 5",
        fullAddress: "Studio Suite 12, Golf Course Road, DLF Phase 5, Gurgaon",
        rent: 9500,
        deposit: 19000,
        bhk: "PG",
        area: 450,
        furnishing: "Full Furnished",
        allowed: "Bachelors Allowed",
        status: "Available",
        vacantDays: 2,
        owner: "Vikram Malhotra",
        availableFrom: "Immediate",
        badge: "Under ₹10k Budget",
        coords: [28.4595, 77.0940],
        localityScore: {
          water: "24h RO Treated Water",
          power: "Zero Power Outage",
          nightSafety: "9.6 / 10 DLF Security",
          metroWalk: "4 min Rapid Metro",
          deliverySpeed: "5 mins (Swiggy Express)"
        },"""

if old_prop_104 in html:
    html = html.replace(old_prop_104, new_prop_104)

old_prop_105 = """        id: "FLAT-105",
        title: "Central Market 1st Floor Shop / Office",
        locality: "Indirapuram",
        fullAddress: "Shop No 14, Aditya Mega Mall Road, Indirapuram, Ghaziabad",
        rent: 18000,
        deposit: 36000,
        bhk: "Shop",
        area: 550,
        furnishing: "Unfurnished",
        allowed: "Commercial Use",
        status: "Available",
        vacantDays: 8,
        owner: "Ramesh Sharma Self",
        availableFrom: "Immediate",
        badge: "Commercial Prime","""

new_prop_105 = """        id: "FLAT-105",
        title: "Central Market 1st Floor Shop / Office",
        locality: "Indirapuram",
        fullAddress: "Shop No 14, Aditya Mega Mall Road, Indirapuram, Ghaziabad",
        rent: 18000,
        deposit: 36000,
        bhk: "Shop",
        area: 550,
        furnishing: "Unfurnished",
        allowed: "Commercial Use",
        status: "Available",
        vacantDays: 8,
        owner: "Ramesh Sharma Self",
        availableFrom: "Immediate",
        badge: "Commercial Prime",
        coords: [28.6380, 77.3680],
        localityScore: {
          water: "Commercial 24h Connection",
          power: "High-Load 3 Phase",
          nightSafety: "9.0 / 10 Market Patrol",
          metroWalk: "8 min Vaishali Metro",
          deliverySpeed: "Direct Mall Access"
        },"""

if old_prop_105 in html:
    html = html.replace(old_prop_105, new_prop_105)

old_prop_106 = """        id: "FLAT-106",
        title: "South Delhi Lajpat Nagar 2BHK Floor",
        locality: "Lajpat Nagar",
        fullAddress: "Floor 2, Block D, Lajpat Nagar 2, New Delhi",
        rent: 22000,
        deposit: 44000,
        bhk: "2BHK",
        area: 980,
        furnishing: "Semi Furnished",
        allowed: "Girls / Family Only",
        status: "Available",
        vacantDays: 1,
        owner: "Smt. Manju Devi",
        availableFrom: "Immediate",
        badge: "South Delhi Prime","""

new_prop_106 = """        id: "FLAT-106",
        title: "South Delhi Lajpat Nagar 2BHK Floor",
        locality: "Lajpat Nagar",
        fullAddress: "Floor 2, Block D, Lajpat Nagar 2, New Delhi",
        rent: 22000,
        deposit: 44000,
        bhk: "2BHK",
        area: 980,
        furnishing: "Semi Furnished",
        allowed: "Girls / Family Only",
        status: "Available",
        vacantDays: 1,
        owner: "Smt. Manju Devi",
        availableFrom: "Immediate",
        badge: "South Delhi Prime",
        coords: [28.5677, 77.2433],
        localityScore: {
          water: "Delhi Jal Board + Tanker",
          power: "Zero Power Cut (Inverter)",
          nightSafety: "9.1 / 10 Gated Colony",
          metroWalk: "2 min Lajpat Nagar Metro",
          deliverySpeed: "7 mins (Blinkit Central)"
        },"""

if old_prop_106 in html:
    html = html.replace(old_prop_106, new_prop_106)

# 2. In Property Card generation (renderPublicPropertyList), add Locality Badges and Compare Button
old_card_amenities = """              <!-- Amenities Small Pill Chips -->
              <div class="flex flex-wrap gap-1.5">
                ${prop.amenities.map(a => `
                  <span class="px-2.5 py-1 rounded-full text-[11px] font-medium bg-white border border-amber-200 text-stone-700">
                    ${a}
                  </span>
                `).join('')}
                <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-cream-200 text-stone-700">
                  + 4 more
                </span>
              </div>"""

new_card_amenities = """              <!-- Delhi-NCR Locality Scorecard Snapshot Row -->
              <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 py-1 text-[11px] font-semibold">
                <div class="flex items-center gap-1.5 px-2 py-1 rounded-lg bg-sky-50 text-sky-800 border border-sky-200">
                  <i class="fa-solid fa-droplet text-sky-600 text-xs"></i>
                  <span class="truncate">${prop.localityScore ? prop.localityScore.water : '24h Ganga Jal'}</span>
                </div>
                <div class="flex items-center gap-1.5 px-2 py-1 rounded-lg bg-amber-50 text-amber-800 border border-amber-200">
                  <i class="fa-solid fa-bolt text-amber-600 text-xs"></i>
                  <span class="truncate">${prop.localityScore ? prop.localityScore.power : 'Zero Power Cut'}</span>
                </div>
                <div class="flex items-center gap-1.5 px-2 py-1 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200">
                  <i class="fa-solid fa-person-walking text-emerald-600 text-xs"></i>
                  <span class="truncate">${prop.localityScore ? prop.localityScore.metroWalk : '5m Metro'}</span>
                </div>
                <div class="flex items-center gap-1.5 px-2 py-1 rounded-lg bg-violet-50 text-violet-800 border border-violet-200">
                  <i class="fa-solid fa-shield-halved text-violet-600 text-xs"></i>
                  <span class="truncate">Safety: ${prop.localityScore ? prop.localityScore.nightSafety : '9.4/10'}</span>
                </div>
              </div>

              <!-- Amenities Small Pill Chips -->
              <div class="flex flex-wrap gap-1.5">
                ${prop.amenities.map(a => `
                  <span class="px-2.5 py-1 rounded-full text-[11px] font-medium bg-white border border-amber-200 text-stone-700">
                    ${a}
                  </span>
                `).join('')}
                <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-cream-200 text-stone-700">
                  + 4 more
                </span>
              </div>"""

if old_card_amenities in html:
    html = html.replace(old_card_amenities, new_card_amenities)

# Add [+ Compare] button to the card bottom row
old_card_bottom = """                <div class="flex items-center gap-2">
                  <!-- WhatsApp Button -->"""

new_card_bottom = """                <div class="flex items-center gap-2">
                  <!-- Compare Toggle Button -->
                  <button 
                    onclick="toggleCompareProperty('${prop.id}', event)" 
                    id="compareBtn-${prop.id}" 
                    class="px-3 py-2 rounded-full text-xs font-bold border transition-all ${isPropertyInCompare(prop.id) ? 'bg-terracotta-700 text-white border-terracotta-700 shadow-sm' : 'bg-white hover:bg-cream-100 text-stone-700 border-amber-300'}"
                    title="Side-by-side compare karein"
                  >
                    <i class="fa-solid fa-code-compare mr-1 text-[11px]"></i>
                    <span>${isPropertyInCompare(prop.id) ? 'Added' : 'Compare'}</span>
                  </button>

                  <!-- WhatsApp Button -->"""

if old_card_bottom in html:
    html = html.replace(old_card_bottom, new_card_bottom)

# 3. Add all master JavaScript functions before </script>
super_js_functions = """
    // ================= SUPER FEATURE 1: PROPERTY COMPARISON TOOL =================
    let selectedCompareList = [];

    function isPropertyInCompare(propId) {
      return selectedCompareList.includes(propId);
    }

    function toggleCompareProperty(propId, event) {
      if (event) event.stopPropagation();
      const index = selectedCompareList.indexOf(propId);
      if (index > -1) {
        selectedCompareList.splice(index, 1);
        showToast("Property comparison se hata di gayi", "info");
      } else {
        if (selectedCompareList.length >= 3) {
          showToast("Aap ek saath maximum 3 properties compare kar sakte hain", "warning");
          return;
        }
        selectedCompareList.push(propId);
        showToast("Property comparison me add ho gayi!", "success");
      }
      renderCompareBar();
      renderPublicPropertyList();
    }

    function renderCompareBar() {
      const bar = document.getElementById('floatingCompareBar');
      const countEl = document.getElementById('compareCount');
      if (!bar || !countEl) return;

      if (selectedCompareList.length > 0) {
        bar.classList.remove('hidden');
        countEl.innerText = selectedCompareList.length;
      } else {
        bar.classList.add('hidden');
      }
    }

    function clearCompareList() {
      selectedCompareList = [];
      renderCompareBar();
      renderPublicPropertyList();
      showToast("Comparison list clear kar di gayi", "info");
    }

    function openCompareModal() {
      if (selectedCompareList.length === 0) {
        showToast("Pehle kam se kam 1 property select karein", "info");
        return;
      }
      const modal = document.getElementById('comparePropertiesModal');
      const body = document.getElementById('compareModalBody');
      if (!modal || !body) return;

      const comparedProps = properties.filter(p => selectedCompareList.includes(p.id));

      body.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-${comparedProps.length} gap-4">
          ${comparedProps.map(p => `
            <div class="bg-white rounded-2xl p-4 border border-amber-200 shadow-sm space-y-3">
              <div class="relative rounded-xl overflow-hidden aspect-[16/10] bg-stone-200">
                <img src="${p.images[0]}" alt="${p.title}" class="w-full h-full object-cover" />
                <span class="absolute top-2 left-2 bg-charcoal-900/90 text-amber-300 font-serif font-bold text-xs px-2.5 py-1 rounded-full">
                  ₹${p.rent.toLocaleString('en-IN')} / mo
                </span>
                <span class="absolute bottom-2 left-2 bg-cream-100 text-charcoal-900 font-bold text-[10px] px-2 py-0.5 rounded-full border border-amber-300">
                  Deposit: ₹${p.deposit.toLocaleString('en-IN')}
                </span>
              </div>

              <div>
                <span class="text-[10px] font-bold text-olive-800 bg-olive-100 px-2 py-0.5 rounded-full">${p.badge || 'Verified'}</span>
                <h4 class="font-serif font-bold text-sm text-charcoal-900 mt-1">${p.title}</h4>
                <p class="text-xs text-stone-500">${p.fullAddress}</p>
              </div>

              <!-- Key Specs Table -->
              <div class="space-y-1.5 text-xs border-t border-amber-100 pt-2">
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Configuration:</span>
                  <span class="font-bold text-charcoal-900">${p.bhk} • ${p.area} sqft</span>
                </div>
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Furnishing:</span>
                  <span class="font-semibold text-charcoal-900">${p.furnishing}</span>
                </div>
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Water Supply:</span>
                  <span class="font-semibold text-sky-800">${p.localityScore ? p.localityScore.water : '24h Water'}</span>
                </div>
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Power Backup:</span>
                  <span class="font-semibold text-amber-800">${p.localityScore ? p.localityScore.power : 'Zero Power Cut'}</span>
                </div>
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Metro Station:</span>
                  <span class="font-semibold text-emerald-800">${p.localityScore ? p.localityScore.metroWalk : 'Near Metro'}</span>
                </div>
                <div class="flex justify-between py-1 border-b border-stone-100">
                  <span class="text-stone-500">Safety Score:</span>
                  <span class="font-bold text-violet-800">${p.localityScore ? p.localityScore.nightSafety : '9.4/10'}</span>
                </div>
                <div class="flex justify-between py-1">
                  <span class="text-stone-500">Grocery Delivery:</span>
                  <span class="font-semibold text-terracotta-700">${p.localityScore ? p.localityScore.deliverySpeed : '8 mins'}</span>
                </div>
              </div>

              <!-- Direct CTA Buttons -->
              <div class="pt-2 flex flex-col gap-2">
                <button onclick="closeCompareModal(); openBookVisitModal('${p.id}');" class="w-full py-2 rounded-full bg-olive-700 hover:bg-olive-800 text-white font-bold text-xs transition-colors shadow-sm">
                  Book Site Visit
                </button>
                <button onclick="closeCompareModal(); openTokenPaymentModal('${p.id}');" class="w-full py-2 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-amber-300 font-bold text-xs transition-colors">
                  Lock ₹2,000 Token
                </button>
              </div>

            </div>
          `).join('')}
        </div>
      `;

      modal.classList.remove('hidden');
    }

    function closeCompareModal() {
      const modal = document.getElementById('comparePropertiesModal');
      if (modal) modal.classList.add('hidden');
    }

    // ================= SUPER FEATURE 2: INTERACTIVE LEAFLET MAP VIEW =================
    let leafletMapInstance = null;
    let leafletMarkersGroup = null;

    function switchListingView(viewMode) {
      const listEl = document.getElementById('propertyCardsList');
      const mapWrapper = document.getElementById('propertyMapWrapper');
      const btnList = document.getElementById('viewToggleList');
      const btnMap = document.getElementById('viewToggleMap');

      if (viewMode === 'map') {
        listEl.classList.add('hidden');
        mapWrapper.classList.remove('hidden');

        btnMap.classList.add('bg-terracotta-700', 'text-white', 'shadow-sm');
        btnMap.classList.remove('text-stone-700');
        btnList.classList.remove('bg-terracotta-700', 'text-white', 'shadow-sm');
        btnList.classList.add('text-stone-700');

        initLeafletMap();
      } else {
        listEl.classList.remove('hidden');
        mapWrapper.classList.add('hidden');

        btnList.classList.add('bg-terracotta-700', 'text-white', 'shadow-sm');
        btnList.classList.remove('text-stone-700');
        btnMap.classList.remove('bg-terracotta-700', 'text-white', 'shadow-sm');
        btnMap.classList.add('text-stone-700');
      }
    }

    function initLeafletMap() {
      if (typeof L === 'undefined') return;

      if (!leafletMapInstance) {
        // Center around Delhi-NCR / Noida / Indirapuram
        leafletMapInstance = L.map('propertyLeafletMap').setView([28.585, 77.34], 12);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; OpenStreetMap contributors • Sharma Rentals'
        }).addTo(leafletMapInstance);

        leafletMarkersGroup = L.layerGroup().addTo(leafletMapInstance);
      }

      setTimeout(() => {
        leafletMapInstance.invalidateSize();
      }, 200);

      renderMapPins();
    }

    function renderMapPins() {
      if (!leafletMarkersGroup) return;
      leafletMarkersGroup.clearLayers();

      const listToRender = getFilteredProperties();

      listToRender.forEach(prop => {
        if (!prop.coords || prop.coords.length !== 2) return;

        const pinHtml = `
          <div class="leaflet-price-pin" onclick="openPropertyDrawer('${prop.id}')">
            <i class="fa-solid fa-house-chimney text-[10px]"></i>
            <span>₹${(prop.rent / 1000).toFixed(1)}k</span>
          </div>
        `;

        const customIcon = L.divIcon({
          html: pinHtml,
          className: 'custom-leaflet-div-icon',
          iconSize: [85, 30],
          iconAnchor: [42, 15]
        });

        const marker = L.marker(prop.coords, { icon: customIcon }).addTo(leafletMarkersGroup);

        const popupContent = `
          <div style="width: 220px;" class="space-y-2">
            <img src="${prop.images[0]}" style="width: 100%; height: 110px; object-fit: cover; border-radius: 12px;" />
            <h5 class="font-serif font-bold text-xs text-charcoal-900">${prop.title}</h5>
            <p class="text-[11px] text-stone-500">${prop.locality} • ${prop.bhk}</p>
            <div class="flex items-center justify-between pt-1">
              <span class="font-serif font-extrabold text-terracotta-700 text-sm">₹${prop.rent.toLocaleString('en-IN')}/mo</span>
              <button onclick="openPropertyDrawer('${prop.id}')" class="px-2.5 py-1 rounded-full bg-charcoal-900 text-white font-bold text-[10px]">Details →</button>
            </div>
          </div>
        `;

        marker.bindPopup(popupContent);
      });
    }

    // ================= SUPER FEATURE 3: AFFORDABILITY CALCULATOR =================
    function updateAffordabilityCalculator() {
      if (!currentSelectedProperty) return;

      const slider = document.getElementById('salarySlider');
      const display = document.getElementById('salaryDisplay');
      const ratioText = document.getElementById('rentVsSalaryText');
      const badge = document.getElementById('affordabilityBadge');
      const bar = document.getElementById('affordabilityBar');
      const advice = document.getElementById('savingsAdvice');
      const depositEmi = document.getElementById('depositEmiText');

      if (!slider) return;

      const salary = parseInt(slider.value, 10);
      display.innerText = "₹" + salary.toLocaleString('en-IN') + " / mahina";

      const rent = currentSelectedProperty.rent;
      const ratio = Math.round((rent / salary) * 100);

      ratioText.innerHTML = `Rent aapki salary ka <b>${ratio}%</b> hai (Recommended: < 30%).`;
      bar.style.width = Math.min(ratio, 100) + "%";

      if (ratio <= 28) {
        badge.innerText = "100% Affordable";
        badge.className = "px-2 py-0.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800 border border-olive-300";
        bar.className = "h-full bg-olive-600 transition-all duration-300";
        advice.innerText = "Perfect Budget Match";
        advice.className = "text-olive-700 font-bold";
      } else if (ratio <= 40) {
        badge.innerText = "Moderate Budget";
        badge.className = "px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-900 border border-amber-300";
        bar.className = "h-full bg-amber-500 transition-all duration-300";
        advice.innerText = "Manageable with Savings";
        advice.className = "text-amber-700 font-bold";
      } else {
        badge.innerText = "High Budget Alert";
        badge.className = "px-2 py-0.5 rounded-full text-[10px] font-bold bg-maroon-100 text-maroon-900 border border-maroon-300";
        bar.className = "h-full bg-maroon-600 transition-all duration-300";
        advice.innerText = "Consider Room Sharing or 1BHK";
        advice.className = "text-maroon-700 font-bold";
      }

      if (depositEmi) {
        const emiPerMonth = Math.round(currentSelectedProperty.deposit / 3);
        depositEmi.innerHTML = `Deposit ₹${currentSelectedProperty.deposit.toLocaleString('en-IN')} ko 3 aasan kishton me dein: <b>₹${emiPerMonth.toLocaleString('en-IN')} / mahina</b>`;
      }
    }

    // ================= SUPER FEATURE 4: POLICE VERIFICATION AUTO-PDF =================
    const POLICE_DATA = {
      "UP": {
        badge: "UTTAR PRADESH POLICE DEPARTMENT",
        thana: "Indirapuram Thana, Ghaziabad",
        title: "TENANT / SERVANT VERIFICATION FORM (किरायेदार सत्यापन प्रपत्र)"
      },
      "DELHI": {
        badge: "DELHI POLICE • CITIZEN SAFETY PORTAL",
        thana: "Lajpat Nagar Police Station, New Delhi",
        title: "DELHI POLICE TENANT VERIFICATION REGISTRATION"
      },
      "HARYANA": {
        badge: "HARYANA POLICE • GURUGRAM COMMISSIONERATE",
        thana: "DLF Phase 1 Police Station, Gurugram",
        title: "GURUGRAM POLICE TENANT SCRUTINY RECORD"
      }
    };

    function populatePoliceDropdowns() {
      const select = document.getElementById('policeTenantSelect');
      if (!select) return;
      select.innerHTML = tenants.map(t => `
        <option value="${t.id}">${t.name} (${t.property})</option>
      `).join('');
      populatePoliceForm();
    }

    function switchPoliceJurisdiction() {
      const state = document.getElementById('policeStateSelect').value;
      const pData = POLICE_DATA[state] || POLICE_DATA["UP"];

      document.getElementById('policeHeaderBadge').innerText = pData.badge;
      document.getElementById('policeThanaName').innerText = pData.thana;
      document.getElementById('policeStationInput').value = pData.thana;
    }

    function populatePoliceForm() {
      const select = document.getElementById('policeTenantSelect');
      if (!select || !tenants.length) return;
      const tenantId = select.value;
      const tenant = tenants.find(t => t.id === tenantId) || tenants[0];

      if (tenant) {
        document.getElementById('policeTenantName').innerText = tenant.name;
        document.getElementById('policeContactId').innerText = `${tenant.phone} • Aadhaar: ${tenant.aadhaar || 'XXXX-XXXX-4821'}`;
        document.getElementById('policeOccupation').innerText = `${tenant.job || 'Corporate Executive'} (${tenant.salary ? 'Salary: ' + tenant.salary : 'Income Verified'})`;
        document.getElementById('policeRentedAddress').innerText = `${tenant.property} • Rent: ₹${tenant.rent.toLocaleString('en-IN')} / month`;
      }
    }

    function printOfficialPoliceForm() {
      window.print();
    }

    // ================= SUPER FEATURE 5: OWNER PAYOUT & RENT SPLIT LEDGER =================
    const DEFAULT_OWNER_PAYOUTS = [
      { id: "PAY-101", property: "Flat 204, Royal Palm", owner: "Sunil Gupta", grossRent: 14500, maintenance: 1500, agentCut: 1000, netPayout: 12000, bankUpi: "sunil.gupta@okhdfcbank", status: "Paid" },
      { id: "PAY-102", property: "Flat 302, Gaur City", owner: "Harish Chandra", grossRent: 12000, maintenance: 1200, agentCut: 1000, netPayout: 9800, bankUpi: "harish.chandra@sbi", status: "Pending" },
      { id: "PAY-103", property: "Tower 4, ATS Pristine", owner: "Col. Rajesh Tyagi", grossRent: 28000, maintenance: 3500, agentCut: 2000, netPayout: 22500, bankUpi: "rajesh.tyagi@icici", status: "Paid" },
      { id: "PAY-104", property: "Studio 12, DLF Phase 5", owner: "Vikram Malhotra", grossRent: 9500, maintenance: 800, agentCut: 700, netPayout: 8000, bankUpi: "vikram.m@paytm", status: "Pending" }
    ];

    let ownerPayouts = [];

    function renderOwnerPayoutTable() {
      const tbody = document.getElementById('adminOwnerPayoutTableBody');
      if (!tbody) return;

      if (!ownerPayouts.length) {
        ownerPayouts = JSON.parse(localStorage.getItem('rentwala_ownerPayouts')) || DEFAULT_OWNER_PAYOUTS;
      }

      tbody.innerHTML = ownerPayouts.map(p => {
        const isPaid = p.status === 'Paid';
        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4">
              <span class="font-bold text-charcoal-900 block">${p.property}</span>
              <span class="text-[11px] text-stone-500">Owner: ${p.owner}</span>
            </td>
            <td class="p-4 font-serif font-bold text-stone-800">₹${p.grossRent.toLocaleString('en-IN')}</td>
            <td class="p-4 text-stone-600 font-serif">-₹${p.maintenance.toLocaleString('en-IN')}</td>
            <td class="p-4 text-terracotta-700 font-serif">-₹${p.agentCut.toLocaleString('en-IN')}</td>
            <td class="p-4">
              <span class="font-serif font-extrabold text-emerald-800 text-sm">₹${p.netPayout.toLocaleString('en-IN')}</span>
            </td>
            <td class="p-4 font-mono text-[11px] text-stone-600">${p.bankUpi}</td>
            <td class="p-4">
              <span class="px-2.5 py-1 rounded-full text-[10px] font-bold ${isPaid ? 'bg-olive-100 text-olive-800 border border-olive-300' : 'bg-amber-100 text-amber-900 border border-amber-300'}">
                ${p.status}
              </span>
            </td>
            <td class="p-4 text-right space-x-1.5">
              ${!isPaid ? `
                <button onclick="transferOwnerPayout('${p.id}')" class="px-3 py-1.5 rounded-full bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-[11px] shadow-sm">
                  Pay UPI
                </button>
              ` : `
                <button onclick="sendOwnerReceiptWhatsApp('${p.owner}', '${p.property}', ${p.netPayout})" class="px-3 py-1.5 rounded-full bg-olive-700 hover:bg-olive-800 text-white font-bold text-[11px] shadow-sm">
                  <i class="fa-brands fa-whatsapp"></i> Receipt
                </button>
              `}
            </td>
          </tr>
        `;
      }).join('');
    }

    function transferOwnerPayout(payoutId) {
      const item = ownerPayouts.find(p => p.id === payoutId);
      if (item) {
        item.status = "Paid";
        localStorage.setItem('rentwala_ownerPayouts', JSON.stringify(ownerPayouts));
        renderOwnerPayoutTable();
        showToast(`₹${item.netPayout.toLocaleString('en-IN')} transferred to ${item.owner} via UPI!`, "success");
      }
    }

    function sendOwnerReceiptWhatsApp(ownerName, property, amount) {
      const msg = encodeURIComponent(`Pranam ${ownerName} Ji, Sharma Rentals dwara aapke flat "${property}" ka is mahine ka net rent payout ₹${amount.toLocaleString('en-IN')} successfully transfer kar diya gaya hai. Receipt attach hai.`);
      window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
    }

    // ================= SUPER FEATURE 6: 11-MONTH RENEWAL & 10% HIKE REMINDERS =================
    function sendHikeNotice(tenantName, property, curRent, newRent) {
      const msg = encodeURIComponent(`Namaste ${tenantName} Ji, aapka 11-month agreement for ${property} jald expire ho raha hai. Standard renewal clause ke anusaar agle 11 mahine ke liye revised rent ₹${newRent.toLocaleString('en-IN')} hoga (10% standard escalation). Kripya agreement renew karwayen - Sharma Rentals.`);
      window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
      showToast(`${tenantName} ko WhatsApp 10% hike notice bhej diya!`, "success");
    }

    function renewAgreementWithHike(tenantName, property, newRent) {
      showToast(`${tenantName} ka agreement ₹${newRent.toLocaleString('en-IN')} par renew ho gaya!`, "success");
    }

    // ================= SUPER FEATURE 7: PWA SERVICE WORKER REGISTRATION =================
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then(reg => {
          console.log('RentWala PWA Service Worker Registered!', reg);
        }).catch(err => {
          console.log('PWA SW Registration bypassed in sandbox', err);
        });
      });
    }
"""

if '// ================= SUPER FEATURE 1: PROPERTY COMPARISON TOOL =================' not in html:
    html = html.replace(
        '// ================= APP INITIALIZATION ON WINDOW LOAD =================',
        super_js_functions + '\n\n    // ================= APP INITIALIZATION ON WINDOW LOAD ================='
    )

# Also ensure initData() calls populatePoliceDropdowns() and renderOwnerPayoutTable()
if 'populatePoliceDropdowns();' not in html:
    html = html.replace(
        'initSignatureCanvas();',
        'initSignatureCanvas();\n      populatePoliceDropdowns();\n      renderOwnerPayoutTable();'
    )

# Also update openPropertyDrawer to populate drawer Locality Score and call updateAffordabilityCalculator
drawer_locality_update = """      // Populate Locality Score
      if (prop.localityScore) {
        const w = document.getElementById('drawerWaterSupply');
        const p = document.getElementById('drawerPowerBackup');
        const s = document.getElementById('drawerNightSafety');
        const m = document.getElementById('drawerMetroWalk');
        const d = document.getElementById('drawerDeliverySpeed');
        if (w) w.innerText = prop.localityScore.water;
        if (p) p.innerText = prop.localityScore.power;
        if (s) s.innerText = prop.localityScore.nightSafety;
        if (m) m.innerText = prop.localityScore.metroWalk;
        if (d) d.innerText = prop.localityScore.deliverySpeed;
      }
      updateAffordabilityCalculator();
"""

if 'drawerWaterSupply' in html and 'prop.localityScore.water' not in html:
    html = html.replace(
        'openGalleryIndex(0);',
        'openGalleryIndex(0);\n' + drawer_locality_update
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 3: All Super Logic successfully injected into index.html!")
