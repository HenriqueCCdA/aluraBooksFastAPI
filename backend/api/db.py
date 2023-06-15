from typing import Annotated, Generator

from fastapi import Depends
from pymongo import MongoClient
from pymongo.database import Database
from decouple import config


def session() -> Generator[Database, None, None]:
    MONGODB_URI = config("MONGODB_URI")
    try:
        client = MongoClient(MONGODB_URI, authSource="admin")
        yield client.get_default_database()
    finally:
        client.close()


get_session = Annotated[Database, Depends(session)]
