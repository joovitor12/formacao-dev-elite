from typing import List
from mamiferos import Mamifero
from enum import Enum

class RacaoCachorro(Enum):
	FILHOTE = "ração para filhotes"
	ADULTO = "ração para adultos"
	IDOSO = "ração para idosos"

class Cachorro(Mamifero):
	raca: str
	racoes_cachorro: List[RacaoCachorro] = [RacaoCachorro.FILHOTE, RacaoCachorro.ADULTO, RacaoCachorro.IDOSO]


def listar_cachorros() -> List[Cachorro]:
	cachorros = [
		Cachorro(nome="Rex", idade=5, raca="Labrador"),
		Cachorro(nome="Bolt", idade=3, raca="Poodle"),
		Cachorro(nome="Luna", idade=2, raca="Bulldog")
	]
	return cachorros
