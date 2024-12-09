import pygame
from game import GomokuGame

pygame.init()

# Set up the game window
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("五子棋游戏")

# Constants for the game
CELL_SIZE = 20

# Instantiate a GomokuGame object
game = GomokuGame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            game.make_move(mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)  # Adjust for cell size
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:  # Example key for undo
                game.undo_move()
            elif event.key == pygame.K_r:  # Example key for reset
                game.reset_game()
                
    # Rendering logic
    screen.fill((255, 255, 255))  # Clear the screen with white
    game.render(screen)  # Render the game state
    pygame.display.flip()  # Update the display

pygame.quit()
