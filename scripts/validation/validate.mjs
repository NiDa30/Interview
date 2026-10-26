#!/usr/bin/env node
// Repository content checks for BRSE Interview Master.
//
//   node scripts/validation/validate.mjs            # schema, cross-references, lesson structure, links
//   node scripts/validation/validate.mjs --render   # also render every Mermaid block with mermaid-cli
//
// Exit code 1 when any error is found. Warnings do not fail the run.

import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const rel = (p) => path.relative(ROOT, p).split(path.sep).join("/");
const abs = (p) => path.join(ROOT, p);
const read = (p) => fs.readFileSync(abs(p), "utf8");

const errors = [];
const warnings = [];
const err = (where, msg) => errors.push(`${where}: ${msg}`);
const warn = (where, msg) => warnings.push(`${where}: ${msg}`);

const EVIDENCE = ["verified", "needs-verification", "author-experience—unverified", "hypothetical"];
const REVIEW = ["draft", "reviewed", "approved"];
const DIFFICULTY = ["basic", "intermediate", "advanced"];
const CATEGORY = [
  "HR & Motivation", "CV & Experience", "Programming", "Web & API", "Frontend & Backend", "Database",
  "Architecture", "Cloud", "DevOps", "Testing", "Requirements", "BrSE Communication",
  "Project Management", "Technical Demo", "Troubleshooting",
];
const VISUAL_TYPE = ["architecture", "sequence", "er", "class", "flowchart", "decision-tree", "comparison", "state", "illustration"];
const PROJECT_STATUS = ["As Implemented", "As Tested", "Proposed Design", "Production Verified", "Not project-specific"];
const VALIDATION = ["pending_visual_review", "rendered", "visual_reviewed"];
const LESSON_SECTIONS = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "出典"];
const SECONDS_PER_CHAR = 1 / 5; // rough speaking rate for the length warning
const MAX_SECONDS = 35;

const norm = (s) => s.replace(/\s+/g, "");

function walk(dir, pred, out = []) {
  for (const e of fs.readdirSync(abs(dir), { withFileTypes: true })) {
    const p = `${dir}/${e.name}`;
    if (e.isDirectory()) walk(p, pred, out);
    else if (pred(p)) out.push(p);
  }
  return out;
}

const lessonFiles = walk("book/chapters", (p) => /\/\d\d-\d\d-[^/]+\.md$/.test(p));

function mermaidBlocks(file) {
  const blocks = [];
  let cur = null;
  for (const line of read(file).split("\n")) {
    if (cur === null && line.startsWith("```mermaid")) cur = [];
    else if (cur !== null && line.startsWith("```")) { blocks.push(cur.join("\n")); cur = null; }
    else if (cur !== null) cur.push(line);
  }
  return blocks;
}
const blockTitle = (b) => (b.match(/^\s*title:?\s+(.+)$/m) || [])[1]?.trim() ?? null;

function requireFields(where, obj, fields) {
  for (const f of fields) if (!(f in obj)) err(where, `missing field "${f}"`);
}
function checkEnum(where, field, value, allowed) {
  if (!allowed.includes(value)) err(where, `${field} "${value}" not in [${allowed.join(", ")}]`);
}

// ---------- question bank ----------
function checkQuestionBank() {
  const file = "data/question-bank.json";
  let data;
  try { data = JSON.parse(read(file)); } catch (e) { return err(file, `invalid JSON: ${e.message}`); }
  const qs = data.questions ?? [];
  const ids = new Set();
  for (const q of qs) {
    const where = `${file} [${q.question_id ?? "?"}]`;
    requireFields(where, q, [
      "question_id", "chapter_id", "lesson_id", "lesson_path", "category", "difficulty",
      "japanese_question", "vietnamese_translation", "interviewer_intent", "required_knowledge",
      "answer_framework", "answer_type", "standard_answer", "professional_answer", "follow_up_questions",
      "variant_of", "vocabulary", "grammar", "related_scenarios", "source_references",
      "evidence_status", "review_status",
    ]);
    if (ids.has(q.question_id)) err(where, "duplicate question_id");
    ids.add(q.question_id);
    checkEnum(where, "category", q.category, CATEGORY);
    checkEnum(where, "difficulty", q.difficulty, DIFFICULTY);
    checkEnum(where, "evidence_status", q.evidence_status, EVIDENCE);
    checkEnum(where, "review_status", q.review_status, REVIEW);
    checkEnum(where, "answer_type", q.answer_type, ["model-answer", "fill-in-frame"]);
    if (q.answer_type === "model-answer" && !q.standard_answer) err(where, "model-answer without standard_answer");
    if (q.answer_type === "fill-in-frame" && q.standard_answer) err(where, "fill-in-frame must not carry a standard_answer");

    if (!fs.existsSync(abs(q.lesson_path))) { err(where, `lesson_path not found: ${q.lesson_path}`); continue; }
    const m = q.lesson_path.match(/(\d\d)-(\d\d)-/);
    if (!m || `${m[1]}.${m[2]}` !== q.lesson_id) err(where, `lesson_id ${q.lesson_id} does not match ${q.lesson_path}`);
    if (m && Number(m[1]) !== q.chapter_id) err(where, `chapter_id ${q.chapter_id} does not match ${q.lesson_path}`);

    const lesson = norm(read(q.lesson_path));
    if (!lesson.includes(norm(q.japanese_question))) err(where, "japanese_question not found verbatim in lesson");
    for (const k of ["standard_answer", "professional_answer"]) {
      if (q[k] && !lesson.includes(norm(q[k]))) err(where, `${k} differs from the lesson text — re-sync it`);
    }
    for (const r of q.source_references ?? []) {
      if (!/^https?:\/\//.test(r) && !fs.existsSync(abs(r))) err(where, `source reference not found: ${r}`);
    }
  }
  for (const q of qs) {
    const where = `${file} [${q.question_id}]`;
    for (const f of q.follow_up_questions ?? []) if (!ids.has(f)) err(where, `follow_up_questions references unknown ${f}`);
    if (q.variant_of && !ids.has(q.variant_of)) err(where, `variant_of references unknown ${q.variant_of}`);
  }
  return qs.length;
}

// ---------- visual manifest ----------
function checkVisualManifest() {
  const file = "data/visual-manifest.json";
  let data;
  try { data = JSON.parse(read(file)); } catch (e) { return err(file, `invalid JSON: ${e.message}`); }
  const assets = data.assets ?? [];
  const ids = new Set();
  const covered = new Set();
  for (const v of assets) {
    const where = `${file} [${v.visual_id ?? "?"}]`;
    requireFields(where, v, [
      "visual_id", "chapter_id", "lesson_id", "title", "visual_type", "source_path", "exported_path",
      "alt_text", "learning_objective", "source_references", "project_status", "validation_status",
    ]);
    if (ids.has(v.visual_id)) err(where, "duplicate visual_id");
    ids.add(v.visual_id);
    checkEnum(where, "visual_type", v.visual_type, VISUAL_TYPE);
    checkEnum(where, "validation_status", v.validation_status, VALIDATION);
    if (!Array.isArray(v.project_status) || v.project_status.length === 0) err(where, "project_status must be a non-empty array");
    else for (const s of v.project_status) checkEnum(where, "project_status", s, PROJECT_STATUS);
    if (!v.alt_text?.trim()) err(where, "empty alt_text");
    if (v.exported_path && !fs.existsSync(abs(v.exported_path))) err(where, `exported_path not found: ${v.exported_path}`);

    const [p, frag] = String(v.source_path).split("#");
    if (!fs.existsSync(abs(p))) { err(where, `source_path not found: ${p}`); continue; }
    const n = Number((frag ?? "").replace("mermaid-", ""));
    const blocks = mermaidBlocks(p);
    if (!n || n > blocks.length) { err(where, `${v.source_path}: lesson has ${blocks.length} mermaid block(s)`); continue; }
    covered.add(`${p}#${n}`);
    const t = blockTitle(blocks[n - 1]);
    if (t !== v.title) err(where, `title "${v.title}" differs from diagram title "${t}"`);
  }
  for (const f of lessonFiles) {
    mermaidBlocks(f).forEach((b, i) => {
      if (!covered.has(`${f}#${i + 1}`)) err(f, `mermaid block ${i + 1} has no entry in ${file}`);
      if (!blockTitle(b)) err(f, `mermaid block ${i + 1} has no title`);
    });
  }
  return assets.length;
}

// ---------- lessons ----------
function checkLessons() {
  for (const f of lessonFiles) {
    const src = read(f);
    const lines = src.split("\n");
    for (const s of LESSON_SECTIONS) {
      if (!lines.some((l) => l.startsWith(`## ${s}`))) err(f, `missing section "## ${s} …"`);
    }
    if (!/\*\*Trạng thái:\*\*/.test(src)) err(f, "header has no **Trạng thái:**");
    if (!/\*\*Cập nhật:\*\*\s*\d{4}-\d{2}-\d{2}/.test(src)) err(f, "header has no **Cập nhật:** YYYY-MM-DD");

    for (const [, tok] of src.matchAll(/`([a-z—-]*(?:verif|hypoth|unverif)[a-z—-]*)`/g)) {
      if (!EVIDENCE.includes(tok)) warn(f, `unknown evidence status \`${tok}\``);
    }

    lines.forEach((l, i) => {
      const m = l.match(/^\*\*応募者[^*]*\*\*[:：]?\s*(.+)$/);
      if (!m || !/[ぁ-ん]/.test(m[1]) || m[1].includes("【")) return;
      const chars = m[1].replace(/[A-Za-z0-9 ./\-]+/g, "xx").replace(/[「」*]/g, "").length;
      const sec = Math.round(chars * SECONDS_PER_CHAR);
      const longForm = /Professional|60/.test(lines.slice(Math.max(0, i - 12), i).join("\n"));
      if (sec > MAX_SECONDS && !longForm) warn(`${f}:${i + 1}`, `answer ≈${sec}s (target 15–30s)`);
    });
  }
  return lessonFiles.length;
}

// ---------- links ----------
function checkLinks() {
  const files = [
    "README.md", "AGENTS.md",
    ...walk("docs", (p) => p.endsWith(".md")),
    ...walk("book/chapters", (p) => p.endsWith(".md")),
    ...walk("knowledge-base", (p) => p.endsWith(".md")),
    ...walk("sources", (p) => p.endsWith(".md") && !p.includes("/_private/")),
  ];
  for (const f of files) {
    const dir = path.posix.dirname(f);
    for (const [, target] of read(f).matchAll(/\]\(([^)\s]+)\)/g)) {
      if (/^(https?:|mailto:|#)/.test(target) || target.includes("{{")) continue;
      const p = path.posix.normalize(`${dir}/${decodeURI(target.split("#")[0])}`);
      if (!fs.existsSync(abs(p))) err(f, `broken link → ${target}`);
    }
  }
}

// ---------- optional render ----------
function findBrowser() {
  if (process.env.PUPPETEER_EXECUTABLE_PATH) return process.env.PUPPETEER_EXECUTABLE_PATH;
  const candidates = [
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  ];
  return candidates.find((c) => fs.existsSync(c)) ?? null; // null → let puppeteer use its own download
}

function renderAll() {
  // Call the CLI script with node directly: .cmd shims break on paths with spaces.
  const mmdc = abs("node_modules/@mermaid-js/mermaid-cli/src/cli.js");
  if (!fs.existsSync(mmdc)) return err("render", "mermaid-cli not installed — run npm install");
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "brse-mermaid-"));
  const browser = findBrowser();
  const args = [];
  if (browser) {
    const cfg = path.join(tmp, "puppeteer.json");
    fs.writeFileSync(cfg, JSON.stringify({ executablePath: browser, headless: "new" }));
    args.push("-p", cfg);
  }
  let n = 0;
  for (const f of lessonFiles) {
    mermaidBlocks(f).forEach((b, i) => {
      const input = path.join(tmp, `d${n}.mmd`);
      fs.writeFileSync(input, b);
      try {
        execFileSync(process.execPath, [mmdc, "-q", ...args, "-i", input, "-o", path.join(tmp, `d${n}.svg`)], { stdio: "pipe" });
      } catch (e) {
        err(`${f} mermaid ${i + 1}`, `render failed: ${String(e.stderr || e.message).split("\n").find((l) => l.trim()) ?? "unknown error"}`);
      }
      n++;
    });
  }
  fs.rmSync(tmp, { recursive: true, force: true });
  return n;
}

// ---------- run ----------
const nq = checkQuestionBank();
const nv = checkVisualManifest();
const nl = checkLessons();
checkLinks();
const nr = process.argv.includes("--render") ? renderAll() : null;

for (const w of warnings) console.log(`WARN  ${w}`);
for (const e of errors) console.log(`ERROR ${e}`);
console.log(
  `\nlessons: ${nl} · questions: ${nq} · visuals: ${nv}` +
  (nr === null ? " · render: skipped (use --render)" : ` · rendered: ${nr}`) +
  ` · ${errors.length} error(s), ${warnings.length} warning(s)`,
);
process.exit(errors.length ? 1 : 0);
