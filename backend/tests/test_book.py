from fastapi import status


def test_list(client, db,  books_names):

    ids = db.livros.insert_many([{"nome": name} for name in books_names])

    response = client.get("/livros/")

    body = response.json()

    assert response.status_code == status.HTTP_200_OK

    excepted = [
        {"nome": books_names[0], "id": str(ids.inserted_ids[0])},
        {"nome": books_names[1], "id": str(ids.inserted_ids[1])},
    ]

    assert body == excepted
