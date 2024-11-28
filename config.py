# config.py

# Hardcoded API keys (fake for testing purposes)
API_KEY = "1234567890abcdef"  # Fake API key
SECRET_KEY = "s3cr3tKey123!"  # Fake secret key

# Database credentials (fake for testing purposes)
DB_USERNAME = "admin"
DB_PASSWORD = "admin123"

# Function to simulate connecting to a service with the API key and secret key
def connect_to_service():
    print(f"Connecting to service with API_KEY: {API_KEY} and SECRET_KEY: {SECRET_KEY}")

# Function to simulate connecting to a database with credentials
def connect_to_db():
    print(f"Connecting to DB as {DB_USERNAME} with password {DB_PASSWORD}")

# Simulate a connection attempt
if __name__ == "__main__":
    connect_to_service()
    connect_to_db()
