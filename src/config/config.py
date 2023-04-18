import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///myapp.db"

    # secrets.token_hex(length) pour generer un token de taille length
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
    LOG_FILE = "logs.log"


# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/myapp"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
