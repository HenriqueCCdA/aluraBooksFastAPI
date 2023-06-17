import pytest
from fastapi import status


@pytest.mark.integration
def test_list(client, books_in_db, books_names):
    response = client.get("/livros/")

    body = response.json()

    assert response.status_code == status.HTTP_200_OK

    excepted = [
        {"nome": books_names[0], "id": str(books_in_db.inserted_ids[0]), "img": "http://testserver/media/fig.png"},
        {"nome": books_names[1], "id": str(books_in_db.inserted_ids[1]), "img": "http://testserver/media/fig.png"},
    ]

    assert body == excepted
