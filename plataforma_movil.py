import pygame

class PlataformaMovil(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, mundo, direccion="horizontal", rango=100, velocidad=2):
        super().__init__()
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mundo = mundo
        self.direccion = direccion
        self.rango = rango
        self.velocidad = velocidad
        self.pos_inicial = (x, y)
        self.visible = True

        # Colores similares a las plataformas normales, pero más vivos
        self.color_dia = (100, 200, 255)    # Azul celeste para día
        self.color_noche = (255, 130, 220)  # Rosa neón para noche
        self.color_brillo = (255, 255, 255)
        self.color_sombra = (0, 0, 0, 50)

        self.actualizar_color(True)

    def actualizar_color(self, mundo_dia):
        """Aplica el mismo diseño visual que las plataformas normales, con colores distintos."""
        color_principal = self.color_dia if mundo_dia else self.color_noche

        # Limpiar superficie
        self.image.fill((0, 0, 0, 0))

        # Base principal con bordes redondeados
        pygame.draw.rect(self.image, color_principal, (0, 0, self.rect.width, self.rect.height), border_radius=6)

        # Sombra inferior
        sombra_color = tuple(int(c * 0.5) for c in color_principal)
        pygame.draw.rect(self.image, sombra_color, (0, self.rect.height - 6, self.rect.width, 6), border_radius=6)

        # Brillo superior
        pygame.draw.rect(self.image, self.color_brillo, (0, 0, self.rect.width, 4), border_radius=6)

        # Sombra proyectada
        sombra = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(sombra, self.color_sombra, (0, 0, self.rect.width, self.rect.height), border_radius=6)
        self.image.blit(sombra, (3, 3), special_flags=pygame.BLEND_RGBA_SUB)

        # Ajustar visibilidad según el mundo
        self.visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        self.image.set_alpha(255 if self.visible else 60)

    def update(self, mundo_dia, jugador=None):
        """Actualiza movimiento, visibilidad y arrastre del jugador."""
        self.visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)

        if not self.visible:
            return  # No se mueve ni colisiona si no es visible

        movimiento_x, movimiento_y = 0, 0

        # Movimiento horizontal o vertical
        if self.direccion == "horizontal":
            self.rect.x += self.velocidad
            movimiento_x = self.velocidad
            if abs(self.rect.x - self.pos_inicial[0]) >= self.rango:
                self.velocidad *= -1
        elif self.direccion == "vertical":
            self.rect.y += self.velocidad
            movimiento_y = self.velocidad
            if abs(self.rect.y - self.pos_inicial[1]) >= self.rango:
                self.velocidad *= -1

        # --- Colisión con jugador ---
        if jugador and jugador.rect.colliderect(self.rect):
            # Verificar si el jugador está encima (solo si cae sobre ella)
            if jugador.rect.bottom <= self.rect.top + 10 and jugador.vel_y >= 0:
                jugador.rect.bottom = self.rect.top
                jugador.vel_y = 0
                jugador.en_suelo = True

                # --- Movimiento con la plataforma ---
                jugador.rect.x += movimiento_x
                jugador.rect.y += movimiento_y
