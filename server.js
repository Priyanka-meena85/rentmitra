/**
 * RentWala - Sharma Rentals
 * Senior Full-Stack Production Server
 * Native Node.js HTTP REST API & Static Asset Server
 */

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const url = require('node:url');

// Route Controllers
const handleStats = require('./src/routes/stats');
const handleProperties = require('./src/routes/properties');
const handleTenants = require('./src/routes/tenants');
const handleVisits = require('./src/routes/visits');
const handleToken = require('./src/routes/token');
const handleRent = require('./src/routes/rent');
const handleCommission = require('./src/routes/commission');
const handleMaintenance = require('./src/routes/maintenance');

const PORT = process.env.PORT || 4000;
const PUBLIC_DIR = path.join(__dirname, 'public');
const ROOT_INDEX = path.join(__dirname, 'index.html');

// Helper to parse JSON request body
function parseBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      if (!body) return resolve({});
      try {
        resolve(JSON.parse(body));
      } catch (e) {
        resolve({});
      }
    });
    req.on('error', err => reject(err));
  });
}

// Send standard JSON response with CORS headers
function sendJson(res, statusCode, payload) {
  res.writeHead(statusCode, {
    'Content-Type': 'application/json; charset=utf-8',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
  });
  res.end(JSON.stringify(payload));
}

// MIME Types Map
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;
  const method = req.method;

  // Handle CORS preflight
  if (method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    });
    return res.end();
  }

  // ================= 1. REST API ROUTING =================
  if (pathname.startsWith('/api/')) {
    // Health Check
    if (pathname === '/api/health' && method === 'GET') {
      return sendJson(res, 200, {
        status: 'online',
        service: 'RentWala - Sharma Rentals Full-Stack API',
        version: '2.5.0',
        port: PORT,
        uptime: process.uptime(),
        database: 'data/db.json (Connected)',
        timestamp: new Date().toISOString()
      });
    }

    // Stats (Bento Grid)
    if (pathname === '/api/stats' && method === 'GET') {
      return handleStats(req, res, sendJson);
    }

    // Properties API
    if (pathname.startsWith('/api/properties')) {
      const handled = await handleProperties(req, res, pathname, method, parsedUrl.query, parseBody, sendJson);
      if (handled !== false) return;
    }

    // Tenants API
    if (pathname.startsWith('/api/tenants')) {
      const handled = await handleTenants(req, res, pathname, method, parseBody, sendJson);
      if (handled !== false) return;
    }

    // Visits & Leads API
    if (pathname.startsWith('/api/visits') || pathname.startsWith('/api/leads')) {
      const handled = await handleVisits(req, res, pathname, method, parseBody, sendJson);
      if (handled !== false) return;
    }

    // Token Lock API
    if (pathname === '/api/token') {
      const handled = await handleToken(req, res, pathname, method, parseBody, sendJson);
      if (handled !== false) return;
    }

    // Rent Collection API
    if (pathname.startsWith('/api/rent')) {
      const handled = await handleRent(req, res, pathname, method, parseBody, sendJson);
      if (handled !== false) return;
    }

    // Commission Tracker API
    if (pathname.startsWith('/api/commissions')) {
      const handled = handleCommission(req, res, pathname, method, sendJson);
      if (handled !== false) return;
    }

    // Maintenance Manager API
    if (pathname.startsWith('/api/maintenance')) {
      const handled = await handleMaintenance(req, res, pathname, method, parseBody, sendJson);
      if (handled !== false) return;
    }

    return sendJson(res, 404, { error: 'API endpoint not found' });
  }

  // ================= 2. STATIC ASSET SERVING =================
  let filePath;
  if (pathname === '/' || pathname === '/index.html') {
    // Check public/index.html first, fallback to root index.html
    const publicIndex = path.join(PUBLIC_DIR, 'index.html');
    filePath = fs.existsSync(publicIndex) ? publicIndex : ROOT_INDEX;
  } else {
    filePath = path.join(PUBLIC_DIR, pathname);
    if (!fs.existsSync(filePath)) {
      filePath = path.join(__dirname, pathname);
    }
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('404 Not Found');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, {
      'Content-Type': contentType,
      'Cache-Control': 'public, max-age=3600'
    });

    const stream = fs.createReadStream(filePath);
    stream.pipe(res);
  });
});

server.listen(PORT, () => {
  console.log('================================================================');
  console.log('  🏛️  RentWala - Sharma Rentals Full-Stack Platform Active  ');
  console.log(`  🔗  Web App:  http://localhost:${PORT}                      `);
  console.log(`  📡  REST API: http://localhost:${PORT}/api/health           `);
  console.log('  💾  Database: data/db.json (Live Persistence)                 ');
  console.log('================================================================');
});
