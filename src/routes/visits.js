const Database = require('../db');

async function handleVisits(req, res, pathname, method, parseBody, sendJson) {
  const db = Database.get();

  if (pathname === '/api/visits' || pathname === '/api/leads') {
    if (method === 'GET') {
      return sendJson(res, 200, db.leads);
    }

    if (method === 'POST') {
      const body = await parseBody(req);
      const bookingId = 'VISIT-' + Math.floor(1000 + Math.random() * 9000);
      const newLead = {
        id: bookingId,
        tenant: body.name || 'New Tenant',
        phone: body.phone || '9876543210',
        property: body.property || 'Flat 204, Royal Palm',
        date: body.date || '2026-11-26',
        time: body.time || '11:00 AM',
        status: 'New'
      };
      db.leads.unshift(newLead);
      Database.save(db);
      return sendJson(res, 201, { success: true, lead: newLead, bookingId });
    }
  }

  if (pathname.startsWith('/api/leads/') || pathname.startsWith('/api/visits/')) {
    const leadId = pathname.split('/')[3];
    const index = db.leads.findIndex(l => l.id === leadId);

    if (index === -1) {
      return sendJson(res, 404, { error: 'Lead not found' });
    }

    if (method === 'PUT') {
      const body = await parseBody(req);
      db.leads[index] = { ...db.leads[index], ...body };
      Database.save(db);
      return sendJson(res, 200, { success: true, lead: db.leads[index] });
    }

    if (method === 'DELETE') {
      db.leads.splice(index, 1);
      Database.save(db);
      return sendJson(res, 200, { success: true });
    }
  }

  return false;
}

module.exports = handleVisits;
