from fastapi import APIRouter

from api.db import get_session
from api.serializers import Livros
from api.services import list_all_books

router = APIRouter()


@router.get("/", response_model=list[Livros])
async def list_livros(db: get_session):
    books = await list_all_books(db)

    return [{"id": str(item["_id"]), **item} for item in books]
