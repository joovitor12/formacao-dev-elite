# Mock do banco de dados
from typing import List
from models import Camisa, CamisaCreate
from enum_cores import Cor
from fastapi import APIRouter

router = APIRouter()

camisas_db: List[Camisa] = []
next_id = 1

@router.get("/")
def read_root():
    return {"message": "Bem-vindo à Loja de Roupas API!"}

@router.get("/cores", response_model=dict)
def listar_cores():
    """Lista todas as cores disponíveis"""
    return {"cores": [cor.value for cor in Cor]}

@router.post("/camisas", response_model=Camisa)
def criar_camisa(camisa: CamisaCreate):
    """Cria uma nova camisa"""
    global next_id
    nova_camisa = Camisa(
        id=next_id,
        cor=camisa.cor,
        tamanho=camisa.tamanho,
        preco=camisa.preco
    )
    camisas_db.append(nova_camisa)
    next_id += 1
    return nova_camisa

@router.get("/camisas", response_model=List[Camisa])
def listar_camisas():
    """Lista todas as camisas"""
    return camisas_db

@router.get("/camisas/{camisa_id}", response_model=Camisa)
def obter_camisa(camisa_id: int):
    """Obtém uma camisa específica pelo ID"""
    for camisa in camisas_db:
        if camisa.id == camisa_id:
            return camisa
    return {"error": "Camisa não encontrada"}

@router.get("/camisas/cor/{cor}")
def listar_camisas_por_cor(cor: Cor):
    """Lista camisas de uma cor específica"""
    camisas_filtradas = [camisa for camisa in camisas_db if camisa.cor == cor]
    return {"cor": cor.value, "camisas": camisas_filtradas}

@router.delete("/camisas/{camisa_id}")
def deletar_camisa(camisa_id: int):
    """Deleta uma camisa pelo ID"""
    global camisas_db
    camisas_db = [camisa for camisa in camisas_db if camisa.id != camisa_id]
    return {"message": f"Camisa {camisa_id} deletada"}