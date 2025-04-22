import time #Modulo que contiene la funcion timesleep



#Calculadora de descuentos para la empresa "Tiendas D1"#
#Declaración de variables fijas

Nombre_producto:str=  0
Precio_unitario:float = 0
Cantidad:int = 0
Descuento:float = 0


#Bienvenida

print("\n\n\n\n\n ★★★★★★★★★★★ Bienvenido al sistema de inventarios del D1 ★★★★★★★★★★★")
time.sleep(1) #tiempo de espera para una mejor lectura

print(" \n\n\n\n A continuación se le pedirán datos de vital importancia para calcular el costo de los productos comprados\n\npor favor lea con atención y llene los datos con total honestidad  ")
time.sleep(1) #tiempo de espera para una mejor lectura

print(" \n\n\n\n★★★★★★★★★★★★ Mercados D1 de todos! ★★★★★★★★★★★★ \n\n\n\n ")

#Entrada de datos

#con modulo para arreglar errores

#ingresa el nombre del producto
try:
                    Nombre_producto = input("Por favor ingrese el nombre de producto que comprará: \n ")
                    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")


#ingresa el precio unitario
try:
                    Precio_unitario= float(input("Por favor ingrese el valor unitario del producto \n"))
                    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")


#ingresa la cantidad de productos a comprar

try:
                    Cantidad = int(input("Por favor ingrese  que comprará \n"))
                    
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")




# Ingresa el valor del descuento 
try:
                    Descuento = float(input("si el producto tiene un descuento, indique la cantidad, si no lo tiene escriba el numero 0 \n"))

                
except ValueError:
                    print(" \n Error: ingresó un valor incorrecto o diferente al solicitado  por favor intentelo nuevamente \n")

            

print("   ")

