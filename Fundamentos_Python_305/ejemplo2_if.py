#PROGRAMA BECA UN SAN JOSE SIM HAMBRE
#EVALUANDO SI EL ALUMNO TIENE UNA CALIFICACION MAYOR A 8
#Y MENOR A 10
calificacion=float(input("Introduce tu calificacion"))
nombre=input("Introduce tu nombre")
if calificacion<=10 and calificacion>=8:
    print("felicidades"+nombre+"gamaste uma beca de 1000")
#evaluando si el alumno tiene una calificacion mayor a 6 
#y menor a 8
elif calificacion<8 and calificacion>6:
     print("felicidades"+nombre+"gamaste uma beca de 500")
else:
        print(""+nombre+"no fuiste beneficiado")