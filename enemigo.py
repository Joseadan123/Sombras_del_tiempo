# enemigo.py
import pygame
from config import NEGRO, BLANCO, ROJO, GRIS

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, mundo="dia"):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.mundo = mundo  # "dia" o "noche"
        self.color_activo = ROJO
        self.color_inactivo = GRIS
        self.image.fill(self.color_activo)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direccion = 1
        self.velocidad = 2
        self.activo = True

    def update(self, mundo_dia):
        # Cambiar estado según el mundo
        if mundo_dia and self.mundo == "dia":
            self.activo = True
            self.image.fill(self.color_activo)
        elif not mundo_dia and self.mundo == "noche":
            self.activo = True
            self.image.fill(self.color_activo)
        else:
            self.activo = False
            self.image.fill(self.color_inactivo)

        # Mover solo si está activo
        if self.activo:
            self.rect.x += self.direccion * self.velocidad
            if self.rect.left < 0 or self.rect.right > 800:
                self.direccion *= -1