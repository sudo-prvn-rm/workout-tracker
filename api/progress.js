// Vercel Serverless Function: /api/progress
const { Pool } = require('pg');

let pool = null;
let dbReady = false;

function getPool() {
  if (pool) return pool;
  const dbUrl = process.env.DB_URL;
  if (!dbUrl) return null;
  try {
    pool = new Pool({
      connectionString: dbUrl,
      ssl: dbUrl.includes('sslmode=require') || dbUrl.includes('.neon.tech') || dbUrl.includes('supabase')
        ? { rejectUnauthorized: false }
        : false
    });
    return pool;
  } catch (err) {
    console.warn('DB Pool init error:', err.message);
    return null;
  }
}

async function ensureTable(p) {
  if (dbReady) return true;
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
    console.warn('DB table check error:', err.message);
    return false;
  }
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const p = getPool();

  if (req.method === 'GET') {
    if (p && await ensureTable(p)) {
      try {
        const result = await p.query('SELECT data FROM workout_progress WHERE id = $1', ['default_user']);
        if (result.rows.length > 0 && result.rows[0].data) {
          res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
          res.end(JSON.stringify(result.rows[0].data));
          return;
        }
      } catch (err) {
        console.error('DB read error:', err.message);
      }
    }
    // Default fallback to empty state (frontend uses localStorage)
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({ checks: {}, water: {}, notes: {} }));
    return;
  }

  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', async () => {
      try {
        const parsed = JSON.parse(body || '{}');
        if (p && await ensureTable(p)) {
          await p.query(`
            INSERT INTO workout_progress (id, data, updated_at)
            VALUES ($1, $2, CURRENT_TIMESTAMP)
            ON CONFLICT (id) DO UPDATE SET data = $2, updated_at = CURRENT_TIMESTAMP;
          `, ['default_user', parsed]);
        }
        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ status: 'ok', saved: true }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
      }
    });
    return;
  }

  res.writeHead(405, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Method not allowed' }));
};
