// Run from site/:  node --test
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import http from 'node:http';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const siteDir = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');
const port = 3900 + Math.floor(Math.random() * 90);
let server;

// Raw request so the path reaches the server exactly as written (no client-side normalisation).
function get(rawPath) {
  return new Promise((resolve, reject) => {
    const req = http.request({ host: '127.0.0.1', port, path: rawPath, method: 'GET' }, res => {
      let body = '';
      res.on('data', chunk => { body += chunk; });
      res.on('end', () => resolve({ status: res.statusCode, body }));
    });
    req.on('error', reject);
    req.end();
  });
}

before(async () => {
  server = spawn(process.execPath, ['server.js'], { cwd: siteDir, env: { ...process.env, PORT: String(port) } });
  for (let i = 0; i < 50; i++) {
    try { await get('/'); return; } catch { await new Promise(r => setTimeout(r, 100)); }
  }
  throw new Error('server did not start');
});
after(() => server?.kill());

test('serves the home page', async () => {
  assert.equal((await get('/')).status, 200);
});

test('malformed percent-encoding does not crash the server', async () => {
  for (const bad of ['/%E0%A4%A', '/%', '/api/v1/sectors/%E0%A4%A']) {
    const res = await get(bad);
    assert.ok([200, 400].includes(res.status), `${bad} -> ${res.status}`);
  }
  assert.equal((await get('/')).status, 200, 'server still up after bad requests');
});

test('path traversal cannot leave public/', async () => {
  for (const bad of ['/../server.js', '/%2e%2e/server.js', '/..%2fserver.js', '/../public-x/secret']) {
    const res = await get(bad);
    assert.ok(!res.body.includes("import http from 'node:http'"), `${bad} leaked server.js`);
  }
});

test('API returns JSON for a known sector and 404 for an unknown one', async () => {
  const list = JSON.parse((await get('/api/v1/sectors')).body);
  assert.ok(list.sectors.length === 20);
  assert.equal((await get(`/api/v1/sectors/${list.sectors[0].slug}`)).status, 200);
  assert.equal((await get('/api/v1/sectors/no-such-sector')).status, 404);
});

test('published sector text has no blank citations', async () => {
  const data = JSON.parse((await get('/data.json')).body);
  for (const s of data.sectors) {
    assert.ok(!/\(\s*\)/.test(s.bottomLine), `${s.slug} has an empty ()`);
    assert.ok(!/The {2}/.test(s.bottomLine), `${s.slug} has a dropped source name`);
  }
});
