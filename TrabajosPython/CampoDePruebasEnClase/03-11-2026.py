list = [1,2,3]

print(list)

list.append(67)

print(list)

list.clear()

print(list)

list[3:7] = 10,11,12,13

print(list)

list.copy()

print(list)

for valor in list:
    print(valor)

list2 = [8,6,4,2]

listu = list + list2

print(listu)

for indice, valor in enumerate(list):
    print(indice, valor)

print("")

for valor1, valor2 in zip(list, list2):
    print(valor1, valor2)

v1, v2, v3, v4 = list

print(v1, v2, v3, v4)

v5, _, v6, _ = list2

print(v5, v6)

