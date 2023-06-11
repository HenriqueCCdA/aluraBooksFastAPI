from fastapi import APIRouter, HTTPException, status

from api.db import (
    delete_fav,
    get_book_by_id,
    insert_fav,
    list_all_fav,
)
from api.serializers import Favoritos

router = APIRouter()


@router.get("/", response_model=list[Favoritos])
async def list_favoritos():
    favs = await list_all_fav()
    return [{"id": str(item["_id"]), **item} for item in favs]


@router.post("/{id}/", tags=["favoritos"], status_code=status.HTTP_201_CREATED)
async def create_favoritos(id: str):
    book = await get_book_by_id(id)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Id do livro {id} não achado.")

    await insert_fav(book)
    return {"detail": "Book insert in Favs"}


@router.delete("/{id}/", tags=["favoritos"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_favoritos(id: str):
    book = await get_book_by_id(id)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Id do livro {id} não achado nos favoritos.")

    await delete_fav(id)
