#1. creando la clase
class vehiculo:
    #creando mi metodo constructor
    def __init__(self,modelo,color,marca,ano):
        #inicializando los atributos
        self. modelo=modelo
        self. color=color
        self. marca=marca
        self. ano=ano
    #creando los metodos
    def acelerar(self):
        return f"{self.modelo}runnnnn"
    def frenar(self):
        return f"{self.marca}iiiiii"
    #crear los objetos o las instancias
carro1=vehiculo("tacoma","negro","toyota","2026")
carro2=vehiculo("versa","azul","nissan","2020")
print(carro1.marca)
print(carro1.modelo)
print(carro2.frenar())