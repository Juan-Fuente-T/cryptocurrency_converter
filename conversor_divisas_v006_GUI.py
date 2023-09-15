import tkinter as tk
from tkinter import ttk


class VisualMoney(tk.Tk):
    #DICCIONARIO CON EL LISTADO DE DIVISAS PARA PRUEBAS Y NO GASTAR LAS LLAMADAS A LA API, que tiene llamadas limitadas mensuales
    divisas = {'success': True, 'timestamp': 1686316503, 'base': 'EUR', 'date': '2023-06-09', 'rates': {'AED': 3.954746, 'AFN': 92.174953, 'ALL': 105.694703, 'AMD': 
    415.806427, 'ANG': 1.939294, 'AOA': 659.488358, 'ARS': 263.747758, 'AUD': 1.59867, 'AWG': 1.938089, 'AZN': 1.88214, 'BAM': 1.955693, 'BBD': 2.172681, 'BDT': 116.493621, 'BGN': 1.955821, 'BHD': 0.405957, 'BIF': 3038.061864, 'BMD': 1.076716, 'BND': 1.446334, 'BOB': 7.435627, 'BRL': 5.278811, 'BSD': 1.076041, 'BTC': 4.0336908e-05, 'BTN': 88.728254, 'BWP': 14.483341, 'BYN': 2.716051, 'BYR': 21103.634453, 'BZD': 2.168981, 'CAD': 1.437653, 'CDF': 2549.663112, 'CHF': 0.970111, 'CLF': 0.030721, 'CLP': 847.688109, 'CNY': 7.677631, 'COP': 4483.725551, 'CRC': 579.270972, 'CUC': 1.076716, 'CUP': 28.532975, 'CVE': 110.263962, 'CZK': 23.674778, 'DJF': 191.591289, 'DKK': 7.450519, 'DOP': 59.03759, 'DZD': 146.73382, 'EGP': 33.330928, 'ERN': 16.150741, 'ETB': 58.536867, 'EUR': 1, 'FJD': 2.391708, 'FKP': 0.858216, 'GBP': 0.85628, 'GEL': 2.81017, 'GGP': 0.858216, 'GHS': 12.159391, 'GIP': 0.858216, 'GMD': 64.011362, 'GNF': 9252.493372, 'GTQ': 8.425539, 'GYD': 227.588595, 'HKD': 8.440086, 'HNL': 26.47955, 'HRK': 7.477083, 'HTG': 150.111781, 'HUF': 368.211064, 'IDR': 15990.902156, 'ILS': 3.87066, 'IMP': 0.858216, 'INR': 88.775781, 'IQD': 1409.622815, 'IRR': 45491.252933, 'ISK': 149.491477, 'JEP': 0.858216, 'JMD': 166.643197, 'JOD': 0.76382, 'JPY': 149.893406, 'KES': 149.802942, 'KGS': 94.298361, 'KHR': 4442.818624, 'KMF': 491.897857, 'KPW': 969.07606, 'KRW': 
    1389.512698, 'KWD': 0.33081, 'KYD': 0.896759, 'KZT': 480.370389, 'LAK': 19547.020458, 'LBP': 16151.7906, 'LKR': 319.612499, 'LRD': 184.388113, 'LSL': 20.489417, 'LTL': 3.179263, 'LVL': 0.651295, 'LYD': 5.197715, 'MAD': 10.843357, 'MDL': 19.192038, 'MGA': 4761.761378, 'MKD': 61.516632, 'MMK': 2259.797251, 'MNT': 3732.624381, 'MOP': 8.689965, 'MRO': 384.387442, 'MUR': 48.829441, 'MVR': 16.538239, 'MWK': 1104.544649, 'MXN': 18.64355, 'MYR': 4.967996, 'MZN': 68.102228, 'NAD': 20.285057, 'NGN': 497.818133, 'NIO': 39.357845, 'NOK': 11.625658, 'NPR': 141.966204, 'NZD': 1.756975, 'OMR': 0.414517, 'PAB': 1.076041, 'PEN': 3.932639, 'PGK': 3.818844, 'PHP': 60.331661, 'PKR': 308.835292, 'PLN': 4.451559, 'PYG': 7795.681745, 'QAR': 3.920432, 'RON': 4.956133, 
    'RSD': 117.227447, 'RUB': 88.76767, 'RWF': 1220.944486, 'SAR': 4.038179, 'SBD': 8.992057, 'SCR': 14.158592, 'SDG': 646.503877, 'SEK': 11.663053, 'SGD': 1.446272, 'SHP': 1.310094, 'SLE': 24.323726, 'SLL': 21265.141813, 'SOS': 613.198711, 'SRD': 40.425316, 'STD': 22285.84822, 'SVC': 9.415484, 'SYP': 2705.350153, 'SZL': 20.174895, 'THB': 37.231225, 'TJS': 11.75622, 'TMT': 3.768506, 'TND': 3.340513, 'TOP': 2.541375, 'TRY': 25.160808, 'TTD': 7.291635, 'TWD': 33.0975, 'TZS': 2557.200547, 'UAH': 39.741278, 'UGX': 4002.780824, 'USD': 1.076716, 'UYU': 41.937704, 'UZS': 12293.326869, 'VEF': 2871018.449141, 
    'VES': 29.958053, 'VND': 25281.292702, 'VUV': 128.704654, 'WST': 2.960564, 'XAF': 655.927176, 'XAG': 0.044423, 'XAU': 0.000548, 'XCD': 2.909879, 'XDR': 0.808956, 'XOF': 655.921085, 'XPF': 119.65572, 'YER': 269.506834, 'ZAR': 20.148437, 'ZMK': 9691.734826, 'ZMW': 21.655915, 'ZWL': 346.702127}}

    keys = list(divisas['rates'].keys()) #se cogen los nombres de las divisas y se meten en una lista donde poder comparar si están las elegidas por el usuario

    #diccionario de divisas ordenadas alfabeticamente por su nombre en castellano
    listado_currencies = [('Afgani afgano', 'AFN'), ('Baht tailandés', 'THB'), ('Balboa panameño', 'PAB'), ('Birr etíope', 'ETB'), ('Bitcoin', 'BTC'), ('Boliviano boliviano', 'BOB'), ('Cedi ghanés', 'GHS'), ('Chelín keniano', 'KES'), ('Chelín somalí', 'SOS'), ('Colon costarricense', 'CRC'), ('Colón salvadoreño', 'SVC'), ('Corona checa', 'CZK'), ('Corona danesa', 'DKK'), ('Corona islandesa', 'ISK'), ('Corona noruega', 'NOK'), ('Corona sueca', 'SEK'), ('Dalasi gambiano', 'GMD'), ('Denar macedonio', 'MKD'), ('Dinar argelino', 'DZD'), ('Dinar bahreiní', 'BHD'), ('Dinar iraquí', 'IQD'), ('Dinar jordano', 'JOD'), ('Dinar kuwaití', 'KWD'), 
    ('Dinar libio', 'LYD'), ('Dinar serbio', 'RSD'), ('Dinar tunecino', 'TND'), ('Dólar americano', 'USD'), ('Dólar australiano', 'AUD'), ('Dólar beliceño', 'BZD'), ('Dólar canadiense', 'CAD'), ('Dólar de Barbados', 'BBD'), ('Dólar de Bermudas', 'BMD'), ('Dólar de Brunéi', 'BND'), ('Dólar de Fiyi', 'FJD'), ('Dólar de Hong Kong', 'HKD'), ('Dólar de las Islas Salomón', 'SBD'), ('Dólar de las Bahamas', 'BSD'), ('Dólar de Nueva Zelanda', 'NZD'), ('Dólar de Singapur', 'SGD'), ('Dólar guyanés', 'GYD'), ('Dólar jamaiquino', 'JMD'), ('Dólar liberiano', 'LRD'), ('Dólar namibio', 'NAD'), ('Dólar surinamés', 'SRD'), ('Dólar trinitense', 'TTD'), ('Dong vietnamita', 'VND'), ('Escudo caboverdiano', 'CVE'), ('Euro', 'EUR'), ('Florín de Aruba', 'AWG'), ('Florín de las Antillas Neerlandesas', 'ANG'), ('Franco burundés', 'BIF'), ('Franco CFA de África Central', 'XAF'), ('Franco CFA de África Occidental', 'XOF'), ('Franco CFP', 'XPF'), ('Franco comorense', 'KMF'), ('Franco congoleño', 'CDF'), ('Franco guineano', 'GNF'), ('Gourde haitiano', 'HTG'), ('Guaraní paraguayo', 'PYG'), ('Hryvnia ucraniano', 'UAH'), ('Kip laosiano', 'LAK'), ('Kuna croata', 'HRK'), ('Kwacha malauí', 'MWK'), ('Kwacha zambiano', 'ZMW'), ('Kwanza angoleño', 'AOA'), 
    ('Kyat birmano', 'MMK'), ('Lari georgiano', 'GEL'), ('Lek albanés', 'ALL'), ('Lempira hondureño', 'HNL'), ('Leone sierraleonés', 'SLL'), ('Lev búlgaro', 'BGN'), ('Libra egipcia', 'EGP'), ('Libra esterlina', 'GBP'), ('Libra sudanesa', 'SDG'), ('Libra siria', 'SYP'), ('Libra sursudanesa', 'SSP'), ('Lilangeni suazi', 'SZL'), ('Loti lesothense', 'LSL'), 
    ('Manat azerbaiyano', 'AZN'), ('Metical mozambiqueño', 'MZN'), ('Naira nigeriano', 'NGN'), ('Nakfa eritreo', 'ERN'), ('Ngultrum butanés', 'BTN'), ('Ouguiya mauritano', 'MRU'), 
    ('Pataca de Macao', 'MOP'), ('Peso argentino', 'ARS'), ('Peso chileno', 'CLP'), ('Peso colombiano', 'COP'), ('Peso cubano', 'CUP'), ('Peso dominicano', 'DOP'), ('Peso filipino', 'PHP'), ('Peso mexicano', 'MXN'), ('Peso uruguayo', 'UYU'), ('Pula botsuano', 'BWP'), 
    ('Qatar Rial catarí', 'QAR'), ('Quetzal guatemalteco', 'GTQ'), ('Rand sudafricano', 'ZAR'), ('Real brasileño', 'BRL'), ('Renminbi chino', 'CNY'), ('Rial iraní', 'IRR'), ('Rial omaní', 'OMR'), ('Riel camboyano', 'KHR'), ('Ringgit malayo', 'MYR'), ('Rublo bielorruso', 'BYN'), ('Rublo ruso', 'RUB'), ('Rufiyaa maldiva', 'MVR'), ('Rupia de las Seychelles', 'SCR'), ('Rupia india', 'INR'), ('Rupia indonesia', 'IDR'), ('Rupia mauriciana', 'MUR'), ('Rupia nepalesa', 'NPR'), ('Rupia pakistaní', 'PKR'), ('Ryazan ruso', 'AMD'), ('Taka bangladesí', 'BDT'), ('Tenge kazajo', 'KZT'), ('Tugrik mongol', 'MNT'), ('Vatu vanuatuense', 'VUV'), ('Won norcoreano', 'KPW'), ('Won surcoreano', 'KRW'), ('Yen japonés', 'JPY'), ('Yuan chino', 'CNY'), ('Zloty polaco', 'PLN')]


    diccionario_currencies = {
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

        self.title("Conversor de Divisas")
        self.iconbitmap("visualmoney.ico")
        self.geometry("600x600+100+100")
        self.configure(bg="alice blue") 

        # Define the style for the combobox widget
        style = ttk.Style()
        style.configure('TCombobox', font=('Helvetica', 20))
        style.configure('TCombobox', fieldbackground='light green', background='white')
        

        self.pantalla = tk.Entry(self, width=12, borderwidth=2,fg="navy", bg="LightSteelBlue1")
        self.cantidad_moneda = tk.Entry(self, width=12, borderwidth=2, fg="navy",bg="LightSteelBlue1" )
        self.nombre_moneda_origen = ttk.Combobox(self, values=[nombre for nombre, _ in self.listado_currencies], state="readonly", width=30)
        self.nombre_moneda_destino = ttk.Combobox(self, values=[nombre for nombre, _ in self.listado_currencies], state="readonly", width=30)
        self.calcular_button = tk.Button(self, text="Calcular", fg="navy", bg="LightSteelBlue1",padx=60, pady=10, command=self.calcular_resultado)

        self.pantalla.place(x=480, y=180, anchor="center")
        self.cantidad_moneda.place(x=120, y=180, anchor="center")
        self.nombre_moneda_origen.place(x=120, y=70, anchor="center")
        self.nombre_moneda_destino.place(x=480, y=70, anchor="center")
        self.calcular_button.place(x=300, y=265, anchor="center")
    

        self.pantalla.configure(font=("Arial Black", 18))
        self.cantidad_moneda.configure(font=("Arial Black", 18))
        self.calcular_button.configure(font=("Arial", 14))

        
        #ventana.columnconfigure(1, weight=2)
        #ventana.columnconfigure(4, weight=2)

        #pantalla = tk.Entry(ventana, width=12, borderwidth=2)
        
        etiqueta_label= tk.Label(self, text="Conversion:", fg="navy",bg="LightSteelBlue1" )
        etiqueta_label.place(x=480, y=120, anchor="center")
        etiqueta_label.configure(font=("Arial", 13))

        cantidad_moneda_label = tk.Label(self, text="Cantidad:", fg="navy",bg="LightSteelBlue1" )
        cantidad_moneda_label.place(x=120, y=120, anchor="center")
        cantidad_moneda_label.configure(font=("Arial", 13),)
        #cantidad_moneda = tk.Entry(ventana, width=12, borderwidth=2)
        

        nombre_moneda_origen_label = tk.Label(self, text="Moneda de origen:", fg="navy",bg="LightSteelBlue1")
        nombre_moneda_origen_label.place(x=120, y=30, anchor="center")
        nombre_moneda_origen_label.configure(font=("Arial", 13))
        #nombre_moneda_origen = tk.Entry(ventana, width=12, borderwidth=2)
        #nombre_moneda_origen = ttk.Combobox(ventana, values=[nombre for nombre, _ in listado_currencies], state="readonly", width=25)
        
        #print("Moneda origen",self.nombre_moneda_origen.get())

        """nombre_moneda_origen.configure(font=("Arial Black", 18))
        nombre_moneda_origen.grid(row=3, column=1, columnspan=2, padx=10, pady=10)"""

        nombre_moneda_destino_label = tk.Label(self, text="Divisa de destino:", fg="navy",bg="LightSteelBlue1")
        nombre_moneda_destino_label.place(x=480, y=30, anchor="center")
        nombre_moneda_destino_label.configure(font=("Arial", 13))
        #nombre_moneda_destino = ttk.Combobox(ventana, values=[nombre for nombre, _ in listado_currencies], state="readonly", width=25)
        #calcular_button = tk.Button(ventana, text="Calcular", padx=60, pady=10, self.command=self.calcular)
        calcular_button_label = tk.Label(self, text="""Conversor de Divisas

                    
Elija de los desplegables la moneda de origen y
            
la moneda de destino. Introduzca la cantidad y 
            
al pulsar el botón calcular obtendrá la 
            
        conversión de divisa.  
            

        CC-BY-NC 2023 Juan Fuente         
                        """, fg="navy", bg="LightSteelBlue1")
        calcular_button_label.place(x=300, y=440, anchor="center")
        calcular_button_label.configure(font=("Arial", 13))
            
        self.change_combobox_style()
        self.nombre_moneda_origen.bind("<<ComboboxSelected>>", self.calcular_resultado)
        self.nombre_moneda_destino.bind("<<ComboboxSelected>>", self.calcular_resultado)

        #self.mostrar_valor_defecto()  # Agregar esta línea para mostrar el valor por defecto

        
   
        

    def change_combobox_style(self):
        self.nombre_moneda_origen.configure(style='My.TCombobox')
        style = ttk.Style()
        style.configure('My.TCombobox', background='navy', font=('Arial', 18))

            
    def calcular_divisa(self,cantidad_moneda, codigo_moneda_origen, codigo_moneda_destino):
        if codigo_moneda_origen in self.divisas['rates'] and codigo_moneda_destino in self.divisas['rates']:
            tasa_moneda_origen = self.divisas['rates'][codigo_moneda_origen]
            tasa_moneda_destino = self.divisas['rates'][codigo_moneda_destino]
            cambio_divisa = round(cantidad_moneda * (1 / tasa_moneda_origen) * tasa_moneda_destino, 5)
            return cambio_divisa
        else:
            return "Error: Moneda no encontrada"

    

        
    """def calcular_resultado(self):
        cantidad_moneda = 1
        cantidad_moneda = float(self.cantidad_moneda.get())


        codigo_moneda_origen = self.diccionario_currencies[self.nombre_moneda_origen.get()]
        codigo_moneda_destino = self.diccionario_currencies[self.nombre_moneda_destino.get()]
        resultado = self.calcular_divisa(float(self.cantidad_moneda.get()), codigo_moneda_origen, codigo_moneda_destino)

        self.pantalla.delete(0, tk.END
        )
        self.pantalla.insert(tk.END, resultado)
        if cantidad_moneda == 1:
            self.cantidad_moneda.insert(tk.END, cantidad_moneda)"""
    

    def calcular_resultado(self, event=None):
        cantidad = self.cantidad_moneda.get()

        if not cantidad:
            cantidad = "1"  # Establecer el valor predeterminado como "1"
            self.cantidad_moneda.insert(tk.END, "1")
            


        try:
            cantidad = float(cantidad)
        except ValueError:
            self.pantalla.delete(0, tk.END)
            return
        
        nombre_moneda_origen = self.nombre_moneda_origen.get()
        nombre_moneda_destino = self.nombre_moneda_destino.get()

        if not nombre_moneda_origen or not nombre_moneda_destino:
            self.messagebox.showerror("Error", "Por favor, seleccione la moneda de origen y la moneda de destino.")
            return

        codigo_moneda_origen = self.diccionario_currencies[self.nombre_moneda_origen.get()]
        codigo_moneda_destino = self.diccionario_currencies[self.nombre_moneda_destino.get()]

        resultado = self.calcular_divisa(cantidad, codigo_moneda_origen, codigo_moneda_destino)
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, resultado)


if __name__ == "__main__":
    ventana = VisualMoney()
    ventana.mainloop()

