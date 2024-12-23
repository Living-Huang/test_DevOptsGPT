import pygame

class Block:
    def __init__(self, shape, color):
        """
        Initialize the Block with a shape and color, and set default size and position.
        
        :param shape: List of tuples representing the block's shape coordinates.
        :param color: Tuple representing the color (RGB values) of the block.
        """
        self.shape = shape
        self.color = color
        self.size = 30
        self.x = 5
        self.y = 0

    def move(self, dx, dy):
        """
        Move the block by a specified amount.

        :param dx: Amount to move the block in the x direction.
        :param dy: Amount to move the block in the y direction.
        """
        self.x += dx
        self.y += dy

    def rotate(self):
        """
        Rotate the block 90 degrees clockwise.
        """
        self.shape = [(-y, x) for x, y in self.shape]

    def unrotate(self):
        """
        Rotate the block 90 degrees counterclockwise, reverting the last rotation.
        """
        self.shape = [(y, -x) for x, y in self.shape]

    def draw(self, surface):
        """
        Draw the block on the given Pygame surface.

        :param surface: The Pygame surface to draw the block on.
        """
        for (x, y) in self.shape:
            pygame.draw.rect(surface, self.color, pygame.Rect((self.x + x) * self.size, (self.y + y) * self.size, self.size, self.size))

    def check_collision(self, grid):
        """
        Check if the block collides with the given grid (or exceeds the grid boundaries).
        
        :param grid: 2D list representing the game grid to check for collisions.
        :return: Boolean value indicating whether a collision occurs.
        """
        for (x, y) in self.shape:
            if self.x + x < 0 or self.x + x >= len(grid[0]) or self.y + y >= len(grid):
                return True
            if grid[self.y + y][self.x + x] != 0:
                return True
        return False
