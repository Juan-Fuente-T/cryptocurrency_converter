import tkinter as tk
from tkinter import ttk

class CryptoConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Criptomonedas")
        self.geometry("600x400")
        self.configure(bg="white")

        # Variables de seguimiento para los valores de las criptomonedas
        self.from_currency_value = tk.DoubleVar()
        self.to_currency_value = tk.DoubleVar()
        self.usd_value = tk.DoubleVar()
        self.max_value = tk.DoubleVar()
        self.percentage_change = tk.DoubleVar()
        self.last_updated = tk.StringVar()
        self.currency_value = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Conversor de Criptomonedas", font=("Arial", 16), bg="white").pack(pady=10)

        # Ventanas de colores
        self.create_crypto_frame("red", "black", "De Moneda", self.from_currency_value)
        self.create_crypto_frame("green", "white", "A Moneda", self.to_currency_value)
        self.create_crypto_frame("blue", "white", "Valor en USD", self.usd_value)
        self.create_crypto_frame("purple", "white", "Máximo Valor Histórico", self.max_value)
        self.create_crypto_frame("orange", "black", "Cambio Porcentual en 24h", self.percentage_change)
        self.create_crypto_frame("yellow", "black", "Última Actualización", self.last_updated)
        self.create_crypto_frame("pink", "black", "Valor de Moneda en Otra Moneda", self.currency_value)

        # Button
        tk.Button(self, text="Convertir", command=self.convert_cryptos, font=("Arial", 14), bg="lightblue").pack(pady=10)

    def create_crypto_frame(self, bg_color, text_color, text_label, value_var):
        frame = tk.Frame(self, bg=bg_color, padx=20, pady=20)
        frame.pack(pady=5)

        label = tk.Label(frame, text=text_label, font=("Arial", 12), bg=bg_color, fg=text_color)
        label.pack(side=tk.TOP, pady=5)

        entry = tk.Entry(frame, font=("Arial", 12), justify="center", textvariable=value_var)
        entry.pack(side=tk.BOTTOM, padx=10)

    def convert_cryptos(self):
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
        self.currency_value.set(data['valor_moneda1_en_moneda2'])

if __name__ == "__main__":
    app = CryptoConverterApp()
    app.mainloop()