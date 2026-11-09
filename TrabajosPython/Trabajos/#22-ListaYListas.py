lista = []
listaLimpia = []
nums = 0
n = 0

while True:
    try:
        nums = int(input("Ingresa la cantidad de números a ingresar (>1): "))
        while nums < 1 :
            nums = int(input("Ingresa la cantidad de números a ingresar (>1): "))
        break
    except ValueError:
        print("ERROR: Ingresa solo números enteros.")

for i in range(nums):
    while True:
        try:
            n = int(input(f"Ingresa el número {i+1}: "))
            lista.append(n)
            
            break 
        except ValueError:
            print("ERROR: Ingresa solo números enteros.")

print(f"Tu lista normal es: {lista}")

for elemento in lista:
    if elemento not in listaLimpia:
        listaLimpia.append(elemento)

print(f"Tu lista limpia es: {listaLimpia}")