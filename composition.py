class Product:
    def __init__(self, id,name, price):
        self.id = id
        self.name = name
        self.price = price
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
class Email_service:
    def send_email(self, to, subject, message):
        print(f"Sending email to {to}: {subject} - {message}")
class Order_service:
    def __init__(self):
        self.email_service = Email_service()
    def create_order(self, customer, product):
        print("Order created")
        self.email_service.send_email(customer.email, "Order Confirmation", "Your order has been placed.")
product1 = Product(1, "Laptop", 999.99)
customer1 = Customer(1, "John Doe", "john.doe@example.com")
order1 = Order_service()
order1.create_order(customer1, product1)
