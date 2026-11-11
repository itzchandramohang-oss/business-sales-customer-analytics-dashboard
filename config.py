import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "false").strip().lower() in {"1", "true", "yes"}
    SQL_HOST = os.getenv("SQL_HOST", "localhost")
    SQL_PORT = int(os.getenv("SQL_PORT", "3306"))
    SQL_DATABASE = os.getenv("SQL_DATABASE", "business_analytics")
    SQL_USER = os.getenv("SQL_USER", "")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD", "")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DATABASE = os.getenv("MONGO_DATABASE", "business_analytics")
    MONGO_ORDERS_COLLECTION = os.getenv("MONGO_ORDERS_COLLECTION", "orders")
