const Database = require('../db');

function handleStats(req, res, sendJson) {
  const db = Database.get();
  const total = db.properties.length;
  const rented = db.properties.filter(p => p.status === 'Rented').length;
  const vacant = db.properties.filter(p => p.status === 'Available' || p.status === 'Vacant').length;
  const booked = db.properties.filter(p => p.status === 'Booked').length;

  let totalVacantLoss = 0;
  db.properties.forEach(p => {
    if ((p.status === 'Available' || p.status === 'Vacant') && p.vacantDays > 0) {
      const dailyRent = Math.round(p.rent / 30);
      totalVacantLoss += (dailyRent * p.vacantDays);
    }
  });

  let totalCommission = 0;
  let receivedCommission = 0;
  db.commissions.forEach(c => {
    totalCommission += (c.commission || 0);
    if (c.status === 'Received') receivedCommission += (c.commission || 0);
  });

  return sendJson(res, 200, {
    totalProperties: total,
    rentedProperties: rented,
    vacantProperties: vacant,
    bookedProperties: booked,
    totalVacantLoss: totalVacantLoss,
    monthlyCollection: {
      target: 450000,
      collected: 380000,
      pending: 70000,
      rate: 84
    },
    commission: {
      total: totalCommission || 60000,
      received: receivedCommission || 48000,
      pending: (totalCommission - receivedCommission) || 12000
    },
    todayVisits: 4
  });
}

module.exports = handleStats;
