from typing import List
from mamiferos import Mamifero
from enum import Enum

class RacaoGato(Enum):
	FILHOTE = "ração para filhotes"
	ADULTO = "ração para adultos"
	IDOSO = "ração para idosos"

class Gato(Mamifero):
	raca: str
	racoes_gato: List[RacaoGato] = [RacaoGato.FILHOTE, RacaoGato.ADULTO, RacaoGato.IDOSO]


def listar_gatos() -> List[Gato]:
	gatos = [
		Gato(nome="Mimi", idade=4, raca="Siamês"),
		Gato(nome="Luna", idade=2, raca="Persa"),
		Gato(nome="Simba", idade=3, raca="Maine Coon")
	]
	return gatos
