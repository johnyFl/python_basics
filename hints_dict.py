from typing import TypedDict

class User(TypedDict):
    id:int
    name: str
    email: str
    active: bool

def get_user(user_id:int) -> User|None:
    if user_id == 1:
        return {"id": 1, "name": "Maria", "email": "maria@example.com", "active": True}
    return None
def get_user_email(user:User)-> str:
    return user["email"]

user = get_user(1)
if user:
    email = get_user_email(user)
    print(email)  # Output:


class product(TypedDict):
    id:int
    name: str
    price: float
    in_stock: bool

def get_product(product_id:int) -> product|None:
    if product_id == 10:
        return {"id": 10, "name": "Laptop", "price": 49.99, "in_stock": True}
    return None
def get_product_price(product:product)-> float:
    return product["price"]
def is_product_available(product:product)-> bool:
    return product["in_stock"]
product = get_product(10)
if product:
    price = get_product_price(product)
    available = is_product_available(product)
    print(price)  # Output: 49.99
    print(available)  # Output: True


products: list[Product] = [
    {"id": 1, "name": "Mouse", "price": 15.5, "in_stock": True},
    {"id": 2, "name": "Keyboard", "price": 49.99, "in_stock": False},
    {"id": 3, "name": "Monitor", "price": 199.99, "in_stock": True},
]

def find_product(products: list[Product], product_id: int) -> Product | None:
    for product in products:
        if product["id"] == product_id:
            return product
    return None
print(find_product(products, 2))