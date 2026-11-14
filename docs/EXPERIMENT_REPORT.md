# Verified local execution report

Command: `python main.py`

Demo exit code: 0

```text
{
  "test_points": 144,
  "model_mae": 0.23585804379158148,
  "naive_mae": 0.2500592132839619,
  "model_rmse": 0.2863023659751478,
  "interval_coverage": 0.5208333333333334,
  "anomaly_flags": 69,
  "interval_radius": 0.2137228345061081
}

```

Test exit code: 0

```text
test_features (test_core.TestCore.test_features) ... ok
test_forecast (test_core.TestCore.test_forecast) ... ok
test_import (test_core.TestCore.test_import) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.287s

OK

```

These are local baseline results on synthetic or tutorial data, not external validation.
