import os
import dotenv

if not dotenv.load_dotenv():
    raise RuntimeError("Failed to load .env file")

debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'

try:
    essential_env = os.environ['DB_HOST']
    print(f"Successfully loaded essential environment variable: {essential_env}")
except KeyError:
    raise RuntimeError("Essential environment variable DB_HOST is missing")
