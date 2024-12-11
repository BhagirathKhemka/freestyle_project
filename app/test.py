from dotenv import load_dotenv
import os

load_dotenv()

# Check if API key is loaded correctly
api_key = os.getenv("NEWS_API")

if not api_key:
    raise ValueError("API Key is missing! Ensure it's set in your environment or .env file.")
print(f"API Key loaded successfully: {api_key}")
