const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = parseInt(process.env.PORT, 10) || 3000;
const DB_URL = process.env.DB_URL || '';
const DATA_FILE = path.join(__dirname, 'progress.json');

// Memory cache for progress state
let localProgress = { checks: {}, water: {}, notes: {} };
if (fs.existsSync(DATA_FILE)) {
  try {
    localProgress = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  } catch (e) {
    console.warn('⚠️ Could not parse existing progress.json:', e.message);
  }
}

// Optional PG Pool if DB_URL is supplied (e.g. Supabase or Neon on Vercel)
let pool = null;
let dbReady = false;

function getPool() {
  if (pool) return pool;
  if (!DB_URL) return null;
  try {
    const { Pool } = require('pg');
    pool = new Pool({
      connectionString: DB_URL,
      ssl: DB_URL.includes('sslmode=require') || DB_URL.includes('.neon.tech') || DB_URL.includes('supabase')
        ? { rejectUnauthorized: false }
        : false
    });
    return pool;
  } catch (err) {
    console.warn('⚠️ Optional pg pool init error (using local storage):', err.message);
    return null;
  }
}

async function ensureTable() {
  if (dbReady) return true;
  const p = getPool();
  if (!p) return false;
  try {
    await p.query(`
      CREATE TABLE IF NOT EXISTS workout_progress (
        id VARCHAR(50) PRIMARY KEY,
        data JSONB NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);
    dbReady = true;
    return true;
  } catch (err) {
    console.warn('⚠️ DB table check error:', err.message);
    return false;
  }
}

async function loadProgress() {
  const p = getPool();
  if (p && await ensureTable()) {
    try {
      const res = await p.query('SELECT data FROM workout_progress WHERE id = $1', ['default_user']);
      if (res.rows.length > 0) return res.rows[0].data;
    } catch (e) {
      console.warn('⚠️ DB read fallback:', e.message);
    }
  }
  return localProgress;
}

async function saveProgress(data) {
  localProgress = data;
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2), 'utf8');
  } catch (e) {
    // Read-only filesystem on Vercel serverless
  }

  const p = getPool();
  if (p && await ensureTable()) {
    try {
      await p.query(`
        INSERT INTO workout_progress (id, data, updated_at)
        VALUES ($1, $2, CURRENT_TIMESTAMP)
        ON CONFLICT (id) DO UPDATE SET data = $2, updated_at = CURRENT_TIMESTAMP;
      `, ['default_user', data]);
    } catch (e) {
      console.warn('⚠️ DB write fallback:', e.message);
    }
  }
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const pathname = url.pathname;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // API endpoints
  if (pathname === '/api/progress') {
    if (req.method === 'GET') {
      const data = await loadProgress();
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(data));
      return;
    }

    if (req.method === 'POST') {
      let body = '';
      req.on('data', chunk => { body += chunk; });
      req.on('end', async () => {
        try {
          const parsed = JSON.parse(body || '{}');
          await saveProgress(parsed);
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ status: 'ok', saved: true }));
        } catch (e) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Invalid JSON' }));
        }
      });
      return;
    }
  }

  // Static files
  let filePath = path.join(__dirname, pathname === '/' ? 'index.html' : pathname);

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const mimeTypes = {
      '.html': 'text/html; charset=utf-8',
      '.js': 'application/javascript; charset=utf-8',
      '.json': 'application/json; charset=utf-8',
      '.css': 'text/css; charset=utf-8',
      '.md': 'text/markdown; charset=utf-8',
      '.svg': 'image/svg+xml'
    };
    const contentType = mimeTypes[ext] || 'application/octet-stream';
    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  } else {
    // Fallback to index.html for SPA routes
    filePath = path.join(__dirname, 'index.html');
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    fs.createReadStream(filePath).pipe(res);
  }
});

server.listen(PORT, () => {
  console.log(`🏋️ Workout Tracker server running at http://localhost:${PORT}`);
});
