"""REQ-08: standard shipping and the free-shipping threshold.

Free shipping depends on the DISCOUNTED subtotal, so each case below works
out the discounted amount first.
"""
from decimal import Decimal

from checkout import Item, checkout


def shipping_for_subtotal(amount: str):
    return checkout([Item("widget", Decimal(amount), 1)]).shipping


def test_small_order_pays_standard_shipping():
    assert shipping_for_subtotal("100.00") == Decimal("60.00")


def test_discounted_subtotal_of_exactly_750_ships_free():
    # 833.33 less 10% (83.33) = 750.00, exactly on the threshold
    assert shipping_for_subtotal("833.33") == Decimal("0.00")


def test_discounted_subtotal_just_below_750_pays_shipping():
    # 833.32 less 10% (83.33) = 749.99, one cent below the threshold
    assert shipping_for_subtotal("833.32") == Decimal("60.00")


# TODO (yours): a very large order, and the middle of the 10% tier (e.g. 800.00)
