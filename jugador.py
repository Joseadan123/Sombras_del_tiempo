# jugador.py
import pygame
from config import ALTO, ANCHO

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Cargar sprites de día y noche
        self.sprite_dia = pygame.image.load("assets/jugador_dia.png").convert_alpha()
        self.sprite_dia = pygame.transform.scale(self.sprite_dia, (40, 60))
        self.sprite_noche = pygame.image.load("assets/jugador_noche.png").convert_alpha()
        self.sprite_noche = pygame.transform.scale(self.sprite_noche, (40, 60))

        self.image = self.sprite_dia
        self.rect = self.image.get_rect(midbottom=(200, 500))
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, 20, 40)

        # Físicas
        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = False
        self.gravedad = 0.6
        self.salto = -12
        self.velocidad = 6

        self.mirando_derecha = True

    def update(self, teclas, plataformas, mundo_dia):
        # Seleccionar sprite según mundo
        self.image = self.sprite_dia if mundo_dia else self.sprite_noche

        # Movimiento lateral
        self.vel_x = 0
        if teclas[pygame.K_LEFT]:
            self.vel_x = -self.velocidad
            self.mirando_derecha = False
        if teclas[pygame.K_RIGHT]:
            self.vel_x = self.velocidad
            self.mirando_derecha = True

        # Salto
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = self.salto
            self.en_suelo = False

        # --- Mantener al jugador dentro de la pantalla ---
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = 0
        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.vel_x = 0

        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0
        elif self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            self.vel_y = 0

        # Gravedad
        self.vel_y += self.gravedad
        if self.vel_y > 10:
            self.vel_y = 10

        # Actualizar posición
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.hitbox.x = self.rect.x + 10
        self.hitbox.y = self.rect.y + 10

        # Colisiones con plataformas
        self.en_suelo = False
        for p in plataformas:
            if self.hitbox.colliderect(p.rect):
                if self.vel_y > 0 and self.hitbox.bottom <= p.rect.bottom:
                    self.rect.bottom = p.rect.top + 10
                    self.vel_y = 0
                    self.en_suelo = True

        # Voltear sprite según dirección
        if not self.mirando_derecha:
            self.image = pygame.transform.flip(self.image, True, False)
