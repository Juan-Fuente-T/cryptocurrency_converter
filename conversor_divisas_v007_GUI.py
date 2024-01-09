                        #//////////////////////////////////////#
                        #                                      #
                        ###       CONVERSOR DE DIVISAS       ###    
                        #                                      #
                        #//////////////////////////////////////#


#CONVERSOR DE DIVISAS v0.1.0

#Esta aplicación multiplataforma (Windows, Linux, Mac) convierte una cantidad de una moneda en codigo ISO, por ejemplo EUR (euros), en el valor correspondiente en otra divisa, por ejemplo USD (dolares americanos), y opera mediante interfaz gráfica. 
# Toma los datos para el cambio en tiempo real mediante API.

# ©2023 Calculadora de divisas GUI de Juan Fuente

"""
Novedades de la version 1.0
- Eliminacion de lista de divisas de prueba e implementacion de la llamada a la API para obtener valores de conversión en tiempo real
- Se termina la documentacion
- Se oculta la api key en el .env
- Se añade manual y EULA
"""


import tkinter as tk
from tkinter import messagebox  #se importa messagebox para mostrar mensaje de error
from tkinter import ttk #ttk es necesario para los desplegables combobox 
import requests #se necesita requests instalado con pip para hacer llamada a la API de conversion
#from decouple import config #importacion para mantener las claves seguras
from ttkthemes import ThemedStyle

class VisualMoney(tk.Tk): 
    
                            #BLOQUE DE CAPTURA DE DATOS MEDIANTE API
    #api_key = config("API_KEY")      
    api_key = "820d753dc0b87f819a178392535c6eb2"      
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}" #url que sirve los datos

    #json_divisas = requests.get(url) #se realiza la llamada a los datos de la url de la api
    #divisas = json_divisas.json() #se guardan los datos de las conversiones en un archivo json
    divisas = {'success': True, 'timestamp': 1704799865, 'base': 'EUR', 'date': '2024-01-09', 'rates': {'AED': 4.014585, 'AFN': 76.929074, 'ALL': 104.057168, 'AMD': 440.020966, 'ANG': 1.961617, 'AOA': 925.006145, 'ARS': 889.65213, 'AUD': 1.633733, 'AWG': 1.956733, 'AZN': 1.859407, 'BAM': 1.948024, 'BBD': 2.186294, 'BDT': 119.706241, 'BGN': 1.953017, 'BHD': 0.412018, 'BIF': 3108.134536, 'BMD': 1.093147, 'BND': 1.452005, 'BOB': 
7.536814, 'BRL': 5.323952, 'BSD': 1.090734, 'BTC': 2.3445545e-05, 'BTN': 90.691952, 'BWP': 14.779455, 'BYN': 3.602356, 'BYR': 21425.683958, 'BZD': 2.19864, 'CAD': 1.461877, 'CDF': 2935.099826, 'CHF': 0.930383, 'CLF': 0.035873, 'CLP': 989.845673, 'CNY': 7.77184, 'COP': 4246.330068, 'CRC': 566.801524, 'CUC': 1.093147, 'CUP': 28.968399, 'CVE': 109.956915, 'CZK': 24.557335, 'DJF': 194.204088, 'DKK': 7.45804, 'DOP': 63.760186, 'DZD': 147.079702, 'EGP': 33.780323, 'ERN': 16.397207, 'ETB': 61.653726, 'EUR': 1, 'FJD': 2.443403, 'FKP': 0.856516, 'GBP': 0.859891, 'GEL': 2.935079, 'GGP': 0.856516, 'GHS': 13.067268, 'GIP': 0.856516, 'GMD': 73.541439, 'GNF': 9378.593681, 'GTQ': 8.532094, 'GYD': 228.198529, 'HKD': 8.543273, 'HNL': 26.916092, 'HRK': 7.632102, 'HTG': 143.723361, 'HUF': 378.594567, 'IDR': 17002.373368, 'ILS': 4.063443, 'IMP': 0.856516, 'INR': 90.877858, 'IQD': 1428.883379, 'IRR': 45953.170324, 'ISK': 150.689962, 'JEP': 0.856516, 'JMD': 168.415041, 'JOD': 0.775478, 'JPY': 157.506069, 'KES': 172.990331, 'KGS': 97.597596, 'KHR': 4467.360423, 'KMF': 491.379149, 'KPW': 983.812132, 'KRW': 1443.150857, 'KWD': 0.336044, 'KYD': 0.908945, 'KZT': 494.987636, 'LAK': 22486.994301, 'LBP': 16394.090799, 'LKR': 351.940687, 'LRD': 206.413523, 'LSL': 20.284462, 'LTL': 3.227779, 'LVL': 0.661234, 'LYD': 5.236281, 'MAD': 10.841026, 'MDL': 19.077547, 'MGA': 4988.975885, 'MKD': 61.496711, 'MMK': 2290.561185, 'MNT': 3742.88252, 'MOP': 8.771324, 'MRU': 43.343138, 'MUR': 49.409871, 'MVR': 16.845428, 'MWK': 1836.130202, 'MXN': 18.413101, 'MYR': 5.076028, 'MZN': 69.141502, 'NAD': 20.331936, 'NGN': 964.800373, 'NIO': 39.917426, 'NOK': 11.332449, 'NPR': 145.103112, 
'NZD': 1.752446, 'OMR': 0.420744, 'PAB': 1.090734, 'PEN': 4.033454, 'PGK': 4.072515, 'PHP': 61.322819, 'PKR': 306.768966, 'PLN': 4.338784, 'PYG': 7912.829259, 'QAR': 3.980695, 'RON': 4.970515, 'RSD': 117.231267, 'RUB': 99.360567, 'RWF': 1383.199145, 'SAR': 4.099602, 'SBD': 9.241126, 'SCR': 14.576962, 'SDG': 656.981352, 'SEK': 11.212274, 'SGD': 1.454892, 'SHP': 1.394202, 'SLE': 24.612364, 'SLL': 21589.655915, 'SOS': 624.186485, 'SRD': 40.028879, 'STD': 22625.938757, 'SYP': 14212.978244, 'SZL': 20.44453, 'THB': 38.238291, 'TJS': 11.94912, 'TMT': 3.836946, 'TND': 3.382231, 'TOP': 2.563813, 'TRY': 32.727402, 'TTD': 7.403325, 'TWD': 33.996112, 'TZS': 2745.985579, 'UAH': 41.720532, 'UGX': 4155.319311, 'USD': 1.093147, 'UYU': 42.800861, 'UZS': 13476.118352, 'VEF': 3930901.398613, 'VES': 39.237005, 'VND': 26639.995819, 'VUV': 130.080195, 'WST': 2.964645, 'XAF': 654.115277, 'XAG': 0.047269, 'XAU': 0.000537, 'XCD': 2.954284, 'XDR': 
0.817303, 'XOF': 654.11826, 'XPF': 119.331742, 'YER': 273.669831, 'ZAR': 20.444913, 'ZMK': 9839.63806, 'ZMW': 28.310677, 'ZWL': 351.992933}}
    print(divisas)    
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


    def __init__(self): 
        super().__init__()

        self.title("Conversor de Divisas") #titulo de la aplicacion
        self.iconbitmap("visualmoney.ico") #icono de la aplicacion
        self.geometry("600x400")
        self.style = ThemedStyle(self)
        self.style.set_theme("equilux")

        self.create_widgets()

    def create_widgets(self):
        self.label_currency_from = ttk.Label(self, text="Selecciona la moneda de origen:")
        self.label_currency_from.pack(pady=10)

        self.combo_currency_from = ttk.Combobox(self, values=self.keys)
        self.combo_currency_from.pack(pady=10)

        self.label_currency_to = ttk.Label(self, text="Selecciona la moneda de destino:")
        self.label_currency_to.pack(pady=10)

        self.combo_currency_to = ttk.Combobox(self, values=self.keys)
        self.combo_currency_to.pack(pady=10)

        self.label_amount = ttk.Label(self, text="Introduce la cantidad:")
        self.label_amount.pack(pady=10)

        self.entry_amount = ttk.Entry(self)
        self.entry_amount.pack(pady=10)

        self.btn_convert = ttk.Button(self, text="Convertir", command=self.convert_currency)
        self.btn_convert.pack(pady=10)


    def on_cantidad_focus_in(self, event):#funcion que se ejecuta cuando la ventana de cantidad_moneda esta en foco, si no lo está por defecto muestra como cantidad un 1
        if self.cantidad_moneda.get() == '1': #evalua si esta la impresion por defecto
            self.cantidad_moneda.delete(0, tk.END)#borra la impresion por defecto
        

    def bind_combobox_events(self):#funcion para vincular los desplegables combobox con la funcion calcular_resultado
        self.nombre_moneda_origen.bind("<<ComboboxSelected>>", self.calcular_resultado) #se asocia el combobox nombre_moneda_origen con la funcion calcular_resultado
        self.nombre_moneda_destino.bind("<<ComboboxSelected>>", self.calcular_resultado)#se asocia el combobox nombre_moneda_destino con la funcion calcular_resultado

    
    def calcular_divisa(self, cantidad_moneda, codigo_moneda_origen, codigo_moneda_destino):#funcion que realiza el calculo de la conversion de divisas
        if codigo_moneda_origen in self.divisas['rates'] and codigo_moneda_destino in self.divisas['rates']:#evalua si la moneda origen y la destino estan dentro de las posibles opciones
            tasa_moneda_origen = self.divisas['rates'][codigo_moneda_origen]#se coge el valor de la moneda origen con respecto al euro  
            tasa_moneda_destino = self.divisas['rates'][codigo_moneda_destino]#se coge el valor de la moneda destino con respecto al euro  
            cambio_divisa = round(cantidad_moneda * (1 / tasa_moneda_origen) * tasa_moneda_destino, 5) #se calcula el valor de cambio de divisa
            return cambio_divisa #se devuelve el valor
        else:
            return "Error: Moneda no encontrada" #devuelve mensaje en caso de no ser una opcion valida

    def calcular_resultado(self, event=None):#funcion para relizar los calculos de conversion entre ambas monedas
        cantidad = self.cantidad_moneda.get()

        if not cantidad: #en caso de no haber seleccionado aun una cantidad de moneda se da valor 1 por defecto
            cantidad = "1" #se asigna el valor 1
            self.cantidad_moneda.insert(tk.END, "1") #se inserta el valor 1 en la pantalla

        try:
            cantidad = float(cantidad) #se hace intento de convertir a float los datos introducidos
        except ValueError:
            self.pantalla.delete(0, tk.END) #si hay un error en los datos se borra la pantalla
            return
        #se obtiene el valor para ambas monedas
        nombre_moneda_origen = self.nombre_moneda_origen.get() 
        nombre_moneda_destino = self.nombre_moneda_destino.get()

        if not nombre_moneda_origen or not nombre_moneda_destino:#se evalua si alguna de las monedas aun no ha sido seleccionada
            if event is None or (event.widget == self.calcular_button if event else False):#se evalua que se este intentando calcular el cambio faltando una moneda
                tk.messagebox.showerror("Error", "Por favor, seleccione la moneda de origen y la moneda de destino.")
                return
        #se toman los codigos correspodientes de cada moneda
        codigo_moneda_origen = self.diccionario_currencies[nombre_moneda_origen]
        codigo_moneda_destino = self.diccionario_currencies[nombre_moneda_destino]

        resultado = self.calcular_divisa(cantidad, codigo_moneda_origen, codigo_moneda_destino) #se realizan los calculos de conversion haciendo la llamada a la funcion
        self.pantalla.delete(0, tk.END) #se borran los datos anteriores
        self.pantalla.insert(tk.END, resultado) #se imprimen los nuevos datos

if __name__ == "__main__": #proporciona la opcion de ejecutar la app como un componente o standalone
    ventana = VisualMoney()
    ventana.mainloop()