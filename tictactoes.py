# https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=GmGsrz69RQlQ&line=101&uniqifier=1

import random

# 1. Initialize the game board
board = {
    'up-left': ' ', 'up-center': ' ', 'up-right': ' ',
    'mid-left': ' ', 'mid-center': ' ', 'mid-right': ' ',
    'down-left': ' ', 'down-center': ' ', 'down-right': ' '
}

# 2. Define player symbols
human_player = 'X'
ai_player = 'O'

# 3. Prompt the human player to choose who goes first
while True:
    first_player_choice = input("Who goes first? (AI, human, random): ").lower()
    if first_player_choice in ['human', 'ai', 'random']:
        break
    else:
        print("Invalid choice. Please enter 'human', 'AI', or 'random'.")

# 4. Determine the starting player
if first_player_choice == 'random':
    current_player = random.choice([human_player, ai_player])
elif first_player_choice == 'human':
    current_player = human_player
else: # AI goes first
    current_player = ai_player

# 5. Print an initial message indicating which player goes first
if current_player == human_player:
    print("You go first!")
else:
    print("The AI goes first!")
