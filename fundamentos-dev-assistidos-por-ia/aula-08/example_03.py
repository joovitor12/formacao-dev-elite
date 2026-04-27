from datetime import datetime

def calcular_idade_anos(data_nascimento_str):
    """
    Calcula a idade em anos a partir de uma string de data de nascimento.
    Aceita formatos como 'dd/mm/yyyy', 'yyyy-mm-dd', 'yyyy/mm/dd', etc.
    """
    
    formatos = [
        '%d/%m/%Y', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%m/%d/%Y', '%m-%d-%Y', '%Y.%m.%d', '%d.%m.%Y'
    ]
    for fmt in formatos:
        try:
            data_nasc = datetime.strptime(data_nascimento_str, fmt)
            hoje = datetime.now()
            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
            return idade
        except Exception:
            continue
    # Tenta extrair o ano manualmente se todos os formatos falharem
    try:
        partes = [int(p) for p in data_nascimento_str.replace('-', '/').replace('.', '/').split('/') if p.isdigit()]
        if len(partes) == 3:
            ano = max(partes) if max(partes) > 31 else partes[-1]
        elif len(partes) == 1:
            ano = partes[0]
        else:
            raise ValueError
        return datetime.now().year - ano
    except Exception:
        raise ValueError('Formato de data inválido. Use formatos como dd/mm/yyyy, yyyy-mm-dd, etc.')


# Exemplo de uso
data_nascimento = "30/02/2002"
idade = calcular_idade_anos(data_nascimento)
print(f"A idade calculada é: {idade} anos")