from bson import ObjectId
from pymongo import MongoClient


async def list_all_books(db: MongoClient):
    return list(db.livros.find({}))


async def list_all_fav(db: MongoClient):
    return list(db.favoritos.find({}))


async def insert_fav(book, db: MongoClient):
    db.favoritos.insert_one(book)


async def delete_fav(id: str, db: MongoClient):
    db.favoritos.delete_one({"_id": ObjectId(id)})


async def get_book_by_id(id: str, db: MongoClient):
    return db.livros.find_one({"_id": ObjectId(id)})
