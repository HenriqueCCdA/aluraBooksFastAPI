from pydantic import BaseModel


class Base(BaseModel):
    id: str
    nome: str
    img: str


class Livros(Base):
    ...


class Favoritos(Base):
    ...


def book_dict(book, base_url):
    return {"id": str(book["_id"]), "img": f"{base_url}media/{book['img']}", "nome": book["nome"]}
