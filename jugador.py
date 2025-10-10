# jugador.py
import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect(midbottom=(200, 500))
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, 20, 40)

        # Físicas
        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = False
        self.gravedad = 0.6
        self.salto = -12
        self.velocidad = 6

        # Animación básica
        self.anim_tiempo = 0
        self.anim_dir = 1

        # Estado del mundo
        self.mundo_dia = True
        self.actualizar_color(self.mundo_dia)

    def actualizar_color(self, mundo_dia):
        """Dibuja al personaje según el mundo (día o noche)."""
        self.image.fill((0, 0, 0, 0))  # limpiar superficie transparente
        self.mundo_dia = mundo_dia

        # Colores según el momento del día
        if mundo_dia:
            capa = (255, 230, 80)
            cuerpo = (180, 180, 200)
            cabeza = (240, 240, 240)
            detalle = (0, 0, 0)
        else:
            capa = (80, 120, 255)
            cuerpo = (90, 90, 120)
            cabeza = (200, 210, 255)
            detalle = (255, 255, 255)

        # Capa
        pygame.draw.polygon(self.image, capa, [(5, 50), (20, 20), (35, 50)])

        # Cuerpo
        pygame.draw.rect(self.image, cuerpo, (12, 25, 16, 20))

        # Cabeza
        pygame.draw.circle(self.image, cabeza, (20, 15), 8)

        # Ojos
        pygame.draw.circle(self.image, detalle, (17, 13), 2)
        pygame.draw.circle(self.image, detalle, (23, 13), 2)

        # Sombra leve
        pygame.draw.rect(self.image, (0, 0, 0, 60), (10, 48, 20, 2))

    def update(self, teclas, plataformas, mundo_dia):
        """Actualiza la posición, físicas y animación."""
        self.actualizar_color(mundo_dia)

        # Movimiento lateral
        self.vel_x = 0
        if teclas[pygame.K_LEFT]:
            self.vel_x = -self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.vel_x = self.velocidad

        # Salto
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = self.salto
            self.en_suelo = False

        # Gravedad
        self.vel_y += self.gravedad
        if self.vel_y > 10:
            self.vel_y = 10

        # Actualizar posición
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.hitbox.x = self.rect.x + 10
        self.hitbox.y = self.rect.y + 10

        # Colisiones con plataformas
        self.en_suelo = False
        for p in plataformas:
            if self.hitbox.colliderect(p.rect):
                # Aterrizaje
                if self.vel_y > 0 and self.hitbox.bottom <= p.rect.bottom:
                    self.rect.bottom = p.rect.top + 10
                    self.vel_y = 0
                    self.en_suelo = True

        # Pequeña animación de “respirar”
        self.anim_tiempo += 0.05
        self.rect.y += int(self.anim_dir * 0.2)
        if abs(self.anim_tiempo) > 2:
            self.anim_dir *= -1
