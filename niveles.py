# niveles.py
from plataforma import Plataforma
from plataforma_movil import PlataformaMovil
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
            "moviles": [],
            "enemigos": [(100, ALTO - 80, "dia")],
            "fragmento": (700, 300)
        },
        # Nivel 2 — plataformas móviles
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "dia"),
                (600, 280, 150, 20, "noche")
            ],
            "moviles": [
                # Horizontal
                (300, 380, 100, 20, "dia", "horizontal", 150, 2),
                # Vertical
                (500, 300, 100, 20, "noche", "vertical", 80, 2)
            ],
            "enemigos": [
                (400, ALTO - 80, "dia"),
                (550, 320, "noche")
            ],
            "fragmento": (750, 240)
        },
        # Nivel 3 — aún más plataformas móviles
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
