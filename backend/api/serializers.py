from pydantic import BaseModel


class Livros(BaseModel):
    id: str
    nome: str


class Favoritos(BaseModel):
    id: str
    nome: str
