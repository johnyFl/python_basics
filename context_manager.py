class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext() as context:
    print("Inside context")

print("--------------------------------")

class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database disconnected")
        print(exc_type)
        print(exc_value)
        return True  # Suppress exception


with DatabaseConnection() as db:
    print("Executing query")
    raise ValueError("Query failed")

print("Program finished")

print("--------------------------------")

from contextlib import contextmanager

@contextmanager
def database_connection():
    print("Database connected")

    try:
        print("now")
        yield 5
    finally:
        print("Database disconnected")


with database_connection() as db:
    print("Executing query")
    print(f"Database connection object: {db}")