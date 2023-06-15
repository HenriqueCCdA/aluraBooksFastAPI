import os
import pytest

from fastapi.testclient import TestClient
from faker import Faker

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
    return [ fake.name(),  fake.name() ]
