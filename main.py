from game import Game
from menu import menu_inicio, menu_victoria

if __name__ == "__main__": 
    if not menu_inicio():
        raise SystemExit

    while True:
        juego = Game()
        juego.run()

        if juego.completed:
            jugar_de_nuevo = menu_victoria()
            if jugar_de_nuevo:
                continue
            break
        else:
            break