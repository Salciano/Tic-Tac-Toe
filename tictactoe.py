import random

def create_board():
# Creates an empty Tic-Tac-Toe board.
    return {
        'up-left': ' ', 'up': ' ', 'up-right': ' ',
        'left': ' ', 'center': ' ', 'right': ' ',
        'down-left': ' ', 'down': ' ', 'down-right': ' '
    }

def display_board(board):
    """Displays the Tic-Tac-Toe board."""
    print(f"""
 {board['up-left']} | {board['up']} | {board['up-right']}
---+---+---
 {board['left']} | {board['center']} | {board['right']}
---+---+---
 {board['down-left']} | {board['down']} | {board['down-right']}
    """)

def is_valid_move(board, move):
    """Checks if a move is valid."""
    valid_moves = ['left', 'right', 'up', 'down', 'center', 'up-left', 'up-right', 'down-left', 'down-right']
    return move.lower() in valid_moves and board.get(move.lower()) == ' '

def make_move(board, move, player):
    """Makes a move on the board."""
    board[move.lower()] = player

def check_win(board, player):
    """Checks if a player has won."""
    win_conditions = [
        ('up-left', 'up', 'up-right'),
        ('left', 'center', 'right'),
        ('down-left', 'down', 'down-right'),
        ('up-left', 'left', 'down-left'),
        ('up', 'center', 'down'),
        ('up-right', 'right', 'down-right'),
        ('up-left', 'center', 'down-right'),
        ('up-right', 'center', 'down-left')
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all(cell != ' ' for cell in board.values())

def get_human_move(board):
    """Gets the human player's move."""
    while True:
        move = input("Enter your move (left, right, up, down, center, up-left, up-right, down-left, down-right): ")
        if is_valid_move(board, move):
            return move
        else:
            print("Invalid move. Please try again.")

def get_ai_move(board):
    """Gets the AI player's move."""
    available_moves = [move for move, value in board.items() if value == ' ']
    return random.choice(available_moves)

def play_game():
    """Plays a game of Tic-Tac-Toe."""
    board = create_board()
    players = ['X', 'O']
    random.shuffle(players)
    human_player, ai_player = players

    print(f"Human is {human_player}. AI is {ai_player}.")
    current_player = human_player if random.random() < 0.5 else ai_player
    print(f"{current_player} goes first.")

    while True:
        display_board(board)
        if current_player == human_player:
            move = get_human_move(board)
        else:
            print("AI is thinking...")
            move = get_ai_move(board)
            print(f"AI chose: {move}")

        make_move(board, move, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = human_player if current_player == ai_player else ai_player

# Start the game
play_game()
