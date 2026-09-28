Funcion CalculoDeVocales(cadenaDeTexto, cantidadVocales Por Referencia, vocalA Por Referencia, vocalE Por Referencia, vocalI Por Referencia, vocalO Por referencia, vocalU Por referencia)
    Definir i Como Entero
	Definir vocal Como Caracter

    Para i <- 1 Hasta Longitud(cadenaDeTexto) Con Paso 1 Hacer
        vocal <- Minusculas(SubCadena(cadenaDeTexto, i, i))

        Si vocal = "a" o vocal = "e" o vocal = "i" o vocal = "o" o vocal = "u" Entonces
            cantidadVocales <- cantidadVocales + 1

            Segun vocal Hacer
                "a":
                    vocalA <- vocalA + 1
                "e":
                    vocalE <- vocalE + 1
                "i":
                    vocalI <- vocalI + 1
                "o":
                    vocalO <- vocalO + 1
                "u":
                    vocalU <- vocalU + 1
            FinSegun
        FinSi
    FinPara
FinFuncion

Proceso ContadorDeVocales
    Definir cadenaDeTexto Como cadena
    Definir cantidadVocales, vocalA, vocalE, vocalI, vocalO, vocalU Como Entero

	cantidadVocales <- 0
	vocalA <- 0
	vocalE <- 0
	vocalI <- 0
	vocalO <- 0
	vocalU <- 0

    Repetir
        Escribir "Ingresa texto para calcular sus vocales."
        Leer cadenaDeTexto
    Hasta Que Longitud(cadenaDeTexto) > 0

	CalculoDeVocales(cadenaDeTexto, cantidadVocales, vocalA, vocalE, vocalI, vocalO, vocalU)

    Si cantidadVocales > 0 Entonces
        Escribir "La cantidad de vocales totales es de: ", cantidadVocales
        Escribir "La cantidad de A es de: ", vocalA
        Escribir "La cantidad de E es de: ", vocalE
        Escribir "La cantidad de I es de: ", vocalI
        Escribir "La cantidad de O es de: ", vocalO
        Escribir "La cantidad de U es de: ", vocalU
    SiNo
        Escribir "No se encontró ninguna vocal."
    FinSi
FInProceso