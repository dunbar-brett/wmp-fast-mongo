from starlette.config import Config
from typing import Optional
# from beanie import init_beanie

from motor.motor_asyncio import AsyncIOMotorClient
import logging
# import models as models

logger = logging.getLogger(__name__)

config = Config(".env")
DATABASE_URL = config("MONGODB_URL", cast=str, default="mongodb://localhost:27017")
SECRET_KEY = config("SECRET_KEY", cast=str, default="secret")

# I likely dont need beanie
# async def initiate_database():
#     client = AsyncIOMotorClient(DATABASE_URL)
#     # example with models
#     # await init_beanie(
#     #     database=client.get_default_database(), document_models=models.__all__
#     # )
#     logger.info("------------------ Initiating database ------------------")

#     await init_beanie(
#         database=client.test_database
#     )

    