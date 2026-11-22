numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator)) 

def get_numbers():
    yield 10
    yield 20
    yield 30

numbers = get_numbers()

print(next(numbers))  # 10
print(next(numbers)) 