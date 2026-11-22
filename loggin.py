import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging information")
logging.info("Application started")
logging.warning("Disk space is getting low")
logging.error("Failed to connect to database")
logging.critical("Application cannot continue")

print("--------------------------------")

logging.basicConfig(level=logging.INFO)

def create_user(username):
    logging.info("Creating user: %s", username)

    if not username:
        logging.error("Username cannot be empty")
        return None

    logging.info("User created successfully")
    return {"username": username}
create_user("john")

print("--------------------------------")
import os

environment = os.getenv("APP_ENV", "development")

if environment == "production":
    print("Production mode")
else:
    print("Development mode")