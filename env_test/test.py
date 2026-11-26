import os
from dotenv import load_dotenv

load_dotenv()

app_env = os.getenv("APP_ENV")
debug = os.getenv("DEBUG")
port = os.getenv("PORT")

print(app_env)
print(debug)
print(port)