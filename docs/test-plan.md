# Test plan: checkout engine

## 1. Scope
In scope: every requirement in `spec.md` (REQ-01 to REQ-11).
Out of scope: user interface, payment, performance.

## 2. Approach
Automated tests with pytest, designed from the spec (not from reading the code), using:
- **Boundary value analysis**: discount tiers, free-shipping threshold, WELCOME5 minimum.
- **Equivalence partitioning**: valid and invalid items, coupons, delivery types.
- **Decision tables**: coupon x delivery x free-shipping combinations.

## 3. Entry and exit criteria
- Entry: spec reviewed, environment set up, `pytest` runs.
- Exit: every requirement has at least one test; all failures are either fixed or logged as a bug with an ID.

## 4. Test cases

| Test | Requirement | Technique | Status |
|---|---|---|---|
| `test_discounts.py` (boundaries at 500 and 1000) | REQ-04 | Boundary values | Written |
| `test_shipping.py` (free-shipping threshold) | REQ-08 | Boundary values | Partly written |
| `test_checkout.py` (totals and rounding) | REQ-10, REQ-11 | Example-based | Partly written |
| Coupons: codes, case, WELCOME5 minimum, FREESHIP | REQ-05, 06, 07 | Equivalence + boundary | **TODO (yours)** |
| Express delivery | REQ-09 | Decision table | **TODO (yours)** |
| Invalid items and empty cart | REQ-01, 02 | Equivalence | **TODO (yours)** |
| Subtotal with several items | REQ-03 | Example-based | **TODO (yours)** |

## 5. Defect log
Record every real defect in `docs/bugs/BUG-001.md`, `BUG-002.md`, ... using `bug-report-template.md`.

## 6. Risks
- The spec may be ambiguous. Log a question rather than guess.
- Money rounding is an easy place for defects to hide.
