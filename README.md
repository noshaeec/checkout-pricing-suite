# QA Checkout Suite

A Quality Assurance portfolio project. It tests a small online-store **checkout pricing engine** (discounts, coupons, shipping, VAT in ZAR) against a written specification, using pytest.

The engine contains deliberately seeded defects. The point of the project is to find them by designing tests from the spec, to report them properly, and to show the process.

## What this project demonstrates

- Reading a specification and breaking it into testable requirements (`docs/spec.md`)
- A test plan with scope, approach, and entry/exit criteria (`docs/test-plan.md`)
- Test design techniques: boundary value analysis, equivalence partitioning, decision tables
- Automated tests with pytest, using parametrized cases
- Defect reports that someone else could act on (`docs/bugs/`)
- Coverage measurement and a CI pipeline (GitHub Actions)

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

## Workflow

1. Pick a requirement from `docs/spec.md`.
2. Design cases for it (boundaries, valid and invalid partitions) and add them to `docs/test-plan.md`.
3. Write the tests in `tests/`.
4. When a test fails, decide: is the **test** wrong or is the **software** wrong? Check the spec.
5. If the software is wrong, log it in `docs/bugs/BUG-00X.md` using `docs/bug-report-template.md`.
6. Mark the test as a known defect so the suite stays readable, and so it flips when the bug is fixed:

   ```python
   @pytest.mark.xfail(strict=True, reason="BUG-001: exactly 1000.00 does not get the 15% tier")
   ```

`strict=True` means that if the bug is fixed and the test starts passing, pytest reports a failure, which reminds you to remove the marker.

## Where things are

```
src/checkout/pricing.py      the system under test (do not read it before testing!)
docs/spec.md                 requirements REQ-01 to REQ-11
docs/test-plan.md            plan and test case table
docs/bug-report-template.md  template for defect reports
tests/                       starter tests (discounts, shipping, totals)
```

`docs/seeded-defects-answer-key.md` lists the defects. Open it only after you have finished testing.

## Starter status

Discounts, part of shipping and part of totals are written. Coupons, express delivery, item validation and multi-item subtotals are left for you (see the TODO rows in the test plan).

## Possible extensions

- Property-based tests with `hypothesis` (for example, total is never negative)
- A mutation testing run to measure the strength of your tests
- Testing a real public API as a second part of the project


WTC-TFCSTY3M
