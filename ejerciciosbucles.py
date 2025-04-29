#Ejercicios de Estructuras Condicionales y Bucles

#Ejercicio numero 1

num1= int(input("Escribe un numero entero: "))
if num1 <0:
    print("El numero es negativo")
elif num1 >0:
    print("El numero es positivo")
else:
    print("El numero es cero")


#Ejercicio numero 2

calificacion = int(input("Ingresa tu calificación de 0 a 100: "))
if calificacion == 100:
    print("Sacaste la nota maxima")
elif calificacion >=60:
    print("Aprobaste la materia")
else:
    print("No aprobaste la materia")


#Ejercicio numero 3

multiplicacion = int(input("ingresa un numero del 1 al 10: "))
for i in range(1,11):
    print(f"{multiplicacion} X {i} = {multiplicacion * i}")

#Ejercicio numero 4

num2 = int(input("Escribe un numero positivo: "))
if num2 >0:
    while num2 >=0:
        print (num2)
        num2= num2-1
else:
    print("El numero tiene que ser positivo")


#Ejercicio numero 5
# Ejercicio número 5

print("Adivina el número")

import random
numaleatorio = random.randrange(11)

# Establecer el número de intentos
intentos = 0
intentosmaximos = 3

while intentos < intentosmaximos:
    num3 = int(input("Ingresa un número: "))
    intentos += 1  # Incrementamos el contador de intentos
    
    if num3 == numaleatorio:
        print("¡Adivinaste el número!")
        break
    elif num3 > numaleatorio:
        print("El número es menor")
    elif num3 < numaleatorio:
        print("El número es mayor")
    
    # Verificar si ya se alcanzaron los intentos
    if intentos == intentosmaximos:
        print("no tienes mas intentos, El número era", numaleatorio)
