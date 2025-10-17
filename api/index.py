# api/index.py
import os, sys

# Make the project root importable so we can import main.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import the FastAPI app from your existing main.py and expose it as `app`
from main import app  # FastAPI instance defined in main.py
