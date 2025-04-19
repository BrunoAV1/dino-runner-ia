import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    try:
        game.run()
    finally:
        game.agent.save_q_table()  # Salva a Q-table ao sair
        pygame.quit()
