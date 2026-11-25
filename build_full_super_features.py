# -*- coding: utf-8 -*-
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Head with Leaflet and Manifest if not present
if 'leaflet.css' not in html:
    leaflet_head = """  <!-- Leaflet Interactive Maps -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
  <link rel="manifest" href="/manifest.json" />
"""
    html = html.replace('</head>', leaflet_head + '\n</head>')

# 2. Add Styles for Leaflet pins and Compare Bar
if '.leaflet-price-pin' not in html:
    custom_styles = """
    /* Leaflet Price Pin Badge */
    .leaflet-price-pin {
      background: #1C1917;
      color: #FDE68A;
      font-family: 'Fraunces', serif;
      font-weight: 800;
      font-size: 11px;
      padding: 5px 12px;
      border-radius: 9999px;
      border: 1.5px solid #C2410C;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .leaflet-price-pin:hover {
      background: #C2410C;
      color: #FFFFFF;
      transform: scale(1.1);
    }
    .leaflet-popup-content-wrapper {
      background: #FFFBF5 !important;
      border-radius: 20px !important;
      border: 1px solid #FDE68A !important;
      box-shadow: 0 10px 25px rgba(28,25,23,0.15) !important;
      font-family: 'Outfit', sans-serif !important;
      padding: 0 !important;
      overflow: hidden;
    }
    .leaflet-popup-content {
      margin: 12px 14px !important;
      line-height: 1.4 !important;
    }
    /* Comparison Floating Bar */
    .compare-bar-enter {
      animation: slideUpCompare 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes slideUpCompare {
      from { transform: translateY(100%); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    /* Police Verification Form Official Paper Style */
    .police-stamp-paper {
      background: #FFFDF9;
      border: 2px solid #78350F;
      box-shadow: inset 0 0 20px rgba(180, 83, 9, 0.05);
    }
"""
    html = html.replace('</style>', custom_styles + '\n</style>')

# 3. Add View Toggle (List vs Map) in Property Listing Header
view_toggle_html = """
          <!-- View Toggle Buttons: List vs Interactive Map -->
          <div class="flex items-center gap-1.5 bg-cream-200/90 p-1 rounded-full border border-amber-300/80 shadow-sm">
            <button id="viewToggleList" onclick="switchListingView('list')" class="px-3.5 py-1.5 rounded-full text-xs font-bold bg-terracotta-700 text-white shadow-sm flex items-center gap-1.5 transition-all">
              <i class="fa-solid fa-list"></i>
              <span>List View</span>
            </button>
            <button id="viewToggleMap" onclick="switchListingView('map')" class="px-3.5 py-1.5 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 flex items-center gap-1.5 transition-all">
              <i class="fa-solid fa-map-location-dot text-terracotta-700"></i>
              <span>Map View (Pins)</span>
            </button>
          </div>
"""

# Place view toggle right next to Sort Select
target_sort_div = '<select id="propertySortSelect"'
if 'id="viewToggleMap"' not in html:
    html = html.replace(
        '<div class="flex items-center gap-2 bg-cream-100 px-4 py-2 rounded-full border border-amber-200/80 shadow-sm">',
        view_toggle_html + '\n          <div class="flex items-center gap-2 bg-cream-100 px-4 py-2 rounded-full border border-amber-200/80 shadow-sm">'
    )

# 4. Add Interactive Map Container right above Property Cards List
map_container_html = """
      <!-- INTERACTIVE LEAFLET MAP VIEW (DELHI-NCR PINS) -->
      <div id="propertyMapWrapper" class="hidden mb-8 w-full h-[520px] rounded-3xl border border-amber-200/90 shadow-warm-card overflow-hidden relative">
        <div id="propertyLeafletMap" class="w-full h-full z-10"></div>
        <div class="absolute top-4 right-4 z-20 bg-white/95 backdrop-blur-md px-3.5 py-2 rounded-2xl border border-amber-200 shadow-md flex items-center gap-2 text-xs font-bold text-charcoal-900">
          <i class="fa-solid fa-layer-group text-terracotta-700"></i>
          <span>Delhi-NCR Verified Clusters</span>
        </div>
      </div>
"""

if 'id="propertyMapWrapper"' not in html:
    html = html.replace(
        '<div id="propertyCardsList" class="space-y-6">',
        map_container_html + '\n      <div id="propertyCardsList" class="space-y-6">'
    )

# 5. Add Locality Score & Affordability Calculator into Property Details Drawer
drawer_locality_and_calc_html = """
        <!-- SHARMA JI LOCALITY & LIFESTYLE SCORECARD (DELHI-NCR) -->
        <div class="bg-cream-100/90 rounded-2xl p-4 border border-amber-200/90">
          <div class="flex items-center justify-between mb-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-charcoal-900 flex items-center gap-1.5">
              <i class="fa-solid fa-award text-amber-600"></i> Sharma Ji Locality & Lifestyle Scorecard
            </h4>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800 border border-olive-300">
              Verified by Field Team
            </span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-xs">
            <div class="bg-white p-2.5 rounded-xl border border-amber-200/60">
              <div class="flex items-center gap-1.5 text-sky-700 font-bold mb-0.5">
                <i class="fa-solid fa-droplet"></i> Paani Ki Suvidha
              </div>
              <p id="drawerWaterSupply" class="text-stone-700 font-medium text-[11px]">24h Ganga Jal + Dual Submersible</p>
            </div>
            <div class="bg-white p-2.5 rounded-xl border border-amber-200/60">
              <div class="flex items-center gap-1.5 text-amber-700 font-bold mb-0.5">
                <i class="fa-solid fa-bolt"></i> Power Cut Status
              </div>
              <p id="drawerPowerBackup" class="text-stone-700 font-medium text-[11px]">Zero Power Cut (100% DG Backup)</p>
            </div>
            <div class="bg-white p-2.5 rounded-xl border border-amber-200/60">
              <div class="flex items-center gap-1.5 text-violet-700 font-bold mb-0.5">
                <i class="fa-solid fa-shield-halved"></i> Night Safety Score
              </div>
              <p id="drawerNightSafety" class="text-stone-700 font-medium text-[11px]">9.4 / 10 (Gated Security + CCTV)</p>
            </div>
            <div class="bg-white p-2.5 rounded-xl border border-amber-200/60">
              <div class="flex items-center gap-1.5 text-emerald-700 font-bold mb-0.5">
                <i class="fa-solid fa-person-walking"></i> Metro Distance
              </div>
              <p id="drawerMetroWalk" class="text-stone-700 font-medium text-[11px]">6 mins walk (Blue Line Metro)</p>
            </div>
            <div class="bg-white p-2.5 rounded-xl border border-amber-200/60 sm:col-span-2">
              <div class="flex items-center gap-1.5 text-terracotta-700 font-bold mb-0.5">
                <i class="fa-solid fa-truck-fast"></i> Instant Grocery Delivery
              </div>
              <p id="drawerDeliverySpeed" class="text-stone-700 font-medium text-[11px]">7-9 mins (Blinkit, Swiggy Instamart, Zepto Live)</p>
            </div>
          </div>
        </div>

        <!-- AFFORDABILITY & RENT VS SALARY CALCULATOR & 3-EMI DEPOSIT SPLIT -->
        <div class="bg-gradient-to-br from-cream-100 to-amber-100/50 rounded-2xl p-4 border border-amber-300/80 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="text-xs font-bold uppercase tracking-wider text-charcoal-900 flex items-center gap-1.5">
              <i class="fa-solid fa-calculator text-terracotta-700"></i> Aapka Monthly Budget & Affordability Check
            </h4>
            <span id="affordabilityBadge" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-olive-100 text-olive-800 border border-olive-300">
              100% Affordable
            </span>
          </div>
          
          <div class="space-y-1.5">
            <div class="flex justify-between text-xs font-semibold text-stone-700">
              <span>Aapki Monthly Salary (Take-Home):</span>
              <span id="salaryDisplay" class="font-serif font-bold text-terracotta-800 text-sm">₹50,000 / mahina</span>
            </div>
            <input 
              type="range" 
              id="salarySlider" 
              min="20000" 
              max="200000" 
              step="5000" 
              value="50000" 
              oninput="updateAffordabilityCalculator()"
              class="w-full accent-terracotta-700 cursor-pointer"
            />
          </div>

          <!-- Affordability Ratio Bar -->
          <div class="p-3 bg-white/90 rounded-xl border border-amber-200 space-y-2">
            <div class="flex justify-between text-[11px] font-medium text-stone-600">
              <span id="rentVsSalaryText">Rent aapki salary ka <b>24%</b> hai (Recommended: < 30%).</span>
              <span id="savingsAdvice" class="text-olive-700 font-bold">Safe & Good Budget</span>
            </div>
            <div class="w-full h-2 rounded-full bg-stone-200 overflow-hidden">
              <div id="affordabilityBar" class="h-full bg-olive-600 transition-all duration-300" style="width: 24%;"></div>
            </div>
          </div>

          <!-- Deposit 3-Installment EMI Split -->
          <div class="p-3 rounded-xl bg-amber-50/90 border border-amber-200 text-xs flex items-center justify-between gap-3">
            <div>
              <p class="font-bold text-charcoal-900">0% Interest Deposit EMI Option</p>
              <p class="text-[11px] text-stone-600" id="depositEmiText">Deposit ₹24,000 ko 3 aasan kishton me dein: <b>₹8,000 / mahina</b></p>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10px] font-extrabold bg-terracotta-700 text-white shrink-0">
              Sharma Ji Assist
            </span>
          </div>
        </div>
"""

if 'id="drawerWaterSupply"' not in html:
    html = html.replace(
        '<!-- Society Amenities Grid -->',
        drawer_locality_and_calc_html + '\n\n        <!-- Society Amenities Grid -->'
    )

# 6. Add Compare Properties Floating Bar and Compare Modal
compare_html = """
  <!-- ==================== FLOATING PROPERTY COMPARE BAR ==================== -->
  <div id="floatingCompareBar" class="hidden fixed bottom-6 left-1/2 -translate-x-1/2 z-40 max-w-xl w-[92%] glass-pill bg-[#FFFBF5]/95 backdrop-blur-md rounded-full px-4 sm:px-6 py-3 border-2 border-terracotta-700 shadow-2xl flex items-center justify-between gap-3 compare-bar-enter">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-full bg-terracotta-700 text-white flex items-center justify-center font-bold text-xs shadow-md">
        <i class="fa-solid fa-code-compare"></i>
      </div>
      <div>
        <p class="text-xs font-bold text-charcoal-900"><span id="compareCount">2</span> Properties Selected</p>
        <p class="text-[10px] text-stone-500">Side-by-side rent, deposit aur scorecard dekhein</p>
      </div>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="clearCompareList()" class="px-3 py-1.5 rounded-full text-xs font-bold text-stone-600 hover:text-stone-900 hover:bg-stone-100 transition-colors">
        Clear
      </button>
      <button onclick="openCompareModal()" class="px-4 py-2 rounded-full bg-terracotta-700 hover:bg-terracotta-800 text-white text-xs font-bold shadow-pill flex items-center gap-1.5 transition-transform hover:scale-105">
        <span>Compare Now</span>
        <i class="fa-solid fa-arrow-right text-[10px]"></i>
      </button>
    </div>
  </div>

  <!-- ==================== PROPERTY COMPARISON MODAL ==================== -->
  <div id="comparePropertiesModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6">
    <div class="bg-[#FFFBF5] rounded-3xl border border-amber-200 shadow-2xl max-w-4xl w-full max-h-[92vh] flex flex-col overflow-hidden">
      
      <!-- Modal Header -->
      <div class="p-5 border-b border-amber-200 flex items-center justify-between bg-cream-100">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-full bg-terracotta-700 text-white flex items-center justify-center">
            <i class="fa-solid fa-code-compare text-sm"></i>
          </div>
          <div>
            <h3 class="font-serif text-lg sm:text-xl font-bold text-charcoal-900">Side-by-Side Property Comparison</h3>
            <p class="text-xs text-stone-500">Rent, deposit, amenities aur Delhi-NCR scorecard ka aamne-samne muqabla</p>
          </div>
        </div>
        <button onclick="closeCompareModal()" class="w-8 h-8 rounded-full bg-amber-200/80 hover:bg-amber-300 text-charcoal-900 flex items-center justify-center transition-colors">
          <i class="fa-solid fa-xmark text-sm"></i>
        </button>
      </div>

      <!-- Modal Body Comparison Table -->
      <div id="compareModalBody" class="p-4 sm:p-6 overflow-y-auto overflow-x-auto space-y-4">
        <!-- Injected via renderCompareModalContent() -->
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-amber-200 bg-cream-50 flex items-center justify-between text-xs text-stone-600">
        <span>Sharma Ji Verified Rates • No Hidden Charges</span>
        <button onclick="closeCompareModal()" class="px-4 py-2 rounded-full bg-stone-200 hover:bg-stone-300 text-stone-800 font-bold transition-colors">
          Band Karein
        </button>
      </div>

    </div>
  </div>
"""

if 'id="floatingCompareBar"' not in html:
    html = html.replace('<!-- ==================== NOTIFICATION TOAST ==================== -->', compare_html + '\n  <!-- ==================== NOTIFICATION TOAST ==================== -->')

# 7. Add Admin Sub-Tabs: 8. Police Verification and 9. Owner Payout Ledger
admin_nav_buttons_html = """      <button onclick="switchAdminTab('policeVerificationTab')" class="admin-tab-btn px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 transition-all whitespace-nowrap">
        <i class="fa-solid fa-building-shield mr-1.5"></i> 8. Police Verification
      </button>
      <button onclick="switchAdminTab('ownerPayoutTab')" class="admin-tab-btn px-4 py-2 rounded-full text-xs font-semibold text-stone-700 hover:text-terracotta-700 transition-all whitespace-nowrap">
        <i class="fa-solid fa-money-bill-transfer mr-1.5"></i> 9. Owner Payout Ledger
      </button>"""

if 'policeVerificationTab' not in html:
    html = html.replace(
        '<button onclick="switchAdminTab(\'maintenanceTab\')"',
        admin_nav_buttons_html + '\n      <button onclick="switchAdminTab(\'maintenanceTab\')"'
    )

# 8. Add Tab 8: Police Verification & Tab 9: Owner Payout Content
admin_tab_contents_html = """
    <!-- ================= TAB 8: POLICE VERIFICATION (AUTO-PDF / PRINT) ================= -->
    <div id="policeVerificationTab" class="admin-tab-content hidden">
      <div class="bg-white rounded-3xl border border-amber-200/80 shadow-warm-card overflow-hidden">
        
        <div class="p-6 border-b border-amber-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-cream-50">
          <div>
            <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-maroon-100 text-maroon-900 border border-maroon-300 mb-1">
              <i class="fa-solid fa-shield-halved"></i> Mandatory Legal Compliance
            </div>
            <h3 class="font-serif text-xl font-bold text-charcoal-900">Tenant Police Verification Form (किरायेदार सत्यापन प्रपत्र)</h3>
            <p class="text-xs text-stone-500">Delhi, UP ya Haryana Police ke standard format me auto-fill karein aur print karein</p>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="printOfficialPoliceForm()" class="px-4 py-2 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-white text-xs font-bold shadow-pill flex items-center gap-2 transition-all">
              <i class="fa-solid fa-print"></i>
              <span>Print Police Form</span>
            </button>
          </div>
        </div>

        <div class="p-6 space-y-6">
          
          <!-- Select Jurisdiction & Tenant Row -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 p-4 rounded-2xl bg-cream-100 border border-amber-200">
            <div>
              <label class="block text-[11px] font-bold uppercase text-stone-500 mb-1">Police State Jurisdiction</label>
              <select id="policeStateSelect" onchange="switchPoliceJurisdiction()" class="w-full bg-white p-2.5 rounded-xl border border-amber-300 text-xs font-bold text-charcoal-900">
                <option value="UP">Uttar Pradesh Police (Ghaziabad / Noida)</option>
                <option value="DELHI">Delhi Police (South / East Delhi)</option>
                <option value="HARYANA">Haryana Police (Gurugram Commissionerate)</option>
              </select>
            </div>
            <div>
              <label class="block text-[11px] font-bold uppercase text-stone-500 mb-1">Select Tenant</label>
              <select id="policeTenantSelect" onchange="populatePoliceForm()" class="w-full bg-white p-2.5 rounded-xl border border-amber-300 text-xs font-bold text-charcoal-900">
                <!-- Injected dynamically -->
              </select>
            </div>
            <div>
              <label class="block text-[11px] font-bold uppercase text-stone-500 mb-1">Local Police Station (Thana)</label>
              <input type="text" id="policeStationInput" value="Indirapuram Thana, Ghaziabad" class="w-full bg-white p-2.5 rounded-xl border border-amber-300 text-xs font-semibold text-charcoal-900" />
            </div>
          </div>

          <!-- Official Police Verification Preview Paper -->
          <div id="policePrintArea" class="police-stamp-paper rounded-2xl p-6 sm:p-8 max-w-3xl mx-auto border-2 border-stone-800 shadow-lg text-charcoal-900 space-y-6">
            
            <!-- Official Header -->
            <div class="text-center border-b-2 border-stone-800 pb-4">
              <div class="inline-block px-3 py-1 rounded bg-stone-900 text-white font-bold text-xs uppercase tracking-widest mb-1" id="policeHeaderBadge">
                UTTAR PRADESH POLICE DEPARTMENT
              </div>
              <h2 class="font-serif text-xl sm:text-2xl font-bold uppercase tracking-wide">TENANT / SERVANT VERIFICATION FORM</h2>
              <p class="text-xs font-semibold text-stone-700">(नियम 4 / 12 के अन्तर्गत किरायेदार सत्यापन प्रपत्र)</p>
              <p class="text-[11px] text-stone-600 mt-1">To: Station House Officer (SHO), <span id="policeThanaName" class="font-bold underline">Indirapuram Thana, Ghaziabad</span></p>
            </div>

            <!-- Photo & Basic Tenant Identity Row -->
            <div class="flex flex-col sm:flex-row gap-6 items-start justify-between">
              <div class="space-y-3 flex-1 text-xs">
                <div>
                  <span class="font-bold text-stone-600 block text-[10px] uppercase">1. Tenant Full Name (किरायेदार का पूरा नाम):</span>
                  <span id="policeTenantName" class="font-serif font-bold text-sm sm:text-base text-charcoal-900">Rahul Verma</span>
                </div>
                <div>
                  <span class="font-bold text-stone-600 block text-[10px] uppercase">2. Father's / Husband's Name (पिता/पति का नाम):</span>
                  <span id="policeFatherName" class="font-bold text-stone-800">Shri Surendra Verma</span>
                </div>
                <div>
                  <span class="font-bold text-stone-600 block text-[10px] uppercase">3. Mobile Number & Aadhaar ID (मोबाइल व आधार संख्या):</span>
                  <span id="policeContactId" class="font-mono font-bold text-stone-900">+91 98112 34567 • Aadhaar: XXXX-XXXX-4821</span>
                </div>
                <div>
                  <span class="font-bold text-stone-600 block text-[10px] uppercase">4. Occupation / Employer (व्यवसाय / कंपनी का नाम व पता):</span>
                  <span id="policeOccupation" class="font-medium text-stone-800">Senior Software Engineer at HCL Tech, Sector 126, Noida</span>
                </div>
              </div>

              <!-- Passport Photo Box -->
              <div class="w-28 h-36 border-2 border-dashed border-stone-400 rounded-lg bg-stone-100 flex flex-col items-center justify-center text-center p-2 shrink-0 self-center sm:self-start">
                <i class="fa-solid fa-user text-2xl text-stone-400 mb-1"></i>
                <span class="text-[9px] font-bold text-stone-500 uppercase">Affix Recent Passport Photo</span>
              </div>
            </div>

            <!-- Address Blocks -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs border-t border-stone-300 pt-4">
              <div class="bg-cream-100/60 p-3 rounded-xl border border-amber-200">
                <span class="font-bold text-stone-600 block text-[10px] uppercase mb-1">5. Permanent Hometown Address (स्थायी पता):</span>
                <p id="policePermanentAddress" class="text-stone-800 font-medium leading-relaxed">
                  H.No. 42, Civil Lines, Near Railway Station, Kanpur, Uttar Pradesh - 208001
                </p>
              </div>
              <div class="bg-cream-100/60 p-3 rounded-xl border border-amber-200">
                <span class="font-bold text-stone-600 block text-[10px] uppercase mb-1">6. Rented Flat Address (वर्तमान किराये का पता):</span>
                <p id="policeRentedAddress" class="text-stone-800 font-medium leading-relaxed">
                  Flat 204, Tower B, Royal Palm, Vaibhav Khand, Indirapuram, Ghaziabad (Rent: ₹14,500)
                </p>
              </div>
            </div>

            <!-- Landlord & Agent Details -->
            <div class="text-xs border-t border-stone-300 pt-4 space-y-2">
              <span class="font-bold text-stone-600 block text-[10px] uppercase">7. Landlord / Authorized Rental Agent (मकान मालिक व अधिकृत एजेंट):</span>
              <p class="text-stone-800">
                <b>Landlord:</b> <span id="policeLandlordName">Sunil Gupta</span> • <b>Authorized Agent:</b> Ramesh Sharma (Sharma Rentals / RentWala, Reg #AGY-2026-DLH)
              </p>
            </div>

            <!-- Legal Declaration -->
            <div class="text-[11px] text-stone-600 border-t border-stone-300 pt-3 leading-relaxed">
              <b>Declaration (घोषणा):</b> Main tasdeek karta hoon ki upar diye gaye sabhi vivaran satya hain aur meri jankari me koi apraadhik record nahi hai.
            </div>

            <!-- Signatures Row -->
            <div class="grid grid-cols-2 gap-8 border-t-2 border-stone-800 pt-6 mt-6 text-center text-xs">
              <div>
                <div class="h-12 flex items-center justify-center font-serif italic text-stone-600">
                  Digitally Verified by Sharma Rentals
                </div>
                <div class="border-t border-stone-400 pt-1 font-bold text-stone-800">
                  Landlord / Agent Signature
                </div>
              </div>
              <div>
                <div class="h-12 flex items-center justify-center font-serif italic text-stone-600">
                  Signature & Thumb Impression
                </div>
                <div class="border-t border-stone-400 pt-1 font-bold text-stone-800">
                  Tenant's Signature (किरायेदार के हस्ताक्षर)
                </div>
              </div>
            </div>

          </div>

        </div>

      </div>
    </div>

    <!-- ================= TAB 9: OWNER PAYOUT & RENT SPLIT LEDGER ================= -->
    <div id="ownerPayoutTab" class="admin-tab-content hidden">
      <div class="bg-white rounded-3xl border border-amber-200/80 shadow-warm-card overflow-hidden">
        
        <div class="p-6 border-b border-amber-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-cream-50">
          <div>
            <h3 class="font-serif text-xl font-bold text-charcoal-900">Owner Payout & Rent Split Ledger (मकान मालिक हिसाब)</h3>
            <p class="text-xs text-stone-500">Rent aane ke baad Society Maintenance, Sharma Ji cut aur Owner net payout ka automatic hisab</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="px-3 py-1.5 rounded-full text-xs font-bold bg-olive-100 text-olive-800 border border-olive-300">
              <i class="fa-solid fa-circle-check mr-1 text-olive-700"></i> Auto Split Active
            </span>
          </div>
        </div>

        <!-- KPI Split Summary Banner -->
        <div class="p-6 border-b border-amber-100 grid grid-cols-1 sm:grid-cols-4 gap-4">
          <div class="p-4 rounded-2xl bg-cream-100 border border-amber-200">
            <span class="text-[11px] font-bold uppercase text-stone-500">Gross Rent Collected</span>
            <p class="font-serif text-2xl font-bold text-charcoal-900 mt-1">₹4,50,000</p>
            <span class="text-[10px] text-stone-500">38 Rented Flats</span>
          </div>
          <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200">
            <span class="text-[11px] font-bold uppercase text-amber-800">Society Maintenance Cut</span>
            <p class="font-serif text-2xl font-bold text-amber-900 mt-1">₹28,000</p>
            <span class="text-[10px] text-amber-700">Paid to RWA Committees</span>
          </div>
          <div class="p-4 rounded-2xl bg-olive-50 border border-olive-200">
            <span class="text-[11px] font-bold uppercase text-olive-800">Sharma Ji Commission</span>
            <p class="font-serif text-2xl font-bold text-olive-900 mt-1">₹60,000</p>
            <span class="text-[10px] text-olive-700">Net Business Revenue</span>
          </div>
          <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-300">
            <span class="text-[11px] font-bold uppercase text-emerald-800">Net Owner Payouts</span>
            <p class="font-serif text-2xl font-bold text-emerald-900 mt-1">₹3,62,000</p>
            <span class="text-[10px] text-emerald-700">₹3,02k Paid • ₹60k Pending</span>
          </div>
        </div>

        <!-- Owner Split Table -->
        <div class="p-6">
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-cream-200/80 text-charcoal-900 text-xs uppercase font-serif tracking-wider border-b border-amber-200">
                  <th class="p-4">Property & Owner</th>
                  <th class="p-4">Gross Rent</th>
                  <th class="p-4">Maintenance</th>
                  <th class="p-4">Agent Cut</th>
                  <th class="p-4">Net Owner Payout</th>
                  <th class="p-4">Bank / UPI Details</th>
                  <th class="p-4">Payout Status</th>
                  <th class="p-4 text-right">Actions</th>
                </tr>
              </thead>
              <tbody id="adminOwnerPayoutTableBody" class="text-xs divide-y divide-amber-100">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>
"""

if 'id="policeVerificationTab"' not in html:
    html = html.replace(
        '<!-- ================= MODAL 1: BOOK SITE VISIT ================= -->',
        admin_tab_contents_html + '\n\n    <!-- ================= MODAL 1: BOOK SITE VISIT ================= -->'
    )

# 9. In Agreement Tab, add the 11-Month Renewal & 10% Hike Reminder Section
renewal_hike_html = """
        <!-- 11-MONTH AGREEMENT RENEWAL & 10% HIKE REMINDER TRACKER -->
        <div class="mt-8 p-6 rounded-2xl bg-gradient-to-r from-amber-100/70 via-cream-100 to-terracotta-50 border-2 border-amber-300 shadow-sm space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-terracotta-100 text-terracotta-900 border border-terracotta-300 mb-1">
                <i class="fa-solid fa-clock-rotate-left"></i> 11-Month Renewal & Escalation Notice
              </div>
              <h4 class="font-serif text-lg font-bold text-charcoal-900">Upcoming 11-Month Agreement Renewals (+10% Rent Escalation)</h4>
              <p class="text-xs text-stone-600">Standard 11-month tenure khatam hone par automatic 10% rent hike ke saath renew karein</p>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-200 text-amber-900 border border-amber-300">
              2 Renewals Due This Month
            </span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            
            <!-- Renewal Card 1 -->
            <div class="p-4 rounded-xl bg-white border border-amber-200/90 shadow-sm space-y-3">
              <div class="flex justify-between items-start">
                <div>
                  <h5 class="font-bold text-charcoal-900 text-sm">Rahul Verma</h5>
                  <p class="text-xs text-stone-500">Flat 204, Royal Palm, Indirapuram</p>
                </div>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-maroon-100 text-maroon-800">
                  Expires in 35 Days (30 Dec)
                </span>
              </div>
              <div class="flex items-center justify-between p-2.5 rounded-lg bg-cream-50 text-xs border border-amber-100">
                <div>
                  <span class="text-stone-500 block text-[10px]">Current Rent:</span>
                  <span class="font-serif font-bold text-stone-800">₹14,500</span>
                </div>
                <div class="text-right">
                  <span class="text-terracotta-700 font-bold block text-[10px]">+10% Hike (+₹1,450):</span>
                  <span class="font-serif font-extrabold text-terracotta-700 text-sm">₹15,950 / mo</span>
                </div>
              </div>
              <div class="flex gap-2">
                <button onclick="sendHikeNotice('Rahul Verma', 'Flat 204', 14500, 15950)" class="flex-1 py-2 rounded-full bg-olive-700 hover:bg-olive-800 text-white font-bold text-[11px] shadow-sm flex items-center justify-center gap-1.5 transition-colors">
                  <i class="fa-brands fa-whatsapp"></i> Send 10% Hike Notice
                </button>
                <button onclick="renewAgreementWithHike('Rahul Verma', 'Flat 204', 15950)" class="px-3 py-2 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-white font-bold text-[11px] shadow-sm transition-colors">
                  Auto-Renew
                </button>
              </div>
            </div>

            <!-- Renewal Card 2 -->
            <div class="p-4 rounded-xl bg-white border border-amber-200/90 shadow-sm space-y-3">
              <div class="flex justify-between items-start">
                <div>
                  <h5 class="font-bold text-charcoal-900 text-sm">Pooja Sharma</h5>
                  <p class="text-xs text-stone-500">Flat 108, Gaur City, Sector 62</p>
                </div>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800">
                  Expires in 42 Days (05 Jan)
                </span>
              </div>
              <div class="flex items-center justify-between p-2.5 rounded-lg bg-cream-50 text-xs border border-amber-100">
                <div>
                  <span class="text-stone-500 block text-[10px]">Current Rent:</span>
                  <span class="font-serif font-bold text-stone-800">₹12,000</span>
                </div>
                <div class="text-right">
                  <span class="text-terracotta-700 font-bold block text-[10px]">+10% Hike (+₹1,200):</span>
                  <span class="font-serif font-extrabold text-terracotta-700 text-sm">₹13,200 / mo</span>
                </div>
              </div>
              <div class="flex gap-2">
                <button onclick="sendHikeNotice('Pooja Sharma', 'Flat 108', 12000, 13200)" class="flex-1 py-2 rounded-full bg-olive-700 hover:bg-olive-800 text-white font-bold text-[11px] shadow-sm flex items-center justify-center gap-1.5 transition-colors">
                  <i class="fa-brands fa-whatsapp"></i> Send 10% Hike Notice
                </button>
                <button onclick="renewAgreementWithHike('Pooja Sharma', 'Flat 108', 13200)" class="px-3 py-2 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-white font-bold text-[11px] shadow-sm transition-colors">
                  Auto-Renew
                </button>
              </div>
            </div>

          </div>
        </div>
"""

if '11-Month Renewal & Escalation Notice' not in html:
    html = html.replace(
        '<!-- Official Stamp Paper Agreement Preview Box -->',
        renewal_hike_html + '\n\n        <!-- Official Stamp Paper Agreement Preview Box -->'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 2: HTML UI markup successfully added!")
