import requests
import time
import os

# Lê variáveis de ambiente ou usa valores padrão
HTTP_DOG_URL = os.environ.get("HTTP_DOG_URL", "https://http.dog")
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", 5))
BACKOFF_FACTOR = float(os.environ.get("BACKOFF_FACTOR", 1))

def get_http_dog_image(status_code, max_retries=MAX_RETRIES, backoff_factor=BACKOFF_FACTOR):
    url = f"{HTTP_DOG_URL}/{status_code}.jpg"
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.content  # Retorna a imagem
            else:
                print(f"Erro: status {response.status_code}")
        except requests.RequestException as e:
            print(f"Tentativa {retries+1} falhou: {e}")

        retries += 1
        sleep_time = backoff_factor * (2 ** (retries - 1))
        print(f"Aguardando {sleep_time} segundos antes de tentar novamente...")
        time.sleep(sleep_time)

    print("Número máximo de tentativas atingido.")
    return None

# Exemplo de uso:
if __name__ == "__main__":
    img = get_http_dog_image(404)
    if img:
        with open("dog_404.jpg", "wb") as f:
            f.write(img)
