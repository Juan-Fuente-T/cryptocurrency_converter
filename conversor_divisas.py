import tkinter as tk
from tkinter import messagebox  #se importa messagebox para mostrar mensaje de error
from tkinter import ttk #ttk es necesario para los desplegables combobox 
import requests #se necesita requests instalado con pip para hacer llamada a la API de conversion
from decouple import config #importacion para mantener las claves seguras

                        #//////////////////////////////////////#
                        #                                      #
                        ###      CONVERSOR DE DIVISAS    ###    
                        #                                      #
                        #//////////////////////////////////////#



                            #CONVERSOR DE DIVISAS v1.0
"""
Esta aplicación multiplataforma (Windows, Linux, Mac) convierte una cantidad de una moneda en codigo ISO, por ejemplo EUR (euros), en el valor correspondiente en otra divisa, por ejemplo USD (dolares americanos), y opera mediante interfaz alfanumérica en el terminal del sistema operativo :
"""
# ©2023 Conversor de divisas  Juan Fuente

"""Novedades de la versión 1.0
- Eliminacion de lista de divisas de prueba e implementacion de la llamada a la API para obtener valores de conversión en tiempo real
- Se termina la documentacion
"""

#Listado de funciones: calcular_divisa (toma los valores de las monedas y realiza el cambio), mostrar_resultado(gestiona el modo en que se van a mostrar los resultados), n_cantidad_focus_in(), bind_combobox_events



class ConversorDivisas(tk.Tk): 
   
      #BLOQUE DE CAPTURA DE DATOS MEDIANTE API
    api_key = config("API_KEY")      
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}" #url que sirve los datos

    json_divisas = requests.get(url) #se realiza la llamada a los datos de la url de la api
    divisas = json_divisas.json() #se guardan los datos de las conversiones en un archivo json

    keys = list(divisas['rates'].keys()) #se cogen los nombres de las divisas y se meten en una lista donde poder comparar si están las elegidas por el usuario

    #diccionario de divisas ordenadas alfabeticamente por su nombre en castellano, de aqui se obtiene el indice para obtener el valor correspondiente en el diccionario divisas
    listado_currencies = [('Afgani afgano', 'AFN'), ('Baht tailandés', 'THB'), ('Balboa panameño', 'PAB'), ('Birr etíope', 'ETB'), ('Bitcoin', 'BTC'), ('Boliviano boliviano', 'BOB'), ('Cedi ghanés', 'GHS'), ('Chelín keniano', 'KES'), ('Chelín somalí', 'SOS'), ('Colon costarricense', 'CRC'), ('Colón salvadoreño', 'SVC'), ('Corona checa', 'CZK'), ('Corona danesa', 'DKK'), ('Corona islandesa', 'ISK'), ('Corona noruega', 'NOK'), ('Corona sueca', 'SEK'), ('Dalasi gambiano', 'GMD'), ('Denar macedonio', 'MKD'), ('Dinar argelino', 'DZD'), ('Dinar bahreiní', 'BHD'), ('Dinar iraquí', 'IQD'), ('Dinar jordano', 'JOD'), ('Dinar kuwaití', 'KWD'), 
    ('Dinar libio', 'LYD'), ('Dinar serbio', 'RSD'), ('Dinar tunecino', 'TND'), ('Dólar americano', 'USD'), ('Dólar australiano', 'AUD'), ('Dólar beliceño', 'BZD'), ('Dólar canadiense', 'CAD'), ('Dólar de Barbados', 'BBD'), ('Dólar de Bermudas', 'BMD'), ('Dólar de Brunéi', 'BND'), ('Dólar de Fiyi', 'FJD'), ('Dólar de Hong Kong', 'HKD'), ('Dólar de las Islas Salomón', 'SBD'), ('Dólar de las Bahamas', 'BSD'), ('Dólar de Nueva Zelanda', 'NZD'), ('Dólar de Singapur', 'SGD'), ('Dólar guyanés', 'GYD'), ('Dólar jamaiquino', 'JMD'), ('Dólar liberiano', 'LRD'), ('Dólar namibio', 'NAD'), ('Dólar surinamés', 'SRD'), ('Dólar trinitense', 'TTD'), ('Dong vietnamita', 'VND'), ('Escudo caboverdiano', 'CVE'), ('Euro', 'EUR'), ('Florín de Aruba', 'AWG'), ('Florín de las Antillas Neerlandesas', 'ANG'), ('Franco burundés', 'BIF'), ('Franco CFA de África Central', 'XAF'), ('Franco CFA de África Occidental', 'XOF'), ('Franco CFP', 'XPF'), ('Franco comorense', 'KMF'), ('Franco congoleño', 'CDF'), ('Franco guineano', 'GNF'), ('Gourde haitiano', 'HTG'), ('Guaraní paraguayo', 'PYG'), ('Hryvnia ucraniano', 'UAH'), ('Kip laosiano', 'LAK'), ('Kuna croata', 'HRK'), ('Kwacha malauí', 'MWK'), ('Kwacha zambiano', 'ZMW'), ('Kwanza angoleño', 'AOA'), 
    ('Kyat birmano', 'MMK'), ('Lari georgiano', 'GEL'), ('Lek albanés', 'ALL'), ('Lempira hondureño', 'HNL'), ('Leone sierraleonés', 'SLL'), ('Lev búlgaro', 'BGN'), ('Libra egipcia', 'EGP'), ('Libra esterlina', 'GBP'), ('Libra sudanesa', 'SDG'), ('Libra siria', 'SYP'), ('Libra sursudanesa', 'SSP'), ('Lilangeni suazi', 'SZL'), ('Loti lesothense', 'LSL'), 
    ('Manat azerbaiyano', 'AZN'), ('Metical mozambiqueño', 'MZN'), ('Naira nigeriano', 'NGN'), ('Nakfa eritreo', 'ERN'), ('Ngultrum butanés', 'BTN'), ('Ouguiya mauritano', 'MRU'), 
    ('Pataca de Macao', 'MOP'), ('Peso argentino', 'ARS'), ('Peso chileno', 'CLP'), ('Peso colombiano', 'COP'), ('Peso cubano', 'CUP'), ('Peso dominicano', 'DOP'), ('Peso filipino', 'PHP'), ('Peso mexicano', 'MXN'), ('Peso uruguayo', 'UYU'), ('Pula botsuano', 'BWP'), 
    ('Qatar Rial catarí', 'QAR'), ('Quetzal guatemalteco', 'GTQ'), ('Rand sudafricano', 'ZAR'), ('Real brasileño', 'BRL'), ('Renminbi chino', 'CNY'), ('Rial iraní', 'IRR'), ('Rial omaní', 'OMR'), ('Riel camboyano', 'KHR'), ('Ringgit malayo', 'MYR'), ('Rublo bielorruso', 'BYN'), ('Rublo ruso', 'RUB'), ('Rufiyaa maldiva', 'MVR'), ('Rupia de las Seychelles', 'SCR'), ('Rupia india', 'INR'), ('Rupia indonesia', 'IDR'), ('Rupia mauriciana', 'MUR'), ('Rupia nepalesa', 'NPR'), ('Rupia pakistaní', 'PKR'), ('Ryazan ruso', 'AMD'), ('Taka bangladesí', 'BDT'), ('Tenge kazajo', 'KZT'), ('Tugrik mongol', 'MNT'), ('Vatu vanuatuense', 'VUV'), ('Won norcoreano', 'KPW'), ('Won surcoreano', 'KRW'), ('Yen japonés', 'JPY'), ('Yuan chino', 'CNY'), ('Zloty polaco', 'PLN')]


    diccionario_currencies = { #diccionario para mostrar en los desplegables combobox de la interfaz gráfica
        'Afgani afgano': 'AFN',
        'Baht tailandés': 'THB',
        'Balboa panameño': 'PAB',
        'Birr etíope': 'ETB',
        'Bitcoin': 'BTC',
        'Boliviano boliviano': 'BOB',
        'Cedi ghanés': 'GHS',
        'Chelín keniano': 'KES',
        'Chelín somalí': 'SOS',
        'Colon costarricense': 'CRC',
        'Colón salvadoreño': 'SVC',
        'Corona checa': 'CZK',
        'Corona danesa': 'DKK',
        'Corona islandesa': 'ISK',
        'Corona noruega': 'NOK',
        'Corona sueca': 'SEK',
        'Dalasi gambiano': 'GMD',
        'Denar macedonio': 'MKD',
        'Dinar argelino': 'DZD',
        'Dinar bahreiní': 'BHD',
        'Dinar iraquí': 'IQD',
        'Dinar jordano': 'JOD',
        'Dinar kuwaití': 'KWD',
        'Dinar libio': 'LYD',
        'Dinar serbio': 'RSD',
        'Dinar tunecino': 'TND',
        'Dólar americano': 'USD',
        'Dólar australiano': 'AUD',
        'Dólar beliceño': 'BZD',
        'Dólar canadiense': 'CAD',
        'Dólar de Barbados': 'BBD',
        'Dólar de Bermudas': 'BMD',
        'Dólar de Brunéi': 'BND',
        'Dólar de Fiyi': 'FJD',
        'Dólar de Hong Kong': 'HKD',
        'Dólar de las Islas Salomón': 'SBD',
        'Dólar de las Bahamas': 'BSD',
        'Dólar de Nueva Zelanda': 'NZD',
        'Dólar de Singapur': 'SGD',
        'Dólar guyanés': 'GYD',
        'Dólar jamaiquino': 'JMD',
        'Dólar liberiano': 'LRD',
        'Dólar namibio': 'NAD',
        'Dólar surinamés': 'SRD',
        'Dólar trinitense': 'TTD',
        'Dong vietnamita': 'VND',
        'Escudo caboverdiano': 'CVE',
        'Euro': 'EUR',
        'Florín de Aruba': 'AWG',
        'Florín de las Antillas Neerlandesas': 'ANG',
        'Franco burundés': 'BIF',
        'Franco CFA de África Central': 'XAF',
        'Franco CFA de África Occidental': 'XOF',
        'Franco CFP': 'XPF',
        'Franco comorense': 'KMF',
        'Franco congoleño': 'CDF',
        'Franco guineano': 'GNF',
        'Gourde haitiano': 'HTG',
        'Guaraní paraguayo': 'PYG',
        'Hryvnia ucraniano': 'UAH',
        'Kip laosiano': 'LAK',
        'Kuna croata': 'HRK',
        'Kwacha malauí': 'MWK',
        'Kwacha zambiano': 'ZMW',
        'Kwanza angoleño': 'AOA',
        'Kyat birmano': 'MMK',
        'Lari georgiano': 'GEL',
        'Lek albanés': 'ALL',
        'Lempira hondureño': 'HNL',
        'Leone sierraleonés': 'SLL',
        'Lev búlgaro': 'BGN',
        'Libra egipcia': 'EGP',
        'Libra esterlina': 'GBP',
        'Libra sudanesa': 'SDG',
        'Libra siria': 'SYP',
        'Libra sursudanesa': 'SSP',
        'Lilangeni suazi': 'SZL',
        'Loti lesothense': 'LSL',
        'Manat azerbaiyano': 'AZN',
        'Metical mozambiqueño': 'MZN',
        'Naira nigeriano': 'NGN',
        'Nakfa eritreo': 'ERN',
        'Ngultrum butanés': 'BTN',
        'Ouguiya mauritano': 'MRU',
        'Pataca de Macao': 'MOP',
        'Peso argentino': 'ARS',
        'Peso chileno': 'CLP',
        'Peso colombiano': 'COP',
        'Peso cubano': 'CUP',
        'Peso dominicano': 'DOP',
        'Peso filipino': 'PHP',
        'Peso mexicano': 'MXN',
        'Peso uruguayo': 'UYU',
        'Pula botsuano': 'BWP',
        'Qatar Rial catarí': 'QAR',
        'Quetzal guatemalteco': 'GTQ',
        'Rand sudafricano': 'ZAR',
        'Real brasileño': 'BRL',
        'Renminbi chino': 'CNY',
        'Rial iraní': 'IRR',
        'Rial omaní': 'OMR',
        'Riel camboyano': 'KHR',
        'Ringgit malayo': 'MYR',
        'Rublo bielorruso': 'BYN',
        'Rublo ruso': 'RUB',
        'Rufiyaa maldiva': 'MVR',
        'Rupia de las Seychelles': 'SCR',
        'Rupia india': 'INR',
        'Rupia indonesia': 'IDR',
        'Rupia mauriciana': 'MUR',
        'Rupia nepalesa': 'NPR',
        'Rupia pakistaní': 'PKR',
        'Ryazan ruso': 'AMD',
        'Taka bangladesí': 'BDT',
        'Tenge kazajo': 'KZT',
        'Tugrik mongol': 'MNT',
        'Vatu vanuatuense': 'VUV',
        'Won norcoreano': 'KPW',
        'Won surcoreano': 'KRW',
        'Yen japonés': 'JPY',
        'Yuan chino': 'CNY',
        'Zloty polaco': 'PLN'
    }


    def __init__(self):  # Constructor de la clase
        super().__init__()  

        self.title("Conversor de Divisas") #titulo de la aplicacion
        self.iconbitmap("conversor_divisas.ico") #icono de la aplicacion
        self.geometry("600x600+100+100") #tamaño de la aplicacion
        self.configure(bg="alice blue") #color de fondo de la aplicacion

        self.pantalla = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1") #se define la pantalla donde se va a mostrar el resultado 
        self.cantidad_moneda = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1") #se define la ventana donde se van a introducir la cantidad de moneda
        self.cantidad_moneda.bind('<FocusIn>', self.on_cantidad_focus_in) #por defecto muestra 1 como cantidad, esto se borra al hacer click dentro de la ventana cogiendo foco
        self.nombre_moneda_origen = ttk.Combobox(self, font=("Arial Black", 8), foreground="navy",values=[nombre for nombre, _ in self.listado_currencies], state="readonly", width=30) #se define el desplegable para moneda origen
        self.nombre_moneda_destino = ttk.Combobox(self, font=("Arial Black", 8), foreground="navy",values=[nombre for nombre, _ in self.listado_currencies], state="readonly", width=30) #se define el desplegable para la moneda destino
        self.calcular_button = tk.Button(self, text="Convertir", fg="navy", bg="LightSteelBlue1", padx=40, pady=4, command=self.mostrar_resultado) #se define el boton para realizar la conversion

        self.pantalla.place(x=480, y=180, anchor="center") #se define la colocacion de la patalla de resultados
        self.cantidad_moneda.place(x=120, y=180, anchor="center")#se define la colocacion de la ventana de cantidad de  moneda 
        self.nombre_moneda_origen.place(x=130, y=70, anchor="center")#se define la colocacion de la ventana de moneda origen
        self.nombre_moneda_destino.place(x=470, y=70, anchor="center")#se define la colocacion de la ventana de moneda destino
        self.calcular_button.place(x=300, y=265, anchor="center")#se define la colocacion del boton de convertir
        

        self.pantalla.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.cantidad_moneda.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.calcular_button.configure(font=("Arial", 14))#se configura el tipo de letra y tamaño del boton de convertir
        self.nombre_moneda_origen.configure(style='My.TCombobox')#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.nombre_moneda_destino.configure(style='My.TCombobox')#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 

        
        self.bind_combobox_events() #llamada a la funcion que vincula los combobox con mostrar_resultado() a traves de eventos
        

        etiqueta_label= tk.Label(self, text="Conversion:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de la pantalla de resultados
        etiqueta_label.place(x=480, y=120, anchor="center")#se define la colocacion de la etiqueta de la pantalla de resultado
        

        cantidad_moneda_label = tk.Label(self, text="Cantidad:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13) )#se define la etiqueta de cantidad de  moneda 
        cantidad_moneda_label.place(x=120, y=120, anchor="center")#se define la colocacion de la etiqueta de cantidad moneda 
        

        nombre_moneda_origen_label = tk.Label(self, text="Moneda de origen:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de moneda origen
        nombre_moneda_origen_label.place(x=120, y=30, anchor="center")#se define la colocacion de la etiqueta de moneda origen

        nombre_moneda_destino_label = tk.Label(self, text="Divisa de destino:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de moneda destino
        nombre_moneda_destino_label.place(x=480, y=30, anchor="center") #se define la colocacion de la etiqueta de moneda destino
        calcular_button_label = tk.Label(self, text=""" 
Conversor de Divisas
                    
Elija de los desplegables la moneda de origen y la moneda de destino. 
   Introduzca la cantidad y al pulsar el botón convertir 
        obtendrá la conversión de divisa.  
                                    

  Por defecto se muestra la conversión para una unidad.

                                         

        CC-BY-NC 2023 Juan Fuente         
                        """, fg="navy", bg="LightSteelBlue1", font=("Arial", 13))
        calcular_button_label.place(x=300, y=440, anchor="center") #se define la colocacion de la etiqueta bajo el boton de convertir
        

    def on_cantidad_focus_in(self, event):#funcion que se ejecuta cuando la ventana de cantidad_moneda esta en foco, si no lo está por defecto muestra como cantidad un 1
        if self.cantidad_moneda.get() == '1': #evalua si esta la impresion por defecto
            self.cantidad_moneda.delete(0, tk.END)#borra la impresion por defecto
        

    def bind_combobox_events(self):#funcion para vincular los desplegables combobox con la funcion mostrar_resultado
        self.nombre_moneda_origen.bind("<<ComboboxSelected>>", self.mostrar_resultado) #se asocia el combobox nombre_moneda_origen con la funcion mostrar_resultado
        self.nombre_moneda_destino.bind("<<ComboboxSelected>>", self.mostrar_resultado)#se asocia el combobox nombre_moneda_destino con la funcion mostrar_resultado

    def calcular_divisa(self, cantidad_moneda, codigo_moneda_origen, codigo_moneda_destino):#funcion que tomas los valores y realiza el calculo de la conversion de divisas
        if codigo_moneda_origen in self.divisas['rates'] and codigo_moneda_destino in self.divisas['rates']:#evalua si la moneda origen y la destino estan dentro de las posibles opciones
            tasa_moneda_origen = self.divisas['rates'][codigo_moneda_origen]#se coge el valor de la moneda origen con respecto al euro  
            tasa_moneda_destino = self.divisas['rates'][codigo_moneda_destino]#se coge el valor de la moneda destino con respecto al euro  
            cambio_divisa = round(cantidad_moneda * (1 / tasa_moneda_origen) * tasa_moneda_destino, 5) #se calcula el valor de cambio de divisa
            return cambio_divisa #se devuelve el valor
        else:
            return "Error: Moneda no encontrada" #devuelve mensaje en caso de no ser una opcion valida

    def mostrar_resultado(self, event=None): #Funcion que gestiona como mostrar los resultados
        cantidad = self.cantidad_moneda.get() 

         # Si no se ha proporcionado una cantidad, se establece por defecto como 1
        if not cantidad:
            cantidad = "1"
            self.cantidad_moneda.insert(tk.END, "1")

        try:
            cantidad = float(cantidad) # Intenta convertir la cantidad ingresada en la ventana a un valor numérico de punto flotante
        except ValueError:
            self.pantalla.delete(0, tk.END) # Si ocurre un error al intentar convertir la cantidad, se borra el contenido de la pantalla
            return
        
        # Obtiene los nombres de las monedas de origen y destino seleccionados en los ComboBox
        nombre_moneda_origen = self.nombre_moneda_origen.get()
        nombre_moneda_destino = self.nombre_moneda_destino.get()

        # Si no se han seleccionado monedas de origen o destino, se muestra un mensaje de error
        if not nombre_moneda_origen or not nombre_moneda_destino:
            if event is None or (event.widget == self.calcular_button if event else False): #evalua si se esta intentando hacer los calculos de conversion cuando todavia falta uno de los datos necesarios 
            # Si no hay ningún evento (ningún elemento activo), o si el evento proviene del botón de cálculo, se mostrará un mensaje de error.

                tk.messagebox.showerror("Error", "Por favor, seleccione la moneda de origen y la moneda de destino.") #mensaje de error
            return
        
        # Se obtienen los códigos de moneda correspondientes a los nombres seleccionados
        codigo_moneda_origen = self.diccionario_currencies[nombre_moneda_origen]
        codigo_moneda_destino = self.diccionario_currencies[nombre_moneda_destino]

        # Se calcula la conversión utilizando la función calcular_divisa
        resultado = self.calcular_divisa(cantidad, codigo_moneda_origen, codigo_moneda_destino)

        # Se actualiza la pantalla con el resultado de la conversión
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, resultado)

if __name__ == "__main__":  # Bloque principal de ejecución
    ventana = ConversorDivisas()
    ventana.mainloop()
