Funcion Intercambiar(a Por Referencia, b Por Referencia)
	Definir Aux Como Entero
	
	aux <- b
	b <- a
	a <- aux
FinFuncion

Proceso IntercambioDeNumeros
	Definir a, b Como Entero
	
	Escribir "Ingresa 2 numeros para intercambiar su ubicacion."
	
	Escribir "Ingresa a: " Sin Saltar
	Leer a
	Escribir "Ingresa b: " Sin Saltar
	Leer b
	
	Escribir "Posiciones originales: a = ", a, " b = ", b
	
	Intercambiar(a,b)
	
	Escribir "Posiciones Intercambiadas : a = ", a, " b = ", b
FinProceso
