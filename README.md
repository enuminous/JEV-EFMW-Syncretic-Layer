# JEV-EFMW Syncretic Layer

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/JEV-EFMW-Syncretic-Layer) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

Reproducible synthetic testbed for a Jev-like typed decision layer plus an EFMW-style recursive coherence monitor.

**Scope:** This does not contain or emulate TypeSafe AI's actual Jev implementation. It simulates bounded decisions, confidence/probability, outcomes, and closed-loop state trajectories.

## Experiments
- **001 Calibration degradation:** compare recursive residual monitoring with rolling calibration, EWMA, and CUSUM.
- **002 Trajectory instability:** keep local decision accuracy approximately nominal while closed-loop dynamics destabilize.
- **003 Equal-information trial:** give conventional trajectory detectors the same state information as the EFMW-style monitor. This is the decisive anti-circularity comparison.

## Run
```bash
pip install -r requirements.txt
python experiments/run_001.py
python experiments/run_002.py
python experiments/run_003.py
pytest
```

## Scientific discipline
Thresholds are calibrated on null streams, then frozen. Confirmatory seeds are disjoint. False-positive rates are matched. Negative results stay in the record. Synthetic performance does not establish EFMW physics, novelty, or performance on actual Jev.
