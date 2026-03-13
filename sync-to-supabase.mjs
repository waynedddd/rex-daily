#!/usr/bin/env node
// Sync issues.json and inspire.json to Supabase
// Usage: node sync-to-supabase.mjs [issues|inspire|all]

import { readFile } from 'fs/promises';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dir = dirname(fileURLToPath(import.meta.url));
const SUPABASE_URL = 'https://yzfvfafmlxdnqdgyaude.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6ZnZmYWZtbHhkbnFkZ3lhdWRlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MzI0ODUzNCwiZXhwIjoyMDg4ODI0NTM0fQ.he1eEpiWY37xHupNqVVrrUm0JjERdXzbL2M-tQDmoEE';

const headers = {
  'apikey': SUPABASE_KEY,
  'Authorization': `Bearer ${SUPABASE_KEY}`,
  'Content-Type': 'application/json',
  'Prefer': 'return=minimal',
};

async function rpc(method, path, body, extraHeaders = {}) {
  const res = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
    method,
    headers: { ...headers, ...extraHeaders },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${method} ${path} → ${res.status}: ${text}`);
  }
  return res;
}

// ── Issues (daily_briefs) ──
async function syncIssues() {
  const raw = JSON.parse(await readFile(join(__dir, 'issues.json'), 'utf8'));

  // Deduplicate: keep last occurrence of each (date, section)
  const seen = new Map();
  for (const item of raw) {
    seen.set(`${item.date}|${item.section}`, item);
  }

  const rows = [...seen.values()].map(i => ({
    date: i.date,
    section: i.section,
    title_zh: i.title?.zh || null,
    title_en: i.title?.en || null,
    content_zh: i.content?.zh || null,
    content_en: i.content?.en || null,
    cover: i.cover || null,
    sources: i.sources || [],
  }));

  // Upsert with conflict on (date, section)
  await rpc('POST', 'daily_briefs?on_conflict=date,section', rows, {
    'Prefer': 'return=minimal,resolution=merge-duplicates',
  });
  console.log(`✅ daily_briefs: upserted ${rows.length} rows`);
}

// ── Inspire ──
async function syncInspire() {
  const raw = JSON.parse(await readFile(join(__dir, 'inspire.json'), 'utf8'));

  // Directions → upsert
  if (raw.directions?.length) {
    const dirRows = raw.directions.map(d => ({
      id: d.id,
      name: d.name,
      name_en: d.name_en || null,
      label: d.label || null,
      color: d.color || null,
      stats: d.stats || [],
    }));
    await rpc('POST', 'inspiration_directions?on_conflict=id', dirRows, {
      'Prefer': 'return=minimal,resolution=merge-duplicates',
    });
    console.log(`✅ inspiration_directions: upserted ${dirRows.length} rows`);
  }

  // Pins → delete current dates then insert
  if (raw.pins?.length) {
    // Collect unique dates
    const dates = [...new Set(raw.pins.map(p => p.date))];
    for (const date of dates) {
      await rpc('DELETE', `daily_inspirations?date=eq.${date}`, null);
    }

    const pinRows = raw.pins.map(p => ({
      date: p.date,
      direction: p.direction || null,
      type: p.type || null,
      title: p.title || (p.body ? p.body.slice(0, 80) : null),
      body_zh: p.body || null,
      body_en: p.body_en || null,
      tags: p.tags || [],
      link: p.link || null,
      link_text: p.linkText || null,
      image: p.image || null,
    }));
    await rpc('POST', 'daily_inspirations', pinRows, {
      'Prefer': 'return=minimal',
    });
    console.log(`✅ daily_inspirations: inserted ${pinRows.length} pins (dates: ${dates.join(', ')})`);
  }
}

// ── Main ──
const target = process.argv[2] || 'all';
try {
  if (target === 'all' || target === 'issues') await syncIssues();
  if (target === 'all' || target === 'inspire') await syncInspire();
  console.log('🎉 Sync complete');
} catch (e) {
  console.error('❌ Sync failed:', e.message);
  process.exit(1);
}
