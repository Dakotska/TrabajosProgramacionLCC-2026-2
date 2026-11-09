import random

palos = ("♥", "♦", "♣", "♠")
#denominaciones = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') 
denominaciones = ('2','3','4','5','6','7','8','9','10') 
baraja = []
casa = 0
jugador = 0
tuplaCasaComp = []
tuplaJugadorComp = []
movimientos = 0

print(palos)
print(denominaciones)

for palo in palos:
    for denom in denominaciones:
        baraja.append((denom, palo))

random.shuffle(baraja)

print("Bienvenido al blackjack!")

while True:
    if movimientos == 0:
        for i in range(2):
            tuplaCasa = baraja.pop(0)
            tuplaCasaComp.append(tuplaCasa)
            print(tuplaCasaComp)
            casa += int(tuplaCasaComp[i][0])

            tuplaJugador = baraja.pop(0)
            tuplaJugadorComp.append(tuplaJugador)
            print(tuplaJugadorComp)
            jugador += int(tuplaJugadorComp[i][0])


print(casa)
print(jugador)

if casa == jugador:
    print("Empate")
elif casa > jugador:
    print("perdiste")
else:
    print("ganaste")