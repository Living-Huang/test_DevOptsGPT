import pygame

class Block:
    def __init__(self, shape, color, x, y, block_size):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.block_size = block_size

def initialize_settings():
    return {
        "block_size": 30,
        "width": 10,
        "height": 20,
        "speed": 500
    }

def print_score(window, score, level):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score} Level: {level}", True, (255, 255, 255))
    window.blit(text, (20, 20))

def draw_block(window, block):
    block_size = block.block_size  # assuming block has a block_size attribute
    for x, y in block.shape:
        pygame.draw.rect(
            window,
            block.color,
            (block.x + x * block_size, block.y + y * block_size, block_size, block_size),
            0
        )

def check_collision(blocks, current_block):
    for x, y in current_block.shape:
        world_x = current_block.x + x
        world_y = current_block.y + y
        if (
            world_x < 0 or world_x >= 10 or
            world_y < 0 or world_y >= 20 or
            any((block.x == world_x and block.y == world_y) for block in blocks)
        ):
            return True
    return False

def clear_full_lines(blocks):
    lines = []
    for y in range(20):
        if all(block.y == y for block in blocks):  # fixed the condition to check y not x
            lines.append(y)

    for line in lines:
        blocks = [block for block in blocks if block.y != line]
        for block in blocks:
            if block.y < line:
                block.y += 1

    return blocks  # Added this to return the updated blocks list

# Initialize pygame and create game window for testing
pygame.init()
settings = initialize_settings()
window = pygame.display.set_mode((settings["width"] * settings["block_size"], settings["height"] * settings["block_size"]))

# Testing code
running = True
clock = pygame.time.Clock()
blocks = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    for block in blocks:
        draw_block(window, block)

    print_score(window, 0, 1)

    pygame.display.flip()
    clock.tick(settings["speed"])

pygame.quit()
