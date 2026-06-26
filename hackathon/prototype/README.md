# PS7 Prototype — smoke test

Proves the end-to-end path **ahead of the 30-h finale**: the reused TRINETRA-X
spine (untrained detector + period-from-spacing) feeding the **new** physics-feature
extractor (classifier design doc §3), run on **real conditioned TESS light curves**.

## Run
```bash
.venv/bin/python hackathon/prototype/smoke_test.py [N]   # N = #light curves (default 60)
```
Inputs: `data/processed/m1/*.npz` (Phase-I conditioned LCs: `time`, `resid`).
Outputs: `out/smoke_features.csv` (feature table) + `figs/folded_<TIC>.png` (example fold).

## Files
- `features.py` — physics-feature extractor: depth, depth_snr, period, fold_R,
  duration, **odd_even_diff**, **secondary_depth/ratio**, **v_over_u** (V-vs-U shape),
  oot_rms, SNRs. These are the physics-branch inputs to the hybrid classifier.
- `smoke_test.py` — batch driver + example folded-LC figure.

## What the first run showed (2026-06-26)
- 60/60 conditioned LCs processed without error; full feature table produced.
- **TIC 100029948** auto-flagged as an **eclipsing binary** (not a planet): ~23% depth,
  V-shape, out-of-eclipse ellipsoidal modulation — the exact transit-vs-eclipse
  discrimination PS7 grades, emerging directly from the physics features.

## Status / next (build phase)
- This is SMOKE-TEST grade (no labels yet, no TPF/centroid blend features).
- Next: train physics branch (GBT) once the organizer's **curated labeled set** arrives;
  add the CNN folded-view branch + conformal calibration; add pixel-level blend features
  if TPFs are pulled. See `../BAH2026_PS7_CLASSIFIER_DESIGN.md`.
