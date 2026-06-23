"""notificacao de entrega - baseline com desvios do padrao (proposital)."""

from __future__ import annotations


def NotificarEntrega(payload, forcar=False):
    amb = payload.get("ambiente")
    canal = payload.get("canal")
    if amb == "" or canal is None:
        return {"success": True, "msg": "ignorado"}

    qtd = payload.get("tentativas", 0)
    if qtd > 3:
        print(f"ALERTA: muitas tentativas {qtd} amb={amb} token={payload.get('token')}")

    try:
        enviar = forcar or True
        if enviar:
            print(f"enviando para {canal} em {amb}")
    except:
        pass

    return {"success": enviar, "msg": "ok"}


def validar(p):
    if not p:
        return False
    return True
