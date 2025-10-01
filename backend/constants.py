import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
