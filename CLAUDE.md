# CLAUDE.md — TRINETRA-X Operating Rules

> Project rules for any Claude Code session in this repository. Read this first. Keep edits to this file under ~200 lines.

## What this project is

TRINETRA-X is an **evidence-first** exoplanet-detection research program for the **TESS** era (ISRO exoplanet challenge). It tests whether *routing on evidence* — detect transit-like events cheaply, infer the period from their spacing, confirm with physics, and run a full search only where no evidence exists — can cut compute without sacrificing recall. Authoritative charter: [`docs/TRINETRA-X.md`](./docs/TRINETRA-X.md).

**Current phase: Phase I — Scientific Validation.** Goal: prove (or falsify) that evidence-first routing beats full TLS on TESS. We are *validating a principle*, not building a product.

## Session Initialization Rule

Do not assume prior chat history exists.

All project knowledge must be derived from repository documents.

If information is missing from the repository, explicitly identify the gap rather than assuming historical context.

## Knowledge Management

Repository documents are authoritative.

Obsidian is the long-term research memory system.

Important discoveries must be written into repository documents and/or Obsidian notes.

No critical project knowledge should remain only inside chat history.

Chats are temporary.

Documents are memory.

## Obsidian Vault

A project Obsidian vault exists at:

vault/

Purpose:

- Long-term research memory
- Literature notes
- Discovery tracking
- Experiment logs
- Publication planning

Repository documents remain authoritative.

Obsidian notes are working research notes and knowledge-management artifacts.

When a significant discovery, benchmark result, mathematical insight, experimental lesson, or publication idea emerges, recommend recording it in the appropriate vault note.

Do not treat Obsidian notes as authoritative specifications unless explicitly promoted into repository documentation.

### Vault synchronization (after major project-state changes)

After any major change to project state — a resolved finding, a decision record, a re-registration, a seal/tag, a milestone start or completion, or a GitHub publish — **synchronize the vault in the same session**:

1. `vault/00_Home/Current_Mission.md` — current status, blockers, current + next milestone, next action.
2. `vault/00_Home/Dashboard.md` — phase, milestone ladder, completion checklist, document list.
3. `vault/01_Research_log/Daily_Research_Log.md` — append a dated entry (decisions, artifacts, risks, next action).
4. On session end, create `SESSION_HANDOFF_<YYYY-MM-DD>.md` so a fresh session can resume with zero reliance on chat history.

The vault must never contradict the repository. The repository is authoritative; the vault mirrors it. Convert relative dates to absolute.

## Prime directive

> **Find evidence first. Spend computation second. Let physics decide.**
> A false positive is acceptable; a missed planet is not. **Photometric significance — depth, shape, repetition — not timing coincidence — is what makes a candidate a planet.** (This is the corrected lesson of the prior version; see [`docs/TRINETRA_CONCEPT_RECONSTRUCTION.md`](./docs/TRINETRA_CONCEPT_RECONSTRUCTION.md) §E.)

## Non-negotiables (do not violate)

1. **Recall > precision.** Never trade away a real planet to improve precision.
2. **No tuning on test data.** Thresholds are set on the calibration set, then sealed. One evaluation on the test set.
3. **Physics decides detection.** The confirmation gate (transit-model significance), not a coherence score, is the arbiter.
4. **Benchmark everything.** Every claim is measured against full TLS on identical data.
5. **Calibrate every confidence.** No uncalibrated scores; period FAP is bootstrap-calibrated, probabilities are conformal.
6. **Reproducible by construction.** Frozen manifests, seeds, versions; provenance carried end-to-end.
7. **Evidence overrides assumptions; physics overrides heuristics; recall over elegance.**

## Working agreement for agents

- **Do not build prematurely.** Phase I has **no learned models, no dashboards, no deployment**. Phase I uses a *simple, untrained* detector on purpose, so a pass/fail is attributable to the routing *principle*, not a model.
- **Pre-registration discipline.** [`docs/TRINETRA_X_PHASE1_VALIDATION.md`](./docs/TRINETRA_X_PHASE1_VALIDATION.md) and [`docs/SCIENTIFIC_HYPOTHESIS.md`](./docs/SCIENTIFIC_HYPOTHESIS.md) freeze the experiment. **Changing a frozen parameter after data is touched is forbidden.** Amendments made *before* data is read are legitimate but must be **re-dated** as a new pre-registration version.
- **Documents are the current deliverables.** No project source code has been written yet. Prefer Markdown docs with LaTeX math (`$…$`); they render in math-aware viewers.
- **Negative results are results.** A clean falsification of the hypothesis is a successful Phase I, to be reported with equal rigor.
- **Ask before scope expansion.** If a task implies building Phase II machinery (learned detector, classifier, habitability), confirm first.

## Document map (canonical sources)

| Document | Role |
|----------|------|
| [`docs/TRINETRA-X.md`](./docs/TRINETRA-X.md) | Master charter (author: Vesper) |
| [`docs/SCIENTIFIC_HYPOTHESIS.md`](./docs/SCIENTIFIC_HYPOTHESIS.md) | Formal H1/H0 + secondary hypotheses, assumptions, success/failure criteria |
| [`docs/TRINETRA_MATHEMATICAL_FOUNDATIONS.md`](./docs/TRINETRA_MATHEMATICAL_FOUNDATIONS.md) | Canonical theory (math only) |
| [`docs/TRINETRA_X_ARCHITECTURE.md`](./docs/TRINETRA_X_ARCHITECTURE.md) | 7-stage system design (full vision) |
| [`docs/TRINETRA_X_PHASE1_VALIDATION.md`](./docs/TRINETRA_X_PHASE1_VALIDATION.md) | Pre-registered Phase I protocol |
| [`docs/TRINETRA_CONCEPT_RECONSTRUCTION.md`](./docs/TRINETRA_CONCEPT_RECONSTRUCTION.md) | Concept lineage & v3 post-mortem |
| [`docs/PAPER_NOTES.md`](./docs/PAPER_NOTES.md) | Publication notebook |
| [`docs/REPOSITORY_GAP_ANALYSIS.md`](./docs/REPOSITORY_GAP_ANALYSIS.md) | Critical cross-document review (12 findings) |
| [`docs/PHASE1_REMEDIATION.md`](./docs/PHASE1_REMEDIATION.md) | Plan to fix the Critical + Must-fix findings (**resolved** — see DR-001) |
| [`docs/PHASE1_READINESS_REPORT.md`](./docs/PHASE1_READINESS_REPORT.md) | Phase I scientific-readiness assessment |
| [`docs/decisions/F1_DECISION_RECORD.md`](./docs/decisions/F1_DECISION_RECORD.md) | DR-001 — F1 compute-scope decision + seal record |
| [`SESSION_HANDOFF_2026-06-15.md`](./SESSION_HANDOFF_2026-06-15.md) | Latest session handoff (resume point) |
| [`archive/`](./archive/) | Historical (Revival-era audit & review) — context only, not current |

## Directory map

```
docs/        canonical specifications and theory
src/         pipeline stages (empty; no code yet): conditioning, detector,
             period_recovery, confirmation, classifier, evaluation
data/        raw, processed, injections, benchmark (empty)
research/    experiments, benchmarks, validation, literature (empty)
results/     outputs (empty)
notebooks/   exploratory notebooks (empty)
papers/      manuscript drafts (empty)
archive/     prior-project audit & review (reference only)
```

## Current status & immediate next step

- **Pre-registration is SEALED (v2, 2026-06-15).** All four Critical/Must-fix findings (F1, F2, F6, F8) are resolved, and the four should-fix items (R-4, R-5, R-6, R-7) were folded into the same seal. **No Critical, Must-fix, or should-fix findings remain open.** Remaining gap-analysis items are Medium/Low hygiene only.
- **F1 decision:** scoped the compute claim to the fast-path-eligible population; survey-representative compute is a pre-registered *secondary* endpoint (with detector overhead ρ_d and break-even prevalence π\*); clean-skip routing deferred to Phase II. Recorded in [`docs/decisions/F1_DECISION_RECORD.md`](./docs/decisions/F1_DECISION_RECORD.md) (**DR-001**).
- **Sealed documents (do not edit without a new re-registration):** `SCIENTIFIC_HYPOTHESIS.md` v2.0, `TRINETRA_X_PHASE1_VALIDATION.md` v2 (incl. Appendix A), `TRINETRA_MATHEMATICAL_FOUNDATIONS.md` v1.1. Seal = git tag **`phase1-prereg-v2`** (commit `723087e`), pushed to GitHub (`origin` = github.com/Ansul-S/TRINETRA-X). Content hashes recorded in DR-001.
- **No data has been read. Milestone M0 has NOT started.**
- **Immediate next step:** author **`PHASE1_EXECUTION_PLAN.md`**, then begin **M0** — freeze the TESS sector/target manifest and the leakage-safe calibration/test split. M0 is the first data-touching step; calibration-derived thresholds get a second seal (manifest hash) at M3 before the single M4 test run.
- **Non-blocking follow-ons:** create `references.bib` (Kunimoto & Matthews 2020 is now load-bearing); add the one-line Phase-I scoping note to the charter.
- Revival/archive material is reference only. Prefer repository documents over chat summaries when they conflict. GSD Core is installed globally in `~/.claude`; no local `.claude/` overrides.

## Conventions

- One claim → one table → one milestone → one frozen dataset. Keep figure/table indices stable.
- Convert relative dates to absolute. Cite the source document + section for any non-obvious claim.
- Do not modify `archive/` contents; they are historical record.
