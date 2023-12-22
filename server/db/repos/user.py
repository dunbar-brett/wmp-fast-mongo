from core import config
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(config.DATABASE_URL)
database = client.user

user_collection = database.get_collection("user_collection")