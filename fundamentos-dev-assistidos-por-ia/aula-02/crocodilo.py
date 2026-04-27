from typing import List

from reptilianos import Reptiliano
from enum import Enum


class RacaoCrocodilo(Enum):
    FILHOTE = "ração para crocodilos filhotes"
    ADULTO = "ração para crocodilos adultos"
    IDOSO = "ração para crocodilos idosos"

class Crocodilo(Reptiliano):
    racoes_crocodilo: List[RacaoCrocodilo] = [RacaoCrocodilo.FILHOTE, RacaoCrocodilo.ADULTO, RacaoCrocodilo.IDOSO]

def listar_crocodilos() -> List[Crocodilo]:
    crocodilos = [
        Crocodilo(nome="Dundee", idade=7, especie="Crocodylus"),
        Crocodilo(nome="Gena", idade=4, especie="Alligator")
    ]
    return crocodilos
