"""REQ-04: volume discount tiers, tested with boundary values."""
from decimal import Decimal

import pytest

from checkout import Item, checkout


def receipt_for_subtotal(amount: str):
    return checkout([Item("widget", Decimal(amount), 1)])


@pytest.mark.parametrize(
    "subtotal, expected_discount",
    [
        ("0.00", "0.00"),        # lowest possible subtotal
        ("499.99", "0.00"),      # just below tier 1
        ("500.00", "50.00"),     # exactly tier 1 -> 10%
        ("500.01", "50.00"),     # just above tier 1 (50.001 rounds to 50.00)
        ("999.99", "100.00"),    # just below tier 2 (99.999 rounds half-up to 100.00)
        ("1000.00", "150.00"),   # exactly tier 2 -> 15%
        ("1000.01", "150.00"),   # just above tier 2 (150.0015 rounds to 150.00)
    ],
)
def test_volume_discount_at_boundaries(subtotal, expected_discount):
    assert receipt_for_subtotal(subtotal).volume_discount == Decimal(expected_discount)


def test_subtotal_is_reported_before_discount():
    assert receipt_for_subtotal("1000.00").subtotal == Decimal("1000.00")
