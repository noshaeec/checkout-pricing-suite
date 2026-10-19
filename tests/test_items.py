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


# TODO (yours), one test each:
#   - quantity 0 is rejected
#   - quantity -1 is rejected
#   - quantity 1.5 is rejected (not a whole number)
#   - price 0.00 with quantity 1 is ACCEPTED (valid boundary: checkout returns a receipt)
#   - two items add up: 2 x 100.00 and 3 x 50.50 give a subtotal of 351.50