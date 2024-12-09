def init_board(size):
    return [[None for _ in range(size)] for _ in range(size)]

def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] is None

def make_move(board, x, y, color, move_history):
    if is_valid_move(board, x, y):
        board[x][y] = color
        move_history.append((x, y, color))

def undo_move(board, move_history):
    if move_history:
        x, y, color = move_history.pop()
        board[x][y] = None

def check_victory(board, x, y, color):
    def count_stones(dx, dy):
        count = 0
        nx, ny = x, y
        while 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == color:
            count += 1
            nx += dx
            ny += dy
        return count - 1  # subtract 1 to avoid counting the stone at (x, y) twice

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        if count_stones(dx, dy) + count_stones(-dx, -dy) >= 4:
            return True
    return False
