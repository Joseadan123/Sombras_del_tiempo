import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, mundo):
        super().__init__()
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_original = y  # Guardar posición real aquí
        self.mundo = mundo  # "dia" o "noche"

        # Colores base de ladrillo
        self.color_dia = (190, 100, 60)      # ladrillo naranja-rojizo
        self.color_noche = (120, 70, 100)    # púrpura oscuro (modo noche)
        self.color_mortero = (220, 180, 150) # líneas entre ladrillos

        self.visible = True
        self.actualizar_color(True)

    def actualizar_color(self, mundo_dia):
        """Dibuja la textura tipo ladrillo y ajusta visibilidad según el mundo."""
        color_principal = self.color_dia if mundo_dia else self.color_noche
        color_mortero = self.color_mortero

        # Fondo base
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, color_principal, (0, 0, self.rect.width, self.rect.height))

        # Patrón de ladrillos
        ancho_ladrillo = 32
        alto_ladrillo = 16
        for fila_y in range(0, self.rect.height, alto_ladrillo):
            desplazamiento = ancho_ladrillo // 2 if (fila_y // alto_ladrillo) % 2 else 0
            for col_x in range(-desplazamiento, self.rect.width, ancho_ladrillo):
                pygame.draw.line(self.image, color_mortero, (col_x, fila_y), (col_x, fila_y + alto_ladrillo), 2)
            pygame.draw.line(self.image, color_mortero, (0, fila_y), (self.rect.width, fila_y), 2)

        # Efectos de sombra y brillo
        sombra = pygame.Surface((self.rect.width, 8), pygame.SRCALPHA)
        sombra.fill((0, 0, 0, 80))
        self.image.blit(sombra, (0, self.rect.height - 8))

        brillo = pygame.Surface((self.rect.width, 5), pygame.SRCALPHA)
        brillo.fill((255, 255, 255, 40))
        self.image.blit(brillo, (0, 0))

        # --- Lógica de visibilidad ---
        self.visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        self.image.set_alpha(255 if self.visible else 60)

        # Si no está visible, moverla fuera del área jugable
        if not self.visible:
            self.rect.y = 99999
        else:
            self.rect.y = self.y_original
