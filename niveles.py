# niveles.py

from plataforma import Plataforma
from enemigo import Enemigo
from fragmento import Fragmento
from config import ALTO

def cargar_nivel(nivel_num):
    niveles = [
        # Nivel 1
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (250, 450, 150, 20, "dia"),
                (550, 350, 150, 20, "noche")
            ],
            "enemigos": [
                (100, ALTO - 80, "dia")
            ],
            "fragmento": (700, 300)
        },
        # Nivel 2
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "dia"),
                (400, 360, 150, 20, "noche"),
                (600, 280, 100, 20, "dia")
            ],
            "enemigos": [
                (300, ALTO - 80, "dia"),
                (500, 320, "noche")
            ],
            "fragmento": (750, 240)
        },
        # Nivel 3 (final)
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "noche"),
                (350, 360, 150, 20, "dia"),
                (550, 300, 150, 20, "noche")
            ],
            "enemigos": [
                (200, ALTO - 80, "dia"),
                (400, 320, "noche"),
                (600, 260, "dia")
            ],
            "fragmento": (750, 260)
        }
    ]

    # Retornar configuración del nivel o None si no existe
    if 0 <= nivel_num < len(niveles):
        return niveles[nivel_num]
    return None
