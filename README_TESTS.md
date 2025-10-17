# Tests and Performance Measurement

## Requirements
- Python 3.9+
- pip install -r requirements.txt

## Run Unit Tests
pytest -v

## Run Performance Script
python perf/perf_measure.py

## GitHub Actions CI/CD
A CI pipeline runs all unit tests automatically on every push and pull request.
See `.github/workflows/ci.yml`.
