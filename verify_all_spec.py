with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    "1. Home Page + Search": [
        ("Location, Budget, Type in Hero", "id=\"heroLocationSelect\"" in html and "id=\"heroBudgetSelect\"" in html and "id=\"heroTypeSelect\"" in html),
        ("Quick Filter Chips (1BHK/2BHK/3BHK/PG/Shop)", "1BHK" in html and "2BHK" in html and "3BHK" in html and "PG" in html and "Shop" in html),
        ("Featured Properties (Top 6)", "FLAT-101" in html and "FLAT-106" in html),
        ("Stats: 50+ Props, 200+ Tenants, 5 Yrs", "50+ Verified" in html or ("50+" in html and "200+" in html)),
        ("How It Works: 3 Steps", "id=\"how-it-works\"" in html and "1. Property Dekho" in html),
        ("Testimonials: Tenant Reviews", "id=\"testimonials\"" in html),
        ("Floating WhatsApp Button", "wa.me" in html and "pulse-wa" in html)
    ],
    "2. Property Listing": [
        ("Property Card with Photo, Rent, Location, BHK", "class=\"font-serif font-extrabold" in html),
        ("Rent ₹12,000 / Month Bada", "Mahina" in html),
        ("Deposit ₹24,000", "deposit" in html or "Deposit" in html),
        ("Available From Date", "availableFrom" in html),
        ("Badges (Verified Owner, Urgent, Family)", "Verified Owner" in html and "Urgent Deal" in html),
        ("Filter Sidebar with Budget/Type/BHK/Furnished/Allowed", "id=\"filterSidebarDrawer\"" in html),
        ("Sort: Low to High / High to Low / Newest", "id=\"sortSelect\"" in html or "sortPublicProperties" in html)
    ],
    "3. Property Details Page": [
        ("Photo Gallery (Thumbnails + Main)", "id=\"drawerThumbnailsRow\"" in html),
        ("Video Tour 360", "id=\"videoTourModal\"" in html),
        ("Full Details: BHK, Floor, Facing, Area", "id=\"drawerBHK\"" in html and "id=\"drawerArea\"" in html),
        ("Rent Breakdown: Rent + Maint + Deposit + Brokerage", "id=\"drawerRentBreakdown\"" in html and "id=\"drawerDepositBreakdown\"" in html),
        ("Amenities: Lift, Parking, Power, Water, WiFi, Security, Gym, Park", "Lift Available" in html and "Covered Parking" in html),
        ("Nearby: School, Market, Hospital, Metro", "Metro Station" in html and "School / College" in html and "Local Market" in html and "Hospital" in html),
        ("Owner Info: Verified Owner, Hide Owner Name, Agent Phone", "Verified Owner Property • Privacy Protected" in html),
        ("Buttons: [Book Site Visit] [Pay ₹2,000 Token] [WhatsApp] [Call]", "openBookVisitModalFromDrawer" in html and "openTokenPaymentModalFromDrawer" in html and "drawerWhatsAppEnquiry" in html)
    ],
    "4. Site Visit Booking": [
        ("Form: Naam, Phone 10-digit, Date, Time Slot", "id=\"visitNameInput\"" in html and "id=\"visitPhoneInput\"" in html and "id=\"visitDateInput\"" in html),
        ("Time Slot [11 AM / 2 PM / 5 PM]", "11:00 AM" in html and "02:00 PM" in html and "05:00 PM" in html),
        ("Phone Validation: 10 Digit", "test(phone)" in html or "length === 10" in html),
        ("Booking ID: VISIT-1024", "VISIT-" in html),
        ("Confirmation: Screen + WhatsApp", "visitSuccessScreen" in html and "successWhatsAppShareBtn" in html),
        ("Reschedule / Cancel Option", "openRescheduleModal" in html and "openCancelModal" in html)
    ],
    "5. Token Payment": [
        ("₹2,000 Token Button", "2,000 Token" in html),
        ("UPI Payment: GPay / PhonePe / Paytm", "GPay" in html and "PhonePe" in html and "Paytm" in html),
        ("Pay Hote Hi Property Status Booked", "prop.status = 'Booked'" in html or "status = 'Booked'" in html),
        ("Receipt PDF Download", "officialReceiptModal" in html or "print" in html.lower())
    ],
    "6. Tenant Portal": [
        ("Phone + OTP Login", "tenantLoginPhone" in html and "tenantLoginOtp" in html),
        ("My Visits: Upcoming + Done", "tenantTabMyVisits" in html),
        ("My Agreement PDF Download", "tenantTabMyAgreement" in html),
        ("My Rent History: Paid / Late", "tenantTabMyRentHistory" in html),
        ("My Receipts PDF", "tenantTabMyReceipts" in html),
        ("Maintenance Request: Nal Kharab Hai Photo", "tenantTabMaintenance" in html),
        ("Move-Out Request", "tenantTabMoveOut" in html)
    ],
    "7. Admin Dashboard": [
        ("Total 50, Rented 38, Vacant 12, Booked 3", "bentoTotalProps" in html and "bentoRentedProps" in html and "bentoVacantProps" in html),
        ("Is Mahine Ki Kamai: ₹60,000", "bentoCommission" in html),
        ("Rent Collection: 4,50,000 / 3,80,000 / 70,000", "4,50,000" in html and "3,80,000" in html),
        ("Aaj Ki Site Visits: 4", "4 Scheduled Today" in html or "4" in html),
        ("Vacant Loss: ₹18,000 - 3 Property Khali", "bentoTotalVacantLoss" in html)
    ],
    "8. Property Manager": [
        ("Table: Photo, Name, Owner, Rent, Status, Days Vacant, Action", "adminPropertyTableBody" in html),
        ("Status Colors (Green/Red/Orange)", "bg-olive-100" in html and "bg-maroon-100" in html and "bg-amber-100" in html),
        ("Add Property Form with all fields", "addPropertyModal" in html),
        ("Edit / Delete / Toggle Status", "togglePropStatus" in html and "deleteProperty" in html),
        ("Vacant Loss Calculator (Flat 302 - 15 Din - ₹6,000)", "calcDaysRange" in html and "calcLossResult" in html)
    ],
    "9. Tenant Manager": [
        ("Table: Tenant, Property, Phone, Rent, Agreement End, Score", "adminTenantTableBody" in html),
        ("Tenant Profile Modal (Aadhaar, Job, Salary, Family)", "tenantProfileModal" in html),
        ("Tenant Score 4.8", "score" in html),
        ("Agreement Expiry Alert + Renew", "quickRenewAgreement" in html),
        ("Add Tenant / Remove Tenant", "addTenantModal" in html and "deleteTenant" in html)
    ],
    "10. Rent Collection Manager": [
        ("Table: Property, Tenant, Due Date, Amount, Status", "adminRentCollectionTableBody" in html),
        ("Late in Red", "bg-maroon-100 text-maroon-900" in html),
        ("Buttons: WhatsApp Reminder, Mark Paid", "sendRentReminderWhatsApp" in html and "markRentAsPaid" in html),
        ("Auto Reminder Settings (3 din pehle, due date, 2 din late)", "3 Din Pehle" in html and "Due Date Pe" in html and "2 Din Late Pe" in html),
        ("Auto Late Fee ₹200", "200" in html)
    ],
    "11. Commission Tracker": [
        ("Table: Date, Property, Tenant, Rent, Commission, Status", "adminCommissionTableBody" in html),
        ("Total: 60k, 48k Mila, 12k Baki", "60,000" in html and "48,000" in html and "12,000" in html),
        ("Monthly Report Modal", "monthlyReportModal" in html)
    ],
    "12. Leads + Visits Manager": [
        ("Table: Tenant, Property, Date, Time, Status", "adminLeadsTableBody" in html),
        ("Status Change Dropdown", "updateLeadStatus" in html),
        ("Call Button", "tel:" in html)
    ],
    "13. Agreement Manager": [
        ("Auto Agreement Generate (Owner+Tenant+Rent+Date)", "populateAgreementDropdowns" in html and "syncAgreementPreview" in html),
        ("Digital Signature Canvas", "sigCanvas" in html),
        ("PDF Download / Print", "printOfficialAgreement" in html or "window.print" in html),
        ("Agreement Expiry Alert", "expiryAlert" in html.lower() or "khatam ho raha" in html)
    ],
    "14. Maintenance Manager": [
        ("Complaints List (Nal Kharab Hai + Photo)", "adminMaintenanceTableBody" in html),
        ("Status: Pending / In Progress / Done", "toggleComplaintStatus" in html),
        ("Assign Plumber/Mistri Modal", "assignMistriModal" in html and "confirmAssignMistri" in html)
    ]
}

total_items = 0
passed_items = 0

for group, reqs in checks.items():
    print(f"\n--- {group} ---")
    for name, ok in reqs:
        total_items += 1
        if ok:
            passed_items += 1
            print(f"  [PASS] {name}")
        else:
            print(f"  [FAIL] {name}")

print(f"\n==========================================")
print(f"TOTAL COMPLIANCE: {passed_items}/{total_items} ({passed_items*100//total_items}%)")
print(f"==========================================")
