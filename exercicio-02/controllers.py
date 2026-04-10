from fastapi import APIRouter
from services import btc_usd_to_brl, buscar_preco_btc_usd_service, usd_to_brl
router = APIRouter()

@router.get("/preco-btc-usd")
def buscar_preco_btc_usd():
    """Busca o preço do Bitcoin em USD na API do Mercado Bitcoin"""
    return buscar_preco_btc_usd_service()

@router.get("/cotacao-usd-brl")
def cotacao_usd_brl():
    """Busca a cotação de USD para BRL na API de Câmbio"""
    return usd_to_brl()

@router.get("/preco-btc-brl")
def preco_btc_brl():
    """Calcula o preço do Bitcoin em BRL usando o preço em USD e a cotação de USD para BRL"""
    return btc_usd_to_brl()