from typing import Optional

from typing import Optional
from enum_cores import Cor
from pydantic import BaseModel
    

class Camisa(BaseModel):
    id: Optional[int] = None
    cor: Cor
    tamanho: str = "M"
    preco: float

# Modelo para criação de camisa
class CamisaCreate(BaseModel):
    cor: Cor
    tamanho: str = "M"
    preco: float