# del archivo game traer la definicion de la clase Game
from game import Game


# necesito una funcion principal o main
if __name__ == "__main__":
    # crear una instancia de una clase llamada "Game"
    # game -> el objeto o la instancia (variable)
    # Game() -> es la llamada al metodo __init__ de la clase Game

    # Nos compramos el juego
    game = Game()
    # encedemos el juego
    game.run()