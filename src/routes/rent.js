const Database = require('../db');

async function handleRent(req, res, pathname, method, parseBody, sendJson) {
  const db = Database.get();

  if (pathname === '/api/rent') {
    if (method === 'GET') {
      return sendJson(res, 200, db.rentCollections);
    }
  }

  if (pathname.startsWith('/api/rent/') && pathname.endsWith('/pay') && method === 'POST') {
    const rentId = pathname.split('/')[3];
    const item = db.rentCollections.find(r => r.id === rentId);
    if (item) {
      item.status = 'Paid';
      Database.save(db);
      return sendJson(res, 200, { success: true, item });
    }
    return sendJson(res, 404, { error: 'Record not found' });
  }

  return false;
}

module.exports = handleRent;
