# enemigo.py
import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, mundo_dia=True):
        super().__init__()

        # Cargar sprites
        self.sprite_rojo = pygame.image.load("assets/enemigo_rojo.png").convert_alpha()
        self.sprite_rojo = pygame.transform.scale(self.sprite_rojo, (40, 60))
        self.sprite_azul = pygame.image.load("assets/enemigo_azul.png").convert_alpha()
        self.sprite_azul = pygame.transform.scale(self.sprite_azul, (40, 60))

        self.image = self.sprite_rojo if mundo_dia else self.sprite_azul
        self.rect = self.image.get_rect(topleft=(x, y))
        self.base_y = y
        self.fluct = 0
        self.vel_fluct = 0.1
        self.direccion = 1
        self.activo = True
        self.mundo_dia = mundo_dia

    def update(self, mundo_dia):
        # Actualizar sprite
        self.image = self.sprite_rojo if mundo_dia else self.sprite_azul

        # Movimiento flotante
        self.fluct += self.vel_fluct * self.direccion
        if abs(self.fluct) > 3:
            self.direccion *= -1
        self.rect.y = self.base_y + int(self.fluct)
