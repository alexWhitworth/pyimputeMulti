# Implementation Spec: Code Coverage for pysynthACS

## 1. Prerequisites
Ensure the following packages are added to your development environment:
* `pytest`
* `pytest-cov`
* `maturin` (for Rust extensions)

## 2. Configuration (`pyproject.toml`)
Add these sections to your `pyproject.toml` to standardize coverage behavior across local and CI environments.

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
# Automatically include coverage flags when running pytest
addopts = "--cov=pysynthACS --cov-report=xml --cov-report=term-missing"

[tool.coverage.run]
source = ["src/pysynthACS"]
omit = [
    "tests/*",
    "**/__init__.py",
    "scripts/*"
]

[tool.coverage.report]
# Threshold enforcement: CI will fail if total coverage is below this %
fail_under = 85
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]

```yaml
name: Tests & Coverage

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  run-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Rust toolchain
        uses: dtolnay/rust-toolchain@stable

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov maturin
          pip install -e .  # Compiles Rust extensions into the environment

      - name: Run Pytest with Coverage
        run: |
          # The report location is defined in pyproject.toml
          pytest

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          slug: alexWhitworth/pysynthACS
          file: ./coverage.xml
          fail_ci_if_error: true
```

4. Integration Steps
- GitHub Secret: Add CODECOV_TOKEN to your GitHub Repository Secrets.
- Status Checks: In GitHub repository settings, enable Branch Protection Rules for master and require the run-tests job and codecov/project status to pass before merging.
- Rust Coverage (Future): As Phase 2 (Rust optimization) progresses, consider adding llvm-cov to the workflow to monitor the memory-safe core logic.