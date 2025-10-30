import pygame
from config import ANCHO, ALTO, BLANCO

# --- Utilidad para dibujar texto centrado ---
def mostrar_texto(ventana, texto, tam, y, color=BLANCO, negrita=True):
    fuente = pygame.font.SysFont("arial", tam, negrita)
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(ANCHO // 2, y))
    ventana.blit(render, rect)


# --- Menú de inicio ---
def menu_inicio():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Sombras del Tiempo - Menú Inicial")
    clock = pygame.time.Clock()

    # Cargar fondo (opcional, puedes cambiar por tus imágenes)
    fondo = pygame.image.load("assets/dias.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Sonido opcional
    # pygame.mixer.music.load("assets/musica_menu.mp3")
    # pygame.mixer.music.play(-1)

    alpha_titulo = 255
    fade_direccion = -5

    activo = True
    while activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return True  # Iniciar juego

        # Fondo
        ventana.blit(fondo, (0, 0))

        # Texto principal
        mostrar_texto(ventana, "Sombras del Tiempo", 56, ALTO // 2 - 100, BLANCO)
        mostrar_texto(ventana, "Una aventura entre la luz y la oscuridad", 26, ALTO // 2 - 50, (230, 230, 255))

        # Texto parpadeante
        alpha_titulo += fade_direccion
        if alpha_titulo <= 80 or alpha_titulo >= 255:
            fade_direccion *= -1

        texto = pygame.font.SysFont("arial", 30, True).render("Presiona ENTER para comenzar", True, (255, 255, 255))
        texto.set_alpha(alpha_titulo)
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2 + 60))
        ventana.blit(texto, rect)

        # Instrucciones extra
        mostrar_texto(ventana, "Pulsa C para cambiar entre Día y Noche", 22, ALTO - 60, (200, 200, 220))

        pygame.display.flip()
        clock.tick(60)


# --- Menú de victoria ---
def menu_victoria():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Sombras del Tiempo - ¡Victoria!")
    clock = pygame.time.Clock()

    # Fondo de noche
    fondo = pygame.image.load("assets/noche.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    activo = True
    while activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return True  # volver a jugar
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False  # salir

        ventana.blit(fondo, (0, 0))

        mostrar_texto(ventana, "¡Has completado todos los niveles!", 44, ALTO // 2 - 60)
        mostrar_texto(ventana, "ENTER: Jugar de nuevo", 28, ALTO // 2 + 10)
        mostrar_texto(ventana, "ESC: Salir del juego", 24, ALTO // 2 + 50)

        pygame.display.flip()
        clock.tick(60)

    return False
