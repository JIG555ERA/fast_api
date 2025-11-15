from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends

MONGO_URL = "mongodb+srv://myindiaventures05_db_user:1j8z4NZsEWh4DCf1@miv05.kmxbfrp.mongodb.net/?retryWrites=true&w=majority&appName=miv05"
DB_NAME = "db05"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
collection = db["users"]