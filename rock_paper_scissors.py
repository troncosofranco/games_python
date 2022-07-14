import random

def jugar(): #No se requiere ningún valor
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel o 'ti' para tijera.\n ").lower #\n: salto de linea
    computadora = random.choice(['pi', 'pa', 'ti']) #random.choice -> elige al azar un elemento de una lista

    if usuario == computadora:
        return '¡Empate!' 
    
    if ganó_el_jugador(usuario, computadora): #llamado a la función
        return '¡Ganaste!'

    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente): # definición de la función
    if ((jugador == 'pi' and oponente == 'ti') #varias condiciones
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(jugar())