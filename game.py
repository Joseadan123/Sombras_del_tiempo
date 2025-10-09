# game.py
import pygame, sys
from config import ANCHO, ALTO, FPS, AZUL, MORADO, BLANCO
from jugador import Jugador
from plataforma import Plataforma
from enemigo import Enemigo
from fragmento import Fragmento
from niveles import cargar_nivel
from plataforma_movil import PlataformaMovil

class Game:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Sombras del Tiempo")
        self.clock = pygame.time.Clock()
        self.mundo_dia = True
        self.running = True
        self.nivel_actual = 0
        self.muerto = False  # Estado de muerte
        self.tiempo_muerte = 0

        # Grupos
        self.todos = pygame.sprite.Group()
        self.plataformas = []
        self.enemigos = pygame.sprite.Group()
        self.fragmentos = pygame.sprite.Group()

        # Jugador
        self.jugador = Jugador()
        self.todos.add(self.jugador)

        # Cargar primer nivel
        self.cargar_nivel(self.nivel_actual)

    def cargar_nivel(self, num):
        self.todos.empty()
        self.plataformas = []
        self.enemigos.empty()
        self.fragmentos.empty()

        # Añadimos jugador
        self.todos.add(self.jugador)
        self.jugador.rect.midbottom = (ANCHO // 2, ALTO - 50)
        self.jugador.vel_x = 0
        self.jugador.vel_y = 0
        self.jugador.en_suelo = True

        nivel = cargar_nivel(num)
        if nivel is None:
            self.mostrar_mensaje("✨ ¡Has completado todos los niveles! 🕰️")
            self.running = False
            return

        # Crear plataformas normales
        for x, y, w, h, mundo in nivel["plataformas"]:
            p = Plataforma(x, y, w, h, mundo)
            self.todos.add(p)
            self.plataformas.append(p)

        # Crear plataformas móviles
        self.plataformas_moviles = []
        for x, y, w, h, mundo, dir, rango, vel in nivel["moviles"]:
            p = PlataformaMovil(x, y, w, h, mundo, dir, rango, vel)
            self.todos.add(p)
            self.plataformas_moviles.append(p)

        # Crear enemigos
        for x, y, mundo in nivel["enemigos"]:
            e = Enemigo(x, y, mundo)
            self.todos.add(e)
            self.enemigos.add(e)

        # Crear fragmento
        fx, fy = nivel["fragmento"]
        f = Fragmento(fx, fy)
        self.todos.add(f)
        self.fragmentos.add(f)

    def verificar_colisiones(self):
        # Si el jugador cae al vacío
        if self.jugador.rect.top > ALTO:
            self.morir(" Has caído al vacío...")

        # Colisión con enemigos activos
        for enemigo in self.enemigos:
            if enemigo.activo and self.jugador.hitbox.colliderect(enemigo.rect):
                self.morir(" Un enemigo te atrapó...")

        # Colisión con fragmento (victoria)
        for fragmento in self.fragmentos:
            if self.jugador.rect.colliderect(fragmento.rect):
                fragmento.recoger()
                self.mostrar_mensaje("Fragmento obtenido ")
                self.nivel_actual += 1
                self.cargar_nivel(self.nivel_actual)

    def morir(self, mensaje):
        self.mostrar_mensaje(mensaje)
        self.muerto = True
        self.tiempo_muerte = pygame.time.get_ticks()

    def reiniciar_nivel(self):
        # Reinicia al jugador y el nivel actual
        self.cargar_nivel(self.nivel_actual)
        self.muerto = False

    def mostrar_mensaje(self, texto):
        fuente = pygame.font.SysFont("arial", 40, True)
        render = fuente.render(texto, True, BLANCO)
        rect = render.get_rect(center=(ANCHO // 2, ALTO // 2))
        self.ventana.blit(render, rect)
        pygame.display.flip()
        pygame.time.wait(1500)

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

            # Si está muerto, esperar un segundo antes de reiniciar
            if self.muerto:
                if pygame.time.get_ticks() - self.tiempo_muerte > 1500:
                    self.reiniciar_nivel()
                continue

            # Actualizar jugador
            self.jugador.update(teclas, self.plataformas, self.mundo_dia)

            # Fondo
            self.ventana.fill(AZUL if self.mundo_dia else MORADO)

            # Actualizar enemigos y plataformas
            for p in self.plataformas:
                p.actualizar_color(self.mundo_dia)
            for pm in self.plataformas_moviles:
                pm.update(self.mundo_dia)
                pm.actualizar_color(self.mundo_dia)

            # Dibujar
            self.todos.draw(self.ventana)

            # Colisiones
            self.verificar_colisiones()

            pygame.display.flip()
            self.clock.tick(FPS)