"""Checkout pricing engine -- the SYSTEM UNDER TEST.

The rules are written in docs/spec.md. This module deliberately contains
a few defects (see docs/seeded-defects-answer-key.md, which you should
only open AFTER you have written your own tests). Your job is to find
them by testing against the spec, not by reading this file.
"""
from dataclasses import dataclass
from decimal import ROUND_DOWN, ROUND_HALF_UP, Decimal

VAT_RATE = Decimal("0.15")
STANDARD_SHIPPING = Decimal("60.00")
EXPRESS_SURCHARGE = Decimal("50.00")
FREE_SHIPPING_THRESHOLD = Decimal("750.00")
TIER_1_THRESHOLD = Decimal("500.00")
TIER_2_THRESHOLD = Decimal("1000.00")
WELCOME5_MINIMUM = Decimal("200.00")
WELCOME5_AMOUNT = Decimal("50.00")


class CheckoutError(Exception):
    """Base class for all checkout errors."""


class EmptyCartError(CheckoutError):
    pass


class InvalidItemError(CheckoutError):
    pass


class InvalidCouponError(CheckoutError):
    pass


@dataclass(frozen=True)
class Item:
    name: str
    unit_price: Decimal
    quantity: int

    def __post_init__(self):
        if self.unit_price < 0:
            raise InvalidItemError("unit_price must not be negative")
        if not isinstance(self.quantity, int) or self.quantity < 1:
            raise InvalidItemError("quantity must be a whole number of at least 1")


@dataclass(frozen=True)
class Receipt:
    subtotal: Decimal
    volume_discount: Decimal
    coupon_discount: Decimal
    shipping: Decimal
    vat: Decimal
    total: Decimal


def money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def volume_discount_rate(subtotal: Decimal) -> Decimal:
    if subtotal > TIER_2_THRESHOLD:
        return Decimal("0.15")
    if subtotal >= TIER_1_THRESHOLD:
        return Decimal("0.10")
    return Decimal("0")


def calculate_shipping(discounted_subtotal: Decimal, express: bool, free_shipping: bool) -> Decimal:
    shipping = STANDARD_SHIPPING
    if free_shipping or discounted_subtotal >= FREE_SHIPPING_THRESHOLD:
        shipping = Decimal("0.00")
    if express and shipping > 0:
        shipping += EXPRESS_SURCHARGE
    return shipping


def checkout(items, coupon=None, express=False) -> Receipt:
    if not items:
        raise EmptyCartError("cart is empty")

    subtotal = money(sum((i.unit_price * i.quantity for i in items), Decimal("0")))
    volume_discount = money(subtotal * volume_discount_rate(subtotal))
    discounted = subtotal - volume_discount

    coupon_discount = Decimal("0.00")
    free_shipping = False
    if coupon is not None:
        if coupon == "WELCOME5":
            if discounted < WELCOME5_MINIMUM:
                raise InvalidCouponError("minimum spend for WELCOME5 not met")
            coupon_discount = WELCOME5_AMOUNT
        elif coupon == "FREESHIP":
            free_shipping = True
        else:
            raise InvalidCouponError(f"unknown coupon: {coupon}")

    shipping = calculate_shipping(subtotal, express, free_shipping)

    taxable = discounted - coupon_discount + shipping
    vat = (taxable * VAT_RATE).quantize(Decimal("0.01"), rounding=ROUND_DOWN)
    total = discounted - coupon_discount + shipping + vat
    return Receipt(subtotal, volume_discount, coupon_discount, shipping, vat, total)
