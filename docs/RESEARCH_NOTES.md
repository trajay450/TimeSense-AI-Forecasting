# Research and engineering notes

## Problem
Time-series forecasting and anomaly detection with chronological splits, baseline comparisons and interval evaluation.

## Baseline assumptions
The baseline is local, deterministic, and small-scale. Any evaluation uses synthetic or built-in public educational data.

## Research questions
1. Does the baseline execute reproducibly?
2. Which failure modes and missing inputs cause incorrect outputs?
3. What changes under stronger baselines and larger datasets?

## Threats to validity
Synthetic distributions, small evaluation sets, deterministic heuristics, missing deployment tests, no external validation, and possible differences across package versions.

## Reproducibility
Run the command in README and inspect outputs. Do not quote the results as production-level findings.
