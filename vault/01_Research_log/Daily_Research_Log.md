# Daily Research Log

---

## 2026-06-15 — Phase I pre-registration completed and sealed (v2)

Worked On:
- Full readiness review of the reconstructed repository + vault → produced docs/PHASE1_READINESS_REPORT.md.
- Resolved the four pre-registration blockers and folded in the four should-fix items, then re-registered to v2 and sealed.

Discoveries / Decisions:
- **F1 decision (DR-001):** scope the Phase I compute claim to the fast-path-eligible population; report survey-representative compute as a pre-registered secondary endpoint (with detector overhead ρ_d and break-even prevalence π* = ρ_d/f_p); defer clean-skip routing to Phase II. Adopted with three guardrails (eligibility frozen on calibration; ρ_d measured; π̂ pre-registered + frontier reported).
- Key insight: at TESS-realistic prevalence π ~ 10⁻², survey-scale saving ≈ π·f_p − ρ_d is near zero/negative by construction — so a near-zero E3 is an *expected, honest* result, not a failure. This is what motivates the Phase II clean-skip tier.
- F2: operational recovery predicate pinned (period 1% / harmonics m∈{2,3} flagged · epoch ±0.5 T₁₄ · SDE ≥ T), applied identically to both arms.
- F6: single occurrence-weighted primary estimand ΔR̄ with log-uniform period prior × Kunimoto & Matthews (2020) radius occurrence; per-cell results secondary (Holm) and never gating.
- F8: TLS baseline, thresholds/targets, and runtime protocol pinned in Validation Appendix A; numeric thresholds correctly deferred to M3 (calibration-derived), sealed before M4.
- R-4: committed circular block-bootstrap FAP scheme (L_b = 3·max(τ_GP, T₁₄), B ≥ 1000) — closes the red-noise exchangeability gap.
- R-5: transit-preservation requirement (median η = δ_post/δ_true ≥ 0.90) as a required pre-M3 check.
- R-6: single-planet + strict-periodicity scope stated explicitly; "model-agnostic" claim scoped to event detection only.
- R-7: monotransit single-event vetting criterion (shape, ingress/egress, no secondary, centroid); weaker FP control acknowledged; excluded from headline.

Artifacts created/updated:
- Re-registered: SCIENTIFIC_HYPOTHESIS.md v2.0, TRINETRA_X_PHASE1_VALIDATION.md v2, TRINETRA_MATHEMATICAL_FOUNDATIONS.md v1.1.
- Created: docs/decisions/F1_DECISION_RECORD.md (DR-001), docs/PHASE1_READINESS_REPORT.md.
- Seal: commit 723087e, annotated tag `phase1-prereg-v2`; content hashes verified against the tagged tree.

Problems / Risks carried forward:
- Top residual risk remains F1/PR-A external validity — mitigated but the scoped claim only holds if ρ_d is genuinely small; must be measured at M3/M4.
- Other live risks (tracked in readiness report §6): seed-accuracy collapse under red noise (the v3 failure mode, a real possible null), bootstrap exchangeability under red noise (mitigated by R-4), conditioning recall cost (R-5), straw-man-baseline avoidance (F8), underpowered cells.

Next Action:
- Begin M0: freeze the TESS sector/target manifest + leakage-safe calibration/test split (first data-touching step). Data must not be read before M0 begins under the sealed protocol.
- Non-blocking: create references.bib; add Phase-I scoping note to the charter.

---

## Template for future entries

Date:

Worked On:

Discoveries:

Questions:

Problems:

Next Action:
