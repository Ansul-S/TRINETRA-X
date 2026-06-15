# Current Mission

Project:
TRINETRA-X

Current Phase:
Phase I — Scientific Validation

Current Goal:
Determine whether evidence-first routing can reduce computational cost while preserving recall.

Current Status:
- Pre-registration **v2 SEALED** — git tag `phase1-prereg-v2` (commit `723087e`), pushed to GitHub.
- Decision **DR-001** recorded (F1 compute-scope decision).
- **No remaining Critical, Must-fix, or Should-fix findings.** (F1, F2, F6, F8 resolved; R-4, R-5, R-6, R-7 folded into v2.)
- **M0 EXECUTED (2026-06-15).** Seal #1 (manifest hash) `1f2d49e1…` cut; 22,723 SPOC 2-min targets (S1–S3 south); leakage-safe 30/70 split; TEST set sealed (read once at M4). M0.5 feasibility passed — no sector widening needed.

Current Milestone:
**M2 — Injection + transit-preservation — DONE / SIGNED OFF (2026-06-16).** Detrend window **finalized at 2.5 d** (from 0.5 d provisional); full η grid (30 cells × 200 inj) **gate PASS** on the measurable population (Rₚ≥2, η≥0.90). **Rₚ=1 (Earth) row excluded as noise-limited** (SNR₁~0.07, below the conditioning floor — the detectability bimodality); **0.5/2 documented borderline** (η=0.892). (M1 η-sample done; M0 Seal #1 `1f2d49e1…`.)

Next Milestone:
**M3 — Threshold calibration** on the CALIBRATION set → derive + hash-seal `z⋆, θ, z_mono, T, α, α_FAP, ε, τ_GP` (**Seal #2**; VAL A.10), before the single M4 test run. Not started.

⚠ **M3 prerequisite:** recompute the M1 noise model (σ/CDPP/τ_GP) at the finalized **2.5 d** window — the 0.5 d η-sample model is superseded.

Next Action:
M2 done + signed off (PR #4 to open). **Begin M3 — threshold calibration** on the CALIBRATION set: first recompute the M1 noise model at the finalized 2.5 d window, then derive `z⋆, θ, z_mono, T, α, α_FAP, ε, τ_GP` on calibration null/injection data and **hash-seal them (Seal #2)** before the single M4 test run. TEST stays sealed until M4. M3 involves frozen-parameter choices (FAR/FAP targets, routing rule) → bring for sign-off before sealing, per the established pattern.

Execution Plan:
`PHASE1_EXECUTION_PLAN.md` (v0.1, M0 increment — M0 executed). Tooling: `research/m0_manifest/`. Manifest + provenance: `data/manifests/m0/`.

Sealed Documents (do not edit without a new re-registration):
- SCIENTIFIC_HYPOTHESIS.md — v2.0
- TRINETRA_X_PHASE1_VALIDATION.md — v2 (incl. Appendix A: frozen parameters)
- TRINETRA_MATHEMATICAL_FOUNDATIONS.md — v1.1

Decision Record:
docs/decisions/F1_DECISION_RECORD.md (DR-001)

GitHub:
origin = https://github.com/Ansul-S/TRINETRA-X — main and tag `phase1-prereg-v2` pushed.

Anti-tuning status:
M0 read **catalog metadata only** (no flux). TEST split **sealed at M0** (read once at M4). **Seal #2** (calibration threshold manifest hash) happens at M3, before the single M4 run. Sealed prereg docs verified byte-identical to `phase1-prereg-v2`.

Non-blocking follow-ons (do not affect sealed hashes):
- Create references.bib (Kunimoto & Matthews 2020 is load-bearing)
- Add the one-line Phase-I scoping note to the charter (docs/TRINETRA-X.md)
