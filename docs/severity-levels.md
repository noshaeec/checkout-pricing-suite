# Severity levels

Severity is how bad the effect of a defect is on the shop or its customers. It is not the same as priority, which is how soon the defect should be fixed. Each bug report picks one level and gives the reason in its Notes.

| Level | Definition | Example in this project |
|---|---|---|
| **Critical** | The checkout crashes or cannot complete for many orders, or the engine produces results that are wildly wrong. No workaround. | Checkout raises an error for every valid cart. |
| **Major** | The checkout completes but a requirement gives a wrong amount on the receipt (the customer is mischarged or the shop loses money), and nothing warns anyone. No workaround. | The free-shipping threshold uses the wrong subtotal (BUG-003). |
| **Minor** | A requirement is not met, but no wrong amount is produced, or an easy workaround exists. The failure is visible to the user. | A valid coupon is refused when typed in lower case (BUG-005). |
| **Cosmetic** | Behaviour is correct. Only wording, naming or presentation is wrong. | A typo in an error message. |

## How to choose
1. Is a wrong amount shown on the receipt? If yes, it is Major or Critical.
2. Is the failure silent (nobody would notice)? Silent money errors are rated higher than loud ones.
3. Is there an easy workaround? If yes, rate it one level lower.
4. State the reason in the Notes of the bug report.