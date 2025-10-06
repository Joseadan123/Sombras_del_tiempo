import pygame 
from config import BLANCO, AMARILLO

class Fragmento(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect(center=(x, y))
        self.recogido = False

    def recoger(self):
        self.recogido = True
        self.kill()  # Elimina el fragmento del grupo de sprites