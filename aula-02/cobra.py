from typing import List

from reptilianos import Reptiliano
from enum import Enum


class RacaoCobra(Enum):
    FILHOTE = "ração para cobras filhotes"
    ADULTO = "ração para cobras adultas"
    IDOSO = "ração para cobras idosas"

class Cobra(Reptiliano):
    racoes_cobra: List[RacaoCobra] = [RacaoCobra.FILHOTE, RacaoCobra.ADULTO, RacaoCobra.IDOSO]

def listar_cobras() -> List[Cobra]:
    cobras = [
        Cobra(nome="Naja", idade=2, especie="Naja"),
        Cobra(nome="Sucuri", idade=5, especie="Sucuri")
    ]
    return cobras
