dim = int(input("Ingresa un numero: "))
simbolo = "*"

"""for i in range(1, dim+1):
    print(f"{i*simbolo:<{dim}s}|{i*simbolo:>{dim}s}")

print("-"*dim*2 + "-")

for j in range(dim, 0, -1):
    print(f"{j*simbolo:<{dim}s}|{j*simbolo:>{dim}s}")

print("-"*dim*2 + "-")
dim = int(input("Ingresa un numero impar: "))
while dim % 2 == 0:
    dim = int(input("ERROR: Ingresa un numero impar: "))
print("-"*dim*2 + "-")

for k in range(1, dim+1, 2):
    print(f"{k*simbolo:^{dim*2 + 1}s}")

print("-"*dim*2 + "-")

for l in range(dim, 0, -2):
    print(f"{l*simbolo:^{dim*2 + 1}s}")"""

cont = 2

for n in range(1, (dim*2)+1):
    if n < dim:
        print(f"{n*simbolo:<{dim}s}")
    else:
        cont += 1
        print(f"{(n-1*cont)*simbolo:<{dim}s}")