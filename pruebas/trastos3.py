import json
import tkinter as tk
from tkinter import ttk

# Cargar la lista de criptomonedas desde el archivo JSON
with open('criptomonedas.json') as jsonfile:
    criptomonedas = json.load(jsonfile)

# Función para manejar la selección de las criptomonedas en los combobox
def on_combobox_select(event):
    selected_cryptos = [combo.get() for combo in comboboxes]
    # Aquí puedes realizar cualquier acción que necesites con las criptomonedas seleccionadas
    print("Criptomonedas seleccionadas:", selected_cryptos)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Seleccionar Criptomonedas")

# Crear comboboxes
comboboxes = []
for i in range(2):  # Crear dos comboboxes según tus necesidades
    combo_var = tk.StringVar(value=criptomonedas[0])  # Establecer el valor inicial
    combo = ttk.Combobox(root, textvariable=combo_var, values=criptomonedas)
    combo.grid(row=i, column=0, padx=10, pady=10)
    comboboxes.append(combo)

# Asociar la función de manejo de selección al evento <<ComboboxSelected>>
for combo in comboboxes:
    combo.bind("<<ComboboxSelected>>", on_combobox_select)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
