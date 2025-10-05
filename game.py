# game.py
import pygame, sys
from config import ANCHO, ALTO, FPS, AZUL, MORADO
from jugador import Jugador
from plataforma import Plataforma
from enemigo import Enemigo

class Game:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Sombras del Tiempo")
        self.clock = pygame.time.Clock()
        self.mundo_dia = True
        self.running = True

        # Grupos
        self.todos = pygame.sprite.Group()
        self.plataformas = []
        self.enemigos = pygame.sprite.Group()

        # Jugador
        self.jugador = Jugador()
        self.todos.add(self.jugador)

        # Crear elementos
        self.crear_plataformas()
        self.crear_enemigos()

    def crear_plataformas(self):
        piso = Plataforma(0, ALTO-40, ANCHO, 40, "dia")
        self.todos.add(piso)
        self.plataformas.append(piso)
        p1 = Plataforma(200, 400, 150, 20, "dia")
        p2 = Plataforma(500, 300, 150, 20, "noche")
        self.todos.add(p1, p2)
        self.plataformas += [p1, p2]

    def crear_enemigos(self):
        e1 = Enemigo(100, ALTO - 80, "dia")
        e2 = Enemigo(600, 260, "noche")
        self.todos.add(e1, e2)
        self.enemigos.add(e1, e2)

    def verificar_colisiones(self):
        for enemigo in self.enemigos:
            if enemigo.activo and self.jugador.rect.colliderect(enemigo.rect):
                print("💀 Nilo ha sido derrotado.")
                self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.mundo_dia = not self.mundo_dia

            teclas = pygame.key.get_pressed()
            self.jugador.update(teclas, self.plataformas)

            # Fondo
            self.ventana.fill(AZUL if self.mundo_dia else MORADO)

            # Actualizaciones
            for p in self.plataformas:
                p.actualizar_color(self.mundo_dia)
            self.enemigos.update(self.mundo_dia)

            # Dibujar
            self.todos.draw(self.ventana)

            # Colisiones
            self.verificar_colisiones()

            pygame.display.flip()
            self.clock.tick(FPS)
