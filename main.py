import pygame
from game import Tetris

# Initialize the pygame library
pygame.init()

# Set up the game window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Create the game instance
game = Tetris()

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    try:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_block_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_block_right()
                elif event.key == pygame.K_UP:
                    game.rotate_block()
                elif event.key == pygame.K_DOWN:
                    game.move_block_down()
                elif event.key == pygame.K_SPACE:
                    game.drop_block()
                elif event.key == pygame.K_p:
                    game.pause()
                elif event.key == pygame.K_r:
                    game.restart()

        # Update game
        game.update()

        # Draw game
        window.fill((0, 0, 0))  # Clear screen with black
        game.draw(window)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        running = False

# Quit pygame
pygame.quit()

