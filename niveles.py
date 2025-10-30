from plataforma import Plataforma
from plataforma_movil import PlataformaMovil
from enemigo import Enemigo
from fragmento import Fragmento
from config import ALTO

def cargar_nivel(nivel_num):
    niveles = [
        # 🌄 Nivel 1 - Simplificado y con mejor colocación
        {
            "plataformas": [
                # Suelo base visible en ambos mundos
                (0, ALTO - 40, 800, 40, "dia"),
                (0, ALTO - 40, 800, 40, "noche"),

                # Escalera suave hacia la derecha
                (200, 500, 180, 20, "dia"),
                (500, 420, 180, 20, "noche"),
                (320, 340, 160, 20, "dia"),
                (650, 300, 120, 20, "noche"),
            ],

            "moviles": [
                # Una sola plataforma móvil para variedad
                (380, 400, 100, 20, "dia", "horizontal", 100, 2),
            ],

            "enemigos": [
                # Enemigos centrados sobre plataformas
                (200 + (180 - 40) // 2, 500 - 60, "dia"),   # sobre (200,500)
                (500 + (180 - 40) // 2, 420 - 60, "noche"), # sobre (500,420)
                (320 + (160 - 40) // 2, 340 - 60, "dia"),   # sobre (320,340)
            ],

            "fragmento": (700, 260)
        },

        # 🕳 Nivel 2 - Introducción a plataformas móviles
                # 🕳 Nivel 2 - Introducción a plataformas móviles
        {
            "plataformas": [
                # Piso base
                (0, ALTO - 40, 800, 40, "dia"),
                (0, ALTO - 40, 800, 40, "noche"),  

                # Tres plataformas bien espaciadas
                (160, 500, 160, 20, "dia"),
                (440, 420, 160, 20, "noche"),
                (660, 340, 140, 20, "dia"),

                # Plataforma final (cerca del fragmento)
                (720, 220, 100, 20, "noche"),
            ],

            "moviles": [
                # Una móvil para conectar la zona media
                (300, 420, 100, 20, "dia", "horizontal", 90, 2),
            ],

            "enemigos": [
                # Colocados justo encima y centrados
                (160 + (160 - 40) // 2, 500 - 60, "dia"),   # sobre (160,500)
                (440 + (160 - 40) // 2, 420 - 60, "noche"), # sobre (440,420)
            ],

            # Fragmento al final, visible dentro del ancho
            "fragmento": (750, 180)
        },
        # 🕰 Nivel 3 - Las Torres del Tiempo (Optimizado)
        {
            "plataformas": [
                # Base
                (0, ALTO - 40, 800, 40, "dia"),

                # Ascenso compacto
                (220, 500, 160, 20, "dia"),
                (460, 430, 160, 20, "noche"),
                (620, 360, 140, 20, "dia"),
                (420, 290, 140, 20, "noche"),
            ],

            "moviles": [
                # Una móvil para variar el ritmo
                (320, 410, 100, 20, "dia", "horizontal", 110, 2),
            ],

            "enemigos": [
                # Centrado sobre cada plataforma estática (no la base)
                (220 + (160 - 40) // 2, 500 - 60, "dia"),   # (220,500)
                (460 + (160 - 40) // 2, 430 - 60, "noche"), # (460,430)
                (620 + (140 - 40) // 2, 360 - 60, "dia"),   # (620,360)
            ],

            # Fragmento accesible desde la última plataforma
            "fragmento": (720, 250)
        }
    ]

    if 0 <= nivel_num < len(niveles):
        return niveles[nivel_num]
    return None
