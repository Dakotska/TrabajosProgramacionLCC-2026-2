Funcion amigos <- CalculoNumerosAmigos(num1, num2)
	Definir amigos Como Logico
	Definir i1, i2, suma1, suma2 Como Entero

	suma1 <- 0
	suma2 <- 0

	Para i1 <- 1 Hasta num1 / 2 Con Paso 1 Hacer
		Si num1 MOD i1 = 0 Entonces
			suma1 <- suma1 + i1
		FinSI
	FinPara

	Para i2 <- 1 Hasta num2 / 2 Con Paso 1 Hacer
		Si num2 MOD i2 = 0 Entonces
			suma2 <- suma2 + i2
		FinSI
	FinPara

	Si suma1 = num2 y suma2 = num1 y num1 <> num2 Entonces
		amigos <- Verdadero
	SiNo
		amigos <- Falso
	FinSi
FinFuncion

Proceso CalculadoraDeNumerosAmigos
	Definir num1, num2 Como Entero

	Repetir
		Escribir "Ingresa un primer numero entero positivo: "
		Leer num1
	Hasta Que num1 > 0

	Repetir
		Escribir "Ingresa un segundo numero entero positivo: "
		Leer num2
	Hasta Que num2 > 0

	Si CalculoNumerosAmigos(num1, num2) Entonces
		Escribir num1, " y ", num2, " Son números amigos."
	SiNo
		Escribir num1, " y ", num2, " No son números amigos."
	FinSI
FInProceso