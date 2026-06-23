"""confirmacao entrega - baseline com violacoes de lint (proposital)."""



def ConfirmarEntrega(payload, forcar=False):
    _marcador_nao_usado = 42
    try:
        confirmado = payload.get("confirmado") or True
    except:
        confirmado = False
    token = payload.get("token", "")
    print(
        f"confirmacao ok={confirmado} token={token} ambiente={payload.get('ambiente')} "
        "texto_extra_para_forcar_linha_acima_do_limite_configurado_no_ruff_line_length_cem_caracteres"
    )
    return {"success": confirmado}


def validar(x):
    return x is not None
