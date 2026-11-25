const Database = require('../db');

async function handleTenants(req, res, pathname, method, parseBody, sendJson) {
  const db = Database.get();

  if (pathname === '/api/tenants') {
    if (method === 'GET') {
      return sendJson(res, 200, db.tenants);
    }

    if (method === 'POST') {
      const body = await parseBody(req);
      const newTenant = {
        id: 'TEN-' + Math.floor(10 + Math.random() * 90),
        name: body.name || 'Alok Sharma',
        property: body.property || 'Flat 204, Royal Palm',
        phone: body.phone || '+91 9876543210',
        rent: parseInt(body.rent) || 14000,
        agreementEnd: body.agreementEnd || '30 Nov 2027',
        score: 4.8,
        aadhaar: body.aadhaar || 'XXXX-XXXX-6677',
        job: body.job || 'Corporate Professional',
        salary: body.salary || '₹1,00,000 / mo',
        familyMembers: body.familyMembers || 'Family (2 Adults)'
      };
      db.tenants.unshift(newTenant);
      Database.save(db);
      return sendJson(res, 201, { success: true, tenant: newTenant });
    }
  }

  if (pathname.startsWith('/api/tenants/') && method === 'DELETE') {
    const tenantId = pathname.split('/')[3];
    const index = db.tenants.findIndex(t => t.id === tenantId);
    if (index !== -1) {
      db.tenants.splice(index, 1);
      Database.save(db);
      return sendJson(res, 200, { success: true });
    }
    return sendJson(res, 404, { error: 'Tenant not found' });
  }

  return false;
}

module.exports = handleTenants;
