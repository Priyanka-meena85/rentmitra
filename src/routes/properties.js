const Database = require('../db');

async function handleProperties(req, res, pathname, method, query, parseBody, sendJson) {
  const db = Database.get();

  // GET /api/properties
  if (pathname === '/api/properties' && method === 'GET') {
    let list = [...db.properties];
    const { bhk, status, locality } = query;
    if (bhk) list = list.filter(p => p.bhk === bhk);
    if (status) list = list.filter(p => p.status === status);
    if (locality) list = list.filter(p => p.locality.toLowerCase().includes(locality.toLowerCase()));
    return sendJson(res, 200, list);
  }

  // POST /api/properties
  if (pathname === '/api/properties' && method === 'POST') {
    const body = await parseBody(req);
    const newProp = {
      id: 'FLAT-' + Math.floor(100 + Math.random() * 900),
      title: body.title || 'New Verified Flat',
      locality: body.locality || 'Indirapuram',
      fullAddress: body.fullAddress || `${body.title}, ${body.locality}`,
      rent: parseInt(body.rent) || 12000,
      deposit: parseInt(body.deposit) || 24000,
      bhk: body.bhk || '2BHK',
      area: parseInt(body.area) || 950,
      furnishing: body.furnishing || 'Full Furnished',
      allowed: body.allowed || 'Family / Bachelor Both',
      status: body.status || 'Available',
      vacantDays: body.status === 'Available' ? 1 : 0,
      owner: body.owner || 'Sharma Ji Verified Owner',
      availableFrom: body.availableFrom || 'Immediate',
      badge: 'New Verified',
      images: body.images || ['https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80'],
      amenities: body.amenities || ['Lift', 'Car Parking', '24h Water', 'Power Backup']
    };
    db.properties.unshift(newProp);
    Database.save(db);
    return sendJson(res, 201, { success: true, property: newProp });
  }

  // PUT /api/properties/:id or DELETE /api/properties/:id
  if (pathname.startsWith('/api/properties/')) {
    const propId = pathname.split('/')[3];
    const index = db.properties.findIndex(p => p.id === propId);

    if (index === -1) {
      return sendJson(res, 404, { error: 'Property not found' });
    }

    if (method === 'PUT') {
      const body = await parseBody(req);
      db.properties[index] = { ...db.properties[index], ...body };
      if (body.status === 'Available') {
        db.properties[index].vacantDays = body.vacantDays || 5;
      } else {
        db.properties[index].vacantDays = 0;
      }
      Database.save(db);
      return sendJson(res, 200, { success: true, property: db.properties[index] });
    }

    if (method === 'DELETE') {
      const deleted = db.properties.splice(index, 1);
      Database.save(db);
      return sendJson(res, 200, { success: true, deleted: deleted[0] });
    }
  }

  return false;
}

module.exports = handleProperties;
