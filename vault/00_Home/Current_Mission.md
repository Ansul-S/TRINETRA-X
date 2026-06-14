# Current Mission

Project:
TRINETRA-X

Current Phase:
Phase I — Scientific Validation

Current Goal:
Determine whether evidence-first routing can reduce computational cost while preserving recall.

Status:
Pre-Implementation — **pre-registration v2 SEALED** (2026-06-15). Ready for M0.

Current Blockers:
- None. The four pre-registration blockers (F1, F2, F6, F8) are resolved and sealed.

Current Milestone:
Pre-registration completion + seal — **DONE** (tag `phase1-prereg-v2`).

Next Milestone:
M0 — Freeze the TESS sector/target manifest and the leakage-safe calibration/test split. Not yet started; unblocked.

What changed (2026-06-15):
- **F1 resolved** — compute claim scoped to the fast-path-eligible population; survey-representative compute added as a pre-registered *secondary* endpoint (with detector overhead ρ_d and break-even prevalence π*); clean-skip routing deferred to Phase II. Decision recorded as **DR-001**.
- **F2 resolved** — operational recovery predicate pinned (period 1% / harmonics flagged · epoch ±0.5 T₁₄ · SDE ≥ T).
- **F6 resolved** — single occurrence-weighted primary estimand (log-uniform in P × Kunimoto & Matthews 2020 radius occurrence) + multiplicity rule.
- **F8 resolved** — thresholds, TLS baseline, and runtime protocol pinned (Validation Appendix A); numeric values remain `[sealed at M3]` (calibration-derived).
- **R-4, R-5, R-6, R-7 folded into the same v2 seal** — block-bootstrap FAP scheme; transit-preservation requirement (η ≥ 0.90); single-planet / strict-periodicity scope; monotransit vetting criterion.
- **Re-registration to v2** applied across the three frozen documents.
- **Seal created** — commit `723087e`, annotated tag `phase1-prereg-v2`, content hashes verified.

Frozen document versions (hash-verified):
- SCIENTIFIC_HYPOTHESIS.md — v2.0
- TRINETRA_X_PHASE1_VALIDATION.md — v2
- TRINETRA_MATHEMATICAL_FOUNDATIONS.md — v1.1

Decision record:
docs/decisions/F1_DECISION_RECORD.md (DR-001)

Anti-tuning status:
No data read. Exactly one sealed-test evaluation will follow at M4. Second seal (calibration manifest hash) happens at M3 before the test run.

Non-blocking follow-ons (do not affect sealed hashes):
- Create references.bib (Kunimoto & Matthews 2020 is now load-bearing)
- Add the one-line Phase-I scoping note to the charter (docs/TRINETRA-X.md)
