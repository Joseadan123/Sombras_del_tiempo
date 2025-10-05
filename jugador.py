# jugador.py
import pygame
from config import ANCHO, ALTO, VERDE

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO // 2, ALTO - 50)

        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = True

    def update(self, teclas, plataformas):
        # Movimiento lateral
        self.vel_x = 0
        if teclas[pygame.K_LEFT]:
            self.vel_x = -5
        if teclas[pygame.K_RIGHT]:
            self.vel_x = 5

        # Salto
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = -15
            self.en_suelo = False

        # Gravedad
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10

        # Aplicar movimiento
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Colisión con plataformas
        self.en_suelo = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect) and self.vel_y >= 0:
                self.rect.bottom = plataforma.rect.top
                self.vel_y = 0
                self.en_suelo = True

        # Piso
        if self.rect.bottom >= ALTO - 40:
            self.rect.bottom = ALTO - 40
            self.vel_y = 0
            self.en_suelo = True
