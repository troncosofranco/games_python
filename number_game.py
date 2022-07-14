import random


def adivina_el_número(x):

    print('========================') 
    print(' ¡Bienvenido al Juego!' )
    print('========================')
    print('Tu meta es adivinar el número generado por la computadora.')

    número_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x (randint -> Genera un entero aleatorio)

    predicción = 0

    while predicción != número_aleatorio:
        predicción = int(input(f'Adivina un número entre 1 y {x}: ')) #f-string - int -> convierte el input en un entero. (input: siempre retorna una cadena de caracteres)

        if predicción < número_aleatorio:
            print('Intenta otra vez. Este número es muy pequeño.')
        elif predicción > número_aleatorio:
            print('Intenta otra vez. Este número es muy grande.')

    print(f'¡Felicitaciones! Adivintaste el número {número_aleatorio} correctamente.')

#Por definición: dejar dos líneas por encima y por debajo de la función

adivina_el_número(20) #Internamente se tiene que especificar la función
