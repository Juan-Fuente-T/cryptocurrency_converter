import requests
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

"""def info_currency(moneda1, moneda2):
    # URL base de la API de CoinGecko
    base_url = "https://api.coingecko.com/api/v3"

    # Parámetros para obtener detalles de una moneda específica y el valor en USD de todas las monedas
    params = {
        'vs_currency': 'usd',
        'ids': f"{moneda1},{moneda2}",
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': False,
        'localization': False,
        'tickers': True,
        'community_data': False,
        'developer_data': False
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{base_url}/coins/markets", params=params)

        # Verificar si la llamada fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON
            data = response.json()

            # Filtrar la información para obtener detalles de moneda1
            info_moneda1 = next((m for m in data if m['id'] == moneda1), None)

            # Filtrar la información para obtener el precio actual de moneda1 en USD
            precio_moneda1_usd = info_moneda1['current_price']

            # Filtrar la información para obtener el precio actual de moneda2 en USD
            precio_moneda2_usd = next((m['current_price'] for m in data if m['id'] == moneda2), None)

            # Calcular el valor de moneda1 en moneda2
            valor_moneda1_en_moneda2 = precio_moneda1_usd / precio_moneda2_usd if precio_moneda2_usd else None

            return info_moneda1, valor_moneda1_en_moneda2

    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None"""



class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Crypto App")
        self.iconbitmap("visualmoney.ico")
        self.geometry("600x600+100+100")
        self.configure(bg="alice blue")

        self.style = ttk.Style()
        self.style.configure('My.TButton', font=('Arial', 12))
        self.style.configure('My.TEntry', font=('Arial Black', 18))
        self.style.configure('My.TCombobox', font=('Arial Black', 8))

        self.create_input_fields()
        self.create_submit_button()

    def create_input_fields(self):
        self.moneda1_entry = ttk.Entry(self, style='My.TEntry')
        self.moneda2_entry = ttk.Entry(self, style='My.TEntry')

        self.moneda1_entry.place(x=480, y=180, anchor="center")
        self.moneda2_entry.place(x=120, y=180, anchor="center")

    def create_submit_button(self):
        submit_button = ttk.Button(self, text="Obtener Datos", command=self.obtener_datos, style='My.TButton')
        submit_button.place(x=300, y=265, anchor="center")

    def create_result_window(self, title, data):
        resultado_window = tk.Toplevel()
        resultado_window.title(title)
        resultado_window.geometry("300x150")
        resultado_window.configure(bg="lightgray")

        label_outside = ttk.Label(resultado_window, text=f"{title}:", font=("Arial", 12), background="lightgray")
        label_outside.pack(pady=10)

        label_inside = ttk.Label(resultado_window, text=data, font=("Arial", 12), background="lightgray")
        label_inside.pack(pady=10)

    @staticmethod
    def info_currency(moneda1, moneda2):
        base_url = "https://api.coingecko.com/api/v3"
        params = {
            'vs_currency': 'usd',
            'ids': f"{moneda1},{moneda2}",
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
            'sparkline': False,
            'localization': False,
            'tickers': True,
            'community_data': False,
            'developer_data': False
        }

        try:
            response = requests.get(f"{base_url}/coins/markets", params=params)
            if response.status_code == 200:
                data = response.json()[0]  # Tomar solo el primer elemento del resultado

                # Mostrar solo los datos específicos y crear ventanas personalizadas para cada uno
                CryptoApp.create_result_window("Valor en USD", data['current_price'])
                CryptoApp.create_result_window("Máximo Valor Histórico", data['ath'])
                CryptoApp.create_result_window("Cambio Porcentual en 24h", data['price_change_percentage_24h'])
                CryptoApp.create_result_window("Última Actualización", data['last_updated'])
                CryptoApp.create_result_window("Valor de Moneda en Otra Moneda", data['valor_moneda1_en_moneda2'])

        except Exception as e:
            print(f"Error al obtener datos: {e}")

    def obtener_datos(self):
        moneda1 = self.moneda1_entry.get()
        moneda2 = self.moneda2_entry.get()

        if moneda1 and moneda2:
            self.info_currency(moneda1, moneda2)
            
        def convert_cryptos(self):
        # Obtener las monedas seleccionadas en los comboboxes
        moneda1 = self.comboboxes[0].get()
        moneda2 = self.comboboxes[1].get()

        # Llamar a la función info_currency con las monedas seleccionadas
        data = self.info_currency(moneda1, moneda2)

        # Imprimir los datos devueltos por la API
        print("Datos de la API:")
        print(json.dumps(data, indent=2))  # Imprimir en formato JSON con sangría

        # Actualizando los valores en las variables de seguimiento
        self.usd_value.set(data['current_price'])
        self.max_value.set(data['ath'])
        self.percentage_change.set(data['price_change_percentage_24h'])
        self.last_updated.set(data['last_updated'])
        self.currency_value.set(data['valor_moneda1_en_moneda2'])

    @staticmethod
    def info_currency(moneda1, moneda2):
        base_url = "https://api.coingecko.com/api/v3"
        params = {
            'vs_currency': 'usd',
            'ids': f"{moneda1},{moneda2}",
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
            'sparkline': False,
            'localization': False,
            'tickers': True,
            'community_data': False,
            'developer_data': False
        }

        try:
            response = requests.get(f"{base_url}/coins/markets", params=params)
            if response.status_code == 200:
                data = response.json()[0]  # Tomar solo el primer elemento del resultado
                return data
            else:
                print(f"Error en la solicitud HTTP. Código de estado: {response.status_code}")
        except Exception as e:
            print(f"Error en la solicitud HTTP: {e}")  

if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()


    

"""class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Crypto App")
        self.geometry("600x400+100+100")
        self.configure(bg="white")

        self.label_valor_ethereum = tk.Label(self, text="Valor de Ethereum:", font=("Arial", 12), bg="white")
        self.label_cambio_porcentual = tk.Label(self, text="Cambio 24h:", font=("Arial", 12), bg="white")
        self.label_valor_historico_maximo = tk.Label(self, text="Valor histórico máximo:", font=("Arial", 12), bg="white")
        self.label_ultima_actualizacion = tk.Label(self, text="Ultima actualización:", font=("Arial", 12), bg="white")
        self.label_valor_ethereum_en_btc = tk.Label(self, text="Valor de Ethereum en Bitcoin:", font=("Arial", 12), bg="white")

        self.label_valor_ethereum.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.label_cambio_porcentual.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.label_valor_historico_maximo.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.label_ultima_actualizacion.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.label_valor_ethereum_en_btc.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        # Ejemplo de datos (puedes reemplazar esto con tus datos reales)
        info_eth = {
            'current_price': 2229.37,
            'price_change_percentage_24h': -0.41298,
            'ath': {'usd': 4878.26},
            'last_updated': '2024-01-08T11:05:11.136Z'
        }
        valor_eth_en_btc = 0.05054229295608606

        self.mostrar_datos(info_eth, valor_eth_en_btc)

    def mostrar_datos(self, info_eth, valor_eth_en_btc):
        self.label_valor_ethereum.config(text=f"Valor de Ethereum: {info_eth['current_price']}")
        self.label_cambio_porcentual.config(text=f"Cambio 24h: {info_eth['price_change_percentage_24h']}%")

        # Acceder al valor histórico máximo
        valor_historico_maximo = info_eth.get('ath', 'No disponible')
        if isinstance(valor_historico_maximo, dict):
            valor_historico_maximo = valor_historico_maximo.get('usd', 'No disponible')
        self.label_valor_historico_maximo.config(text=f"Valor histórico máximo: {valor_historico_maximo}")

        self.label_ultima_actualizacion.config(text=f"Ultima actualización: {info_eth['last_updated']}")
        self.label_valor_ethereum_en_btc.config(text=f"Valor de Ethereum en Bitcoin: {valor_eth_en_btc}")

# Crear y ejecutar la aplicación
app = CryptoApp()
app.mainloop() """

"""
# Función para manejar el botón de obtener datos
def input_data():
    moneda1 = entrada_moneda1.get()
    moneda2 = entrada_moneda2.get()

    info_moneda1, valor_moneda1_en_moneda2 = info_currency(moneda1, moneda2)

    if info_moneda1 and valor_moneda1_en_moneda2 is not None:
        # Actualizar las etiquetas en la ventana de resultados
        etiqueta_valor_actual.config(text=f'Valor actual de {moneda1}: ${info_moneda1["current_price"]}')
        etiqueta_cambio_porcentual.config(text=f'Cambio porcentual en 24 horas: {info_moneda1["price_change_percentage_24h"]}%')
        
        # Acceder al valor histórico máximo, teniendo en cuenta que puede ser un número directo
        valor_historico_maximo = info_moneda1.get('ath', 'No disponible')
        if isinstance(valor_historico_maximo, dict):
            valor_historico_maximo = valor_historico_maximo.get('usd', 'No disponible')
        etiqueta_valor_historico.config(text=f'Valor histórico máximo de {moneda1}: ${valor_historico_maximo}')
        
        etiqueta_ultima_actualizacion.config(text=f'Última actualización de {moneda1}: {info_moneda1["last_updated"]}')

        # Mostrar la segunda ventana con el valor de moneda1 en moneda2
        ventana_moneda2.deiconify()
        etiqueta_valor_moneda2.config(text=f'Valor de {moneda1} en {moneda2}: {valor_moneda1_en_moneda2}')
    else:
        etiqueta_resultados.config(text='No se pudo obtener la información necesaria.')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Consulta de Criptomonedas')

# Crear y colocar los widgets en la ventana principal
etiqueta_instrucciones = ttk.Label(ventana, text='Ingrese el nombre de la moneda:')
etiqueta_instrucciones.grid(row=0, column=0, padx=10, pady=10)

entrada_moneda1 = ttk.Entry(ventana)
entrada_moneda1.grid(row=0, column=1, padx=10, pady=10)

etiqueta_instrucciones2 = ttk.Label(ventana, text='Ingrese otra moneda:')
etiqueta_instrucciones2.grid(row=1, column=0, padx=10, pady=10)

entrada_moneda2 = ttk.Entry(ventana)
entrada_moneda2.grid(row=1, column=1, padx=10, pady=10)

boton_obtener_datos = ttk.Button(ventana, text='Obtener Datos', command=obtener_datos)
boton_obtener_datos.grid(row=2, column=0, columnspan=2, pady=10)

# Ventana para mostrar los resultados
ventana_resultados = tk.Toplevel(ventana)
ventana_resultados.title('Resultados')
ventana_resultados.withdraw()  # Ocultar la ventana al inicio

etiqueta_valor_actual = ttk.Label(ventana_resultados, text='')
etiqueta_valor_actual.pack(padx=10, pady=10)

etiqueta_cambio_porcentual = ttk.Label(ventana_resultados, text='')
etiqueta_cambio_porcentual.pack(padx=10, pady=10)

etiqueta_valor_historico = ttk.Label(ventana_resultados, text='')
etiqueta_valor_historico.pack(padx=10, pady=10)

etiqueta_ultima_actualizacion = ttk.Label(ventana_resultados, text='')
etiqueta_ultima_actualizacion.pack(padx=10, pady=10)

# Ventana para mostrar el valor de moneda1 en moneda2
ventana_moneda2 = tk.Toplevel(ventana)
ventana_moneda2.title('Valor de Moneda1 en Moneda2')
ventana_moneda2.withdraw()  # Ocultar la ventana al inicio

etiqueta_valor_moneda2 = ttk.Label(ventana_moneda2, text='')
etiqueta_valor_moneda2.pack(padx=10, pady=10)

# Ajustar la expansión de las filas y columnas
ventana.rowconfigure(3, weight=1)
ventana.columnconfigure(0, weight=1)

# Iniciar el bucle principal de la aplicación
ventana.mainloop() """



# Ejemplo de uso para obtener información sobre Ethereum (ETH) y el valor de ETH en Bitcoin (BTC)
"""info_eth, valor_eth_en_btc = info_currency("ethereum", "bitcoin")

if info_eth and valor_eth_en_btc is not None:
    print(f"Valor de Ethereum: {info_eth['current_price']}")
    print(f"Price_change_percentage_24h: {info_eth['price_change_percentage_24h']}")
    # Acceder al valor histórico máximo, teniendo en cuenta que puede ser un número directo
    valor_historico_maximo = info_eth.get('ath', 'No disponible')
    if isinstance(valor_historico_maximo, dict):
        valor_historico_maximo = valor_historico_maximo.get('usd', 'No disponible')

    print(f"Valor historico máximo: {valor_historico_maximo}")
    print(f"Ultima actualizacion: {info_eth['last_updated']}")
    
    print(f"Valor de Ethereum en Bitcoin: {valor_eth_en_btc}")
else:
    print("No se pudo obtener la información necesaria.")"""