class Product():
    def __init__(self,name:str,price:float,category:str):
        self.name=name
        self.price=price
        self.category=category

    def __str__(self):
       return (f"{self.name} {self.price} {self.category}")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        if not self.is_valid_price(val):
            raise ValueError("Price cannot be negative")
        self._price = val
        
    @classmethod
    def create_free_product(cls, name, category):
        return cls(name,0,category)
    @staticmethod
    def is_valid_price(price):
        return price>=0

p1 = Product("Laptop", 1200, "Electronics")
p2 = Product.create_free_product("Sample", "Software")

print(p1.price)
print(p2.price)

p1.price = -100  # Πρέπει να εγείρει ValueError






