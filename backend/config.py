import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
    DATABASE_URI = os.environ.get('DATABASE_URI', '')