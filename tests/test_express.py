"""REQ-09: express delivery adds R50.00 on top of the shipping amount."""
from decimal import Decimal

import pytest

from checkout import Item, checkout


def test_express_adds_50_to_standard_shipping():
    # 100.00 order: no discount, standard shipping 60.00, express adds 50.00
    receipt = checkout([Item("widget", Decimal("100.00"), 1)], express=True)
    assert receipt.shipping == Decimal("110.00")


@pytest.mark.xfail(strict=True, reason="BUG-004: express fee is dropped when standard shipping is free (REQ-09)")
def test_express_adds_50_even_when_shipping_is_free():
    # 2000.00 order: 15% discount (300.00) leaves 1700.00, which ships free,
    # but express still costs 50.00
    receipt = checkout([Item("widget", Decimal("2000.00"), 1)], express=True)
    assert receipt.shipping == Decimal("50.00")