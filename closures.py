def filter(x):
    def multip(y):
        return x*y
    return multip

double=filter(2)
triple=filter(3)

def filter(x):
    def multip(y):
        return x*y
    return multip

double=filter(2)
triple=filter(3)

def event(eventName):
    c=0
    def counter():
        nonlocal c
        c=c+1 
        return eventName + str(c)
    return counter

login=event("Login")
logout=event("Logout")

def validator(length):
    def validate(username):
        return len(username) >= length
    return validate

val5=validator(5)
val10=validator(10)
print(val5("user1"))
print(val5("us"))
print(val10("user1fdfdsfsdfsd"))
print(val10("us"))
