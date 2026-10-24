
def divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # None

print("------------------------------")

def calculate_age(birth_year: int) -> int:
    if birth_year > 2026:
        raise ValueError("Birth year cannot be in the future.")
    else:
        current_year = 2026
        return current_year - birth_year
try:
    print(calculate_age(2000))  # 26
    print(calculate_age(2026))  # 0
    print(calculate_age(2030))  # ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Birth year cannot be in the future.

print("------------------------------")

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance for withdrawal.")
    return balance - amount

try:
    new_balance = withdraw(2000, 150)
    print(f"New balance: {new_balance}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")  # Output: Error: Insufficient balance for withdrawal.

print("------------------------------")

users_db = {
    1: {"id": 1, "name": "Maria", "email": "maria@example.com"},
    2: {"id": 2, "name": "Nikos", "email": "nikos@example.com"}
}

class UserNotFoundError(Exception):
    pass


class InvalidUserIdError(Exception):
    pass

def find_user_by_id(user_id: int) -> dict:
    if not isinstance(user_id, int) or user_id <= 0:
        raise InvalidUserIdError("User ID must be a positive integer.")
    if user_id not in users_db:
        raise UserNotFoundError(f"User with ID {user_id} not found.")
    return users_db[user_id]

def get_user_service(user_id: int) -> dict:
        return find_user_by_id(user_id)
    

for user_id in [1, 3, -1]:
    try: 
        print({"status":200,"data": find_user_by_id(user_id)})
    except (UserNotFoundError) as e:
        print ({"status":404,"error": str(e)})
    except (InvalidUserIdError) as e:
        print ({"status":400,"error": str(e)})
    
