"""REQ-05, REQ-06, REQ-07: coupons. Expected values are worked out from spec.md."""
from decimal import Decimal

import pytest

from checkout import Item, checkout, InvalidCouponError


def one_item(price):
    return [Item("widget", Decimal(price), 1)]


def test_welcome5_takes_50_off():
    # 200.00, no volume discount. Shipping 60.00. VAT = 15% of (200 - 50 + 60) = 31.50
    receipt = checkout(one_item("200.00"), coupon="WELCOME5")
    assert receipt.coupon_discount == Decimal("50.00")
    assert receipt.shipping == Decimal("60.00")
    assert receipt.vat == Decimal("31.50")
    assert receipt.total == Decimal("241.50")


def test_welcome5_rejected_just_below_minimum():
    # 199.99 is below the R200.00 minimum (REQ-06)
    with pytest.raises(InvalidCouponError):
        checkout(one_item("199.99"), coupon="WELCOME5")


@pytest.mark.xfail(strict=True, reason="BUG-005: coupon codes are case-sensitive (REQ-05)")
def test_coupon_codes_are_not_case_sensitive():
    # REQ-05: "welcome5" must behave exactly like "WELCOME5"
    receipt = checkout(one_item("200.00"), coupon="welcome5")
    assert receipt.coupon_discount == Decimal("50.00")
    assert receipt.total == Decimal("241.50")

@pytest.mark.xfail(strict=True, reason="BUG-005: coupon codes are case-sensitive (REQ-05)")
def test_freeship_is_not_case_sensitive():
    receipt = checkout(one_item("100.00"), coupon="freeship")
    assert receipt.shipping == Decimal("0.00")


def test_unknown_coupon_is_rejected():
    with pytest.raises(InvalidCouponError):
        checkout(one_item("100.00"), coupon="BOGUS")


def test_freeship_makes_standard_shipping_free():
    # 100.00, shipping 0.00, VAT = 15% of 100 = 15.00
    receipt = checkout(one_item("100.00"), coupon="FREESHIP")
    assert receipt.shipping == Decimal("0.00")
    assert receipt.vat == Decimal("15.00")
    assert receipt.total == Decimal("115.00")


def test_coupon_does_not_change_free_shipping_threshold():
    # 840.00 -> 10% discount (84.00) -> 756.00, which is >= 750.00, so shipping is free.
    # REQ-08 checks the threshold before any coupon, so WELCOME5 must not change that.
    # VAT = 15% of (756 - 50 + 0) = 105.90, total = 706 + 105.90 = 811.90
    receipt = checkout(one_item("840.00"), coupon="WELCOME5")
    assert receipt.shipping == Decimal("0.00")
    assert receipt.vat == Decimal("105.90")
    assert receipt.total == Decimal("811.90")