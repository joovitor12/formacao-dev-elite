
import asyncio
from salvar_csv import salvar_noticias_csv

noticias = {
    "tech": "Novos avanços em IA...",
    "finance": "Mercado em alta...",
    "sports": "Final do campeonato..."
}

async def processar_noticia(categoria, texto):
    await asyncio.sleep(0.1)
    return f"{categoria} processada"

async def main():
    print("--- Investigando Orquestrador de Notícias ---")

    categorias = list(noticias.items())
    tasks = []
    for cat, txt in categorias:
        noticias[f"{cat}_status"] = "lendo"
        tasks.append(processar_noticia(cat, txt))
    await asyncio.gather(*tasks)

    # Salvar as notícias em CSV após o processamento
    salvar_noticias_csv(noticias, "noticias.csv")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        print(f"\n❌ ERRO CRÍTICO NO TERMINAL: {e}")
    except Exception as e:
        print(f"\n⚠️ Outro erro: {e}")