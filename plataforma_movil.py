# plataforma_movil.py
import pygame
from config import BLANCO

class PlataformaMovil(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, mundo, direccion="horizontal", rango=100, velocidad=2):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.color_base = BLANCO
        self.image.fill(self.color_base)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mundo = mundo
        self.direccion = direccion
        self.rango = rango
        self.velocidad = velocidad
        self.pos_inicial = (x, y)

    def actualizar_color(self, mundo_dia):
        # Aparece solo en su mundo
        visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        self.image.set_alpha(255 if visible else 60)

    def update(self, mundo_dia):
        # Movimiento solo si es visible
        visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        if not visible:
            return

        # Movimiento horizontal
        if self.direccion == "horizontal":
            self.rect.x += self.velocidad
            if abs(self.rect.x - self.pos_inicial[0]) >= self.rango:
                self.velocidad *= -1

        # Movimiento vertical
        elif self.direccion == "vertical":
            self.rect.y += self.velocidad
            if abs(self.rect.y - self.pos_inicial[1]) >= self.rango:
                self.velocidad *= -1