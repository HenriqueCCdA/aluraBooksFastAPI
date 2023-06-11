from fastapi import APIRouter

from .favoritos import router as favoritos_router
from .livros import router as livros_router

main_router = APIRouter()

main_router.include_router(livros_router, prefix="/livros", tags=["livros"])
main_router.include_router(favoritos_router, prefix="/favoritos", tags=["favoritos"])
