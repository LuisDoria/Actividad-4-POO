import math
import tkinter as tk
from tkinter import messagebox

# Clase: FiguraGeometrica
"""
Esta clase denominada FiguraGeometrica modela una figura
geométrica que cuenta con un volumen y una superficie a ser
calculados de acuerdo al tipo de figura geométrica.
"""
class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0  # Atributo que identifica el volumen de una figura geométrica
        self._superficie = 0.0 # Atributo que identifica la superficie de una figura geométrica

    @property
    def volumen(self):
        """
        Método para obtener el volumen de una figura geométrica
        :return: El volumen de una figura geométrica
        """
        return self._volumen

    @volumen.setter
    def volumen(self, volumen):
        """
        Método para establecer el volumen de una figura geométrica
        :param volumen: Parámetro que define el volumen de una figura geométrica
        """
        self._volumen = volumen

    @property
    def superficie(self):
        """
        Método para obtener la superficie de una figura geométrica
        :return: La superficie de una figura geométrica
        """
        return self._superficie

    @superficie.setter
    def superficie(self, superficie):
        """
        Método para establecer la superficie de una figura geométrica
        :param superficie: Parámetro que define la superficie de una figura geométrica
        """
        self._superficie = superficie

# Clase: Cilindro
"""
Esta clase denominada Cilindro es una subclase de FiguraGeometrica
que cuenta con un radio y una altura.
"""
class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio  # Atributo que establece el radio de un cilindro
        self.altura = altura # Atributo que establece la altura de un cilindro
        self.volumen = self.calcular_volumen()  # Calcula el volumen y establece su atributo
        self.superficie = self.calcular_superficie() # Calcula la superficie y establece su atributo

    def calcular_volumen(self):
        """
        Método para calcular el volumen de un cilindro
        :return: El volumen de un cilindro
        """
        volumen = math.pi * self.altura * (self.radio ** 2)
        return volumen

    def calcular_superficie(self):
        """
        Método para calcular la superficie de un cilindro
        :return: La superficie de un cilindro
        """
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * (self.radio ** 2)
        return area_lado_a + area_lado_b

# Clase: Esfera
"""
Esta clase denominada Esfera es una subclase de FiguraGeometrica
que cuenta con un radio.
"""
class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio  # Atributo que identifica el radio de una esfera
        self.volumen = self.calcular_volumen()  # Calcula el volumen y establece su atributo
        self.superficie = self.calcular_superficie() # Calcula la superficie y establece su atributo

    def calcular_volumen(self):
        """
        Método para calcular el volumen de una esfera
        :return: El volumen de una esfera
        """
        volumen = (4/3) * math.pi * (self.radio ** 3) # Se usa 4/3 para precisión con floats
        return volumen

    def calcular_superficie(self):
        """
        Método para calcular la superficie de una esfera
        :return: La superficie de una esfera
        """
        superficie = 4.0 * math.pi * (self.radio ** 2)
        return superficie

# Clase: Piramide
"""
Esta clase denominada Piramide es una subclase de FiguraGeometrica
que cuenta con una base, una altura y un apotema.
"""
class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base    # Atributo que identifica la base de una pirámide
        self.altura = altura  # Atributo que identifica la altura de una pirámide
        self.apotema = apotema # Atributo que identifica el apotema de una pirámide
        self.volumen = self.calcular_volumen()  # Calcula el volumen y establece su atributo
        self.superficie = self.calcular_superficie() # Calcula la superficie y establece su atributo

    def calcular_volumen(self):
        """
        Método para calcular el volumen de una pirámide
        :return: El volumen de una pirámide
        """
        volumen = ((self.base ** 2) * self.altura) / 3.0
        return volumen

    def calcular_superficie(self):
        """
        Método para calcular la superficie de una pirámide
        :return: La superficie de una pirámide
        """
        area_base = self.base ** 2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

# Clase: VentanaCilindro
"""
Esta clase denominada VentanaCilindro define una ventana para
ingresar los datos de un cilindro y calcular su volumen y superficie.
"""
class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.centrar_ventana()
        self.inicio()

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def inicio(self):
        # Etiquetas y campos de texto
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20, width=135, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135, height=23)

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50, width=135, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135, height=23)

        # Botón
        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=100, y=80, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=110, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=140, width=135, height=23)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())

            cilindro = Cilindro(radio, altura)
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

# Clase: VentanaEsfera
"""
Esta clase denominada VentanaEsfera define una ventana para
ingresar los datos de una esfera y calcular su volumen y superficie.
"""
class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        self.centrar_ventana()
        self.inicio()

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def inicio(self):
        # Etiquetas y campos de texto
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20, width=135, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135, height=23)

        # Botón
        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=100, y=50, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=90, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=120, width=135, height=23)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

# Clase: VentanaPiramide
"""
Esta clase denominada VentanaPiramide define una ventana para
ingresar los datos de una pirámide y calcular su volumen y superficie.
"""
class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)
        self.centrar_ventana()
        self.inicio()

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def inicio(self):
        # Etiquetas y campos de texto
        self.base_label = tk.Label(self, text="Base (cms):")
        self.base_label.place(x=20, y=20, width=135, height=23)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20, width=135, height=23)

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50, width=135, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50, width=135, height=23)

        self.apotema_label = tk.Label(self, text="Apotema (cms):")
        self.apotema_label.place(x=20, y=80, width=135, height=23)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80, width=135, height=23)

        # Botón
        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=120, y=110, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=140, width=135, height=23)
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=170, width=135, height=23)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())

            piramide = Piramide(base, altura, apotema)
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.volumen:.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

# Clase: VentanaPrincipal
"""
Esta clase denominada VentanaPrincipal define una interfaz gráfica
que permitirá consultar un menú principal con tres figuras
geométricas.
"""
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.centrar_ventana()
        self.inicio()

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def inicio(self):
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True) # Usamos pack para un layout más simple o grid
        # Si prefieres el layout nulo como en Java, sería: self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(1, weight=1)
        self.contenedor.grid_columnconfigure(2, weight=1)
        self.contenedor.grid_rowconfigure(0, weight=1)

        self.cilindro_btn = tk.Button(self.contenedor, text="Cilindro", command=self.abrir_cilindro)
        self.cilindro_btn.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.esfera_btn = tk.Button(self.contenedor, text="Esfera", command=self.abrir_esfera)
        self.esfera_btn.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.piramide_btn = tk.Button(self.contenedor, text="Pirámide", command=self.abrir_piramide)
        self.piramide_btn.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

# Clase: Principal
"""
Esta clase define el punto de ingreso al programa de figuras
geométricas. Por lo tanto, cuenta con un método main de acceso al
programa.
"""
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
    