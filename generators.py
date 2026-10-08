def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

users = [
    {"id": 1, "name": "Nikos", "active": True},
    {"id": 2, "name": "Maria", "active": False},
    {"id": 3, "name": "Giorgos", "active": True},
    {"id": 4, "name": "Eleni", "active": True},
    {"id": 5, "name": "Kostas", "active": False},
]

def active_users(users):
    for user in users:
        if user["active"]:
            yield user
for user in active_users(users):
    print(user) 
user_generator=active_users(users)
print(next(user_generator))
print(next(user_generator))
print(next(user_generator))


orders = [
    {"id": 1, "user": "Nikos", "amount": 120},
    {"id": 2, "user": "Maria", "amount": 80},
    {"id": 3, "user": "Giorgos", "amount": 250},
    {"id": 4, "user": "Eleni", "amount": 60},
    {"id": 5, "user": "Kostas", "amount": 300},
    {"id": 6, "user": "Anna", "amount": 150},
    {"id": 7, "user": "John", "amount": 90},
]

def order_batches(orders, batch_size):
    for i in range(0, len(orders), batch_size):
        yield orders[i:i + batch_size]
for batch in order_batches(orders, 3):
    print(batch)


