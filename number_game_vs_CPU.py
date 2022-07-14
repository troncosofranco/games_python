import random


def adivina_el_número_computadora(x): 

    print('========================')
    print(' ¡Bienvenido al Juego! ')
    print('========================')
    print(f'Selecciona un número entre 1 y {x} para que la computadura intente adivinarlo')

    limite_inferior = 1 #[1, x]
    limite_superior = x

    respuesta = ''
    while respuesta != 'c':
        #generar una predicción
        if limite_inferior != limite_superior:
            predicción = random.randint(limite_inferior, limite_superior)  
        else:
            predicción = limite_inferior

        #Obtener respuesta del usuario
        respuesta = input(f'Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja ingresa (B). Si es correcta, ingresa (C): ').lower() # conviert el string a letras minúsculas

        if respuesta == 'a':
            limite_superior = predicción - 1
        elif respuesta == 'b':
            limite_inferior = predicción + 1
    
    print(f'¡Sí! La computadora adivinó tu número correctamente {predicción}')


adivina_el_número_computadora(10)