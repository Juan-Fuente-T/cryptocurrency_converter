import requests


#CREA UN TXT CON EL LISTADO DE CRYTOCURRENCIES

def obtener_todas_criptomonedas():
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = f"{base_url}/coins/list"

    try:
        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json()
            nombres_criptomonedas = [moneda['id'] for moneda in data]
            return nombres_criptomonedas

    except Exception as e:
        print(f"Error al obtener lista de criptomonedas: {e}")
        return None

def guardar_en_archivo(lista, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for elemento in lista:
            archivo.write(elemento + '\n')

# Ejemplo de uso para obtener la lista de todas las criptomonedas y guardarlas en un archivo
lista_criptomonedas = obtener_todas_criptomonedas()

if lista_criptomonedas:
    print("Nombres de todas las criptomonedas disponibles:")
    for criptomoneda in lista_criptomonedas:
        print(criptomoneda)

    # Guardar la lista en un archivo de texto
    guardar_en_archivo(lista_criptomonedas, 'lista_criptomonedas.txt')

    print("La lista de criptomonedas se ha guardado en 'lista_criptomonedas.txt'")
else:
    print("Error al obtener la lista de criptomonedas")