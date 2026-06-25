# Phase II — Kepler Scaling Experiment: Pre-Registration SKETCH

| Field | Value |
|-------|-------|
| **Status** | **DRAFT SKETCH — not sealed.** A *new, separately pre-registered* experiment (Phase-I stopping rule P-8). It does **not** reopen or amend sealed Phase I (v3 is terminal; no v4). Requires full owner sign-off + sealing before any Kepler data is read. |
| **Date** | 2026-06-25 |
| **Author** | Ansul Suryawanshi |
| **Relation to Phase I** | Phase I (TESS) falsified H1's *compute* branch (E2: 24.4% < 30%) while *supporting* recall non-inferiority. This experiment tests the **mechanistic explanation** for that failure — that the compute advantage is a function of search-space size, which TESS under-powers. |

> Disclosed as distinct from Phase I per P-8. The Phase-I result stands unchanged. This sketch lays out the hypothesis, design, endpoints, and the anti-tuning discipline; it is a skeleton for refinement, not a sealed protocol.

---

## 1. Motivation & the corrected scaling claim

Per trial period, the evidence-first fast lane folds **k detected events**; full TLS folds **N data points**. Because **k ≪ N**, the fast-lane cost per period (~$B\cdot k$ including the bootstrap) is a small fraction of TLS's (~$N\cdot n_D$). As the observation baseline grows, the number of trial periods $n_P$ grows for **both** arms, so TLS's absolute cost ($n_P\cdot N\cdot n_D$) explodes while the fast lane ($n_P\cdot B\cdot k$) grows far more slowly.

**Therefore the compute advantage should grow with search-space size.** TESS's 27-day baseline gives a small $n_P$, so the advantage is small (Phase I, 24.4%). Kepler's **~4-year continuous baseline** gives a much larger $n_P$ on dense, real-red-noise data — the regime where the advantage should appear, on data that **exists today**.

**Important corrections carried from the Phase-I post-mortem (do not repeat the loose versions):**
- The fast-lane overhead is **not** baseline-independent — the bootstrap re-runs `best_period` over a baseline-scaled grid (verified in `period_recovery.period_fap`). The advantage comes from **k ≪ N**, not from a "fixed" overhead.
- LSST is **out of scope** — its sparse, irregular, multi-band sampling is a *different* detection problem. Kepler (dense, continuous, long baseline) is the correct proving ground; PLATO/Roman are the future analogues.
- This is a **hypothesis to test**, not a claim to assert (Phase-I NN#4). A negative result here (advantage does *not* scale as predicted) is a valid, reportable outcome.

## 2. Hypotheses

- **H1ᴋ (primary, scaling):** the *scoped* compute reduction of evidence-first routing vs full TLS **increases monotonically with the search-space size** (baseline / $n_P$), and at the full ~4-year Kepler baseline **exceeds the TESS Phase-I value (24.4%)** by a pre-registered margin.
- **H2ᴋ (recall, carried):** recall non-inferiority is preserved (one-sided 95% lower bound on occurrence-weighted $\overline{\Delta R}$ ≥ −2 pp), as in Phase I.
- **H0:** the reduction does not grow with baseline (flat or non-monotonic), or recall non-inferiority fails → the scaling explanation is falsified.

## 3. Design (mirrors Phase-I discipline: design-by-theory, threshold-by-calibration, one sealed read)

- **Data.** Kepler DR25 long-cadence (or short-cadence for a subsample), ~4-year baseline, FGK dwarfs; injection–recovery into **real** conditioned light curves (preserve red noise). Leakage-safe calibration/test split, hash-sealed (Seal-1 analogue) before conditioning.
- **Pipeline.** The **identical v3 architecture** (detector → period-from-spacing → B-bootstrap period-FAP → transit-LR confirmer → full-TLS fallback). Statistic *forms* fixed from theory before calibration.
- **Thresholds.** **Re-calibrated on the Kepler calibration split** (different cadence/noise → TESS thresholds do not transfer), then sealed. One test read. (This re-calibration is *not* tuning — it is the same threshold-by-calibration step Phase I used; thresholds are set to a pre-stated FAR, never selected by outcome.)
- **The scaling measurement (the headline).** Run the **same** test injections at **truncated baselines** — e.g. {1 quarter, 1 year, 2 years, 4 years} — and measure the scoped compute ratio at each. The primary deliverable is the **reduction-vs-baseline curve**.
- **Primary endpoint isolation.** To test the *scaling* cleanly and avoid the Lever-3 confound (no-evidence stars dominating the population budget), the **primary E2ᴋ is the per-fast-path-eligible-star compute ratio** (fast lane vs full TLS), as a function of baseline. Population/survey-representative compute is a secondary endpoint (and is expected to remain fallback-limited until Lever 3).

## 4. Anti-tuning (same as Phase I)
Thresholds sealed on calibration before the test read; **one** test evaluation; pre-committed E1/E2/scaling-verdict mapping; seal-hash verification; `git diff` against the sealed tag must be empty. The bootstrap B is carried at the Phase-I value (B=1000) unless a *separately justified, pre-registered* reduction is argued (reducing B to widen the win would be tuning unless equivalence-gated).

## 5. Explicit scope boundaries
- **Lever 3 (calibrated clean-skip)** — a *separate* experiment; not bundled here (it would confound the scaling test and carries its own recall risk).
- **Cross-domain generalization** — separate; if pursued, against correct incumbents in a genuinely periodic-search domain.
- **Monotransit** — out of scope (as in Phase I).

## 6. Risks
- **R-1:** Kepler systematics/red noise differ from TESS → re-calibration may shift thresholds; the bootstrap may behave differently. Mitigated by full re-calibration + the same equivalence discipline.
- **R-2:** the per-star scaling win may be real yet the *population* compute still fallback-limited (Lever-3 territory) → report scoped vs population separately; do not conflate.
- **R-3:** `best_period` inside the bootstrap scales with baseline → confirm the fast-lane cost model empirically as part of the scaling curve (it is itself a measured output, not assumed).
- **R-4:** another large compute campaign (Kepler is bigger than TESS) → plan compute budget + checkpointing up front.

## 7. Decisions for owner sign-off (before drafting the full pre-registration)
| # | Decision |
|---|----------|
| D1 | Cadence: long-cadence (cheaper, more targets) vs short-cadence subsample vs both. |
| D2 | Target sample + size; FGK selection; calibration/test split fraction. |
| D3 | Baseline-truncation set for the scaling curve (e.g. {0.25, 1, 2, 4} yr). |
| D4 | Pre-registered margin for H1ᴋ ("exceeds TESS 24.4% by ≥ X pp" and/or "monotone increasing"). |
| D5 | Compute budget / hardware (Kepler campaign is larger than TESS's 3-day run). |

## 8. Next step
On owner sign-off of §7, promote this sketch to a full Phase-II pre-registration (hypotheses, frozen parameters, endpoints, sealing plan) — mirroring `SCIENTIFIC_HYPOTHESIS.md` / `TRINETRA_X_PHASE1_VALIDATION.md` — then build M0-analogue (manifest + split) and proceed milestone-by-milestone. **Nothing is sealed or run until that pre-registration is signed.**

---

*Phase-II Kepler scaling experiment — pre-registration SKETCH, 2026-06-25. A new experiment (P-8); Phase I remains sealed and final. Tests whether the evidence-first compute advantage scales with search-space size, on the dense long-baseline dataset (Kepler) that TESS could not provide.*
