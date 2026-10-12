# Checkout engine specification

All amounts are in South African rand (ZAR), rounded **half-up** to 2 decimal places.

| ID | Requirement |
|---|---|
| REQ-01 | An item has a name, a unit price (not negative) and a whole-number quantity of at least 1. Anything else is rejected with `InvalidItemError`. |
| REQ-02 | Checking out an empty cart raises `EmptyCartError`. |
| REQ-03 | Subtotal = sum of unit price x quantity for every item. |
| REQ-04 | Volume discount on the subtotal: below R500.00 no discount; R500.00 up to (but not including) R1000.00 = 10%; R1000.00 or more = 15%. |
| REQ-05 | A coupon is optional. At most one coupon per order. Coupon codes are not case-sensitive. An unknown code raises `InvalidCouponError`. |
| REQ-06 | `WELCOME5` takes R50.00 off the discounted subtotal, but only if the discounted subtotal is at least R200.00. Otherwise it raises `InvalidCouponError`. |
| REQ-07 | `FREESHIP` makes standard shipping free. |
| REQ-08 | Standard shipping costs R60.00, and is free when the **discounted** subtotal (after the volume discount, before any coupon) is R750.00 or more. |
| REQ-09 | Express delivery adds R50.00 on top of the shipping amount, always, even when standard shipping is free. |
| REQ-10 | VAT is 15% of (discounted subtotal - coupon discount + shipping). |
| REQ-11 | Total = discounted subtotal - coupon discount + shipping + VAT. |
