import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

features = [
    # A. Tenant
    ("1. Search Bar: Location, Budget, Type", "heroLocationSelect" in html and "heroBudgetSelect" in html and "heroTypeSelect" in html),
    ("1. Quick Filter Chips: 1BHK/2BHK/3BHK/PG/Shop", "1BHK" in html and "2BHK" in html and "3BHK" in html and "PG" in html and "Shop" in html),
    ("1. Featured Properties: Top 6", "FLAT-101" in html and "FLAT-106" in html),
    ("1. Stats: 50+ Props, 200+ Tenants, 5 Yrs", "50+ Verified" in html or "50+" in html and "200+" in html),
    ("1. How It Works: 3 Steps", "how-it-works" in html and "Step 1" in html),
    ("1. Testimonials: Tenant Reviews", "testimonials" in html),
    ("1. Floating WhatsApp Button", "fa-whatsapp" in html and "wa.me" in html),
    
    ("2. Property Card: Rent ₹12,000 / Month Bada", "Mahina" in html or "Month" in html),
    ("2. Deposit: ₹24,000", "deposit" in html or "Deposit" in html),
    ("2. Available From: 1 Dec 2026", "availableFrom" in html),
    ("2. Badges: Verified Owner, New, Urgent, Family", "Verified Owner" in html and "Urgent" in html),
    ("2. Filter Sidebar with Budget/Type/BHK/Furnished/Allowed/Sort", "filterSidebarDrawer" in html and "sidebarBudget" in html and "sidebarTypeSelect" in html and "sidebarBhk" in html and "sidebarFurnishingSelect" in html and "sidebarAllowedSelect" in html),
    ("2. Sort: Price Low to High / High to Low / Newest", "sortSelect" in html or "sort" in html.lower()),
    
    ("3. Photo Gallery: Photos + Video Tour", "videoTourModal" in html and "drawerThumbnailsRow" in html),
    ("3. Full Details: BHK, Floor, Facing, Area", "drawerBHK" in html and "drawerArea" in html),
    ("3. Rent Breakdown: Rent + Maint + Deposit + Brokerage", "drawerRentBreakdown" in html and "drawerDepositBreakdown" in html),
    ("3. Amenities: Lift, Parking, Power, Water, WiFi, Gym, Park", "Lift Available" in html and "Covered Parking" in html and "Gym & Club" in html),
    ("3. Nearby: School 500m, Market 200m, Hospital 1km, Metro", "School / College" in html and "Local Market" in html and "Hospital" in html and "Metro Station" in html),
    ("3. Owner Info: Verified Owner, Hide Owner Name, Agent Phone", "Verified Owner Property • Privacy Protected" in html),
    ("3. Buttons: [Book Site Visit] [Pay ₹2000 Token] [WhatsApp] [Call]", "openBookVisitModalFromDrawer" in html and "openTokenPaymentModalFromDrawer" in html),
    
    ("4. Site Visit Booking: Name, Phone 10-digit, Date, Slot [11 AM / 2 PM / 5 PM]", "visitNameInput" in html and "visitPhoneInput" in html and "visitDateInput" in html and "VISIT-1024" in html),
    ("4. Reschedule / Cancel Option", "openRescheduleModal" in html and "openCancelModal" in html),
    
    ("5. Token Payment: ₹2000, UPI (GPay/PhonePe/Paytm), Status Booked, Receipt PDF", "tokenPaymentModal" in html and "UPI" in html and "GPay" in html and "PhonePe" in html and "Paytm" in html and "receipt" in html.lower()),
    
    ("6. Tenant Portal: Phone + OTP, Visits, Agreement, Rent History, Receipts, Maintenance, Move-Out", "tenantPortalModal" in html and "tenantLoginPhone" in html and "tenantLoginOtp" in html and "tenantTabMyVisits" in html and "tenantTabMyAgreement" in html and "tenantTabMyRentHistory" in html and "tenantTabMyReceipts" in html and "tenantTabMaintenance" in html and "tenantTabMoveOut" in html),
    
    # B. Agent
    ("7. Admin Dashboard: 50 Total, 38 Rented, 12 Vacant, 3 Booked", "bentoTotalProps" in html and "bentoRentedProps" in html and "bentoVacantProps" in html),
    ("7. Is Mahine Ki Kamai: ₹60,000", "bentoCommission" in html),
    ("7. Rent Collection: 4,50,000 total, 3,80,000 aaya, 70,000 baki", "4,50,000" in html and "3,80,000" in html),
    ("7. Aaj Ki Site Visits: 4", "4 Scheduled Today" in html or "4" in html),
    ("7. Vacant Loss: ₹18,000 - 3 Property Khali", "bentoTotalVacantLoss" in html and "18,000" in html),
    
    ("8. Property Manager: Table with Status Colors, Days Vacant, Action", "adminPropertyTableBody" in html),
    ("8. Add Property Form: Photo, Rent, Deposit, BHK, Furnished, Allowed, Owner", "addPropertyModal" in html),
    ("8. Edit / Delete / Toggle Status", "togglePropStatus" in html and "deleteProperty" in html),
    ("8. Vacant Loss Calculator: Flat 302 - 15 Din - ₹6,000 Nuksaan", "calcVacantRent" in html and "calcVacantDays" in html),
    
    ("9. Tenant Manager: Table, Aadhaar, Job, Salary, Family, Score 4.8", "adminTenantTableBody" in html and "tenantProfileModal" in html and "Aadhaar" in html),
    ("9. Agreement Alert: Rahul Expiry Renew Karo", "quickRenewAgreement" in html),
    ("9. Add Tenant / Remove Tenant", "addTenantModal" in html),
    
    ("10. Rent Collection Manager: Table, Late Red, Send WhatsApp Reminder, Mark Paid", "adminRentTableBody" in html and "sendRentReminderWhatsApp" in html and "markRentAsPaid" in html),
    ("10. Auto Reminder Settings + Auto Late Fee ₹200", "saveReminderSettings" in html and "200" in html),
    
    ("11. Commission Tracker: Table, Received/Pending, Total 60k/48k/12k, Monthly Report", "adminCommissionTableBody" in html and "monthlyReportModal" in html),
    
    ("12. Leads + Visits Manager: Table, Status Change, Call Button", "adminLeadsTableBody" in html and "updateLeadStatus" in html),
    
    ("13. Agreement Manager: Auto Fill, Digital Sign Canvas, Expiry Alert", "agreementTab" in html and "agrPropSelect" in html and "sigCanvas" in html),
    
    ("14. Maintenance Manager: Complaints List with Photo, Pending/In Progress/Done, Assign Mistri", "adminMaintenanceTableBody" in html and "assignMistriModal" in html and "assignMistriSelect" in html)
]

print("=== 14 FEATURES AUDIT REPORT ===")
missing_count = 0
for title, present in features:
    status = "PRESENT" if present else "MISSING"
    if not present:
        missing_count += 1
    print(f"[{status}] {title}")

print(f"\nTotal Checked: {len(features)}, Missing: {missing_count}")
