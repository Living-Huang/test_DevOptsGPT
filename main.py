import pygame
import os
from game import Game

def main():
    pygame.init()
    
    # Set up game window
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("贪吃蛇游戏")
    
    # Load background music
    music_file = "background_music.mp3"
    
    try:
        if not os.path.isfile(music_file):
            raise FileNotFoundError(f"Music file '{music_file}' not found.")
            
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
    
    except pygame.error as e:
        print(f"Error loading music: {e}")
        return
    except FileNotFoundError as e:
        print(e)
        return
    
    # Game instance
    game = Game(screen)
    
    try:
        game.run()
    except Exception as e:
        print(f"An error occurred while running the game: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
