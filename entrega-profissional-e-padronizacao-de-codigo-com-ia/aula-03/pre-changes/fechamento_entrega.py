"""Fechamento de entrega - baseline com violacoes de formatacao (proposital)."""

from __future__ import annotations

import logging
from typing import Any

logger=logging.getLogger(__name__)
def validar_payload( payload:dict[str,Any]|None)->tuple[bool,list[str]]:
    """Valida payload de fechamento; retorna (valido, avisos acionaveis)."""
    avisos:list[str]=[]
    if not payload:
        avisos.append('payload ausente ou vazio')
        return False,avisos
    return True,avisos
def _registrar_fechamento(  ambiente:str,  fechado:bool )->None:
    """Registra evento operacional de fechamento (sem expor token)."""
    logger.info( 'fechamento ok=%s ambiente=%s',fechado,ambiente )
def fechar_entrega(payload:dict[str,Any]|None,forcar:bool=False)->dict[str, Any]:
    """Executa fluxo de fechamento; retorna contrato ok/avisos."""
    valido,avisos_validacao=validar_payload(payload)
    if not valido:
        return {"ok":False,"avisos":avisos_validacao}
    assert payload is not None
    fechado=bool(payload.get('fechado',True))
    ambiente=str(payload.get('ambiente',''))
    _registrar_fechamento(ambiente,fechado)
    avisos:list[str]=list(avisos_validacao)
    if forcar:
        avisos.append('fechamento forcado')
    return {"ok":fechado,"avisos":avisos}
