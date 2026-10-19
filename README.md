# checkout-pricing-suite

A Quality Assurance portfolio project. It tests a small online-store **checkout pricing engine** (discounts, coupons, shipping, VAT in ZAR) against a written specification, using pytest.

The engine contained seeded defects. The goal was to find them by designing tests from the spec, to report them properly, and to show the process.

## Results

Five defects found, each with a failing test and a written bug report. Final run: **23 passed, 6 expected failures (xfail)**, no unexpected failures.

| Bug | Requirement | Summary | Severity |
|---|---|---|---|
| [BUG-001](docs/bugs/BUG-001.md) | REQ-10 | VAT is rounded down instead of half-up | Major |
| [BUG-002](docs/bugs/BUG-002.md) | REQ-04 | An order of exactly R1000.00 gets 10% off instead of 15% | Major |
| [BUG-003](docs/bugs/BUG-003.md) | REQ-08 | Free shipping is decided on the original subtotal, not the discounted one | Major |
| [BUG-004](docs/bugs/BUG-004.md) | REQ-09 | Express fee is dropped when standard shipping is free | Major |
| [BUG-005](docs/bugs/BUG-005.md) | REQ-05 | Coupon codes are case-sensitive | Major |

Each known defect has a test marked `xfail`, so the build stays green while the defects stay documented. When a bug is fixed, remove its marker. Because the markers use `strict=True`, a fixed bug makes the suite fail until the marker is removed.

## What this project demonstrates

- Reading a specification and breaking it into testable requirements (`docs/spec.md`)
- A test plan with scope, approach, and entry/exit criteria (`docs/test-plan.md`)
- Test design techniques: boundary value analysis, equivalence partitioning, decision tables
- Automated tests with pytest, including parametrized cases and `xfail` for known defects
- Defect reports that someone else could act on (`docs/bugs/`, severity scale in `docs/severity-levels.md`)
- A CI pipeline (GitHub Actions) that runs the tests on every push

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

On Linux or macOS, activate with `source .venv/bin/activate`. If PowerShell blocks the activate script, run `Set-ExecutionPolicy -Scope Process Bypass` first.

## Running the tests

```powershell
pytest                                   # all tests
pytest tests/test_discounts.py -v        # one file, verbose
pytest --cov=checkout --cov-report=term-missing   # with coverage
```

## Where things are

```
src/checkout/pricing.py      the system under test
docs/spec.md                 requirements REQ-01 to REQ-11
docs/test-plan.md            plan and test case table
docs/bug-report-template.md  template for defect reports
docs/bugs/                   BUG-001 to BUG-005
docs/severity-levels.md      how severity is rated
tests/                       tests for discounts, coupons, shipping, express, items and totals
```

The seeded-defects answer key is kept out of the repository.

## Possible extensions

- Property-based tests with `hypothesis` (for example, total is never negative)
- A mutation testing run to measure the strength of your tests
- Testing a real public API as a second part of the project

---

WTC-TFCSTY3M
