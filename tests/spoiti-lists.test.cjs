/**
 * Minimal test for the source-backed Mornye package layout.
 */

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const sourceDir = path.join(root, 'sources', 'spoiti-lists');
const registryPath = path.join(root, 'registry.json');

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

test('spoiti-lists source manifest exists and is valid', () => {
  const manifest = readJson(path.join(sourceDir, 'manifest.json'));
  assert.equal(manifest.name, 'spoiti-lists');
  assert.ok(manifest.displayName);
  assert.ok(manifest.version);
  assert.ok(Array.isArray(manifest.settings));
});

test('spoiti-lists source JS exists and registers an extension', () => {
  const file = path.join(sourceDir, 'index.js');
  assert.ok(fs.existsSync(file));
  const body = fs.readFileSync(file, 'utf8');
  assert.ok(body.length > 200);
  assert.match(body, /registerExtension\s*\(/);
});

test('registry contains the Mornye store entry', () => {
  const registry = readJson(registryPath);
  const hasEntry = Array.isArray(registry.extensions) && registry.extensions.some((entry) => entry.id === 'spoiti-lists');
  assert.equal(hasEntry, true);
});
