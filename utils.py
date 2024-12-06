import random
from typing import List

def random_position() -> List[int]:
    """Generate a random position for the food within the game boundaries."""
    return [random.randint(0, 79) * 10, random.randint(0, 59) * 10]

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
