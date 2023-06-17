from fastapi import APIRouter

from .books import router as livros_router
from .favorites import router as favoritos_router

main_router = APIRouter()

main_router.include_router(livros_router, prefix="/livros", tags=["livros"])
main_router.include_router(favoritos_router, prefix="/favoritos", tags=["favoritos"])
