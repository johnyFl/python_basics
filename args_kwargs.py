def log_call(func,*args, **kwargs):
    print (f" {func.__name__}")
    print (f"args: {args}")
    print (f"kwargs: {kwargs}")
    result=func(*args, **kwargs)
    return result

def create_user(name, email, is_active=True):
    return {"name": name, "email": email, "is_active": is_active}

print(log_call(create_user, "John Doe", "john.doe@example.com"))
print(log_call(
    create_user,
    name="Maria",
    email="maria@test.com",
    is_active=False
))
