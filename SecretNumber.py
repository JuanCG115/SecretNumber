from random import *
jugador = input('Cual es tu nombre: ')
numero = 0
valor = randint(1,100)
n_intentos = 0
print(f'Bueno, {jugador}, he pensado un número entre 1 y 100, \ny tienes solo ocho intentos para adivinar')

while n_intentos < 8:
    numero = int(input('En que numero estoy pensando? '))
    n_intentos +=1
    if numero not in range(1,101):
        print('Has elegido un numero que no esta permitido')
    elif numero<valor:
        print('Mi número secreto es mayor')
    elif numero>valor:
        print('Mi número secreto es menor')
    else:
        print(f'Felicidades {jugador} has ganado en {n_intentos} intentos')
        break
if numero != valor:
    print(f'Lo siento {jugador} has agotado lo intentos permitidos, \nel numero secreto es: {valor}')