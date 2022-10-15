from pygame.locals import *
from juego import *
from jugador import *
from manzana import *
from random import randint
import pygame
import time
import sys


class Aplicacion:
    # pestaña
    windowWidth = 1200
    windowHeight = 920
    jugador = 0
    manzana = 0
    fresa = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._manzana_surf = None
        self.juego = Juego()
        self.jugador = Jugador(3)
        self.manzana = Manzana(5, 5)
        self.fresa = Manzana(3, 3)
        self.banano = Manzana(3, 4)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('El juego de la serpiente')# aqui es la pestaña cuando se ejecuta es el mensaje que sale
        self._running = True
        # cambiar imagenes
        self._image_surf = pygame.image.load("imagenes/cuadrado.jpg").convert()
        self._manzana_surf = pygame.image.load("imagenes/manzana.png").convert()
        self._fresa_surf = pygame.image.load("imagenes/fresa.jpg").convert()
        self._banano_surf = pygame.image.load("imagenes/banano.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.jugador.update()

        # comer manzana
        for i in range(0, self.jugador.longitud):
            if self.juego.isCollision(self.manzana.x, self.manzana.y, self.jugador.x[i], self.jugador.y[i], 44):
                self.manzana.x = randint(2, 9) * 44
                self.manzana.y = randint(2, 9) * 44
                # Esto sirve para que aumenten los cuadritos cuando se come
                # para las diferntes frutas
                self.jugador.longitud = self.jugador.longitud + 1  # sirve para que le sume uno cuadro media vez que come la fruta manzana

            elif self.juego.isCollision(self.fresa.x, self.fresa.y, self.jugador.x[i], self.jugador.y[i], 44):
                self.fresa.x = randint(2, 9) * 44
                self.fresa.y = randint(2, 9) * 44
                self.jugador.longitud = self.jugador.longitud + 2 # sirve para que le sume dos cuadro media vez que come la fruta fresa

            elif self.juego.isCollision(self.banano.x, self.banano.y, self.jugador.x[i], self.jugador.y[i], 44):
                self.banano.x = randint(2, 9) * 44
                self.banano.y = randint(2, 9) * 44
                self.jugador.longitud = self.jugador.longitud + 3 # sirve para que le sume tres cuadro media vez que come la fruta banano


        # chocas consigo mismo
        for i in range(2, self.jugador.longitud):
            if self.juego.isCollision(self.jugador.x[0], self.jugador.y[0], self.jugador.x[i], self.jugador.y[i], 40):
                print("¡Perdiste! Chocaste ")
                print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
                exit(0)

        # pass

    def on_render(self):
        # aqui sirve para imprimir el imagen
        self._display_surf.fill((0, 0, 0))
        self.jugador.draw(self._display_surf, self._image_surf)
        self.manzana.draw(self._display_surf, self._manzana_surf)
        self.fresa.draw(self._display_surf, self._fresa_surf)
        self.banano.draw(self._display_surf, self._banano_surf)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.jugador.moveRight()

            if (keys[K_LEFT]):
                self.jugador.moveLeft()

            if (keys[K_UP]):
                self.jugador.moveUp()

            if (keys[K_DOWN]):
                self.jugador.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)# aqui va velocidad en que va el juego
        self.on_cleanup()

    def salir(self):
        return sys.exit()