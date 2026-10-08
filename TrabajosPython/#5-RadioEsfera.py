import math as mt

print("Bienvenido a la calculadora de volumen de una esfera.")

radio = int(input("Ingresa el radio de tu esfera: "))

if radio <= 0:
    print("Ingresa un numero entero positivo")
    radio = int(input("Ingresa el radio de tu esfera: "))

volumen = (4/3) * mt.pi * (radio ** 3)

print(f"El volumen total de tu esfera es de {volumen} u³")