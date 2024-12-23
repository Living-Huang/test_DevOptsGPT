import pygame
import random
import time
from utils import random_food_position, draw_text, play_sound_effect

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
        self.position = random_food_position()
        self.is_eaten = False

    def respawn(self):
        self.position = random_food_position()
        self.is_eaten = False

class SnakeGame:
    def __init__(self, window, eat_sound, game_over_sound):
        self.window = window
        self.eat_sound = eat_sound
        self.game_over_sound = game_over_sound
        self.score = 0
        self.high_score = 0
        self.start_new_game()

    def start_new_game(self):
        self.snake = Snake()
        self.food = Food()
        self.direction = pygame.K_RIGHT
        self.game_over = False
        self.choose_difficulty()

    def choose_difficulty(self):
        level = input('Choose difficulty (easy, medium, hard): ')
        if level == 'easy':
            self.speed = 150
        elif level == 'medium':
            self.speed = 100
        elif level == 'hard':
            self.speed = 50
        else:
            self.speed = 100 

    def update(self):
        self.snake.move()
        if check_collision(self.snake.position, self.food.position):
            self.snake.grow()
            self.food.respawn()
            play_sound_effect(self.eat_sound)

        if self.snake.check_collision():
            self.game_over = True
            play_sound_effect(self.game_over_sound)
            if self.snake.score > self.high_score:
                self.high_score = self.snake.score
                time.sleep(2)
                pygame.quit()
                exit()

    def draw(self):
        self.window.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.window, (0, 255, 0), (segment[0], segment[1], MOVE_STEP, MOVE_STEP))
        pygame.draw.rect(self.window, (255, 0, 0), (self.food.position[0], self.food.position[1], MOVE_STEP, MOVE_STEP))
        draw_text(self.window, f'Score: {self.score}', 10, 10)
        draw_text(self.window, f'High Score: {self.high_score}', 10, 30)
        pygame.display.flip()

    def handle_keypress(self, key):
        if key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            self.direction = key

MOVE_STEP = 10
MAX_SPEED = 20
LEVEL_UP_THRESHOLD = 50

pygame.init()
screen = pygame.display.set_mode((800, 600))
eat_sound = pygame.mixer.Sound('eat_sound.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')
game = SnakeGame(screen, eat_sound, game_over_sound)

def game_loop():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                game.handle_keypress(event.key)
        game.update()
        game.draw()
        clock.tick(game.speed)

game_loop()