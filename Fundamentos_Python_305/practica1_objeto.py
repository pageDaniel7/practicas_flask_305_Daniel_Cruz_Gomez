class Producto:
   def __init__(self, nombre, precio, cantidad):
       self.nombre = nombre
       self.precio = precio
       self.cantidad = cantidad

   def calcular_total(self):
       return self.precio * self.cantidad

Producto1 = Producto("cuaderno", 35.50, 3)
print("Producto:", Producto1.nombre)
print("Precio:", Producto1.precio)
print("Cantidad:", Producto1.cantidad)
print("Total:", Producto1.calcular_total())