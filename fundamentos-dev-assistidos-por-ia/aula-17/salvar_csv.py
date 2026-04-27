import pandas as pd

def salvar_noticias_csv(noticias, caminho_arquivo):
    """
    Salva as notícias em um arquivo CSV usando pandas.
    :param noticias: dicionário de notícias (categoria: texto)
    :param caminho_arquivo: caminho do arquivo CSV
    """
    dados = [
        {'categoria': categoria, 'texto': texto}
        for categoria, texto in noticias.items()
        if not categoria.endswith('_status')
    ]
    df = pd.DataFrame(dados)
    df.to_csv(caminho_arquivo, index=False, encoding='utf-8')
