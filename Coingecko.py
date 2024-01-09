import requests
from ttkthemes import ThemedStyle


def obtener_datos_moneda(moneda_id):
    # Endpoint para obtener datos de una criptomoneda específica
    endpoint = f'https://api.coingecko.com/api/v3/coins/{moneda_id}'

    # Parámetros opcionales para obtener más detalles
    params = {
        'localization': False,
        'tickers': True,
        'market_data': True,
        'community_data': False,
        'developer_data': False,
        'sparkline': True
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        print("Data:" ,data)

        # Obtener el cambio porcentual en 24 horas
        cambio_porcentual_24h = data['market_data']['price_change_percentage_24h']

        # Obtener el valor histórico máximo
        valor_historico_maximo = data['market_data']['ath']['usd']

        # Obtener el precio actual
        precio_actual = data['market_data']['current_price']['usd']
        

        # Devolver los resultados
        return cambio_porcentual_24h, valor_historico_maximo, precio_actual

    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

# Ejemplo de uso
moneda_id_ejemplo = 'bitcoin'
resultados = obtener_datos_moneda(moneda_id_ejemplo)

if resultados:
    cambio_porcentual, valor_maximo, precio_actual = resultados
    print(f'Cambio porcentual en 24 horas: {cambio_porcentual}%')
    print(f'Valor histórico máximo: ${valor_maximo}')
    print(f'Precio actual: ${precio_actual}')