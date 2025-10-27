import pygame

class Fragmento(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_original = pygame.Surface((30, 30), pygame.SRCALPHA)

        # Dibujar un fragmento dorado con brillo
        pygame.draw.circle(self.image_original, (255, 215, 0), (15, 15), 12)
        pygame.draw.circle(self.image_original, (255, 255, 255, 80), (15, 10), 5)
        pygame.draw.circle(self.image_original, (255, 255, 150, 150), (15, 15), 8)

        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.tiempo_anim = 0
        self.subiendo = True

    def update(self):
        """Animación de brillo y leve flotación."""
        # Oscilar suavemente arriba y abajo
        if self.subiendo:
            self.rect.y -= 0.3
            if self.rect.y <= self.rect.y - 3:
                self.subiendo = False
        else:
            self.rect.y += 0.3
            if self.rect.y >= self.rect.y + 3:
                self.subiendo = True

        # Pequeño parpadeo del brillo
        brillo = (200 + int(55 * abs(pygame.time.get_ticks() % 1000 - 500) / 500))
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (255, 215, 0), (15, 15), 12)
        pygame.draw.circle(self.image, (255, 255, brillo), (15, 15), 8)

    def recoger(self):
        """Acción al tocar el fragmento."""
        print("✨ Fragmento recogido")
