from calc import calculate_discount
import pytest

def test_calculate_discount():
    assert calculate_discount(100,80)==20

def test_negative_price():
    with pytest.raises(ValueError,match="Price cannot be negative"):
        calculate_discount(-100,80)

def test_invalid_discount():
    with pytest.raises(ValueError,match="Invalid discount"):
        calculate_discount(100,120)
