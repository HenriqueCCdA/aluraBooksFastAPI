from typing import Annotated, Generator

from fastapi import Depends
from pymongo import MongoClient
from pymongo.database import Database

mongodb_uri = "mongodb://alura:123456@localhost:27017/"
port = 27017


def session() -> Generator[Database, None, None]:
    try:
        client = MongoClient(mongodb_uri, port)
        yield client["alura"]
    finally:
        client.close()


get_session = Annotated[Database, Depends(session)]
