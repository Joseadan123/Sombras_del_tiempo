import pygame
from config import GRIS, VIOLETA

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, mundo="dia"):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.mundo = mundo  # "dia" o "noche"
        self.color_dia = GRIS
        self.color_noche = VIOLETA
        self.image.fill(self.color_dia if mundo == "dia" else self.color_noche)
        self.rect = self.image.get_rect(topleft=(x, y))

    def actualizar_color(self, mundo_dia):
        if mundo_dia and self.mundo == "dia":
            self.image.fill(self.color_dia)
        elif not mundo_dia and self.mundo == "noche":
            self.image.fill(self.color_noche)
        else:
            # Plataforma "inactiva"
            self.image.fill((0,0,0))
