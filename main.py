import pygame
import os
from game import SnakeGame

def main():
    pygame.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("贪吃蛇游戏")
    
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
    
    # 加载音效
    eat_sound = pygame.mixer.Sound('eat.wav')
    game_over_sound = pygame.mixer.Sound('game_over.wav')
    
    # 创建游戏实例
    game = SnakeGame(screen, eat_sound, game_over_sound)
    
    running = True
    paused = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif paused:
                    if event.key == pygame.K_r:
                        game.start_new_game()
                        paused = False
                else:
                    game.handle_keypress(event.key)
        
        if not paused:
            game.update()
            if game.game_over:
                paused = True
        
        game.draw()
        pygame.display.flip()
        pygame.time.delay(game.speed)

    pygame.quit()

if __name__ == "__main__":
    main()
