# Hola
from juego import *
from aplicacion import *
from manzana import *
from jugador import *









# Nota solo por el momento esta el menu todavia falta agregar lo de velociodad



while True:

    print('Niveles de dificultad:')
    print('1- Facil: ')
    print('2- Intermedio:')
    print('3- Dificil:')
    print('4- Dinamico: ')
    print('5- Salir')
    opcion = int(input('Ingrese los opciones: '))
    if opcion == 1:
        aplicacion = Aplicacion()
        aplicacion.on_execute()
    elif opcion == 2:
        aplicacion = Aplicacion()
        aplicacion.on_execute()
    elif opcion == 3:
        aplicacion = Aplicacion()
        aplicacion.on_execute()
    elif opcion == 4:
        aplicacion = Aplicacion()
        aplicacion.on_execute()
    elif opcion == 5:
        break
    else:
        continue









