import requests

def obtener_lista_relevante():
    # Obtener datos de CoinGecko
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "trade_volume_24h_desc",  # Ordenar por volumen de transacciones
        "per_page": 200,  # Ajustado a 200 criptomonedas
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Obtener nombres de las criptomonedas
    criptomonedas = [moneda["id"] for moneda in data]

    return criptomonedas

# Ejemplo de uso
lista_relevante = obtener_lista_relevante()
print("Lista relevante de criptomonedas:", lista_relevante)
