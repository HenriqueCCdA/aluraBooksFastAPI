from fastapi import APIRouter

from api.db import list_all_books
from api.serializers import Livros

router = APIRouter()


@router.get("/", response_model=list[Livros])
async def list_livros():
    books = await list_all_books()
    return [{"id": str(item["_id"]), **item} for item in books]
