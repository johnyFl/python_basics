from calc import calculate_discount,Product
import pytest

@pytest.fixture()
def product():
    return Product("Laptop", 1000)

@pytest.mark.parametrize(
    " discount, expected",
    [
        ( 20, 800),
        ( 50, 500),
        ( 10, 900),
    ]
)
def test_calculate_discount(product, discount, expected):
    assert calculate_discount(product.price, discount) == expected

@pytest.mark.parametrize(
    "price, discount, error_message",
    [
        (-100, 20, "Price cannot be negative"),
        (100, -10, "Invalid discount"),
        (100, 120, "Invalid discount"),
    ]
)
def test_invalid_discount(price, discount, error_message):
    with pytest.raises(ValueError, match=error_message):
        calculate_discount(price, discount)
