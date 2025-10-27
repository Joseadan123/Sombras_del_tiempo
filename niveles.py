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
                (500, ALTO - 90, "dia"),
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

            "fragmento": (730, ALTO - 350)
        },

        # 🕳 Nivel 2 - Introducción a plataformas móviles
                # 🕳 Nivel 2 - Introducción a plataformas móviles
        {
            "plataformas": [
                # Piso base
                (0, ALTO - 40, 800, 40, "dia"),
                (0, ALTO - 40, 800, 40, "noche"),  

                # Plataformas intermedias
                (150, 500, 150, 20, "dia"),
                (400, 440, 150, 20, "noche"),
                (650, 380, 150, 20, "dia"),

                # Plataformas elevadas
                (250, 320, 150, 20, "noche"),
                (550, 260, 150, 20, "dia"),

                # Plataforma final (cerca del fragmento)
                (700, 220, 100, 20, "noche"),
            ],

            "moviles": [
                # Plataformas móviles que conectan secciones
                (300, 420, 100, 20, "dia", "horizontal", 80, 2),
                (500, 300, 100, 20, "noche", "vertical", 60, 2),
                (600, 340, 100, 20, "dia", "horizontal", 100, 3),
            ],

            "enemigos": [
                (700, 400, "dia"),
            ],

            # Fragmento al final, visible dentro del ancho
            "fragmento": (750, 180)
        },
        # 🕰 Nivel 3 - Las Torres del Tiempo (Optimizado)
        {
            "plataformas": [
                # Base
                (0, ALTO - 40, 800, 40, "dia"),

                # Plataforma baja (inicio de ascenso)
                (200, 500, 150, 20, "dia"),

                # Plataforma intermedia
                (450, 420, 150, 20, "noche"),

                # Plataforma media-alta
                (650, 340, 150, 20, "dia"),

                # Plataforma alta (previo al fragmento)
                (400, 260, 150, 20, "noche"),
            ],

            "moviles": [
                # Plataforma móvil horizontal (zona media)
                (300, 400, 100, 20, "dia", "horizontal", 120, 2),

                # Plataforma móvil vertical (sube hasta la parte alta)
                (600, 300, 100, 20, "noche", "vertical", 80, 2),
            ],

            "enemigos": [
                # Enemigo en el suelo
                (250, ALTO - 80, "dia"),

                # Enemigo en zona media
                (500, 380, "noche"),

                # Enemigo alto (protege fragmento)
                (650, 280, "dia"),
            ],

            # Fragmento en zona visible y accesible desde las plataformas altas
            "fragmento": (720, 220)
        }
    ]

    if 0 <= nivel_num < len(niveles):
        return niveles[nivel_num]
    return None
