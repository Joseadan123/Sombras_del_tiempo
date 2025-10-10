# enemigo.py
import pygame
import random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, mundo_dia=True):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.base_y = y
        self.fluct = 0
        self.vel_fluct = 0.1
        self.direccion = 1
        self.activo = True
        self.mundo_dia = mundo_dia
        self.tiempo_cambio = random.randint(1000, 3000)
        self.ultimo_cambio = pygame.time.get_ticks()
        self.actualizar_color(mundo_dia)

    def actualizar_color(self, mundo_dia):
        """Cambia el color del enemigo dependiendo del mundo (día/noche)."""
        self.mundo_dia = mundo_dia
        self.image.fill((0, 0, 0, 0))  # limpiar fondo transparente

        if mundo_dia:
            # 🌞 Enemigo de día: golem rojizo brillante
            cuerpo = (200, 80, 60)
            sombra = (150, 50, 40)
            ojo = (255, 255, 255)
        else:
            # 🌙 Enemigo de noche: sombra oscura con ojos brillantes
            cuerpo = (40, 40, 70)
            sombra = (25, 25, 45)
            ojo = (120, 200, 255)

        # Cuerpo base (rectángulo principal)
        pygame.draw.rect(self.image, sombra, (0, 8, 40, 32))
        pygame.draw.rect(self.image, cuerpo, (0, 0, 40, 30))

        # Ojos
        pygame.draw.circle(self.image, ojo, (12, 10), 3)
        pygame.draw.circle(self.image, ojo, (28, 10), 3)

        # Decoración: cuernos / brillo superior
        if mundo_dia:
            pygame.draw.polygon(self.image, (250, 180, 150), [(5, 0), (10, -5), (15, 0)])
            pygame.draw.polygon(self.image, (250, 180, 150), [(25, 0), (30, -5), (35, 0)])
        else:
            pygame.draw.polygon(self.image, (150, 180, 255), [(5, 0), (10, -5), (15, 0)])
            pygame.draw.polygon(self.image, (150, 180, 255), [(25, 0), (30, -5), (35, 0)])

    def update(self, mundo_dia):
        """Animación flotante + cambio de color dinámico."""
        tiempo_actual = pygame.time.get_ticks()

        # Flotación suave
        self.fluct += self.vel_fluct * self.direccion
        if abs(self.fluct) > 3:
            self.direccion *= -1
        self.rect.y = self.base_y + int(self.fluct)

        # Actualizar color según el mundo actual
        if tiempo_actual - self.ultimo_cambio > self.tiempo_cambio:
            self.actualizar_color(mundo_dia)
            self.ultimo_cambio = tiempo_actual
