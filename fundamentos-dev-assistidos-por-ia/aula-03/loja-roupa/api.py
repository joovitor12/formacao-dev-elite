from enum_cores import Cor
from pydantic import BaseModel

## aplica a cor vermelha a camisa
class CamisaVermelha(BaseModel):
    cor = Cor.VERMELHO

## aplica a cor azul a camisa
class CamisaAzul(BaseModel):
    cor = Cor.AZUL