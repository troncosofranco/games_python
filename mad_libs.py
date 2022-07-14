# Concatenar cadenas de caracateres

# organización = 'FreeCodeCamp'

#print('Aprende a programar con ' + organización)
#print ('Aprende a programar con {}'.format(organización)) #format -> reemplaza el contenido entre {}
#print(f'Aprende a programar con {organización}') # f-string

# Mad Libs (Historias locas)
#Alt + Z -> Línea debajo

adj = input('Adjetivo: ')
verbo1 = input('Verbo: ')
verbo2 = input('Verbo: ')
sustantivo_plural = input('Sustantivo (plural): ')

madlib = f'¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1}. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!'

print(madlib)