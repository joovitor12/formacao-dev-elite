from pydantic import BaseModel

class Mamifero(BaseModel):
    nome: str
    idade: int