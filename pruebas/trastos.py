import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Divisas")
        self.geometry("600x400")
        self.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Conversor de Divisas", font=("Arial", 16), bg="white").pack(pady=10)

        tk.Label(self, text="Moneda 1:", font=("Arial", 12), bg="white").pack(pady=5)
        self.create_currency_frame("Moneda 1", "red", "black")

        tk.Label(self, text="Moneda 2:", font=("Arial", 12), bg="white").pack(pady=5)
        self.create_currency_frame("Moneda 2", "black", "white")

        # Button
        tk.Button(self, text="Convertir", command=self.convert_currencies, font=("Arial", 14), bg="lightblue").pack(pady=10)

    def create_currency_frame(self, currency_name, bg_color, text_color):
        frame = tk.Frame(self, bg=bg_color, padx=20, pady=20)
        frame.pack(pady=5)

        tk.Label(frame, text=f"{currency_name}:", font=("Arial", 12), bg=bg_color, fg=text_color).pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=("Arial", 12), justify="center")
        entry.pack(side=tk.LEFT, padx=10)

        setattr(self, f"{currency_name.lower().replace(' ', '_')}_entry", entry)

    def convert_currencies(self):
        currency1_value = float(self.moneda_1_entry.get())
        currency2_value = self.convert_currency(currency1_value)
        self.moneda_2_entry.delete(0, tk.END)
        self.moneda_2_entry.insert(tk.END, f"{currency2_value:.2f}")

    def convert_currency(self, value):
        # Aquí puedes implementar la lógica de conversión de una moneda a otra
        # Puedes usar un factor fijo o hacer llamadas a una API para obtener tasas en tiempo real
        # Por ahora, simplemente devolvemos el doble del valor para demostrar la funcionalidad
        return value * 2

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()