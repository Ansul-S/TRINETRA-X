"""M0 manifest pipeline — Phase I (scaffold).

Executes milestone M0 of PHASE1_EXECUTION_PLAN.md: freeze the TESS sector/target
manifest and the leakage-safe calibration/test split, then content-hash it (Seal #1).

SCAFFOLD ONLY. Archive-touching bodies raise NotImplementedError until the M0
frozen-choices proposal (PHASE1_M0_CHOICES.md) is signed off and config/m0_config.yaml
is filled. This module is metadata-only by contract:

  * no light-curve flux is downloaded (that is M1);
  * no detection threshold is set (those are M3 / Seal #2);
  * no statistic is computed on the TEST split (plan G1).

Run order (post sign-off):
  python m0_pipeline.py --config config/m0_config.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

# NOTE: heavy imports (astroquery, astropy, healpy, pandas, pyarrow) are deferred
# into the step bodies so `--help` and import work before the stack is installed.


def load_config(config_path: str) -> dict[str, Any]:
    """Load and validate the frozen-choices config.

    Guards: rejects a config that sets training_split=true, or that smuggles in any
    detection-threshold key (z*, theta, T, ...) — those belong to M3, not M0.
    """
    raise NotImplementedError("Implement after sign-off (validates m0_config.yaml).")


def m0_1_freeze_sectors(cfg: dict[str, Any]) -> dict[str, Any]:
    """M0.1 — record the frozen SPOC 2-min sector list + rationale (VAL §3)."""
    raise NotImplementedError


def m0_2_build_target_manifest(cfg: dict[str, Any], sectors: dict[str, Any]) -> Any:
    """M0.2 — enumerate 2-min targets in the frozen sectors and apply the
    outcome-independent inclusion/exclusion cuts; cross-match TIC for coords,
    camera/CCD, R_star + limb-darkening inputs, and per-target baseline. Tag
    multi-planet/TTV systems. Metadata only — no flux. (VAL §3, A.1)."""
    raise NotImplementedError


def m0_3_assemble_labels(cfg: dict[str, Any], targets: Any) -> Any:
    """M0.3 — pin + version TOI (planet) and EB/variable (FP) catalogs in-sector;
    define the null pool as known-host-removed; record incompleteness caveat (VAL §3, A.2; H4)."""
    raise NotImplementedError


def m0_4_leakage_safe_split(cfg: dict[str, Any], targets: Any, labels: Any) -> Any:
    """M0.4 — whole-block (HEALPix or camera/CCD) calibration/test split, TIC-disjoint,
    seeded, NO training split; assign all four sub-samples consistently; run leakage audit
    (zero shared TIC; spatial separation). TEST is sealed here (VAL §3, §7)."""
    raise NotImplementedError


def m0_5_feasibility_check(cfg: dict[str, Any], split: Any) -> Any:
    """M0.5 — from per-target baselines, count hosts reaching n_transits>=2 per (P,R_p)
    cell per split; confirm >=500 injections/cell and §6 power; flag at-risk cells.
    Uses baselines/coordinates only — computes NO detection statistic on TEST (plan G1)."""
    raise NotImplementedError


def m0_6_seal_manifest(cfg: dict[str, Any], *parts: Any) -> str:
    """M0.6 — assemble the frozen manifest (Table T1) + provenance (catalog/tool versions,
    timestamps, seeds), compute SHA-256 (Seal #1), and emit the TEST-set access rule.
    Returns the hash string to record in the plan + research log (VAL §7, A.10)."""
    raise NotImplementedError


def run(config_path: str) -> None:
    cfg = load_config(config_path)
    sectors = m0_1_freeze_sectors(cfg)
    targets = m0_2_build_target_manifest(cfg, sectors)
    labels = m0_3_assemble_labels(cfg, targets)
    split = m0_4_leakage_safe_split(cfg, targets, labels)
    feasibility = m0_5_feasibility_check(cfg, split)
    seal = m0_6_seal_manifest(cfg, sectors, targets, labels, split, feasibility)
    print(f"M0 complete. Seal #1 (manifest SHA-256): {seal}")


def main() -> None:
    p = argparse.ArgumentParser(description="M0 manifest pipeline (Phase I).")
    p.add_argument(
        "--config",
        default=str(Path(__file__).parent / "config" / "m0_config.yaml"),
        help="Path to the signed-off frozen-choices config.",
    )
    args = p.parse_args()
    run(args.config)


if __name__ == "__main__":
    main()
