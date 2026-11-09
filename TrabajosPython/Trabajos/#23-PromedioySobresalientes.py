listaAlumnos = []
listaSobresalientes = []
numCalif = 0
calif = 0
promedio = 0

while True:
    try:
        numsCalif = int(input("Ingresa la cantidad de números a ingresar (mayor a 0): "))
        while numsCalif < 1:
            numsCalif = int(input("ERROR: Ingresa una cantidad mayor a 0: "))
        
        break 
    except ValueError:
        print("ERROR: Ingresa solo números enteros.")

for i in range(numsCalif):
    while True:
        try:
            calif = float(input(f"Ingresa la calificación {i+1}: "))
            while calif < 0 or calif > 100:
                calif = float(input("ERROR: Ingresa una calificación entre 0 y 100: "))
            
            listaAlumnos.append(calif)
            break 
        except ValueError:
            print("ERROR: Ingresa solo números reales (enteros o decimales).")

for l in range(len(listaAlumnos)):
    promedio += listaAlumnos[l]

promedio = promedio / numsCalif

for j in range(len(listaAlumnos)):
    if listaAlumnos[j] > promedio:
        listaSobresalientes.append(listaAlumnos[j])

if len(listaSobresalientes) > 0:
    print("El promedio es de", promedio)
    for k in range(len(listaSobresalientes)):
        print(f"Alumno: {listaSobresalientes[k]}")
else:
    print("No hubo alumnos sobresalientes.")