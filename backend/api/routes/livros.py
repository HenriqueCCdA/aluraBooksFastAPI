from fastapi import APIRouter, Request

from api.db import get_session
from api.serializers import Livros, book_dict
from api.services import list_all_books

router = APIRouter()


@router.get("/", response_model=list[Livros])
async def list_livros(db: get_session, request: Request):
    books = await list_all_books(db)

    return [book_dict(b, request.base_url._url) for b in books]
