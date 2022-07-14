import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_válida(lista_palabras):
    #seleccionar una palabra al azar de la lista
    #de palabras válidas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()

def ahorcado():

    print('=====================================')
    print(' ¡Bienvenido al juego del Ahorcado! ')
    print('=====================================')

    palabra = obtener_palabra_válida(palabras)  
     
    letras_por_adivinar = set(palabra) #conjunto de letras por adivinar
    letras_adivinadas = set() #No {} -> se crea diccionario
    abecedario = set(string.ascii_uppercase) # ascii -> devuelve el abecesario (sin ñ)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
       
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") #join -> Une los elementos de un conjunto o secuencia con el caracter especificado

        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] # -> List Comprehension
        # Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input('Escoge una letra: ').upper()

#Si la letra escogda por el usario está en el abecesario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas

        if letra_usuario in abecedario - letras_adivinadas: #no está en letras adivinadas
            letras_adivinadas.add(letra_usuario)     
        
        #Si la letra está en la palabra remover la letra del conjunto de letras pendientes por adivinar, sino quitar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vidas -= 1
                print(f'\nTu letra, {letra_usuario} no está en la palabra')
        #Si la letra escogida por el ususario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print('\nYa escogiste esta letra. Por favor escoge una letra nueva')
        else: 
            print('\nEsta letra no es válida.')
    #El juego llega a esta línea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del jugador

    if vidas == 0:
        print(vidas_diccionario_visual)
        print(f"¡Ahorcado! Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente!¡Adivinaste la palabra! {palabra}')

ahorcado()



