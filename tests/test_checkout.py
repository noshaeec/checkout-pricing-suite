"""REQ-10 and REQ-11: VAT and the final total."""
from decimal import Decimal

import pytest

from checkout import Item, checkout


def test_simple_order_total():
    receipt = checkout([Item("widget", Decimal("100.00"), 1)])
    # 100.00 + 60.00 shipping = 160.00 taxable; VAT = 24.00; total = 184.00
    assert receipt.vat == Decimal("24.00")
    assert receipt.total == Decimal("184.00")


@pytest.mark.xfail(strict=True, reason="BUG-001: VAT is rounded down instead of half-up (REQ-10)")
def test_vat_rounds_half_up():
    receipt = checkout([Item("widget", Decimal("100.10"), 1)])
    # taxable = 100.10 + 60.00 = 160.10; VAT = 24.015, which rounds half-up to 24.02
    assert receipt.vat == Decimal("24.02")
    assert receipt.total == Decimal("184.12")

# TODO (yours): a total that combines a discount, a coupon and express delivery
