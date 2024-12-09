from utils import init_board, is_valid_move, make_move, undo_move, check_victory
import pygame

class GomokuGame:
    def __init__(self, size=30):
        self.size = size
        self.board = init_board(size)
        self.current_turn = "black"
        self.move_history = []
        self.score = {"black": 0, "white": 0}
        self.victory_message = None
        
    def reset_game(self):
        self.board = init_board(self.size)
        self.current_turn = "black"
        self.move_history = []
        self.victory_message = None
        
    def make_move(self, x, y):
        if is_valid_move(self.board, x, y):
            make_move(self.board, x, y, self.current_turn)
            self.move_history.append((x, y, self.current_turn))
            if check_victory(self.board, x, y, self.current_turn):
                self.score[self.current_turn] += 1
                self.victory_message = f"{self.current_turn.capitalize()} wins!"
                self.reset_game()
            else:
                self.victory_message = None
                self.switch_turn()
            
    def undo_move(self):
        if self.move_history:
            last_move = self.move_history.pop()
            undo_move(self.board, last_move)
            self.switch_turn()
            
    def switch_turn(self):
        self.current_turn = "white" if self.current_turn == "black" else "black"
        
    def get_score(self):
        return self.score
    
    def render(self, screen):
        cell_size = 20
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                if self.board[x][y] == "black":
                    pygame.draw.circle(screen, (0, 0, 0), rect.center, cell_size // 2 - 2)
                elif self.board[x][y] == "white":
                    pygame.draw.circle(screen, (255, 255, 255), rect.center, cell_size // 2 - 2)
        
        font = pygame.font.Font(None, 36)
        score_text = f"Black: {self.score['black']} - White: {self.score['white']}"
        text = font.render(score_text, True, (0, 0, 0))
        screen.blit(text, (20, 20))

        if self.victory_message:
            victory_font = pygame.font.Font(None, 48)
            victory_text = victory_font.render(self.victory_message, True, (255, 0, 0))
            screen.blit(victory_text, (20, 60))
