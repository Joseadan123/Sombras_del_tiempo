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
        self.muerto = False
        self.tiempo_muerte = 0
        self.completed = False

        # Fondos
        self.fondo_dia = pygame.image.load("assets/dias.png").convert()
        self.fondo_dia = pygame.transform.scale(self.fondo_dia, (ANCHO, ALTO))
        self.fondo_noche = pygame.image.load("assets/noche.png").convert()
        self.fondo_noche = pygame.transform.scale(self.fondo_noche, (ANCHO, ALTO))

        # Grupos
        self.todos = pygame.sprite.Group()
        self.plataformas = []
        self.enemigos = pygame.sprite.Group()
        self.fragmentos = pygame.sprite.Group()
        self.plataformas_moviles = []

        # Jugador
        self.jugador = Jugador()
        self.todos.add(self.jugador)

        # Tiempo de inicio
        self.tiempo_inicio = pygame.time.get_ticks()

        self.cargar_nivel(self.nivel_actual)


    def dibujar_fondo(self):
        fondo = self.fondo_dia if self.mundo_dia else self.fondo_noche
        self.ventana.blit(fondo, (0, 0))

    def cargar_nivel(self, num):
        datos = cargar_nivel(num)
        if datos is None:
            self.mostrar_mensaje(" ¡Has completado todos los niveles! ")
            self.completed = True
            self.running = False
            return

        self.mundo_dia = True
        # Reiniciar contador de tiempo al cargar nivel
        self.tiempo_inicio = pygame.time.get_ticks()

        # Limpiar grupos
        self.todos.empty()
        self.enemigos.empty()
        self.fragmentos.empty()
        self.plataformas_moviles.clear()
        self.plataformas.clear()

        # Reiniciar jugador
        self.jugador.rect.midbottom = (ANCHO // 2, ALTO - 100)
        self.jugador.vel_x = 0
        self.jugador.vel_y = 0
        self.jugador.en_suelo = False
        self.todos.add(self.jugador)

        # Cargar plataformas
        for x, y, w, h, mundo in datos["plataformas"]:
            p = Plataforma(x, y, w, h, mundo)
            self.todos.add(p)
            self.plataformas.append(p)

        # Cargar plataformas móviles
        for x, y, w, h, mundo, dir, rango, vel in datos["moviles"]:
            pm = PlataformaMovil(x, y, w, h, mundo, dir, rango, vel)
            self.todos.add(pm)
            self.plataformas_moviles.append(pm)

        # Cargar enemigos
        for x, y, mundo in datos["enemigos"]:
            e = Enemigo(x, y, mundo, rango=120, velocidad=2)
            self.todos.add(e)
            self.enemigos.add(e)

        # Cargar fragmento
        fx, fy = datos["fragmento"]
        f = Fragmento(fx, fy)
        self.todos.add(f)
        self.fragmentos.add(f)
    
    def mostrar_tiempo(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = max(0, 30 - (tiempo_actual - self.tiempo_inicio) // 1000)

        fuente = pygame.font.SysFont("arial", 30, True)
        texto = fuente.render(f"Tiempo: {tiempo_restante}", True, BLANCO)
        # Mostrar en la esquina superior izquierda
        self.ventana.blit(texto, (10, 10))

        if tiempo_restante <= 0:
            self.morir("Tiempo agotado")
            self.nivel_actual = 0
            self.mundo_dia = True 
            self.reiniciar_nivel()

    def verificar_colisiones(self):
        if self.jugador.rect.top > ALTO:
            self.morir("Has caído al vacío...")

        for enemigo in self.enemigos:
            if enemigo.activo and self.jugador.hitbox.colliderect(enemigo.rect):
                self.morir("Un enemigo te atrapó...")

        for fragmento in self.fragmentos:
            if self.jugador.rect.colliderect(fragmento.rect):
                fragmento.recoger()
                self.mostrar_mensaje("Fragmento obtenido ✨")
                self.nivel_actual += 1
                self.cargar_nivel(self.nivel_actual)

    def morir(self, mensaje):
        self.mostrar_mensaje(mensaje)
        self.muerto = True
        self.tiempo_muerte = pygame.time.get_ticks()

        # Reinicia al primer nivel
        self.nivel_actual = 0
        self.mundo_dia = True
        self.reiniciar_nivel()

    def reiniciar_nivel(self):
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

            if self.muerto:
                if pygame.time.get_ticks() - self.tiempo_muerte > 1500:
                    self.reiniciar_nivel()
                continue
        
            # Actualizar fragmento animado
            for f in self.fragmentos:
                f.update()

            # Fondo dinámico
            self.dibujar_fondo()

            # Actualizar jugador
            self.jugador.update(teclas, self.plataformas + self.plataformas_moviles, self.mundo_dia)

            # Actualizar plataformas móviles
            for pm in self.plataformas_moviles:
                pm.update(self.mundo_dia)

            # Actualizar enemigos
            for e in self.enemigos:
                e.update(self.mundo_dia)

            # Actualizar colores de plataformas
            for p in self.plataformas:
                p.actualizar_color(self.mundo_dia)
            for pm in self.plataformas_moviles:
                pm.actualizar_color(self.mundo_dia)

            # Dibujar todo
            self.todos.draw(self.ventana)

            # Dibujar tiempo en pantalla
            self.mostrar_tiempo()

            # Verificar colisiones
            self.verificar_colisiones()

            pygame.display.flip()
            self.clock.tick(FPS)