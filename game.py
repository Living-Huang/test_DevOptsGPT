import pygame
import random
from utils import initialize_settings, print_score, draw_block, check_collision, clear_full_lines

class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0  # Shape rotation index
        self.x = 3
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def unrotate(self):
        self.rotation = (self.rotation - 1) % len(self.shape)

    def get_cells(self):
        cells = []
        for index in self.shape[self.rotation]:
            x = self.x + (index % 4)
            y = self.y + (index // 4)
            cells.append((x, y))
        return cells

class Tetris:
    def __init__(self):
        self.settings = initialize_settings()
        self.score = 0
        self.level = 1
        self.paused = False
        self.game_over_flag = False
        self.blocks = []
        self.current_block = self.generate_new_block()

    def generate_new_block(self):
        shapes = [
            [[1, 5, 9, 13], [4, 5, 6, 7]],  # I-shape
            [[1, 2, 5, 6]],                 # O-shape
            [[1, 2, 6, 10], [4, 5, 6, 2]],  # T-shape
            [[1, 2, 6, 5], [0, 4, 5, 6]],   # S-shape
            [[1, 5, 6, 7], [6, 5, 4, 0]]    # Z-shape
        ]
        return Block(random.choice(shapes), (255, 255, 255))

    def move_block_left(self):
        self.current_block.move(-1, 0)
        if check_collision(self.blocks, self.current_block):
            self.current_block.move(1, 0)

    def move_block_right(self):
        self.current_block.move(1, 0)
        if check_collision(self.blocks, self.current_block):
            self.current_block.move(-1, 0)

    def rotate_block(self):
        self.current_block.rotate()
        if check_collision(self.blocks, self.current_block):
            self.current_block.unrotate()

    def move_block_down(self):
        self.current_block.move(0, 1)
        if check_collision(self.blocks, self.current_block):
            self.current_block.move(0, -1)
            self.blocks.append(self.current_block)
            lines_cleared = clear_full_lines(self.blocks)
            self.update_score_and_level(lines_cleared)
            self.current_block = self.generate_new_block()
            if check_collision(self.blocks, self.current_block):
                self.set_game_over()

    def drop_block(self):
        while not check_collision(self.blocks, self.current_block):
            self.current_block.move(0, 1)
        self.current_block.move(0, -1)
        self.blocks.append(self.current_block)
        lines_cleared = clear_full_lines(self.blocks)
        self.update_score_and_level(lines_cleared)
        self.current_block = self.generate_new_block()
        if check_collision(self.blocks, self.current_block):
            self.set_game_over()

    def pause(self):
        self.paused = not self.paused

    def restart(self):
        self.__init__()

    def update(self):
        if self.paused or self.game_over_flag:
            return
        if not check_collision(self.blocks, self.current_block):
            self.current_block.move(0, 1)
        else:
            self.current_block.move(0, -1)
            self.blocks.append(self.current_block)
            lines_cleared = clear_full_lines(self.blocks)
            self.update_score_and_level(lines_cleared)
            self.current_block = self.generate_new_block()
            if check_collision(self.blocks, self.current_block):
                self.set_game_over()

    def draw(self, window):
        for block in self.blocks:
            draw_block(window, block)
        draw_block(window, self.current_block)
        print_score(window, self.score, self.level)

    def set_game_over(self):
        self.game_over_flag = True

    def update_score_and_level(self, lines_cleared):
        line_points = {1: 40, 2: 100, 3: 300, 4: 1200}
        self.score += line_points.get(lines_cleared, 0) * self.level
        if self.score >= self.level * 1000:
            self.level += 1

# Assumed code for utils.py for testing purposes
# This should be in a `utils.py` file
def initialize_settings():
    return {
        'width': 300,
        'height': 600,
        'block_size': 30,
        'fps': 30
    }

def print_score(window, score, level):
    font = pygame.font.Font(None, 36)
    text = f'Score: {score}   Level: {level}'
    label = font.render(text, 1, (255, 255, 255))
    window.blit(label, (10, 10))

def draw_block(window, block):
    for (x, y) in block.get_cells():
        pygame.draw.rect(window, block.color,
                         (x * 30, y * 30, 30, 30))

def check_collision(blocks, current_block):
    for (x, y) in current_block.get_cells():
        if x < 0 or x >= 10 or y >= 20:
            return True
        if any((x == bx and y == by) for (bx, by) in b.get_cells() for b in blocks):
            return True
    return False

def clear_full_lines(blocks):
    full_lines = [y for y in range(20) if all((x, y) in [(cx, cy) for c in blocks for (cx, cy) in c.get_cells()] for x in range(10))]
    new_blocks = []
    for block in blocks:
        cells = [(x, y) for (x, y) in block.get_cells() if y not in full_lines]
        if cells:
            block.shape = [[x + y * 4 for (x, y) in cells]] * 4
            new_blocks.append(block)
    blocks[:] = new_blocks
    return len(full_lines)
