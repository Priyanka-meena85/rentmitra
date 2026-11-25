with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="tenantPortalModal"' in l or 'id="bookVisitModal"' in l or 'id="tokenPaymentModal"' in l:
        print(f"{i+1}: {l.strip()[:100]}")
