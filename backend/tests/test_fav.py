import pytest
from bson import ObjectId
from fastapi import status


@pytest.mark.integration
def test_list(client, fav_in_db, books_names):
    response = client.get("/favoritos/")

    body = response.json()

    assert response.status_code == status.HTTP_200_OK

    excepted = [
        {"nome": books_names[0], "id": str(fav_in_db.inserted_ids[0])},
        {"nome": books_names[1], "id": str(fav_in_db.inserted_ids[1])},
    ]

    assert body == excepted


@pytest.mark.integration
def test_create(client, books_in_db, books_names, db):
    id_ = books_in_db.inserted_ids[0]

    response = client.post(f"/favoritos/{str(id_)}/")

    body = response.json()

    assert response.status_code == status.HTTP_201_CREATED

    assert body["detail"] == "Book insert in Favs"

    favs = db.favoritos.find_one({"_id": ObjectId(id_)})

    assert favs == {"_id": id_, "nome": books_names[0]}
