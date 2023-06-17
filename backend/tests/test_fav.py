import pytest
from bson import ObjectId
from fastapi import status


@pytest.mark.integration
def test_list(client, fav_in_db, books_names):
    response = client.get("/favoritos/")

    body = response.json()

    assert response.status_code == status.HTTP_200_OK

    excepted = [
        {"nome": books_names[0], "id": str(fav_in_db.inserted_ids[0]), "img": "http://testserver/media/fig.png"},
        {"nome": books_names[1], "id": str(fav_in_db.inserted_ids[1]), "img": "http://testserver/media/fig.png"},
    ]

    assert body == excepted


@pytest.mark.integration
def test_create(client, books_in_db, books_names, db):
    id_ = books_in_db.inserted_ids[0]

    response = client.post(f"/favoritos/{str(id_)}/")

    body = response.json()

    assert response.status_code == status.HTTP_201_CREATED

    assert body["detail"] == "Book insert in Favs"

    fav = db.favoritos.find_one({"_id": ObjectId(id_)})

    assert fav == {"_id": id_, "nome": books_names[0], "img": "fig.png"}


@pytest.mark.integration
def test_delete(client, fav_in_db, db):
    id_ = fav_in_db.inserted_ids[0]

    response = client.delete(f"/favoritos/{str(id_)}/")

    assert response.status_code == status.HTTP_204_NO_CONTENT

    fav = db.favoritos.find_one({"_id": ObjectId(id_)})

    assert not fav
