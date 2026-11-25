const Database = require('../db');

async function handleToken(req, res, pathname, method, parseBody, sendJson) {
  if (pathname === '/api/token' && method === 'POST') {
    const body = await parseBody(req);
    const db = Database.get();
    const propId = body.propertyId;
    const prop = db.properties.find(p => p.id === propId || p.title === body.propertyTitle);

    if (prop) {
      prop.status = 'Booked';
    }

    const tokenId = 'TOK-' + Math.floor(1000 + Math.random() * 9000);
    const receipt = {
      tokenId: tokenId,
      amount: 2000,
      property: prop ? prop.title : body.propertyTitle,
      date: new Date().toLocaleDateString('en-IN'),
      mode: 'UPI Instant Guarantee',
      status: 'LOCKED & CONFIRMED'
    };

    Database.save(db);
    return sendJson(res, 200, { success: true, receipt, lockedProperty: prop });
  }

  return false;
}

module.exports = handleToken;
