class Auto:

    def __init__(self, marca, modelo, anio):
       self.marca = marca
       self.modelo = modelo
       self.anio = anio

    def mostrar_informacion(self):
       print(f"Marca: {self.marca}")
       print(f"Modelo: {self.modelo}")
       print(f"Anio: {self.anio}")

auto1 = Auto("PORSCHE", "911_GT3RS", 2003)
auto2 = Auto("FERRARI", "ENZO", 2004)

auto1.mostrar_informacion()
auto2.mostrar_informacion()
       