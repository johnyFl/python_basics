class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
def calculate_discount(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return price - (price * discount / 100)