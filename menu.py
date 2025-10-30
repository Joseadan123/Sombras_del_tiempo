import pygame
from config import ANCHO, ALTO, BLANCO


def mostrar_texto(ventana, texto, tam, y):
    fuente = pygame.font.SysFont("arial", tam, True)
    render = fuente.render(texto, True, BLANCO)
    rect = render.get_rect(center=(ANCHO // 2, y))
    ventana.blit(render, rect)


def menu_inicio():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Sombras del Tiempo - Menú")
    clock = pygame.time.Clock()

    activo = True
    while activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    activo = False

        ventana.fill((20, 20, 30))
        mostrar_texto(ventana, "Sombras del Tiempo", 48, ALTO // 2 - 60)
        mostrar_texto(ventana, "Presiona ENTER para iniciar", 28, ALTO // 2 + 10)
        mostrar_texto(ventana, "C para cambiar Día/Noche en juego", 22, ALTO // 2 + 60)
        pygame.display.flip()
        clock.tick(60)

    return True


def menu_victoria():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Sombras del Tiempo - Victoria")
    clock = pygame.time.Clock()

    activo = True
    while activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return True  # jugar de nuevo
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False  # salir

        ventana.fill((15, 25, 20))
        mostrar_texto(ventana, "¡Has completado los 3 niveles!", 40, ALTO // 2 - 40)
        mostrar_texto(ventana, "ENTER: Jugar de nuevo", 28, ALTO // 2 + 10)
        mostrar_texto(ventana, "ESC: Salir", 24, ALTO // 2 + 50)
        pygame.display.flip()
        clock.tick(60)

    return False


