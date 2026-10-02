#1.Definimos la clase
class perro:
    def __init__(self,nombre,raza):
        #Definimos los atributos
        self.nombre=nombre
        self.raza=raza
    #metodo de comportamiento
    def ladrar(self):
        return f"{self.nombre}dice:¡Guau"
    def comer(self):
        return f"{self.nombre}come croquetas"
    #2. creamos los objetos(instancias de la clase)    
mi_perro=perro("firulais","labrador")
otro_perro=perro("solovino","electrico")
un_perro_mas()
#3. usar los objetos
print(mi_perro.nombre)#acceder al atributo nombre
print(otro_perro.ladrar())#acceder al metodos
print(otro_perro.comer())