import pygame
from utils import random_position, check_collision
import time

MOVE_STEP = 10
MAX_SPEED = 20
LEVEL_UP_THRESHOLD = 50  # Score threshold to increase level

class Snake:
    def __init__(self, speed=2):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.speed = speed
        self.score = 0
        self.grow_flag = False

    def move(self):
        if self.direction == 'UP':
            new_head = [self.position[0], self.position[1] - MOVE_STEP]
        elif self.direction == 'DOWN':
            new_head = [self.position[0], self.position[1] + MOVE_STEP]
        elif self.direction == 'LEFT':
            new_head = [self.position[0] - MOVE_STEP, self.position[1]]
        elif self.direction == 'RIGHT':
            new_head = [self.position[0] + MOVE_STEP, self.position[1]]

        self.body.insert(0, new_head)
        if self.grow_flag:
            self.score += 10
            self.grow_flag = False
        else:
            self.body.pop()

        self.position = new_head

    def grow(self):
        self.grow_flag = True

    def check_collision(self):
        if (self.position[0] < 0 or self.position[0] >= 800 or 
            self.position[1] < 0 or self.position[1] >= 600 or 
            self.position in self.body[1:]):
            return True
        return False

class Food:
    def __init__(self):
        self.position = random_position()
        self.is_eaten = False

    def respawn(self):
        self.position = random_position()
        self.is_eaten = False

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()
        self.level = 1
        self.food_timer = 5  # Timer for food appearance
        self.last_food_time = time.time()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    if event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'
                    if event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'
                    if event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'

            self.snake.move()

            if check_collision(self.snake.position, self.food.position):
                self.snake.grow()
                self.food.respawn()
                self.audio_feedback()

            if self.snake.check_collision():
                self.game_over()

            self.screen.fill((0, 0, 0))  
            self.draw_elements()
            self.clock.tick(min(10 + self.snake.score // 10, MAX_SPEED))  # Cap the speed

    def audio_feedback(self):
        eat_sound = pygame.mixer.Sound("eat_sound.wav")
        eat_sound.play()

    def draw_elements(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], MOVE_STEP, MOVE_STEP))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], MOVE_STEP, MOVE_STEP))
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.SysFont('arial', 36)
        text = font.render("Game Over! Your score: {}".format(self.snake.score), True, (255, 255, 255))
        self.screen.blit(text, (200, 250))
        pygame.display.flip()
        time.sleep(2)  # Give time to read message
        pygame.quit()
        exit()

pygame.init()
screen = pygame.display.set_mode((800, 600))
game = Game(screen)
game.run()
