const Database = require('../db');

function handleCommission(req, res, pathname, method, sendJson) {
  const db = Database.get();

  if (pathname === '/api/commissions' && method === 'GET') {
    return sendJson(res, 200, db.commissions);
  }

  if (pathname.startsWith('/api/commissions/') && pathname.endsWith('/receive') && method === 'POST') {
    const comId = pathname.split('/')[3];
    const c = db.commissions.find(item => item.id === comId);
    if (c) {
      c.status = 'Received';
      Database.save(db);
      return sendJson(res, 200, { success: true, commission: c });
    }
    return sendJson(res, 404, { error: 'Commission record not found' });
  }

  return false;
}

module.exports = handleCommission;
