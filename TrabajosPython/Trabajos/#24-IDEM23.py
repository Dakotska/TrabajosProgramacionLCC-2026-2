listaAlumnos = []
listaSobresalientes = []
nombresSobre = []
nombres = []
numCalif = 0
calif = 0
promedio = 0
nombre = ""

while True:
    try:
        numsCalif = int(input("Ingresa la cantidad de números a ingresar (>1): "))
        while numsCalif < 1 :
            numsCalif = int(input("Error: Ingresa la cantidad de números a ingresar (>1): "))
        break
    except ValueError:
        print("ERROR: Ingresa solo números enteros.")


for i in range(numsCalif):
    while True:
        try:
            nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
            while len(nombre.strip()) < 1:
                nombre = input(f"ERROR: Ingresa el nombre del alumno {i+1}: ")
            
            calif = float(input(f"Ingresa la calificación de {nombre}: "))
            while calif < 0 or calif > 100:
                calif = float(input(f"ERROR: Ingresa una calificación válida (0-100) para {nombre}: "))
            
            nombres.append(nombre)
            listaAlumnos.append(calif)
            break 
        except ValueError:
            print("ERROR: Ingresa un número válido para la calificación.")

for l in range(len(listaAlumnos)):
    promedio += listaAlumnos[l]

promedio = promedio / numsCalif

for j in range(len(listaAlumnos)):
    if listaAlumnos[j] > promedio:
        listaSobresalientes.append(listaAlumnos[j])
        nombresSobre.append(nombres[j])

if len(listaSobresalientes) > 0:
    print("El promedio es de", promedio)
    for k in range(len(listaSobresalientes)):
        print(f"Alumno {k+1}: {nombresSobre[k]} {listaSobresalientes[k]}")
else:
    print("No hubo alumnos sobresalientes.")