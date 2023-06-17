import os

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from api.app import app
from api.db import session

fake = Faker()


@pytest.fixture(scope="session", autouse=True)
def env():
    os.environ["MONGODB_URI"] = "mongodb://alura:123456@localhost:27017/tests"


@pytest.fixture
def db():
    test_session = session()
    test_db = next(test_session)

    test_db.create_collection("livros")
    test_db.create_collection("favoritos")

    yield test_db

    test_db.drop_collection("livros")
    test_db.drop_collection("favoritos")


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def books_names():
    return [fake.name(), fake.name()]


@pytest.fixture
def books_in_db(db, books_names):
    return db.livros.insert_many([{"nome": name, "img": "fig.png"} for name in books_names])


@pytest.fixture
def fav_in_db(db, books_names, books_in_db):
    return db.favoritos.insert_many(
        [
            {
                "nome": name,
                "img": "fig.png",
                "_id": id_,
            }
            for name, id_ in zip(books_names, books_in_db.inserted_ids)
        ]
    )
