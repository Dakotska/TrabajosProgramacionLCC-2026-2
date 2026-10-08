import sys

print("Calculadora de cambio según billetes.")

Precio = int(input("Precio del articulo en enteros positivos: "))

if Precio < 0:
    print("Ingresa un numero entero positivo.", file=sys.stderr)
    Precio = int(input("Precio del articulo en enteros positivos: "))

Importe = int(input("Ingresa tu importe en enteros positivos: "))

if Importe < Precio or Importe < 0:
    print("Ingresa un numero mayor al importe y que sea entero positivo", file=sys.stderr)
    Importe = int(input("Ingresa tu importe en enteros positivos: "))

if Importe - Precio > 0:
    Vuelto = Importe - Precio

    mxn500 = Vuelto // 500
    Vuelto = Vuelto - mxn500 * 500
    mxn200 = Vuelto // 200
    Vuelto = Vuelto - mxn200 * 200
    mxn100 = Vuelto // 100
    Vuelto = Vuelto - mxn100 * 100
    mxn50 = Vuelto // 50
    Vuelto = Vuelto - mxn50 * 50
    mxn20 = Vuelto // 20
    Vuelto = Vuelto - mxn20 * 20
    mxn10 = Vuelto // 10
    Vuelto = Vuelto - mxn10 * 10
    mxn5 = Vuelto // 5
    Vuelto = Vuelto - mxn5 * 5
    mxn2 = Vuelto // 2
    Vuelto = Vuelto - mxn2 * 2
    mxn1 = Vuelto // 1
    Vuelto = Vuelto - mxn100

    print(f"Precio total del producto = {Precio}")
    print(f"Importe total = {Importe}")
    print(f"Vuelto esperado = {Importe - Precio}")
    if mxn500 > 0:
        print(f"Billetes de 500 = {mxn500}")
    if mxn200 > 0:
        print(f"Billetes de 200 = {mxn200}")
    if mxn100 > 0:
        print(f"Billetes de 100 = {mxn100}")
    if mxn50 > 0:
        print(f"Billetes de 50 = {mxn50}")
    if mxn20 > 0:
        print(f"Billetes de 20 = {mxn20}")
    if mxn10 > 0:
        print(f"Monedas de 10 = {mxn10}")
    if mxn5 > 0:
        print(f"Monedas de 5 = {mxn5}")
    if mxn2 > 0:
        print(f"Monedas de 2 = {mxn2}")
    if mxn1 > 0:
        print(f"Monedas de 1 = {mxn1}")
else:
    print("Tu vuelto es de 0", file=sys.stderr)