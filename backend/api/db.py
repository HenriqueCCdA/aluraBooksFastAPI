from bson import ObjectId
from pymongo import MongoClient

mongodb_uri = "mongodb://alura:123456@localhost:27017/"
port = 27017


client = MongoClient(mongodb_uri, port)
db = client["alura"]


async def list_all_books():
    return list(db.livros.find({}))


async def list_all_fav():
    return list(db.favoritos.find({}))


async def insert_fav(book):
    db.favoritos.insert_one(book)


async def delete_fav(id: str):
    db.favoritos.delete_one({"_id": ObjectId(id)})


async def get_book_by_id(id: str):
    return db.livros.find_one({"_id": ObjectId(id)})
