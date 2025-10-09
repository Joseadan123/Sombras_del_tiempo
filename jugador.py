import pygame
from config import ANCHO, ALTO, AMARILLO, AZUL, BLANCO, NEGRO

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Imagen simulada (32x48)
        self.image = pygame.Surface((32, 48), pygame.SRCALPHA)
        self.color_dia = (255, 230, 50)
        self.color_noche = (60, 100, 255)
        self.color_cuerpo = (200, 200, 200)
        self.color_cabeza = (250, 220, 190)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO // 2, ALTO - 50)

        # Física del jugador
        self.vel_x = 0
        self.vel_y = 0
        self.aceleracion = 0.5
        self.friccion = -0.15
        self.gravedad = 0.8
        self.fuerza_salto = -15
        self.velocidad_max = 6
        self.en_suelo = True
        self.mirando_derecha = True

        # Área de colisión
        self.hitbox = self.rect.inflate(-5, -10)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.vel_x -= self.aceleracion
            self.mirando_derecha = False
        elif teclas[pygame.K_RIGHT]:
            self.vel_x += self.aceleracion
            self.mirando_derecha = True
        else:
            # aplicar fricción solo cuando no se presiona nada
            if abs(self.vel_x) < 0.1:
                self.vel_x = 0
            else:
                self.vel_x += self.vel_x * self.friccion

        # Limitar velocidad
        self.vel_x = max(-self.velocidad_max, min(self.vel_x, self.velocidad_max))

    def aplicar_gravedad(self, teclas):
        self.vel_y += self.gravedad
        if self.vel_y > 10:
            self.vel_y = 10

        # Si suelta el espacio antes, corta el salto
        if not teclas[pygame.K_SPACE] and self.vel_y < 0:
            self.vel_y += 1

    def update(self, teclas, plataformas, mundo_dia=True):
        self.mover(teclas)
        self.aplicar_gravedad(teclas)

        # Salto
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = self.fuerza_salto
            self.en_suelo = False

        # Aplicar movimiento
        self.rect.x += int(self.vel_x)
        self.rect.y += int(self.vel_y)
        self.hitbox.topleft = self.rect.topleft

        # Colisiones con plataformas
                # Colisiones con plataformas
        self.en_suelo = False   
        margen = 5  # margen para detectar el suelo correctamente

        # Colisiones con plataformas 
        for plataforma in plataformas:
            if self.hitbox.colliderect(plataforma.rect):
                # Verificar que el jugador viene cayendo
                if self.vel_y >= 0 and self.rect.bottom <= plataforma.rect.bottom + margen:
                    # Coloca al jugador justo sobre la plataforma
                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.en_suelo = True
                    self.hitbox.topleft = self.rect.topleft

                    # Si la plataforma se mueve, mover al jugador con ella
                    if hasattr(plataforma, "velocidad"):
                        if plataforma.direccion == "horizontal":
                            self.rect.x += plataforma.velocidad
                        elif plataforma.direccion == "vertical":
                            self.rect.y += plataforma.velocidad
                        self.hitbox.topleft = self.rect.topleft


        # Límite del mapa
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.vel_x = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO - 40
            self.vel_y = 0
            self.en_suelo = True

        # Dibujar personaje en base al mundo
        self.dibujar_personaje(mundo_dia)

    def dibujar_personaje(self, mundo_dia):
        """Dibuja el personaje con rectángulos pixel-art básicos."""
        self.image.fill((0, 0, 0, 0))  # limpiar imagen
        capa_color = self.color_dia if mundo_dia else self.color_noche

        # Capa
        pygame.draw.rect(self.image, capa_color, (4, 20, 24, 20))
        # Cuerpo
        pygame.draw.rect(self.image, self.color_cuerpo, (10, 14, 12, 18))
        # Cabeza
        pygame.draw.rect(self.image, self.color_cabeza, (10, 2, 12, 12))

        # Si mira a la izquierda, voltear el dibujo
        if not self.mirando_derecha:
            self.image = pygame.transform.flip(self.image, True, False)
