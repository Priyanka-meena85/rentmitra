const Database = require('../db');

async function handleMaintenance(req, res, pathname, method, parseBody, sendJson) {
  const db = Database.get();

  if (pathname === '/api/maintenance') {
    if (method === 'GET') {
      return sendJson(res, 200, db.complaints);
    }

    if (method === 'POST') {
      const body = await parseBody(req);
      const newComplaint = {
        id: 'TKT-' + Math.floor(100 + Math.random() * 900),
        date: 'Today',
        tenant: body.tenant || 'Rahul Verma',
        property: body.property || 'Flat 204',
        issue: body.issue || 'Nal tapak raha hai',
        category: body.category || 'Plumbing',
        photo: body.photo || 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=200&q=80',
        mistri: body.mistri || 'Raju Mistri (Plumber)',
        status: 'Pending'
      };
      db.complaints.unshift(newComplaint);
      Database.save(db);
      return sendJson(res, 201, { success: true, complaint: newComplaint });
    }
  }

  if (pathname.startsWith('/api/maintenance/')) {
    const parts = pathname.split('/');
    const ticketId = parts[3];
    const action = parts[4];
    const c = db.complaints.find(x => x.id === ticketId);

    if (!c) {
      return sendJson(res, 404, { error: 'Complaint ticket not found' });
    }

    if (action === 'assign' && method === 'PUT') {
      const body = await parseBody(req);
      c.mistri = body.mistri || 'Raju Mistri (Plumber)';
      c.status = 'In Progress';
      Database.save(db);
      return sendJson(res, 200, { success: true, complaint: c });
    }

    if (action === 'status' && method === 'PUT') {
      const body = await parseBody(req);
      c.status = body.status || (c.status === 'Done' ? 'Pending' : 'Done');
      Database.save(db);
      return sendJson(res, 200, { success: true, complaint: c });
    }
  }

  return false;
}

module.exports = handleMaintenance;
