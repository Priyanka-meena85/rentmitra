
    // Initial Seed Data for Authentic Indian Rental Properties
    const DEFAULT_PROPERTIES = [
      {
        id: "FLAT-101",
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
        amenities: ["Lift", "Car Parking", "24h Water", "Power Backup", "WiFi", "Gym"]
      },
      {
        id: "FLAT-102",
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
        images: [
          "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Lift", "24h Water", "Gated Security", "WiFi", "Market 100m"]
      },
      {
        id: "FLAT-103",
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
        images: [
          "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Clubhouse", "Swimming Pool", "2 Reserved Parking", "Power Backup", "Gym"]
      },
      {
        id: "FLAT-104",
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
        images: [
          "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?auto=format&fit=crop&w=900&q=80",
          "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Food Included Option", "AC", "WiFi", "Daily Cleaning", "Power Backup"]
      },
      {
        id: "FLAT-105",
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
        images: [
          "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Main Road Facing", "High Footfall", "Water Connection", "24/7 Access"]
      },
      {
        id: "FLAT-106",
        title: "South Delhi Lajpat Nagar 2BHK Floor",
        locality: "Lajpat Nagar",
        fullAddress: "C-Block, Lajpat Nagar 2, Near Central Market Metro, New Delhi",
        rent: 22000,
        deposit: 44000,
        bhk: "2BHK",
        area: 980,
        furnishing: "Full Furnished",
        allowed: "Family / Girls Only",
        status: "Booked",
        vacantDays: 0,
        owner: "Mrs. Kamla Devi",
        availableFrom: "Booked by Token",
        badge: "Direct Metro 200m",
        images: [
          "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=900&q=80"
        ],
        amenities: ["Park Facing", "Metro 200m", "Modular Kitchen", "Terrace Access"]
      }
    ];

    // Seed Tenants
    const DEFAULT_TENANTS = [
      {
        id: "TEN-01",
        name: "Rahul Verma",
        property: "Flat 204, Royal Palm",
        phone: "+91 98111 22334",
        rent: 14500,
        agreementEnd: "30 Dec 2026",
        score: 4.8,
        aadhaar: "XXXX-XXXX-9821",
        job: "Sr. Software Engineer @ Adobe",
        salary: "₹1,40,000 / mo",
        familyMembers: "2 Adults (Husband & Wife)"
      },
      {
        id: "TEN-02",
        name: "Amit Singhal",
        property: "Flat 302, Gaur City",
        phone: "+91 98712 34567",
        rent: 12000,
        agreementEnd: "15 Apr 2027",
        score: 4.5,
        aadhaar: "XXXX-XXXX-4512",
        job: "Marketing Lead @ Zomato",
        salary: "₹95,000 / mo",
        familyMembers: "Bachelor (Single)"
      },
      {
        id: "TEN-03",
        name: "Col. Rajesh Tyagi",
        property: "Tower 4, ATS Pristine",
        phone: "+91 94120 88990",
        rent: 28000,
        agreementEnd: "31 Aug 2027",
        score: 4.9,
        aadhaar: "XXXX-XXXX-1102",
        job: "Retired Indian Army",
        salary: "Pension + Consulting",
        familyMembers: "Family (3 Members)"
      }
    ];

    // Seed Rent Collections
    const DEFAULT_RENT_COLLECTIONS = [
      { id: "RC-01", property: "Flat 204, Royal Palm", tenant: "Rahul Verma", dueDate: "05 Dec 2026", amount: 14500, status: "Paid" },
      { id: "RC-02", property: "Flat 302, Gaur City", tenant: "Amit Singhal", dueDate: "05 Nov 2026", amount: 12200, status: "Late" }, // +₹200 Late Fee
      { id: "RC-03", property: "Tower 4, ATS Pristine", tenant: "Col. Rajesh Tyagi", dueDate: "05 Dec 2026", amount: 28000, status: "Paid" },
      { id: "RC-04", property: "Studio 12, DLF Phase 5", tenant: "Deepak Rawat", dueDate: "01 Dec 2026", amount: 9500, status: "Pending" }
    ];

    // Seed Commissions
    const DEFAULT_COMMISSIONS = [
      { id: "COM-01", date: "15 Nov 2026", property: "Flat 204, Royal Palm", tenant: "Rahul Verma", rent: 14500, commission: 14500, status: "Received" },
      { id: "COM-02", date: "20 Nov 2026", property: "ATS Pristine 3BHK", tenant: "Col. Rajesh Tyagi", rent: 28000, commission: 28000, status: "Received" },
      { id: "COM-03", date: "24 Nov 2026", property: "Studio 12, Gurgaon", tenant: "Deepak Rawat", rent: 9500, commission: 9500, status: "Received" },
      { id: "COM-04", date: "25 Nov 2026", property: "Lajpat Nagar 2BHK", tenant: "Mrs. Kamla Devi Deal", rent: 22000, commission: 8000, status: "Pending" }
    ];

    // Seed Leads
    const DEFAULT_LEADS = [
      { id: "VISIT-1024", tenant: "Amit Kumar", phone: "9876501234", property: "Flat 204, Royal Palm", date: "26 Nov 2026", time: "11:00 AM", status: "Visit Done" },
      { id: "VISIT-1025", tenant: "Pooja Hegde", phone: "9811199887", property: "Flat 302, Gaur City", date: "26 Nov 2026", time: "02:00 PM", status: "Token Done" },
      { id: "VISIT-1026", tenant: "Saurabh Mishra", phone: "9988776655", property: "ATS Pristine 3BHK", date: "27 Nov 2026", time: "05:00 PM", status: "New" }
    ];

    // Seed Complaints / Maintenance
    const DEFAULT_COMPLAINTS = [
      { id: "TKT-401", date: "24 Nov", tenant: "Rahul Verma", property: "Flat 204", issue: "Master bathroom ka nal tapak raha hai", category: "Plumbing", photo: "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=200&q=80", mistri: "Raju Mistri (Plumber - 9811199000)", status: "In Progress" },
      { id: "TKT-402", date: "22 Nov", tenant: "Amit Singhal", property: "Flat 302", issue: "Balcony light socket spark kar raha hai", category: "Electricity", photo: "https://images.unsplash.com/photo-1558227691-41ea78d1f631?auto=format&fit=crop&w=200&q=80", mistri: "Sonu Wireman (Electrician)", status: "Done" }
    ];

    // Global State management with LocalStorage
    let properties = [];
    let tenants = [];
    let rentCollections = [];
    let commissions = [];
    let leads = [];
    let complaints = [];

    let currentFilter = 'all';
    let currentSelectedProperty = null;
    let selectedTimeSlot = '11:00 AM';

    let isBackendConnected = false;

    // Initialize Data from Server REST API (with LocalStorage fallback)
    async function initData() {
      // 1. Immediately load local data so UI renders in 0ms without waiting
      properties = JSON.parse(localStorage.getItem('rentwala_properties')) || DEFAULT_PROPERTIES;
      tenants = JSON.parse(localStorage.getItem('rentwala_tenants')) || DEFAULT_TENANTS;
      rentCollections = JSON.parse(localStorage.getItem('rentwala_rentCollections')) || DEFAULT_RENT_COLLECTIONS;
      commissions = JSON.parse(localStorage.getItem('rentwala_commissions')) || DEFAULT_COMMISSIONS;
      leads = JSON.parse(localStorage.getItem('rentwala_leads')) || DEFAULT_LEADS;
      complaints = JSON.parse(localStorage.getItem('rentwala_complaints')) || DEFAULT_COMPLAINTS;

      // Initial instant render
      renderPublicPropertyList();
      updateDashboardBentoStats();
      renderAdminPropertyTable();
      renderAdminTenantTable();
      renderAdminRentCollectionTable();
      renderAdminCommissionTable();
      renderAdminLeadsTable();
      renderAdminMaintenanceTable();
      populateAgreementDropdowns();
      initSignatureCanvas();

      // Set default tomorrow date in visit form
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      const tomorrowStr = tomorrow.toISOString().split('T')[0];
      const visitDateEl = document.getElementById('visitDateInput');
      if (visitDateEl) visitDateEl.value = tomorrowStr;

      // 2. If running on a web server (http: or https:), sync live with Node.js backend
      if (window.location.protocol === 'http:' || window.location.protocol === 'https:') {
        try {
          const healthRes = await fetch('/api/health');
          if (healthRes.ok) {
            isBackendConnected = true;
            const statusBadge = document.getElementById('backendStatusBadge');
            const statusText = document.getElementById('backendStatusText');
            if (statusBadge && statusText) {
              statusBadge.classList.remove('hidden');
              statusText.innerText = "Node.js Server LIVE";
            }

            const [propsRes, tenRes, leadsRes, maintRes] = await Promise.all([
              fetch('/api/properties'),
              fetch('/api/tenants'),
              fetch('/api/leads'),
              fetch('/api/maintenance')
            ]);

            if (propsRes.ok) properties = await propsRes.json();
            if (tenRes.ok) tenants = await tenRes.json();
            if (leadsRes.ok) leads = await leadsRes.json();
            if (maintRes.ok) complaints = await maintRes.json();

            // Re-render with live server data
            renderPublicPropertyList();
            updateDashboardBentoStats();
            renderAdminPropertyTable();
            renderAdminTenantTable();
            renderAdminLeadsTable();
            renderAdminMaintenanceTable();
          }
        } catch (err) {
          console.log('Running in local client mode');
        }
      }
    }

    function saveState() {
      localStorage.setItem('rentwala_properties', JSON.stringify(properties));
      localStorage.setItem('rentwala_tenants', JSON.stringify(tenants));
      localStorage.setItem('rentwala_rentCollections', JSON.stringify(rentCollections));
      localStorage.setItem('rentwala_commissions', JSON.stringify(commissions));
      localStorage.setItem('rentwala_leads', JSON.stringify(leads));
      localStorage.setItem('rentwala_complaints', JSON.stringify(complaints));

      updateDashboardBentoStats();
    }

    function resetDemoData() {
      if (confirm("Kya aap sach me demo data reset karna chahte hain?")) {
        localStorage.removeItem('rentwala_properties');
        localStorage.removeItem('rentwala_tenants');
        localStorage.removeItem('rentwala_rentCollections');
        localStorage.removeItem('rentwala_commissions');
        localStorage.removeItem('rentwala_leads');
        localStorage.removeItem('rentwala_complaints');
        location.reload();
      }
    }

    // ================= VIEW TOGGLING =================
    function toggleAgentPortal() {
      const publicView = document.getElementById('publicView');
      const agentDashboardView = document.getElementById('agentDashboardView');
      const agentBtnText = document.getElementById('agentBtnText');

      if (agentDashboardView.classList.contains('hidden')) {
        agentDashboardView.classList.remove('hidden');
        publicView.classList.add('hidden');
        agentBtnText.innerText = "Tenant Website";
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showToast("Sharma Ji Admin Portal khul gaya hai!", "info");
      } else {
        showPublicSite();
      }
    }

    // ================= CENTRAL SPA NAVIGATION ROUTER =================
    function navTo(section) {
      const publicView = document.getElementById('publicView');
      const agentDashboardView = document.getElementById('agentDashboardView');
      const tenantPortalPage = document.getElementById('tenantPortalPageSection');
      const homeSection = document.getElementById('home');
      const propertiesSection = document.getElementById('properties-section');
      const howItWorksSection = document.getElementById('how-it-works');
      const testimonialsSection = document.getElementById('testimonials');
      const footerSection = document.querySelector('footer');

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
        if (footerSection) footerSection.classList.add('hidden');

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
        if (footerSection) footerSection.classList.remove('hidden');

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

    function showPublicSite() {
      const publicView = document.getElementById('publicView');
      const agentDashboardView = document.getElementById('agentDashboardView');
      const agentBtnText = document.getElementById('agentBtnText');

      agentDashboardView.classList.add('hidden');
      publicView.classList.remove('hidden');
      agentBtnText.innerText = "Agent Portal (Sharma Ji)";
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function switchAdminTab(tabId, clickedBtn = null) {
      document.querySelectorAll('.admin-tab-content').forEach(el => el.classList.add('hidden'));
      const targetTab = document.getElementById(tabId);
      if (targetTab) targetTab.classList.remove('hidden');

      document.querySelectorAll('.admin-tab-btn').forEach(btn => {
        btn.classList.remove('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        btn.classList.add('text-stone-700');
      });

      const activeBtn = clickedBtn || (window.event && window.event.currentTarget) || document.querySelector(`[onclick*="${tabId}"]`);
      if (activeBtn) {
        activeBtn.classList.add('active-admin-tab', 'bg-terracotta-700', 'text-white', 'shadow-sm');
        activeBtn.classList.remove('text-stone-700');
      }
    }

    // ================= PUBLIC PROPERTY RENDERING =================
    function renderPublicPropertyList(filteredList = null) {
      const container = document.getElementById('propertyCardsList');
      const countEl = document.getElementById('totalFlatsCount');
      const noResultsEl = document.getElementById('noResultsState');

      const listToRender = filteredList || getFilteredProperties();

      if (countEl) countEl.innerText = properties.length;

      if (!listToRender || listToRender.length === 0) {
        container.innerHTML = "";
        noResultsEl.classList.remove('hidden');
        return;
      }

      noResultsEl.classList.add('hidden');

      container.innerHTML = listToRender.map(prop => {
        const isBooked = prop.status === 'Booked';
        const isRented = prop.status === 'Rented';
        
        let statusBadge = '';
        if (isBooked) {
          statusBadge = '<span class="px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-300"><i class="fa-solid fa-lock mr-1"></i> Booked via Token</span>';
        } else if (isRented) {
          statusBadge = '<span class="px-3 py-1 rounded-full text-xs font-bold bg-stone-200 text-stone-700 border border-stone-300"><i class="fa-solid fa-circle-check mr-1"></i> Rented Out</span>';
        } else {
          statusBadge = '<span class="px-3 py-1 rounded-full text-xs font-bold bg-olive-100 text-olive-800 border border-olive-300"><i class="fa-solid fa-circle text-[8px] mr-1 text-olive-700"></i> Available</span>';
        }

        const waText = encodeURIComponent(`Namaste Sharma Ji, mujhe "${prop.title}" (Rent: ₹${prop.rent}) ke bare me detail chahiye.`);

        return `
          <div class="bg-amber-50/80 hover:bg-white rounded-[28px] border border-amber-200/90 shadow-warm-soft hover:shadow-warm-card transition-all duration-300 p-4 sm:p-6 flex flex-col md:flex-row gap-6 group">
            
            <!-- LEFT 40% WIDTH: BIG PHOTO + OVERLAPPING BADGES -->
            <div class="md:w-2/5 relative rounded-2xl overflow-hidden aspect-[16/11] md:aspect-auto bg-stone-200 flex-shrink-0">
              <img 
                src="${prop.images[0]}" 
                alt="${prop.title}" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
              
              <!-- Floating Price Badge Overlapping Photo (Dark Charcoal with Terracotta Accent) -->
              <div class="absolute top-3 left-3 bg-charcoal-900/90 backdrop-blur-md px-3.5 py-1.5 rounded-full border border-white/20 text-white shadow-lg flex items-center gap-1.5">
                <span class="font-serif font-extrabold text-sm sm:text-base text-amber-300">₹${prop.rent.toLocaleString('en-IN')}</span>
                <span class="text-[10px] text-stone-300 font-medium">/ Mahina</span>
              </div>

              <!-- Deposit & Ready To Move Tag -->
              <div class="absolute bottom-3 left-3 flex flex-wrap gap-1.5">
                <span class="bg-cream-100/95 backdrop-blur-sm text-charcoal-900 text-[10px] font-bold px-2.5 py-1 rounded-full border border-amber-300 shadow-sm">
                  Deposit: ₹${prop.deposit.toLocaleString('en-IN')}
                </span>
                <span class="bg-olive-800/90 backdrop-blur-sm text-white text-[10px] font-bold px-2 py-1 rounded-full shadow-sm">
                  ${prop.availableFrom}
                </span>
              </div>

              <!-- Wishlist Heart Toggle Button -->
              <button onclick="toggleWishlist('${prop.id}', this)" class="absolute top-3 right-3 w-8 h-8 rounded-full bg-white/90 backdrop-blur-md text-stone-600 hover:text-terracotta-700 flex items-center justify-center shadow-md transition-transform active:scale-90">
                <i class="fa-regular fa-heart text-xs"></i>
              </button>
            </div>

            <!-- RIGHT 60% WIDTH: PROPERTY DETAILS -->
            <div class="md:w-3/5 flex flex-col justify-between space-y-4">
              
              <div>
                <div class="flex items-center justify-between gap-2 mb-1.5">
                  <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-cream-200 text-terracotta-800 text-[11px] font-semibold border border-amber-300/60">
                    <i class="fa-solid fa-shield-check text-olive-700"></i> ${prop.badge || 'Verified Owner'}
                  </div>
                  <div>${statusBadge}</div>
                </div>

                <!-- Title in Fraunces Serif -->
                <h3 onclick="openPropertyDrawer('${prop.id}')" class="font-serif text-xl sm:text-2xl font-bold text-charcoal-900 group-hover:text-terracotta-700 transition-colors cursor-pointer leading-snug">
                  ${prop.title}
                </h3>

                <!-- Location with Pin Icon -->
                <p class="text-xs text-stone-600 mt-1 flex items-center gap-1.5 font-medium">
                  <i class="fa-solid fa-location-dot text-terracotta-700 text-xs"></i>
                  <span>${prop.fullAddress}</span>
                </p>
              </div>

              <!-- 3 Icons Feature Row: BHK | Area | Furnished -->
              <div class="grid grid-cols-3 gap-2 py-2.5 px-3 rounded-2xl bg-cream-100/90 border border-amber-200/70 text-xs font-semibold text-charcoal-900">
                <div class="flex items-center gap-2">
                  <i class="fa-solid fa-couch text-terracotta-700 text-sm"></i>
                  <span>${prop.bhk}</span>
                </div>
                <div class="flex items-center gap-2 border-l border-amber-200/90 pl-3">
                  <i class="fa-solid fa-ruler-combined text-terracotta-700 text-sm"></i>
                  <span>${prop.area} sqft</span>
                </div>
                <div class="flex items-center gap-2 border-l border-amber-200/90 pl-3">
                  <i class="fa-solid fa-bed text-terracotta-700 text-sm"></i>
                  <span class="truncate">${prop.furnishing}</span>
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
              </div>

              <!-- Bottom Row: Owner Verified Badge + View Details + WhatsApp -->
              <div class="pt-3 border-t border-amber-200/70 flex flex-wrap items-center justify-between gap-3">
                <div class="flex items-center gap-2 text-xs font-semibold text-olive-800">
                  <div class="w-6 h-6 rounded-full bg-olive-100 text-olive-700 flex items-center justify-center text-[10px]">
                    <i class="fa-solid fa-check"></i>
                  </div>
                  <span>Owner: Verified by Sharma Ji</span>
                </div>

                <div class="flex items-center gap-2">
                  <!-- WhatsApp Button -->
                  <a 
                    href="https://wa.me/919876543210?text=${waText}" 
                    target="_blank"
                    class="w-10 h-10 rounded-full bg-olive-600 hover:bg-olive-700 text-white flex items-center justify-center text-sm shadow-sm transition-transform hover:scale-105 active:scale-95" 
                    title="Enquire on WhatsApp"
                  >
                    <i class="fa-brands fa-whatsapp text-lg"></i>
                  </a>

                  <!-- View Details Pill Button -->
                  <button 
                    onclick="openPropertyDrawer('${prop.id}')" 
                    class="px-5 py-2.5 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-white text-xs font-bold shadow-pill flex items-center gap-2 transition-all hover:scale-105 active:scale-95"
                  >
                    <span>View Details</span>
                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                  </button>
                </div>
              </div>

            </div>

          </div>
        `;
      }).join('');
    }

    // Filter Chips Logic
    function setFilter(filterType, btnEl) {
      currentFilter = filterType;

      document.querySelectorAll('.filter-chip').forEach(btn => {
        btn.classList.remove('active-chip', 'bg-terracotta-700', 'text-white', 'shadow-pill');
        btn.classList.add('bg-white', 'text-stone-700', 'border', 'border-amber-200');
      });

      if (btnEl) {
        btnEl.classList.add('active-chip', 'bg-terracotta-700', 'text-white', 'shadow-pill');
        btnEl.classList.remove('bg-white', 'text-stone-700');
      }

      renderPublicPropertyList();
    }

    function getFilteredProperties() {
      let list = [...properties];

      if (currentFilter === '1BHK') {
        list = list.filter(p => p.bhk === '1BHK');
      } else if (currentFilter === '2BHK') {
        list = list.filter(p => p.bhk === '2BHK');
      } else if (currentFilter === '3BHK') {
        list = list.filter(p => p.bhk === '3BHK');
      } else if (currentFilter === 'under10k') {
        list = list.filter(p => p.rent <= 10000);
      } else if (currentFilter === 'family') {
        list = list.filter(p => p.allowed.includes('Family'));
      } else if (currentFilter === 'bachelor') {
        list = list.filter(p => p.allowed.includes('Bachelor'));
      } else if (currentFilter === 'furnished') {
        list = list.filter(p => p.furnishing.includes('Full'));
      } else if (currentFilter === 'shop') {
        list = list.filter(p => p.bhk === 'Shop');
      }

      return list;
    }

    function handleSortChange() {
      const sortVal = document.getElementById('propertySortSelect').value;
      let list = getFilteredProperties();

      if (sortVal === 'price-asc') {
        list.sort((a, b) => a.rent - b.rent);
      } else if (sortVal === 'price-desc') {
        list.sort((a, b) => b.rent - a.rent);
      } else if (sortVal === 'newest') {
        list.reverse();
      }

      renderPublicPropertyList(list);
    }

    function applyHeroSearch() {
      const loc = document.getElementById('heroLocationSelect').value;
      const budget = document.getElementById('heroBudgetSelect').value;
      const type = document.getElementById('heroTypeSelect').value;

      let list = [...properties];

      if (loc) {
        list = list.filter(p => p.locality.toLowerCase().includes(loc.toLowerCase()));
      }

      if (budget === 'under10k') {
        list = list.filter(p => p.rent < 10000);
      } else if (budget === '10k-15k') {
        list = list.filter(p => p.rent >= 10000 && p.rent <= 15000);
      } else if (budget === '15k-25k') {
        list = list.filter(p => p.rent > 15000 && p.rent <= 25000);
      } else if (budget === 'above25k') {
        list = list.filter(p => p.rent > 25000);
      }

      if (type) {
        list = list.filter(p => p.bhk === type);
      }

      renderPublicPropertyList(list);

      // Scroll smoothly to properties section
      document.getElementById('properties-section').scrollIntoView({ behavior: 'smooth' });
      showToast(`${list.length} properties dhoondhi gayi!`, 'success');
    }

    function filterByLocation(locName) {
      document.getElementById('heroLocationSelect').value = locName;
      applyHeroSearch();
    }

    function resetAllFilters() {
      currentFilter = 'all';
      document.getElementById('heroLocationSelect').value = "";
      document.getElementById('heroBudgetSelect').value = "";
      document.getElementById('heroTypeSelect').value = "";
      setFilter('all', document.querySelector('.filter-chip'));
    }

    function toggleWishlist(propId, btnEl) {
      const icon = btnEl.querySelector('i');
      if (icon.classList.contains('fa-regular')) {
        icon.classList.remove('fa-regular');
        icon.classList.add('fa-solid', 'text-terracotta-700');
        showToast("Property Saved in Wishlist", "success");
      } else {
        icon.classList.remove('fa-solid', 'text-terracotta-700');
        icon.classList.add('fa-regular');
        showToast("Removed from Wishlist", "info");
      }
    }

    // ================= PROPERTY DETAILS SLIDE DRAWER =================
    function openPropertyDrawer(propId) {
      const prop = properties.find(p => p.id === propId);
      if (!prop) return;

      currentSelectedProperty = prop;

      document.getElementById('drawerTitle').innerText = prop.title;
      document.getElementById('drawerLocation').innerHTML = `<i class="fa-solid fa-location-dot text-terracotta-700"></i> ${prop.fullAddress}`;
      document.getElementById('drawerBHK').innerText = prop.bhk;
      document.getElementById('drawerArea').innerText = `${prop.area} sqft`;
      document.getElementById('drawerFurnishing').innerText = prop.furnishing;
      
      document.getElementById('drawerRentBreakdown').innerText = `₹${prop.rent.toLocaleString('en-IN')}`;
      document.getElementById('drawerDepositBreakdown').innerText = `₹${prop.deposit.toLocaleString('en-IN')}`;
      document.getElementById('drawerRentBottom').innerHTML = `₹${prop.rent.toLocaleString('en-IN')} <span class="text-xs font-normal text-stone-500">/ Mahina</span>`;

      // Status badge in drawer
      const statusBadge = document.getElementById('drawerStatusBadge');
      if (prop.status === 'Booked') {
        statusBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-300";
        statusBadge.innerText = "LOCKED / BOOKED";
      } else if (prop.status === 'Rented') {
        statusBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-stone-200 text-stone-700 border border-stone-300";
        statusBadge.innerText = "RENTED OUT";
      } else {
        statusBadge.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-olive-100 text-olive-800 border border-olive-300";
        statusBadge.innerText = "AVAILABLE";
      }

      // Photos
      document.getElementById('drawerMainImage').src = prop.images[0];
      const thumbsContainer = document.getElementById('drawerThumbnailsRow');
      thumbsContainer.innerHTML = prop.images.map((img, idx) => `
        <img 
          src="${img}" 
          onclick="document.getElementById('drawerMainImage').src='${img}'"
          class="w-16 h-12 rounded-xl object-cover border-2 ${idx === 0 ? 'border-terracotta-700' : 'border-transparent'} hover:border-terracotta-700 cursor-pointer flex-shrink-0"
        />
      `).join('');

      // WhatsApp link
      const waMsg = encodeURIComponent(`Namaste Sharma Ji, mujhe "${prop.title}" (Rent: ₹${prop.rent}) ke bare me enquiry karni hai.`);
      document.getElementById('drawerWhatsAppEnquiry').href = `https://wa.me/919876543210?text=${waMsg}`;

      // Open drawer animation
      const drawer = document.getElementById('propertyDrawer');
      const panel = document.getElementById('drawerPanel');
      drawer.classList.remove('pointer-events-none', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('translate-x-full');
      panel.classList.add('translate-x-0');
      document.body.style.overflow = 'hidden';
    }

    function closePropertyDrawer() {
      const drawer = document.getElementById('propertyDrawer');
      const panel = document.getElementById('drawerPanel');
      panel.classList.remove('translate-x-0');
      panel.classList.add('translate-x-full');
      drawer.classList.remove('opacity-100');
      drawer.classList.add('opacity-0');
      setTimeout(() => {
        drawer.classList.add('pointer-events-none');
        document.body.style.overflow = 'auto';
      }, 300);
    }

    // ================= MODAL: 360 VIDEO TOUR =================
    function triggerVideoTourModal() {
      document.getElementById('videoTourModal').classList.remove('hidden');
    }

    function closeVideoTourModal() {
      document.getElementById('videoTourModal').classList.add('hidden');
    }

    function switchVideoRoom(roomName, imgUrl) {
      document.getElementById('videoTourRoomLabel').innerText = roomName;
      const imgEl = document.getElementById('videoTourDisplayImage');
      imgEl.style.opacity = '0.3';
      setTimeout(() => {
        imgEl.src = imgUrl;
        imgEl.style.opacity = '1';
      }, 150);
    }

    // ================= MODAL: FILTER SIDEBAR =================
    function openFilterSidebar() {
      const drawer = document.getElementById('filterSidebarDrawer');
      const panel = document.getElementById('filterDrawerPanel');
      drawer.classList.remove('pointer-events-none', 'opacity-0');
      drawer.classList.add('opacity-100');
      panel.classList.remove('-translate-x-full');
      panel.classList.add('translate-x-0');
    }

    function closeFilterSidebar() {
      const drawer = document.getElementById('filterSidebarDrawer');
      const panel = document.getElementById('filterDrawerPanel');
      panel.classList.remove('translate-x-0');
      panel.classList.add('-translate-x-full');
      drawer.classList.remove('opacity-100');
      drawer.classList.add('opacity-0');
      setTimeout(() => {
        drawer.classList.add('pointer-events-none');
      }, 300);
    }

    function applySidebarFilters() {
      const budgetRadio = document.querySelector('input[name="sidebarBudget"]:checked')?.value;
      const type = document.getElementById('sidebarTypeSelect').value;
      const bhkRadio = document.querySelector('input[name="sidebarBhk"]:checked')?.value;
      const furnishing = document.getElementById('sidebarFurnishingSelect').value;
      const allowed = document.getElementById('sidebarAllowedSelect').value;
      const hideBooked = document.getElementById('sidebarHideBooked').checked;

      let list = [...properties];

      if (budgetRadio === '5k-10k') list = list.filter(p => p.rent >= 5000 && p.rent <= 10000);
      else if (budgetRadio === '10k-15k') list = list.filter(p => p.rent > 10000 && p.rent <= 15000);
      else if (budgetRadio === '15k+') list = list.filter(p => p.rent > 15000);

      if (type) list = list.filter(p => p.bhk.includes(type) || p.title.includes(type));
      if (bhkRadio) list = list.filter(p => p.bhk === bhkRadio);
      if (furnishing) list = list.filter(p => p.furnishing.includes(furnishing));
      if (allowed) list = list.filter(p => p.allowed.includes(allowed));
      if (hideBooked) list = list.filter(p => p.status !== 'Booked');

      closeFilterSidebar();
      renderPublicPropertyList(list);
      showToast(`${list.length} properties filtered!`, 'info');
    }

    function resetSidebarFilters() {
      document.querySelector('input[name="sidebarBudget"][value=""]').checked = true;
      document.getElementById('sidebarTypeSelect').value = '';
      document.querySelector('input[name="sidebarBhk"][value=""]').checked = true;
      document.getElementById('sidebarFurnishingSelect').value = '';
      document.getElementById('sidebarAllowedSelect').value = '';
      document.getElementById('sidebarHideBooked').checked = false;
      renderPublicPropertyList();
      closeFilterSidebar();
      showToast('Filters reset.', 'info');
    }

    // ================= MODAL: RESCHEDULE & CANCEL VISIT =================
    let currentVisitActionId = null;

    function openRescheduleModal(visitId) {
      currentVisitActionId = visitId;
      document.getElementById('rescheduleVisitModal').classList.remove('hidden');
    }

    function closeRescheduleModal() {
      document.getElementById('rescheduleVisitModal').classList.add('hidden');
    }

    function confirmReschedule() {
      const newDate = document.getElementById('rescheduleDateInput').value;
      const newSlot = document.getElementById('rescheduleSlotSelect').value;
      if (!newDate) {
        showToast('Kripya nayi date chunein', 'error');
        return;
      }
      document.getElementById('tenantVisitSlot').innerText = `Date: ${newDate} at ${newSlot} • ${currentVisitActionId || 'VISIT-1024'}`;
      closeRescheduleModal();
      showToast(`Site visit rescheduled to ${newDate} at ${newSlot}!`, 'success');
    }

    function openCancelModal(visitId) {
      currentVisitActionId = visitId;
      document.getElementById('cancelVisitModal').classList.remove('hidden');
    }

    function closeCancelModal() {
      document.getElementById('cancelVisitModal').classList.add('hidden');
    }

    function confirmCancelVisit() {
      const statusEl = document.getElementById('tenantVisitStatus');
      if (statusEl) {
        statusEl.className = 'inline-block px-2 py-0.5 mt-1 rounded text-[10px] font-bold bg-red-100 text-red-800';
        statusEl.innerText = 'Cancelled by Tenant';
      }
      closeCancelModal();
      showToast('Site visit cancel ho gayi hai.', 'info');
    }

    // ================= MODAL: OFFICIAL INVOICE RECEIPT =================
    function viewOfficialReceipt(id, title, amount, property) {
      const modal = document.getElementById('officialReceiptModal');
      const card = document.getElementById('officialReceiptCard');
      card.innerHTML = `
        <div class="flex justify-between border-b border-amber-300 pb-2">
          <span class="font-serif font-black text-charcoal-900 text-sm tracking-wider">SHARMA RENTALS</span>
          <span class="text-terracotta-700 font-bold">${id}</span>
        </div>
        <p><b>Description:</b> ${title}</p>
        <p><b>Property:</b> ${property}</p>
        <p><b>Amount:</b> ₹${amount.toLocaleString('en-IN')} (Paid)</p>
        <p><b>Date:</b> ${new Date().toLocaleDateString('en-IN')}</p>
        <p><b>Payment Status:</b> Confirmed & Settled</p>
        <p class="text-[10px] text-stone-500 pt-2 border-t border-amber-200">
          Official GST & RERA verified receipt issued by Sharma Rentals NCR.
        </p>
      `;
      modal.classList.remove('hidden');
    }

    function closeOfficialReceiptModal() {
      document.getElementById('officialReceiptModal').classList.add('hidden');
    }

    // ================= MODAL: MONTHLY COMMISSION REPORT =================
    function openMonthlyReportModal() {
      document.getElementById('monthlyReportModal').classList.remove('hidden');
    }

    function closeMonthlyReportModal() {
      document.getElementById('monthlyReportModal').classList.add('hidden');
    }

    // ================= VACANT LOSS CALCULATOR TOOL =================
    function runVacantLossCalc() {
      const propSel = document.getElementById('calcPropSelect');
      const range = document.getElementById('calcDaysRange');
      const display = document.getElementById('calcDaysDisplay');
      const result = document.getElementById('calcLossResult');

      if (!propSel || !range) return;

      const days = parseInt(range.value) || 15;
      display.innerText = `${days} Din`;

      const selectedOpt = propSel.options[propSel.selectedIndex];
      const rent = selectedOpt ? parseInt(selectedOpt.getAttribute('data-rent')) || 12000 : 12000;
      const daily = Math.round(rent / 30);
      const totalLoss = daily * days;

      result.innerText = `₹${totalLoss.toLocaleString('en-IN')}`;
    }

    // ================= MODAL 1: BOOK VISIT SYSTEM =================
    function openBookVisitModalFromDrawer() {
      if (!currentSelectedProperty) return;
      document.getElementById('visitModalSubtitle').innerText = `${currentSelectedProperty.title} • Rent: ₹${currentSelectedProperty.rent}`;
      document.getElementById('bookVisitForm').classList.remove('hidden');
      document.getElementById('visitSuccessScreen').classList.add('hidden');
      document.getElementById('bookVisitModal').classList.remove('hidden');
    }

    function closeBookVisitModal() {
      document.getElementById('bookVisitModal').classList.add('hidden');
    }

    function selectTimeSlot(slot, btnEl) {
      selectedTimeSlot = slot;
      document.querySelectorAll('.slot-pill').forEach(b => {
        b.classList.remove('active-slot', 'bg-terracotta-700', 'text-white');
        b.classList.add('bg-white', 'text-stone-700');
      });
      btnEl.classList.add('active-slot', 'bg-terracotta-700', 'text-white');
      btnEl.classList.remove('bg-white', 'text-stone-700');
    }

    function handleBookVisitSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('visitNameInput').value.trim();
      const phone = document.getElementById('visitPhoneInput').value.trim();
      const date = document.getElementById('visitDateInput').value;

      // Phone Validation: 10 Digits
      if (!/^\d{10}$/.test(phone)) {
        document.getElementById('phoneError').classList.remove('hidden');
        return;
      }
      document.getElementById('phoneError').classList.add('hidden');

      const bookingId = "VISIT-" + Math.floor(1000 + Math.random() * 9000);

      // Add to leads array
      const newLead = {
        id: bookingId,
        tenant: name,
        phone: phone,
        property: currentSelectedProperty ? currentSelectedProperty.title : "Royal Palm Flat",
        date: date,
        time: selectedTimeSlot,
        status: "New"
      };
      leads.unshift(newLead);
      saveState();
      renderAdminLeadsTable();

      // Confetti burst
      if (typeof confetti === 'function') {
        confetti({ particleCount: 70, spread: 60, origin: { y: 0.6 } });
      }

      // Show success screen
      document.getElementById('bookVisitForm').classList.add('hidden');
      document.getElementById('visitSuccessScreen').classList.remove('hidden');
      document.getElementById('successBookingId').innerText = bookingId;
      document.getElementById('successPropName').innerText = newLead.property;
      document.getElementById('successSlot').innerText = `${date} at ${selectedTimeSlot}`;

      const waShareText = encodeURIComponent(`Namaste Sharma Ji, maine "${newLead.property}" ke liye visit book ki hai.\nBooking ID: ${bookingId}\nDate: ${date} at ${selectedTimeSlot}\nNaam: ${name}`);
      document.getElementById('successWhatsAppShareBtn').href = `https://wa.me/919876543210?text=${waShareText}`;

      showToast(`Site Visit Confirmed! Booking ID: ${bookingId}`, 'success');
    }

    // ================= MODAL 2: TOKEN PAYMENT ₹2,000 =================
    function openTokenPaymentModalFromDrawer() {
      if (!currentSelectedProperty) return;
      document.getElementById('tokenModalSubtitle').innerText = `${currentSelectedProperty.title} • Rent: ₹${currentSelectedProperty.rent}`;
      document.getElementById('tokenPropTitle').innerText = currentSelectedProperty.title;
      document.getElementById('tokenStep1').classList.remove('hidden');
      document.getElementById('tokenStepSuccess').classList.add('hidden');
      document.getElementById('tokenPaymentModal').classList.remove('hidden');
    }

    function closeTokenModal() {
      document.getElementById('tokenPaymentModal').classList.add('hidden');
    }

    function processTokenPayment() {
      if (!currentSelectedProperty) return;

      const upiId = document.getElementById('tokenUpiInput').value.trim();
      if (!upiId) {
        showToast("Kripya UPI ID dalein", "error");
        return;
      }

      showToast("UPI Processing ₹2,000...", "info");

      setTimeout(() => {
        // Change property status to Booked immediately!
        currentSelectedProperty.status = "Booked";
        saveState();
        renderPublicPropertyList();
        renderAdminPropertyTable();

        // Confetti burst!
        if (typeof confetti === 'function') {
          confetti({ particleCount: 100, spread: 80, origin: { y: 0.5 } });
        }

        const tokenId = "TOK-" + Math.floor(1000 + Math.random() * 9000);
        document.getElementById('receiptTokenId').innerText = tokenId;
        document.getElementById('receiptPropName').innerText = currentSelectedProperty.title;

        document.getElementById('tokenStep1').classList.add('hidden');
        document.getElementById('tokenStepSuccess').classList.remove('hidden');

        // Also update drawer if open
        openPropertyDrawer(currentSelectedProperty.id);

        showToast("Token Received! Flat successfully locked.", "success");
      }, 1000);
    }

    function downloadTokenReceipt() {
      window.print();
    }

    // ================= MODAL 3: TENANT PORTAL =================
    function openTenantPortalModal() {
      document.getElementById('tenantPortalModal').classList.remove('hidden');
    }

    function closeTenantPortalModal() {
      document.getElementById('tenantPortalModal').classList.add('hidden');
    }

    function sendTenantOtp() {
      const btn = document.getElementById('tenantLoginBtn');
      const otpContainer = document.getElementById('otpInputContainer');

      if (otpContainer.classList.contains('hidden')) {
        otpContainer.classList.remove('hidden');
        btn.innerText = "Verify OTP & Open Portal";
        showToast("Demo OTP sent: 1234", "info");
      } else {
        const otp = document.getElementById('tenantLoginOtp').value;
        if (otp === "1234") {
          document.getElementById('tenantLoginSection').classList.add('hidden');
          document.getElementById('tenantDashboardSection').classList.remove('hidden');
          showToast("Welcome Rahul Verma Ji!", "success");
        } else {
          showToast("Galat OTP! Kripya 1234 dalein.", "error");
        }
      }
    }

    function logoutTenant() {
      document.getElementById('tenantLoginSection').classList.remove('hidden');
      document.getElementById('tenantDashboardSection').classList.add('hidden');
      document.getElementById('otpInputContainer').classList.add('hidden');
      document.getElementById('tenantLoginBtn').innerText = "Send OTP on SMS";
    }

    function switchTenantTab(tabKey) {
      document.querySelectorAll('.tenant-tab-pane').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tenant-subtab').forEach(b => {
        b.classList.remove('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
        b.classList.add('text-stone-600');
      });

      if (tabKey === 'myVisits') {
        document.getElementById('tenantTabMyVisits').classList.remove('hidden');
      } else if (tabKey === 'myAgreement') {
        document.getElementById('tenantTabMyAgreement').classList.remove('hidden');
      } else if (tabKey === 'myRentHistory') {
        document.getElementById('tenantTabMyRentHistory').classList.remove('hidden');
      } else if (tabKey === 'myReceipts') {
        document.getElementById('tenantTabMyReceipts').classList.remove('hidden');
      } else if (tabKey === 'maintenanceRequest') {
        document.getElementById('tenantTabMaintenance').classList.remove('hidden');
      } else if (tabKey === 'moveOutTab') {
        document.getElementById('tenantTabMoveOut').classList.remove('hidden');
      }

      const activeTenantBtn = (window.event && window.event.currentTarget) || document.querySelector(`[onclick*="${tabKey}"]`);
      if (activeTenantBtn) {
        activeTenantBtn.classList.add('text-terracotta-700', 'border-b-2', 'border-terracotta-700', 'font-bold');
        activeTenantBtn.classList.remove('text-stone-600');
      }
    }

    function rescheduleVisitAlert() {
      alert("Aapka site visit reschedule request Sharma Ji ko bhej diya gaya hai. Vo aapse jaldi call pe contact karenge.");
    }

    function cancelVisitAlert() {
      if (confirm("Kya aap sach me yeh visit cancel karna chahte hain?")) {
        showToast("Site visit cancelled.", "info");
      }
    }

    function payRentOnline() {
      alert("UPI Payment Gateway Opening for ₹14,200 (Includes ₹200 late fee)...");
      showToast("Rent Paid Successfully! Receipt generated.", "success");
    }

    function handleTenantComplaintSubmit(e) {
      e.preventDefault();
      const category = document.getElementById('complaintCategory').value;
      const details = document.getElementById('complaintDetails').value;

      const newTkt = {
        id: "TKT-" + Math.floor(100 + Math.random() * 900),
        date: "Today",
        tenant: "Rahul Verma",
        property: "Flat 204",
        issue: details,
        category: category,
        photo: "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=200&q=80",
        mistri: category === 'Plumbing' ? "Raju Mistri (Plumber)" : "Sonu Wireman",
        status: "Pending"
      };

      complaints.unshift(newTkt);
      saveState();
      renderAdminMaintenanceTable();

      alert(`Complaint register ho gayi hai! Ticket ID: ${newTkt.id}\nSharma Ji ke plumber ko alert bhej diya gaya hai.`);
      document.getElementById('complaintDetails').value = "";
    }

    function submitMoveOutAlert() {
      alert("Move-out notice submit ho gaya hai! Sharma Ji inspection ke baad 100% deposit refund karenge.");
    }

    // ================= ADMIN DASHBOARD: BENTO STATS =================
    function updateDashboardBentoStats() {
      const total = properties.length;
      const rented = properties.filter(p => p.status === 'Rented').length;
      const vacant = properties.filter(p => p.status === 'Available').length;
      
      // Vacant Loss Calculation: sum of (vacantDays * dailyRent)
      let totalVacantLoss = 0;
      properties.forEach(p => {
        if (p.status === 'Available' && p.vacantDays > 0) {
          const dailyRent = Math.round(p.rent / 30);
          totalVacantLoss += (dailyRent * p.vacantDays);
        }
      });

      document.getElementById('bentoTotalProps').innerText = total;
      document.getElementById('bentoRentedProps').innerText = rented;
      document.getElementById('bentoVacantProps').innerText = vacant;
      document.getElementById('bentoTotalVacantLoss').innerText = `₹${totalVacantLoss.toLocaleString('en-IN')}`;
    }

    // ================= ADMIN TAB 1: PROPERTY MANAGER TABLE =================
    function renderAdminPropertyTable() {
      const tbody = document.getElementById('adminPropertyTableBody');
      const filter = document.getElementById('adminPropFilter').value;
      const calcSelect = document.getElementById('calcPropSelect');

      // Populate Vacant Loss Calculator Select
      if (calcSelect) {
        calcSelect.innerHTML = properties.map(p => `
          <option value="${p.id}" data-rent="${p.rent}" ${p.id === 'FLAT-102' ? 'selected' : ''}>
            ${p.title} (Rent: ₹${p.rent.toLocaleString('en-IN')})
          </option>
        `).join('');
        runVacantLossCalc();
      }

      let list = [...properties];
      if (filter !== 'all') {
        list = list.filter(p => p.status === filter);
      }

      tbody.innerHTML = list.map(p => {
        const dailyRent = Math.round(p.rent / 30);
        const lossAmount = p.status === 'Available' ? (dailyRent * p.vacantDays) : 0;

        let statusClass = "bg-olive-100 text-olive-800 border-olive-300";
        if (p.status === 'Vacant' || p.status === 'Available') statusClass = "bg-maroon-100 text-maroon-800 border-maroon-300";
        if (p.status === 'Booked') statusClass = "bg-amber-100 text-amber-900 border-amber-300";

        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4 flex items-center gap-3">
              <img src="${p.images[0]}" class="w-12 h-10 rounded-xl object-cover border border-amber-200">
              <div>
                <p class="font-bold text-charcoal-900 font-serif">${p.title}</p>
                <p class="text-[10px] text-stone-500">${p.locality} • ${p.bhk}</p>
              </div>
            </td>
            <td class="p-4 text-stone-700">${p.owner}</td>
            <td class="p-4">
              <span class="font-serif font-bold text-charcoal-900">₹${p.rent.toLocaleString('en-IN')}</span>
              <p class="text-[10px] text-stone-500">Dep: ₹${p.deposit.toLocaleString('en-IN')}</p>
            </td>
            <td class="p-4">
              <span class="px-2.5 py-1 rounded-full text-[11px] font-bold border ${statusClass}">
                ${p.status}
              </span>
            </td>
            <td class="p-4">
              ${p.status === 'Available' ? `
                <div class="text-maroon-800 font-semibold">
                  <p>${p.vacantDays} Din Se Khali</p>
                  <p class="font-extrabold font-serif text-maroon-900">₹${lossAmount.toLocaleString('en-IN')} Nuksaan</p>
                </div>
              ` : `<span class="text-stone-400">0 Din (Occupied)</span>`}
            </td>
            <td class="p-4 text-right space-x-1 whitespace-nowrap">
              <button onclick="togglePropStatus('${p.id}', 'Available')" class="px-2 py-1 rounded-full bg-cream-200 text-stone-800 text-[10px] font-bold hover:bg-stone-300" title="Mark Vacant">Vacant</button>
              <button onclick="togglePropStatus('${p.id}', 'Rented')" class="px-2 py-1 rounded-full bg-olive-100 text-olive-800 text-[10px] font-bold hover:bg-olive-200" title="Mark Rented">Rented</button>
              <button onclick="togglePropStatus('${p.id}', 'Booked')" class="px-2 py-1 rounded-full bg-amber-100 text-amber-900 text-[10px] font-bold hover:bg-amber-200" title="Mark Booked">Booked</button>
              <button onclick="deleteProperty('${p.id}')" class="px-2 py-1 rounded-full bg-red-100 text-red-700 text-[10px] font-bold hover:bg-red-200"><i class="fa-solid fa-trash"></i></button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function togglePropStatus(id, newStatus) {
      const prop = properties.find(p => p.id === id);
      if (prop) {
        prop.status = newStatus;
        if (newStatus === 'Available') {
          prop.vacantDays = 5;
        } else {
          prop.vacantDays = 0;
        }
        saveState();
        renderPublicPropertyList();
        renderAdminPropertyTable();
        showToast(`Property marked as ${newStatus}!`, "success");
      }
    }

    function deleteProperty(id) {
      if (confirm("Kya aap iss property ko delete karna chahte hain?")) {
        properties = properties.filter(p => p.id !== id);
        saveState();
        renderPublicPropertyList();
        renderAdminPropertyTable();
        showToast("Property deleted.", "info");
      }
    }

    function openAddPropertyModal() {
      document.getElementById('addPropertyModal').classList.remove('hidden');
    }

    function closeAddPropertyModal() {
      document.getElementById('addPropertyModal').classList.add('hidden');
    }

    function handleAddPropertySubmit(e) {
      e.preventDefault();
      const title = document.getElementById('newPropTitle').value.trim();
      const location = document.getElementById('newPropLocation').value.trim();
      const bhk = document.getElementById('newPropBHK').value;
      const rent = parseInt(document.getElementById('newPropRent').value) || 12000;
      const deposit = parseInt(document.getElementById('newPropDeposit').value) || (rent * 2);
      const furnishing = document.getElementById('newPropFurnishing').value;
      const allowed = document.getElementById('newPropAllowed').value;
      const owner = document.getElementById('newPropOwner').value || "Sharma Ji Client";
      const status = document.getElementById('newPropStatus').value;
      const image = document.getElementById('newPropImage').value || "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80";

      const newP = {
        id: "FLAT-" + Math.floor(100 + Math.random() * 900),
        title: title,
        locality: location,
        fullAddress: `${title}, ${location}`,
        rent: rent,
        deposit: deposit,
        bhk: bhk,
        area: 950,
        furnishing: furnishing,
        allowed: allowed,
        status: status,
        vacantDays: status === 'Available' ? 1 : 0,
        owner: owner,
        availableFrom: "Immediate",
        badge: "New Listing",
        images: [image],
        amenities: ["Lift", "Car Parking", "24h Water", "Power Backup"]
      };

      properties.unshift(newP);
      saveState();
      renderPublicPropertyList();
      renderAdminPropertyTable();
      populateAgreementDropdowns();
      closeAddPropertyModal();
      showToast("Nayi property add ho gayi!", "success");
    }

    // ================= ADMIN TAB 2: TENANT MANAGER & CIRCULAR PROGRESS RING =================
    function renderAdminTenantTable() {
      const tbody = document.getElementById('adminTenantTableBody');
      tbody.innerHTML = tenants.map(t => {
        // Calculate Circular Progress Ring SVG Dashoffset
        // Circumference for r=18 is ~113
        const scorePercent = (t.score / 5.0);
        const dashOffset = 113 - (113 * scorePercent);

        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4 flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-cream-200 text-charcoal-900 font-bold flex items-center justify-center font-serif">
                ${t.name.split(' ').map(n=>n[0]).join('')}
              </div>
              <div>
                <p class="font-bold text-charcoal-900">${t.name}</p>
                <p class="text-[10px] text-stone-500">${t.job} • <span class="text-olive-700 font-bold">Aadhaar Verified</span></p>
              </div>
            </td>
            <td class="p-4 text-stone-700 font-medium">${t.property}</td>
            <td class="p-4 text-stone-600">${t.phone}</td>
            <td class="p-4 font-serif font-bold text-charcoal-900">₹${t.rent.toLocaleString('en-IN')}</td>
            <td class="p-4 text-stone-600">${t.agreementEnd}</td>
            
            <!-- Circular Progress Meter (4.8 Score) using pure CSS border & styling -->
            <td class="p-4 text-center">
              <div class="inline-flex items-center justify-center">
                <div class="w-10 h-10 rounded-full border-2 border-amber-200 border-t-olive-700 border-r-olive-700 flex items-center justify-center font-serif text-[11px] font-bold text-charcoal-900 bg-cream-100 shadow-sm">
                  ${t.score}
                </div>
              </div>
              <p class="text-[9px] text-stone-500 mt-1">Time pe rent</p>
            </td>

            <td class="p-4 text-right">
              <button onclick="viewTenantProfile('${t.id}')" class="px-3 py-1 rounded-full bg-cream-200 hover:bg-cream-300 text-charcoal-900 text-xs font-bold">Profile</button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function viewTenantProfile(id) {
      const t = tenants.find(x => x.id === id);
      if (!t) return;
      const modal = document.getElementById('tenantProfileModal');
      const body = document.getElementById('tenantProfileCardBody');
      body.innerHTML = `
        <div class="bg-cream-100 p-4 rounded-2xl border border-amber-200 flex items-center gap-3">
          <div class="w-12 h-12 rounded-full bg-terracotta-700 text-white font-serif font-bold text-lg flex items-center justify-center">
            ${t.name.split(' ').map(n=>n[0]).join('')}
          </div>
          <div>
            <h4 class="font-bold text-charcoal-900 text-sm">${t.name}</h4>
            <p class="text-stone-600 font-medium">${t.job}</p>
            <span class="inline-block px-2 py-0.5 mt-1 rounded text-[10px] font-bold bg-olive-100 text-olive-800">Aadhaar: ${t.aadhaar}</span>
          </div>
        </div>
        <div class="space-y-1.5 p-2 bg-stone-50 rounded-xl border border-stone-200">
          <div class="flex justify-between"><span>Allotted Property:</span><b class="text-charcoal-900">${t.property}</b></div>
          <div class="flex justify-between"><span>Monthly Rent:</span><b class="text-charcoal-900 font-serif">₹${t.rent.toLocaleString('en-IN')}</b></div>
          <div class="flex justify-between"><span>Salary:</span><b>${t.salary}</b></div>
          <div class="flex justify-between"><span>Family Members:</span><b>${t.familyMembers}</b></div>
          <div class="flex justify-between"><span>Agreement End:</span><b class="text-terracotta-700">${t.agreementEnd}</b></div>
          <div class="flex justify-between"><span>Tenant Punctuality Score:</span><b class="text-olive-700 font-bold">${t.score} / 5.0 ⭐ (Excellent)</b></div>
        </div>
      `;
      modal.classList.remove('hidden');
    }

    function closeTenantProfileModal() {
      document.getElementById('tenantProfileModal').classList.add('hidden');
    }

    function quickRenewAgreement(name) {
      showToast(`Agreement Renewed for ${name} till Nov 2027!`, "success");
    }

    function openAddTenantModal() {
      const propSel = document.getElementById('modalTenantPropSelect');
      propSel.innerHTML = properties.map(p => `<option value="${p.title}">${p.title}</option>`).join('');
      document.getElementById('addTenantModal').classList.remove('hidden');
    }

    function closeAddTenantModal() {
      document.getElementById('addTenantModal').classList.add('hidden');
    }

    function handleAddTenantSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('modalTenantName').value.trim();
      const phone = document.getElementById('modalTenantPhone').value.trim();
      const rent = parseInt(document.getElementById('modalTenantRent').value) || 14000;
      const prop = document.getElementById('modalTenantPropSelect').value;
      const job = document.getElementById('modalTenantJob').value || "Corporate Employee";
      const salary = document.getElementById('modalTenantSalary').value || "₹85,000 / mo";
      const aadhaar = document.getElementById('modalTenantAadhaar').value || "XXXX-XXXX-9988";
      const family = document.getElementById('modalTenantFamily').value || "Family";

      tenants.push({
        id: "TEN-" + Math.floor(10 + Math.random() * 90),
        name: name,
        property: prop,
        phone: "+91 " + phone,
        rent: rent,
        agreementEnd: "30 Nov 2027",
        score: 4.8,
        aadhaar: aadhaar,
        job: job,
        salary: salary,
        familyMembers: family
      });

      saveState();
      renderAdminTenantTable();
      populateAgreementDropdowns();
      closeAddTenantModal();
      showToast("Naya tenant successfully add ho gaya!", "success");
    }

    // ================= ADMIN TAB 3: RENT COLLECTION MANAGER =================
    function renderAdminRentCollectionTable() {
      const tbody = document.getElementById('adminRentCollectionTableBody');
      tbody.innerHTML = rentCollections.map(rc => {
        const isLate = rc.status === 'Late';
        const isPaid = rc.status === 'Paid';

        let badgeClass = "bg-olive-100 text-olive-800 border-olive-300";
        if (isLate) badgeClass = "bg-maroon-100 text-maroon-800 border-maroon-300 font-bold";
        if (rc.status === 'Pending') badgeClass = "bg-amber-100 text-amber-900 border-amber-300";

        return `
          <tr class="table-cream-row border-b border-amber-100 ${isLate ? 'bg-red-50/50' : ''}">
            <td class="p-4 font-bold text-charcoal-900">${rc.property}</td>
            <td class="p-4 text-stone-700">${rc.tenant}</td>
            <td class="p-4 text-stone-600">${rc.dueDate}</td>
            <td class="p-4">
              <span class="font-serif font-bold ${isLate ? 'text-maroon-900' : 'text-charcoal-900'}">₹${rc.amount.toLocaleString('en-IN')}</span>
              ${isLate ? '<span class="text-[9px] text-maroon-700 block">+ ₹200 Auto Late Fee</span>' : ''}
            </td>
            <td class="p-4">
              <span class="px-2.5 py-1 rounded-full text-xs font-semibold border ${badgeClass}">
                ${rc.status}
              </span>
            </td>
            <td class="p-4 text-right space-x-2">
              <button onclick="sendRentReminderWhatsApp('${rc.tenant}', '${rc.property}', ${rc.amount})" class="px-3 py-1.5 rounded-full bg-olive-700 hover:bg-olive-800 text-white text-[11px] font-bold shadow-sm">
                <i class="fa-brands fa-whatsapp mr-1"></i> Send Reminder
              </button>
              ${!isPaid ? `
                <button onclick="markRentAsPaid('${rc.id}')" class="px-3 py-1.5 rounded-full bg-charcoal-900 hover:bg-terracotta-700 text-white text-[11px] font-bold shadow-sm">
                  Mark Paid
                </button>
              ` : `<span class="text-xs text-olive-700 font-bold"><i class="fa-solid fa-check"></i> Cleared</span>`}
            </td>
          </tr>
        `;
      }).join('');
    }

    function sendRentReminderWhatsApp(tenant, prop, amount) {
      const msg = encodeURIComponent(`Namaste ${tenant} Ji, Sharma Rentals se reminder hai ki aapka ${prop} ka is mahine ka rent ₹${amount.toLocaleString('en-IN')} due hai. Kripya time pe pay karein taki koi late fee na lage.`);
      window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
      showToast(`Reminder sent to ${tenant}!`, "info");
    }

    function markRentAsPaid(id) {
      const item = rentCollections.find(x => x.id === id);
      if (item) {
        item.status = "Paid";
        saveState();
        renderAdminRentCollectionTable();
        showToast(`Rent marked as PAID for ${item.tenant}!`, "success");
      }
    }

    // ================= ADMIN TAB 4: COMMISSION TRACKER =================
    function renderAdminCommissionTable() {
      const tbody = document.getElementById('adminCommissionTableBody');
      tbody.innerHTML = commissions.map(c => {
        const isReceived = c.status === 'Received';
        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4 text-stone-600">${c.date}</td>
            <td class="p-4 font-bold text-charcoal-900">${c.property}</td>
            <td class="p-4 text-stone-700">${c.tenant}</td>
            <td class="p-4 font-serif text-stone-600">₹${c.rent.toLocaleString('en-IN')}</td>
            <td class="p-4 font-serif font-extrabold text-terracotta-800 text-sm">₹${c.commission.toLocaleString('en-IN')}</td>
            <td class="p-4">
              <span class="px-2.5 py-1 rounded-full text-[11px] font-bold ${isReceived ? 'bg-olive-100 text-olive-800' : 'bg-maroon-100 text-maroon-800'}">
                ${c.status}
              </span>
            </td>
            <td class="p-4 text-right">
              ${!isReceived ? `
                <button onclick="markCommissionReceived('${c.id}')" class="px-3 py-1 rounded-full bg-olive-700 text-white text-xs font-bold hover:bg-olive-800">
                  Mark Received
                </button>
              ` : `<span class="text-xs text-olive-700 font-bold"><i class="fa-solid fa-circle-check"></i> Received</span>`}
            </td>
          </tr>
        `;
      }).join('');
    }

    function markCommissionReceived(id) {
      const c = commissions.find(x => x.id === id);
      if (c) {
        c.status = "Received";
        saveState();
        renderAdminCommissionTable();
        showToast("Commission marked as RECEIVED!", "success");
      }
    }

    // ================= ADMIN TAB 5: LEADS & SITE VISITS =================
    function renderAdminLeadsTable() {
      const tbody = document.getElementById('adminLeadsTableBody');
      tbody.innerHTML = leads.map(l => {
        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4">
              <p class="font-bold text-charcoal-900">${l.tenant}</p>
              <p class="text-[10px] text-terracotta-700 font-mono font-bold">${l.id} • ${l.phone}</p>
            </td>
            <td class="p-4 text-stone-700 font-medium">${l.property}</td>
            <td class="p-4 text-stone-600">${l.date}</td>
            <td class="p-4 font-bold text-charcoal-900">${l.time}</td>
            <td class="p-4">
              <select onchange="updateLeadStatus('${l.id}', this.value)" class="text-xs font-bold p-1.5 rounded-full border border-amber-300 bg-white">
                <option value="New" ${l.status === 'New' ? 'selected' : ''}>New</option>
                <option value="Visit Done" ${l.status === 'Visit Done' ? 'selected' : ''}>Visit Done</option>
                <option value="Token Done" ${l.status === 'Token Done' ? 'selected' : ''}>Token Done</option>
                <option value="Agreement Done" ${l.status === 'Agreement Done' ? 'selected' : ''}>Agreement Done</option>
                <option value="Rented" ${l.status === 'Rented' ? 'selected' : ''}>Rented Out</option>
              </select>
            </td>
            <td class="p-4 text-right space-x-1">
              <a href="tel:${l.phone}" class="w-8 h-8 rounded-full bg-charcoal-900 text-white inline-flex items-center justify-center text-xs hover:bg-terracotta-700"><i class="fa-solid fa-phone"></i></a>
              <a href="https://wa.me/91${l.phone}?text=Namaste%20Ji,%20Sharma%20Rentals%20se%20call%20hai" target="_blank" class="w-8 h-8 rounded-full bg-olive-700 text-white inline-flex items-center justify-center text-xs hover:bg-olive-800"><i class="fa-brands fa-whatsapp"></i></a>
            </td>
          </tr>
        `;
      }).join('');
    }

    function updateLeadStatus(id, newStatus) {
      const l = leads.find(x => x.id === id);
      if (l) {
        l.status = newStatus;
        saveState();
        showToast(`Lead status updated to: ${newStatus}`, "info");
      }
    }

    // ================= ADMIN TAB 6: AUTO AGREEMENT GENERATOR & SIGNATURE =================
    function populateAgreementDropdowns() {
      const propSel = document.getElementById('agrPropSelect');
      const tenSel = document.getElementById('agrTenantSelect');

      if (propSel) {
        propSel.innerHTML = properties.map(p => `
          <option value="${p.title}" data-rent="${p.rent}" data-deposit="${p.deposit}" data-owner="${p.owner}">
            ${p.title} (Rent: ₹${p.rent})
          </option>
        `).join('');
      }

      if (tenSel) {
        tenSel.innerHTML = tenants.map(t => `
          <option value="${t.name}">${t.name} (${t.phone})</option>
        `).join('');
      }

      syncAgreementPreview();
    }

    function syncAgreementPreview() {
      const propSel = document.getElementById('agrPropSelect');
      const tenSel = document.getElementById('agrTenantSelect');
      const rentInp = document.getElementById('agrRentInput');
      const depInp = document.getElementById('agrDepositInput');
      const startInp = document.getElementById('agrStartDate');
      const periodSel = document.getElementById('agrPeriod');

      if (!propSel || !tenSel) return;

      const selectedPropOpt = propSel.options[propSel.selectedIndex];
      const owner = selectedPropOpt ? selectedPropOpt.getAttribute('data-owner') : "Sunil Gupta";

      const rentVal = rentInp ? rentInp.value : "14500";
      const depVal = depInp ? depInp.value : "29000";

      document.getElementById('prevOwner').innerText = owner || "Sunil Gupta";
      document.getElementById('prevTenant').innerText = tenSel.value;
      document.getElementById('prevProperty').innerText = propSel.value;
      document.getElementById('prevRent').innerText = `₹${parseInt(rentVal).toLocaleString('en-IN')}`;
      document.getElementById('prevDeposit').innerText = `₹${parseInt(depVal).toLocaleString('en-IN')}`;
      document.getElementById('prevPeriod').innerText = `${periodSel ? periodSel.value : '11'} Mahine`;
      document.getElementById('prevStart').innerText = startInp ? startInp.value : '2026-12-01';
      document.getElementById('tenantSignDisplay').innerText = tenSel.value;
    }

    function initSignatureCanvas() {
      const canvas = document.getElementById('sigCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let isDrawing = false;

      ctx.strokeStyle = '#1C1917';
      ctx.lineWidth = 2;
      ctx.lineCap = 'round';

      function startDraw(e) {
        isDrawing = true;
        draw(e);
      }
      function endDraw() {
        isDrawing = false;
        ctx.beginPath();
      }
      function draw(e) {
        if (!isDrawing) return;
        const rect = canvas.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0].clientX);
        const clientY = e.clientY || (e.touches && e.touches[0].clientY);
        const x = clientX - rect.left;
        const y = clientY - rect.top;

        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);
      }

      canvas.addEventListener('mousedown', startDraw);
      canvas.addEventListener('mouseup', endDraw);
      canvas.addEventListener('mousemove', draw);

      canvas.addEventListener('touchstart', startDraw);
      canvas.addEventListener('touchend', endDraw);
      canvas.addEventListener('touchmove', draw);
    }

    function clearSignatureCanvas() {
      const canvas = document.getElementById('sigCanvas');
      if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }

    function printOrSaveAgreement() {
      window.print();
    }

    function generateNewAgreementForm() {
      document.getElementById('agreementTab').scrollIntoView({ behavior: 'smooth' });
      showToast("Agreement Form Ready to fill!", "info");
    }

    // ================= ADMIN TAB 7: MAINTENANCE MANAGER =================
    function renderAdminMaintenanceTable() {
      const tbody = document.getElementById('adminMaintenanceTableBody');
      tbody.innerHTML = complaints.map(c => {
        let statusBadge = "bg-amber-100 text-amber-900";
        if (c.status === 'Done') statusBadge = "bg-olive-100 text-olive-800";
        if (c.status === 'Pending') statusBadge = "bg-maroon-100 text-maroon-800";

        return `
          <tr class="table-cream-row border-b border-amber-100">
            <td class="p-4">
              <span class="font-mono font-bold text-terracotta-700">${c.id}</span>
              <p class="text-[10px] text-stone-500">${c.date}</p>
            </td>
            <td class="p-4 font-bold text-charcoal-900">${c.tenant} <br/><span class="text-xs font-normal text-stone-500">${c.property}</span></td>
            <td class="p-4 text-stone-700">${c.issue}</td>
            <td class="p-4">
              <img src="${c.photo}" class="w-10 h-10 rounded-lg object-cover border border-amber-200">
            </td>
            <td class="p-4 font-bold text-stone-800 text-xs">${c.mistri}</td>
            <td class="p-4">
              <span class="px-2.5 py-1 rounded-full text-[11px] font-bold ${statusBadge}">
                ${c.status}
              </span>
            </td>
            <td class="p-4 text-right space-x-1 whitespace-nowrap">
              <button onclick="reassignMistri('${c.id}')" class="px-2 py-1 rounded-full bg-cream-200 text-stone-800 text-[10px] font-bold">Assign Mistri</button>
              <button onclick="toggleComplaintStatus('${c.id}')" class="px-2 py-1 rounded-full bg-olive-100 text-olive-800 text-[10px] font-bold">Mark Done</button>
            </td>
          </tr>
        `;
      }).join('');
    }

    let currentAssignTicketId = null;

    function reassignMistri(id) {
      currentAssignTicketId = id;
      document.getElementById('assignModalTicketId').innerText = id;
      document.getElementById('assignMistriModal').classList.remove('hidden');
    }

    function closeAssignMistriModal() {
      document.getElementById('assignMistriModal').classList.add('hidden');
    }

    function confirmAssignMistri() {
      if (!currentAssignTicketId) return;
      const mistri = document.getElementById('assignMistriSelect').value;
      const c = complaints.find(x => x.id === currentAssignTicketId);
      if (c) {
        c.mistri = mistri;
        c.status = "In Progress";
        saveState();
        renderAdminMaintenanceTable();
        closeAssignMistriModal();
        showToast(`Mistri assigned to ticket ${currentAssignTicketId}!`, "success");
      }
    }

    function toggleComplaintStatus(id) {
      const c = complaints.find(x => x.id === id);
      if (c) {
        c.status = c.status === 'Done' ? 'Pending' : 'Done';
        saveState();
        renderAdminMaintenanceTable();
        showToast(`Ticket status updated to ${c.status}!`, "info");
      }
    }

    function openNewComplaintModal() {
      const defaultIssues = [
        "Bathroom ka nal leak kar raha hai",
        "Geyser garam pani nahi de raha",
        "Balcony light fuse ho gayi hai",
        "Kitchen sink drain jam hai"
      ];
      const randomIssue = defaultIssues[Math.floor(Math.random() * defaultIssues.length)];
      complaints.unshift({
        id: "TKT-" + Math.floor(100 + Math.random() * 900),
        date: "Today",
        tenant: "Walk-in Tenant",
        property: "Royal Palm Flat 204",
        issue: randomIssue,
        category: "Plumbing",
        photo: "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=200&q=80",
        mistri: "Raju Mistri (Plumber)",
        status: "Pending"
      });
      saveState();
      renderAdminMaintenanceTable();
      showToast("Nayi maintenance complaint add ho gayi!", "success");
    }

    // ================= TOAST SYSTEM =================
    function showToast(message, type = 'info') {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      
      let icon = '<i class="fa-solid fa-circle-info text-terracotta-700"></i>';
      let border = 'border-amber-300';
      if (type === 'success') {
        icon = '<i class="fa-solid fa-circle-check text-olive-700"></i>';
        border = 'border-olive-400';
      } else if (type === 'error') {
        icon = '<i class="fa-solid fa-circle-exclamation text-maroon-700"></i>';
        border = 'border-maroon-400';
      }

      toast.className = `glass-pill pointer-events-auto flex items-center gap-2.5 px-4 py-2.5 rounded-full shadow-warm-card border ${border} text-xs font-bold text-charcoal-900 transform transition-all duration-300 translate-y-2 opacity-0`;
      toast.innerHTML = `${icon} <span>${message}</span>`;
      container.appendChild(toast);

      setTimeout(() => {
        toast.classList.remove('translate-y-2', 'opacity-0');
      }, 20);

      setTimeout(() => {
        toast.classList.add('opacity-0', '-translate-y-2');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // Bulletproof initialization on DOM ready or immediate if already interactive
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initData);
    } else {
      initData();
    }
  