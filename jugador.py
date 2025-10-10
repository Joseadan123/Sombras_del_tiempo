# jugador.py
import pygame
from config import ANCHO, ALTO

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Superficie del personaje (dibujado manualmente)
        self.image = pygame.Surface((34, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect(midbottom=(ANCHO // 2, ALTO - 50))

        # Físicas
        self.vel_x = 0
        self.vel_y = 0
        self.aceleracion = 0.5
        self.friccion = -0.15
        self.gravedad = 0.8
        self.fuerza_salto = -15
        self.velocidad_max = 6
        self.en_suelo = True
        self.mirando_derecha = True

        # Colores base
        self.color_cabeza = (255, 230, 200)
        self.color_cuerpo = (200, 200, 200)
        self.color_capa_dia = (255, 200, 0)
        self.color_capa_noche = (100, 150, 255)
        self.color_borde = (40, 40, 40)

        self.hitbox = self.rect.inflate(-6, -8)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.vel_x -= self.aceleracion
            self.mirando_derecha = False
        elif teclas[pygame.K_RIGHT]:
            self.vel_x += self.aceleracion
            self.mirando_derecha = True
        else:
            if abs(self.vel_x) < 0.1:
                self.vel_x = 0
            else:
                self.vel_x += self.vel_x * self.friccion
        self.vel_x = max(-self.velocidad_max, min(self.vel_x, self.velocidad_max))

    def aplicar_gravedad(self):
        self.vel_y += self.gravedad
        if self.vel_y > 10:
            self.vel_y = 10

    def saltar(self):
        if self.en_suelo:
            self.vel_y = self.fuerza_salto
            self.en_suelo = False

    def update(self, teclas, plataformas, mundo_dia=True):
        self.mover(teclas)
        self.aplicar_gravedad()

        # Salto
        if teclas[pygame.K_SPACE]:
            self.saltar()

        # Movimiento
        self.rect.x += int(self.vel_x)
        self.rect.y += int(self.vel_y)
        self.hitbox.topleft = self.rect.topleft

        # --- Colisiones verticales (versión estable) ---
        self.en_suelo = False
        margen = 10

        # Primero, mover en Y y luego revisar colisiones
        for plataforma in plataformas:
            # Solo detectar si el jugador viene cayendo
            if self.vel_y >= 0:
                # Comprobación más suave del suelo
                if (self.rect.bottom + margen > plataforma.rect.top and
                    self.rect.bottom < plataforma.rect.bottom and
                    self.rect.right > plataforma.rect.left + 5 and
                    self.rect.left < plataforma.rect.right - 5):

                    # Solo si el jugador está cayendo y justo encima
                    if self.rect.bottom <= plataforma.rect.top + margen:
                        self.rect.bottom = plataforma.rect.top
                        self.vel_y = 0
                        self.en_suelo = True
                        self.hitbox.topleft = self.rect.topleft

                        # Mover con plataforma si es móvil
                        if hasattr(plataforma, "velocidad"):
                            if plataforma.direccion == "horizontal":
                                self.rect.x += plataforma.velocidad
                            elif plataforma.direccion == "vertical":
                                self.rect.y += plataforma.velocidad
                            self.hitbox.topleft = self.rect.topleft
                        break  # ✅ Detener tras encontrar una plataforma válida

        # Límites del mapa
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.vel_x = 0
        if self.rect.bottom > ALTO - 40:
            self.rect.bottom = ALTO - 40
            self.vel_y = 0
            self.en_suelo = True

        # Dibujar personaje
        self.dibujar_personaje(mundo_dia)

    def dibujar_personaje(self, mundo_dia):
        """Dibuja al personaje con estilo pixel-art, sin sprites."""
        self.image.fill((0, 0, 0, 0))
        capa_color = self.color_capa_dia if mundo_dia else self.color_capa_noche

        # Capa
        pygame.draw.polygon(self.image, capa_color, [(6, 25), (28, 25), (30, 46), (4, 46)])
        pygame.draw.line(self.image, (255, 255, 255), (8, 26), (26, 26), 1)

        # Cuerpo
        pygame.draw.rect(self.image, self.color_cuerpo, (10, 14, 14, 20), border_radius=3)
        pygame.draw.rect(self.image, self.color_borde, (10, 14, 14, 20), 1, border_radius=3)

        # Cabeza
        pygame.draw.rect(self.image, self.color_cabeza, (11, 3, 12, 12), border_radius=3)
        pygame.draw.rect(self.image, self.color_borde, (11, 3, 12, 12), 1, border_radius=3)

        # Voltear si mira a la izquierda
        if not self.mirando_derecha:
            self.image = pygame.transform.flip(self.image, True, False)
