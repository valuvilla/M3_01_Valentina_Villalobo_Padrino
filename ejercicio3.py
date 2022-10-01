#pedimos al usuario una valor para el peso y otro para la altura
#Los almacenamos en dos variables
alt=float(input("introduce altura"))
peso=float(input("introduce peso"))
#Maneras de escribir el resultado
#Utilizamos el comando format de la maner más basica
print("P1 : La altura es {} metros y el peso es de {} KG".format(alt, peso))
print("\n")
#Indicamos el el número de digitos de la parte decimal
print("P2 : La altura es {:.02f} metros y el peso es de {:.03f} KG".format(alt, peso))
print("\n")
#Indicamos el orden de las variables
print("P3 : La altura es {0} metros y el peso es de {1} KG".format(alt, peso))
print("\n")
print("P4 : La altura es {1} metros y el peso es de {0} KG".format(peso, alt))
print("\n")
#Creamos otras dos variables
print("P5 : La altura es {alt} metros y el peso es de {peso} KG".format(alt=alt, peso=peso))
print("\n")
#Para optimizar la escritura, agregamos la f, de format al principio de la frase
print(f'P6 : la altura es {alt} metros y el peso es de {peso} KG')
print("\n")
#El signo de porcetaje también hace la función de format
print('P7 : La altura es %(alt)s metros y el peso es de %(peso)s KG'% {"alt":alt,"peso":peso})
print("\n")
#Creamos una variable que compile toda la frase y luego hace uso del comando de format
text = "P8 : La altura es {} metros y el peso es de {} KG"
print(text.format(alt, peso))
print("\n")
#Mismo procedimiento que la "P7" pero fragmentamos la frase
part1 = "La altura es {} metros"
part2 = "El peso es de {} KG"
print("P9 : " + part1.format(alt) + " y " + part2.format(peso))
print("\n")