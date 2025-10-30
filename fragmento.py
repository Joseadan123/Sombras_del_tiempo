import pygame
import math

class Fragmento(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Cargar la imagen del fragmento (reloj o gema)
        self.image_base = pygame.image.load("assets/fragmento.png").convert_alpha()
        self.image_base = pygame.transform.scale(self.image_base, (30, 30))
        
        self.image = self.image_base.copy()
        self.rect = self.image.get_rect(center=(x, y))
        
        # Variables para animación
        self.base_y = y
        self.tiempo = 0
        self.brillo = 255
        self.subiendo = True

    def update(self):
        """Animación suave de flotación y brillo."""
        self.tiempo += 0.05
        
        # Movimiento vertical oscilante (flotación)
        self.rect.y = self.base_y + math.sin(self.tiempo) * 5  # sube y baja suavemente

        # Parpadeo del brillo
        intensidad = 200 + int(55 * abs(math.sin(self.tiempo * 2)))
        
        # Crear un efecto de brillo alrededor
        self.image = self.image_base.copy()
        brillo = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(brillo, (255, 255, 100, intensidad), (15, 15), 14)
        self.image.blit(brillo, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

    def recoger(self):
        """Acción al tocar el fragmento."""
        print("✨ Fragmento recogido")
