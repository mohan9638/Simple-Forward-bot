# config.py
from os import environ

API_ID = int(environ.get("API_ID", "25693368"))
API_HASH = environ.get("API_HASH", "2dcf91b0f99c0b9d4875e87020e6bd07")
BOT_TOKEN = environ.get("BOT_TOKEN", "7547785716:AAFp29f8MM4p2WbAcDkpWEBQGPsFaWfWUsQ")
MONGO_URI = environ.get("MONGO_URI", "mongodb+srv://pawedal810:HOFEIUUSvhAWHHW7@cluster0.8sxxbgw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(environ.get("OWNER_ID", "5927517339"))
