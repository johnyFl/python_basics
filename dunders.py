class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}"
product1=Product(1, "Laptop", 999.99)
Product2=Product(2, "Smartphone", 499.99)
print(product1)
print(Product2)
print(repr(product1))
print(repr(Product2))
list_of_products=[product1, Product2]
print(list_of_products)