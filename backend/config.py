import os
from dotenv import load_dotenv
import redis

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '')

    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', '')

    SESSION_TYPE = os.environ.get('SESSION_TYPE', '')
    SESSION_PERMANENT = os.environ.get('SESSION_PERMANENT', False)
    SESSION_USE_SIGNER = os.environ.get('SESSION_USE_SIGNER', True)
    SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS_URL', ''))