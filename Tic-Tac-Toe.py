import math

def draw_board(brd):
    for row in brd:
        print(" | ".join(row))
        print("-" * 10)

def winner_exists(board, player):
    rows = board
    cols = list(zip(*board))
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]

    for line in rows + cols + [diag1, diag2]:
        if all(cell == player for cell in line):
            return True
    return 

def get_open_spots(b):
    open_cells = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                open_cells.append((i, j))
    return open_cells


def run_minimax(state, ai_turn):
    if winner_exists(state, 'O'):
        return 1
    elif winner_exists(state, 'X'):
        return -1
    elif not get_open_spots(state):
        return 0

    
    if ai_turn:
        top_score = -math.inf
    else:
        top_score = math.inf


    for x, y in get_open_spots(state):
        state[x][y] = 'O' if ai_turn else 'X'
        result = run_minimax(state, not ai_turn)
        state[x][y] = ' '

        if ai_turn:
            top_score = max(top_score, result)
        else:
            top_score = min(top_score, result)

    return top_score


def choose_ai_move(game):
    highest = -math.inf
    move_choice = (-1, -1)

    for x, y in get_open_spots(game):
        game[x][y] = 'O'
        val = run_minimax(game, False)
        game[x][y] = ' '
        if val > highest:
            highest = val
            move_choice = (x, y)

    return move_choice

state = [[' '] * 3 for _ in range(3)]

while True:
    draw_board(state)
    try:
        pos = input("Your move (row col): ").strip()
        r, c = map(int, pos.split())
    except:
        print("Input error. Try format: row col")
        continue

    if state[r][c] != ' ':
        print("That spot is taken. Try again.")
        continue

    state[r][c] = 'X'

    if winner_exists(state, 'X') or not get_open_spots(state):
        break

    ai_choice = choose_ai_move(state)
    if ai_choice != (-1, -1):
        state[ai_choice[0]][ai_choice[1]] = 'O'

    if winner_exists(state, 'O') or not get_open_spots(state):
        break

draw_board(state)


if winner_exists(state, 'X'):
    print("Congrats, you win!")
elif winner_exists(state, 'O'):
    print("AI dominates!")
else:
    print("Match tie.")
