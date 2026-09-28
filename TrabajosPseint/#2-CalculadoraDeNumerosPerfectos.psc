Funcion perfecto <- CalculoNUmeroPerfecto(num)
	Definir perfecto Como Logico
	Definir i, suma Como Entero

	suma <- 0

	Para i <- 1 Hasta num / 2 Con Paso 1 Hacer
		Si num MOD i = 0 Entonces
			suma <- suma + i
		FinSI
	FinPara

	Si suma = num Entonces
		perfecto <- Verdadero
	SiNo
		perfecto <- Falso
	FinSi
FinFuncion

Proceso CalculadoraDeNumerosPerfectos
	Definir num Como Entero

	Repetir
		Escribir "Ingresa un numero entero positivo: "
		Leer num
	Hasta Que num > 0

	Si CalculoNUmeroPerfecto(num) Entonces
		Escribir num, " Es un numero perfecto."
	SiNo
		Escribir num, " No es un numero perfecto."
	FinSI
FInProceso