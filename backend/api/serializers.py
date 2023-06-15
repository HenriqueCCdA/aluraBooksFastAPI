from pydantic import BaseModel


class Base(BaseModel):
    id: str
    nome: str


class Livros(Base):
    ...


class Favoritos(Base):
    ...
