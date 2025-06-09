import tkinter as tk
from tkinter import messagebox
import math

## Notas
class Notas:
    
    def __init__(self):
        self.listaNotas = [0.0] * 5 

    def calcularPromedio(self):
        suma = 0
        for i in range(1, len(self.listaNotas)):  
            suma += self.listaNotas[i]
        return suma / len(self.listaNotas)

    def calcularDesviacion(self):
        prom = self.calcularPromedio()
        suma = 0
        for i in range(len(self.listaNotas)):
            suma += (self.listaNotas[i] - prom) ** 2
        return math.sqrt(suma / len(self.listaNotas))

    def calcularMenor(self):
        menor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] < menor:
                menor = self.listaNotas[i]
        return menor

    def calcularMayor(self):
        mayor = self.listaNotas[0]
        for i in range(len(self.listaNotas)):
            if self.listaNotas[i] > mayor:
                mayor = self.listaNotas[i]
        return mayor
## Ventana principal
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
       
        self.nota1 = tk.Label(self, text="Nota 1:")
        self.nota1.place(x=20, y=20, width=135, height=23)
        self.campoNota1 = tk.Entry(self)
        self.campoNota1.place(x=105, y=20, width=135, height=23)

        self.nota2 = tk.Label(self, text="Nota 2:")
        self.nota2.place(x=20, y=50, width=135, height=23)
        self.campoNota2 = tk.Entry(self)
        self.campoNota2.place(x=105, y=50, width=135, height=23)

        self.nota3 = tk.Label(self, text="Nota 3:")
        self.nota3.place(x=20, y=80, width=135, height=23)
        self.campoNota3 = tk.Entry(self)
        self.campoNota3.place(x=105, y=80, width=135, height=23)

        self.nota4 = tk.Label(self, text="Nota 4:")
        self.nota4.place(x=20, y=110, width=135, height=23)
        self.campoNota4 = tk.Entry(self)
        self.campoNota4.place(x=105, y=110, width=135, height=23)

        self.nota5 = tk.Label(self, text="Nota 5:")
        self.nota5.place(x=20, y=140, width=135, height=23)
        self.campoNota5 = tk.Entry(self)
        self.campoNota5.place(x=105, y=140, width=135, height=23)

        
        self.calcular = tk.Button(self, text="Calcular", command=self._calcular)
        self.calcular.place(x=20, y=170, width=100, height=23)

        
        self.limpiar = tk.Button(self, text="Limpiar", command=self._limpiar)
        self.limpiar.place(x=125, y=170, width=80, height=23)

        
        self.promedio = tk.Label(self, text="Promedio = ")
        self.promedio.place(x=20, y=210, width=200, height=23)

        self.desviacion = tk.Label(self, text="Desviación estándar = ")
        self.desviacion.place(x=20, y=240, width=200, height=23)

        self.mayor = tk.Label(self, text="Valor mayor = ")
        self.mayor.place(x=20, y=270, width=200, height=23)

        self.menor = tk.Label(self, text="Valor menor = ")
        self.menor.place(x=20, y=300, width=200, height=23)

    def _calcular(self):
        notas = Notas()
        try:
            notas.listaNotas[0] = float(self.campoNota1.get())
            notas.listaNotas[1] = float(self.campoNota2.get())
            notas.listaNotas[2] = float(self.campoNota3.get())
            notas.listaNotas[3] = float(self.campoNota4.get())
            notas.listaNotas[4] = float(self.campoNota5.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese todas las notas como números válidos.")
            return

        promedio = notas.calcularPromedio()
        desviacion = notas.calcularDesviacion()
        mayor = notas.calcularMayor()
        menor = notas.calcularMenor()

        self.promedio.config(text=f"Promedio = {promedio:.2f}")
        self.desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
        self.mayor.config(text=f"Valor mayor = {mayor}")
        self.menor.config(text=f"Valor menor = {menor}")

    def _limpiar(self):
        self.campoNota1.delete(0, tk.END)
        self.campoNota2.delete(0, tk.END)
        self.campoNota3.delete(0, tk.END)
        self.campoNota4.delete(0, tk.END)
        self.campoNota5.delete(0, tk.END)
        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación estándar = ")
        self.mayor.config(text="Valor mayor = ")
        self.menor.config(text="Valor menor = ")


# Principal

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()

