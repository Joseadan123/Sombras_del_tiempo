# niveles.py
from plataforma import Plataforma
from plataforma_movil import PlataformaMovil
from enemigo import Enemigo
from fragmento import Fragmento
from config import ALTO

def cargar_nivel(nivel_num):
    niveles = [
        # 🌄 Nivel 1 - Extendido y con recorrido largo
        {
            "plataformas": [
                # Piso base (recorrido largo)
                (0, ALTO - 40, 800, 40, "dia"),
                (800, ALTO - 40, 800, 40, "dia"),
                (1600, ALTO - 40, 800, 40, "dia"),

                # Plataformas bajas
                (300, 500, 150, 20, "dia"),
                (600, 450, 150, 20, "dia"),
                (900, 400, 150, 20, "dia"),
                (1200, 350, 150, 20, "dia"),
                (1500, 420, 150, 20, "dia"),

                # Plataformas elevadas
                (500, 300, 120, 20, "noche"),
                (850, 250, 120, 20, "noche"),
                (1300, 280, 120, 20, "noche"),
                (1700, 230, 120, 20, "noche"),

                # Final del nivel
                (2100, ALTO - 100, 150, 20, "dia")
            ],
            "moviles": [
                # Plataformas móviles horizontales
                (400, 380, 100, 20, "dia", "horizontal", 100, 2),
                (1100, 320, 100, 20, "noche", "horizontal", 80, 2),
                # Plataformas móviles verticales
                (1400, 280, 100, 20, "dia", "vertical", 60, 2),
                (1800, 400, 100, 20, "noche", "vertical", 80, 2)
            ],
            "enemigos": [
                (500, ALTO - 80, "dia"),
                (1000, ALTO - 80, "dia"),
                (1400, 320, "noche"),
                (1800, ALTO - 80, "dia")
            ],
            "fragmento": (2150, ALTO - 140)
        },
        # 🕳 Nivel 2
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "dia"),
                (600, 280, 150, 20, "noche")
            ],
            "moviles": [
                (300, 380, 100, 20, "dia", "horizontal", 150, 2),
                (500, 300, 100, 20, "noche", "vertical", 80, 2)
            ],
            "enemigos": [
                (400, ALTO - 80, "dia"),
                (550, 320, "noche")
            ],
            "fragmento": (750, 240)
        },
        # 🕰 Nivel 3
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "noche"),
                (350, 360, 150, 20, "dia")
            ],
            "moviles": [
                (200, 330, 100, 20, "dia", "horizontal", 120, 3),
                (500, 270, 100, 20, "noche", "vertical", 100, 2)
            ],
            "enemigos": [
                (200, ALTO - 80, "dia"),
                (400, 320, "noche"),
                (600, 260, "dia")
            ],
            "fragmento": (750, 260)
        }
    ]

    if 0 <= nivel_num < len(niveles):
        return niveles[nivel_num]
    return None
