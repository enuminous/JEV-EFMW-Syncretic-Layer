# JEV-EFMW Syncretic Layer

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
