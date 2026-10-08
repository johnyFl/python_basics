class User():
    def __init__(self, id,name, email,is_active):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active

class Admin(User):
    def __init__(self, id,name, email, is_active, department):
        super().__init__(id,name, email, is_active)
        self.department = department
    def permission(self):
        return ["create_user", "delete_user", "view_users"]
    def __str__(self):
        return f"Admin: {self.id} {self.name} {self.email} {self.is_active} {self.department}"
class Customer(User):
    def __init__(self, id,name, email, is_active, customer_id):
        super().__init__(id,name, email, is_active)
        self.customer_id = customer_id
    def permission(self):
        return ["view_profile","place_order"]
    def __str__(self):
        return f"Customer: {self.id} {self.name} {self.email} {self.is_active} {self.customer_id}"

user1 = Admin(1, "John Doe", "john.doe@example.com", True, "IT")
user2 = Customer(2, "Jane Smith", "jane.smith@example.com", True, "CUST001")
print(user1)
print(user2)    