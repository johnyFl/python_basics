import time

def timer(func):
    def wrapper(*args,**kargs):
        print("start counter")
        start=time.perf_counter()
        result=func(*args,**kargs)
        end=time.perf_counter()
        print(f"{func.__name__} {end-start}")
        return result
    return wrapper

@timer
def test(x):
    for i in range(10):
        x=x+1
    return x
print(test(1))


def log_calls(func):
    def wrapper(*args,**kwargs):    
        print(f"start {func.__name__}")
        result=func(*args,**kwargs)
        print(f"end {func.__name__}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(add(3,5))
print(greet("john"))
print("\n\n\n\n")

admin = {
    "name": "Nikos",
    "role": "admin"
}

customer = {
    "name": "Maria",
    "role": "customer"
}

def require_role(role):
    def logger(func):
        def wrapper(*args,**kwargs):
            if args[0]["role"]==role:
                result=func(*args,**kwargs)
                return result
            else:
                return(f"not permit {args[0]['name']}")
        return wrapper
    return logger

@require_role("admin")
def delete_user(user):
    return f"User deleted by {user['name']}"

print(delete_user(admin))
print(delete_user(customer))