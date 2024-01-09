import tkinter as tk
from tkinter import ttk
import json
import requests

class CryptoConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Criptomonedas")
        self.geometry("600x1000")
        self.configure(bg="white")

        # Variables de seguimiento para los valores de las criptomonedas
        self.from_currency_value = tk.DoubleVar()
        self.to_currency_value = tk.DoubleVar()
        self.usd_value = tk.DoubleVar()
        self.max_value = tk.DoubleVar()
        self.percentage_change = tk.DoubleVar()
        self.last_updated = tk.StringVar()
        self.currency_value = tk.DoubleVar()

        # Cargar lista de criptomonedas desde el archivo JSON
        self.load_cryptos_list()

        self.create_widgets()
        
        # Aplicar estilos personalizados
        self.style = ttk.Style()
        self.style.configure("TEntry", padding=(10, 5))  # Ajusta el espaciado interno de las entradas



    def load_cryptos_list(self):
        # Cargar la lista de criptomonedas desde el archivo JSON
        with open('criptomonedas.json') as jsonfile:
            self.criptomonedas = json.load(jsonfile)

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Conversor de Criptomonedas", font=("Arial", 16), bg="white").pack(pady=10)

        # Ventanas de colores
        self.create_crypto_frame("red", "black", "De Moneda", self.from_currency_value, 0)
        self.create_crypto_frame("black", "white", "A Moneda", self.to_currency_value, 1)
        self.create_crypto_frame("blue", "white", "Valor en USD", self.usd_value, 2)
        self.create_crypto_frame("purple", "white", "Máximo Valor Histórico", self.max_value, 3)
        self.create_crypto_frame("orange", "black", "Cambio Porcentual en 24h", self.percentage_change, 4)
        self.create_crypto_frame("yellow", "black", "Última Actualización", self.last_updated, 5)
        self.create_crypto_frame("pink", "black", "Valor de Moneda en Otra Moneda", self.currency_value, 6)

        # Comboboxes
        self.create_comboboxes()

        # Button
        tk.Button(self, text="Convertir", command=self.convert_cryptos, font=("Arial", 14), bg="lightblue").pack(pady=10)

    def create_comboboxes(self):
        # Crear comboboxes
        self.comboboxes = []
        for i in range(2):  # Crear dos comboboxes según tus necesidades
            combo_var = tk.StringVar(value=self.criptomonedas[0])  # Establecer el valor inicial
            combo = ttk.Combobox(self, textvariable=combo_var, values=self.criptomonedas)
            combo.pack(pady=5)
            self.comboboxes.append(combo)

    def create_crypto_frame(self, bg_color, text_color, text_label, value_var, row):
        frame = tk.Frame(self, bg=bg_color, padx=20, pady=20)
        frame.pack(pady=5)

        canvas = tk.Canvas(frame, width=frame.winfo_reqwidth(), height=frame.winfo_reqheight())
        canvas.pack(fill='both', expand=True)

        oval = canvas.create_oval(0, 0, frame.winfo_reqwidth(), frame.winfo_reqheight())
        canvas.tag_lower(oval)

        label = tk.Label(canvas, text=text_label, font=("Arial", 12), bg=bg_color, fg=text_color)
        label.place(relx=0.5, rely=0.1, anchor='center')

        entry = ttk.Entry(canvas, font=("Arial", 12), width=50, justify="center", textvariable=value_var, style="Rounded.TEntry")
        entry.place(relx=0.5, rely=0.5, anchor='center')
        
    def convert_cryptos(self):
        # Obtener las monedas seleccionadas en los comboboxes
        moneda1 = self.comboboxes[0].get()
        moneda2 = self.comboboxes[1].get()

        # Llamar a la función info_currency con las monedas seleccionadas
        #data = self.info_currency(moneda1, moneda2)
        data = [{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400', 'current_price': 45900, 'market_cap': 893954852685, 'market_cap_rank': 1, 'fully_diluted_valuation': 958147642134, 'total_volume': 25153394943, 'high_24h': 45977, 'low_24h': 43248, 'price_change_24h': 1750.41, 'price_change_percentage_24h': 3.96477, 'market_cap_change_24h': 29916217647, 'market_cap_change_percentage_24h': 3.46237, 'circulating_supply': 19593068.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 69045, 'ath_change_percentage': -33.93226, 'ath_date': '2021-11-10T14:24:11.849Z', 'atl': 67.81, 'atl_change_percentage': 67171.77915, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2024-01-08T18:11:32.492Z'}, {'id': 'ethereum', 'symbol': 
'eth', 'name': 'Ethereum', 'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1696501628', 'current_price': 2317.07, 'market_cap': 278639304088, 'market_cap_rank': 2, 'fully_diluted_valuation': 278639304088, 'total_volume': 22121512369, 'high_24h': 2323.35, 'low_24h': 2170.31, 'price_change_24h': 74.91, 'price_change_percentage_24h': 3.34085, 'market_cap_change_24h': 9065911550, 'market_cap_change_percentage_24h': 3.36306, 'circulating_supply': 120184188.645257, 'total_supply': 120184188.645257, 'max_supply': None, 'ath': 4878.26, 'ath_change_percentage': -52.75678, 'ath_date': '2021-11-10T14:24:19.604Z', 'atl': 0.432979, 'atl_change_percentage': 532177.05186, 'atl_date': '2015-10-20T00:00:00.000Z', 'roi': {'times': 66.44914794822482, 'currency': 'btc', 'percentage': 6644.914794822482}, 'last_updated': '2024-01-08T18:11:11.067Z'}]
        
        if data:
            # Extraer datos específicos para cada moneda
            #data_moneda1 = data[0] if data[0]['id'] == moneda1 else data[1]
            #data_moneda2 = data[0] if data[0]['id'] == moneda2 else data[1]

            # Realizar los cálculos necesarios y actualizar las variables de seguimiento
            data_moneda1 = data[0]
            valor_moneda1_en_moneda2 = data_moneda1['current_price'] / data[1]['current_price'] 
            print("Valor1:",data_moneda1['current_price'] )
            print("Valor2:",data[1]['current_price'] )
            # Tomar solo el primer elemento de la lista (moneda1)

            # Actualizar la variable de seguimiento con el valor actual de moneda1
            self.usd_value.set(data_moneda1['current_price'])
            # Actualizar las variables de seguimiento con el valor calculado
            self.max_value.set(data_moneda1['ath'])
            self.percentage_change.set(data_moneda1['price_change_percentage_24h'])
            self.last_updated.set(data_moneda1['last_updated'])
            self.currency_value.set(valor_moneda1_en_moneda2)

            # Imprimir los datos devueltos por la API
            print("Datos de la API:")
            print(json.dumps(data, indent=2))  # Imprimir en formato JSON con sangría
            print(f"Valor de {moneda1} en {moneda2}: {valor_moneda1_en_moneda2}")
        
        else:
            print("No se pudo obtener información detallada de las monedas seleccionadas.")


    @staticmethod
    def info_currency(moneda1, moneda2):
        base_url = "https://api.coingecko.com/api/v3"
        params = {
            'vs_currency': 'usd',
            'ids': f"{moneda1},{moneda2}",
            'order': 'market_cap_desc',
            'per_page': 2,
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
                data = response.json()
                #print("DATA:", data)
                return data
            else:
                print(f"Error en la solicitud HTTP. Código de estado: {response.status_code}")
        except Exception as e:
            print(f"Error en la solicitud HTTP: {e}")


""" @staticmethod
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
        print(f"Error en la solicitud HTTP: {e}")"""

"""def convert_cryptos(self):
    # Simulando datos de la API para propósitos de prueba
    data = {
        'current_price': 50000.0,
        'ath': 60000.0,
        'price_change_percentage_24h': 5.0,
        'last_updated': '2024-01-10',
        'valor_moneda1_en_moneda2': 45000.0
    }

    # Actualizando los valores en las variables de seguimiento
    self.usd_value.set(data['current_price'])
    self.max_value.set(data['ath'])
    self.percentage_change.set(data['price_change_percentage_24h'])
    self.last_updated.set(data['last_updated'])
    self.currency_value.set(data['valor_moneda1_en_moneda2'])"""

if __name__ == "__main__":
    app = CryptoConverterApp()
    app.mainloop()
    