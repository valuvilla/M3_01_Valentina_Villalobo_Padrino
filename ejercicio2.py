#Imput nos permite capturar información por teclado
#Creamos una variable
e1= int(input("Dime un número entero: "))
#Presentamos el número obtenido en el formato de 5 dígitos con relleno de 0s.
print("{:05d}".format(e1))
###########################
#Creamos otro variable
e2=float(input("Dime un número flotante"))
#Presentamos el número con 5 digita en la parte entera y 3 en la decimal.
print("{:09.03f}".format(e2))

      