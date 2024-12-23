import random
from typing import List
import pygame

# 保留原有的 random_position 函数

def random_position() -> List[int]:
    """Generate a random position for the food within the game boundaries."""
    return [random.randint(0, 79) * 10, random.randint(0, 59) * 10]

# 保留原有的 check_collision 函数

def check_collision(pos1: List[int], pos2: List[int]) -> bool:
    """Check if two positions are colliding.

    Args:
        pos1 (List[int]): The first position.
        pos2 (List[int]): The second position.

    Returns:
        bool: True if the positions collide, False otherwise.
    """
    # Validate inputs
    if not (isinstance(pos1, list) and isinstance(pos2, list)):
        raise ValueError("Both positions must be lists.")
    if len(pos1) != 2 or len(pos2) != 2:
        raise ValueError("Both positions must be lists of length 2.")

    return pos1 == pos2

# 新增 draw_text 函数

def draw_text(window, text, x, y):
    font = pygame.font.Font(None, 36)
    surface = font.render(text, True, (255, 255, 255))
    window.blit(surface, (x, y))

# 新增 play_sound_effect 函数

def play_sound_effect(sound):
    sound.play()