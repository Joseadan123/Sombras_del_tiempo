import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, mundo, rango=120, velocidad=2):
        super().__init__()

        # Cargar sprites
        self.sprite_rojo = pygame.image.load("assets/enemigo_rojo.png").convert_alpha()
        self.sprite_rojo = pygame.transform.scale(self.sprite_rojo, (40, 60))
        self.sprite_azul = pygame.image.load("assets/enemigo_azul.png").convert_alpha()
        self.sprite_azul = pygame.transform.scale(self.sprite_azul, (40, 60))

        # Estado inicial
        self.image = self.sprite_rojo if mundo == "dia" else self.sprite_azul
        self.rect = self.image.get_rect(topleft=(x, y))
        self.base_x = x
        self.rango = rango
        self.velocidad = velocidad
        self.direccion = 1
        self.mundo = mundo
        self.activo = True

        # Movimiento flotante leve (decorativo)
        self.base_y = y
        self.fluct = 0
        self.vel_fluct = 0.1
        self.fluct_dir = 1

    def update(self, mundo_dia):
        # --- Visibilidad según mundo ---
        visible = (self.mundo == "dia" and mundo_dia) or (self.mundo == "noche" and not mundo_dia)
        self.image.set_alpha(255 if visible else 0)
        self.activo = visible

        if not self.activo:
            return  # No se mueve si no corresponde al mundo actual

        # --- Movimiento horizontal de patrulla ---
        self.rect.x += self.velocidad * self.direccion
        if abs(self.rect.x - self.base_x) >= self.rango:
            self.direccion *= -1
            # Voltear sprite al cambiar dirección
            self.image = pygame.transform.flip(self.image, True, False)

        # --- Movimiento flotante suave (arriba/abajo) ---
        self.fluct += self.vel_fluct * self.fluct_dir
        if abs(self.fluct) > 3:
            self.fluct_dir *= -1
        self.rect.y = self.base_y + int(self.fluct)

        # --- Actualizar sprite según modo ---
        self.image = self.sprite_rojo if mundo_dia else self.sprite_azul
        # Mantener la orientación correcta después del cambio
        if self.direccion == -1:
            self.image = pygame.transform.flip(self.image, True, False)
