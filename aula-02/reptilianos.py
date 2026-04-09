from pydantic import BaseModel

class Reptiliano(BaseModel):
    nome: str
    idade: int
    especie: str