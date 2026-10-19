"""REQ-01, REQ-02, REQ-03: items, empty cart and subtotal."""
from decimal import Decimal

import pytest

from checkout import EmptyCartError, InvalidItemError, Item, checkout


def test_empty_cart_is_rejected():
    with pytest.raises(EmptyCartError):
        checkout([])


def test_negative_price_is_rejected():
    with pytest.raises(InvalidItemError):
        checkout([Item("widget", Decimal("-1.00"), 1)])


def test_quantity_zero_is_rejected():
    with pytest.raises(InvalidItemError):
        checkout([Item("widget", Decimal("10.00"), 0)])


def test_negative_quantity_is_rejected():
    with pytest.raises(InvalidItemError):
        checkout([Item("widget", Decimal("10.00"), -1)])


def test_fractional_quantity_is_rejected():
    with pytest.raises(InvalidItemError):
        checkout([Item("widget", Decimal("10.00"), 1.5)])


def test_zero_price_is_accepted():
    receipt = checkout([Item("freebie", Decimal("0.00"), 1)])
    assert receipt.subtotal == Decimal("0.00")


def test_several_items_add_up():
    items = [
        Item("widget", Decimal("100.00"), 2),
        Item("gadget", Decimal("50.50"), 3),
    ]
    receipt = checkout(items)
    assert receipt.subtotal == Decimal("351.50")