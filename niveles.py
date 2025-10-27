from plataforma import Plataforma
from plataforma_movil import PlataformaMovil
from enemigo import Enemigo
from fragmento import Fragmento
from config import ALTO

def cargar_nivel(nivel_num):
    niveles = [
        # 🌄 Nivel 1 - Largo y con alternancia día/noche
        {
            "plataformas": [
                # === SUELO PRINCIPAL (día) ===
                (0, ALTO - 40, 800, 40, "dia"),
                (800, ALTO - 40, 800, 40, "dia"),
                (1600, ALTO - 40, 800, 40, "dia"),
                (2400, ALTO - 40, 800, 40, "dia"),

                (0, ALTO - 40, 800, 40, "noche"),
                (800, ALTO - 40, 800, 40, "noche"),
                (1600, ALTO - 40, 800, 40, "noche"),
                (2400, ALTO - 40, 800, 40, "noche"),

                # === ZONA MEDIA (mixta) ===
                (300, 500, 150, 20, "dia"),
                (600, 450, 150, 20, "dia"),
                (900, 400, 150, 20, "noche"),
                (1200, 350, 150, 20, "dia"),
                (1500, 420, 150, 20, "noche"),
                (1750, 380, 150, 20, "dia"),
                (1950, 340, 150, 20, "noche"),

                # === PLATAFORMAS ALTAS ===
                (2100, 300, 120, 20, "dia"),
                (2250, 260, 120, 20, "noche"),
                (2400, 230, 120, 20, "dia"),
                (2550, 260, 120, 20, "noche"),
                (2700, 230, 120, 20, "dia"),

                # === ZONA SECRETA (solo día) ===
                (2200, 180, 100, 20, "dia"),
                (2350, 160, 100, 20, "dia"),
                (2500, 140, 100, 20, "dia"),

                # === ZONA FINAL ===
                (2800, 400, 150, 20, "dia"),
                (3000, 360, 150, 20, "noche"),
                (3200, 320, 150, 20, "dia"),
                (3400, 280, 150, 20, "noche"),
                (3600, 260, 150, 20, "dia"),

                # === FINAL DEL NIVEL ===
                (3800, ALTO - 120, 150, 20, "dia"),
                (4000, ALTO - 160, 150, 20, "noche"),
                (4200, ALTO - 200, 150, 20, "dia"),
                (4400, ALTO - 40, 800, 40, "dia"),
            ],

            "moviles": [
                # --- Horizontales ---
                (400, 380, 100, 20, "dia", "horizontal", 100, 2),
                (1100, 320, 100, 20, "noche", "horizontal", 80, 2),
                (2400, 220, 100, 20, "noche", "horizontal", 120, 2),
                (3200, 300, 100, 20, "dia", "horizontal", 160, 2),

                # --- Verticales ---
                (1500, 300, 100, 20, "dia", "vertical", 60, 2),
                (1800, 400, 100, 20, "noche", "vertical", 80, 2),
                (3400, 280, 100, 20, "noche", "vertical", 100, 2),
                (3800, 200, 100, 20, "dia", "vertical", 90, 2),
            ],

            "enemigos": [
                # --- Suelo ---
                (500, ALTO - 80, "dia"),
                (1000, ALTO - 80, "dia"),
                (1400, ALTO - 80, "noche"),
                (1800, ALTO - 80, "dia"),
                (2300, ALTO - 80, "noche"),
                (3100, ALTO - 80, "dia"),

                # --- Aéreos ---
                (1900, 280, "noche"),
                (2500, 170, "noche"),
                (3300, 280, "dia"),
                (4000, ALTO - 200, "noche"),
            ],

            "fragmento": (450, ALTO - 140)
        },

        # 🕳 Nivel 2 - Introducción a plataformas móviles
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "dia"),
                (600, 280, 150, 20, "noche"),
                (900, 340, 150, 20, "dia"),
                (1200, 300, 150, 20, "noche"),
            ],
            "moviles": [
                (300, 380, 100, 20, "dia", "horizontal", 150, 2),
                (500, 300, 100, 20, "noche", "vertical", 80, 2),
                (800, 260, 100, 20, "dia", "horizontal", 100, 3),
            ],
            "enemigos": [
                (400, ALTO - 80, "dia"),
                (550, 320, "noche"),
                (1000, 260, "dia"),
            ],
            "fragmento": (1350, 240)
        },

        # 🕰 Nivel 3 - Avanzado y más vertical
        {
            "plataformas": [
                (0, ALTO - 40, 800, 40, "dia"),
                (150, 420, 150, 20, "noche"),
                (350, 360, 150, 20, "dia"),
                (600, 320, 150, 20, "noche"),
                (850, 280, 150, 20, "dia"),
            ],
            "moviles": [
                (200, 330, 100, 20, "dia", "horizontal", 120, 3),
                (500, 270, 100, 20, "noche", "vertical", 100, 2),
                (800, 240, 100, 20, "dia", "horizontal", 140, 2),
            ],
            "enemigos": [
                (200, ALTO - 80, "dia"),
                (400, 320, "noche"),
                (600, 260, "dia"),
                (900, 260, "noche"),
            ],
            "fragmento": (1050, 200)
        }
    ]

    if 0 <= nivel_num < len(niveles):
        return niveles[nivel_num]
    return None
