# plataforma.py
import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, mundo):
        super().__init__()
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mundo = mundo
        self.color_dia = (139, 195, 74)     # Verde suave
        self.color_noche = (100, 60, 150)   # Morado místico
        self.color_borde = (60, 40, 90)     # Sombra
        self.color_brillo = (180, 255, 100) # Luz superior
        self.actualizar_color(True)

    def actualizar_color(self, mundo_dia):
        # Fondo y bordes
        color_principal = self.color_dia if mundo_dia else self.color_noche
        color_sombra = (color_principal[0] * 0.6, color_principal[1] * 0.6, color_principal[2] * 0.6)
        color_sombra = tuple(map(int, color_sombra))

        # Rellenar base
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, color_principal, (0, 0, self.rect.width, self.rect.height), border_radius=6)
        
        # Borde inferior (sombra)
        pygame.draw.rect(self.image, color_sombra, (0, self.rect.height - 6, self.rect.width, 6), border_radius=6)
        
        # Borde superior (brillo)
        pygame.draw.rect(self.image, self.color_brillo, (0, 0, self.rect.width, 4), border_radius=6)
        
        # Sombra lateral
        sombra = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(sombra, (0, 0, 0, 50), (0, 0, self.rect.width, self.rect.height), border_radius=6)
        self.image.blit(sombra, (3, 3), special_flags=pygame.BLEND_RGBA_SUB)
        
        # Ajustar transparencia según mundo
        visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        self.image.set_alpha(255 if visible else 60)
