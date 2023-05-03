from random import randint


def create_board():
    board = []
    for i in range(0, 8):
        board.append(["O"] * 8)
    return board

# adding rows to the board


def print_board(board):
    for row in board:
        print(" ".join(row))


board = create_board()
# function to display to logo.


def print_logo():
    logo = r"""
,-----.             ,--.     ,--.   ,--.          ,---.   ,--.      ,--.
|  |) /_  ,--,--. ,-'  '-. ,-'  '-. |  |  ,---.  '   .-'  |  ,---.  `--' ,---.'
|  .-.  \ ' ,-.  | '-.  .-' '-.  .-' |  | | .-. : `.  `-.  |  .-.  | ,--.| .-.|
|  '--' / \ '-'  |   |  |     |  |   |  | \   --. .-'    | |  | |  | |  || '-''
`------'   `--`--'   `--'     `--'   `--'  `----' `-----'  `--' `--' `--'| |-'
                                                                         `--'
"""

    print(logo)


print_logo()

# game instructions
print("Welcome to BattleShip!\n")
print("You got ten attempts to sink the all 3 ships!")
print("If you get bored after a few attempts, just press Enter to exit\n")

username = input("Please select a username: ")

print(f"Let's play BattleShip, {username.upper()}!\n")
print_board(board)

# function for random rows


def random_row(board):
    return randint(0, len(board) - 1)

# function for random columns


def random_col(board):
    return randint(0, len(board) - 1)


# number of ships and the locations.

num_ship = 3
ship_loca = [(random_row(board), random_col(board)) for _ in range(num_ship)]

# Ships found.
ships_found = 0

# main game loop
turn = 0
while True:
    print("\nTurn", turn + 1)
    turn += 1
    # user guessing row or column where the ship is.
    guess_row_input = input("Guess Row: (Or press Enter to quit!) ")
    guess_col_input = input("guess Col: (Or press enter to quit!) ")

    # if the user decides to leave the game, by pressing Enter.
    if not guess_row_input or not guess_col_input:
        print("Exiting the game!")
        break
    # converting user input to integer.
    guess_row = int(guess_col_input)
    guess_col = int(guess_col_input)
    # if a ship is hit i get's marked by and S
    if (guess_row, guess_col) in ship_loca:
        print("You hit a BattleShip!")
        board[guess_row][guess_col] = "S"
        ship_loca.remove((guess_row, guess_col))
        # increases the the number of ships found
        ships_found += 1
        # if the user found all 3 ships breaks the loop.
    if ships_found == num_ship:
        print("You've sunk all (3) ships!")
        break

else:
    if guess_row not in range(8) or guess_col not in range(8):
        print("Not even close! Try again!")
    elif board[guess_row][guess_col] in ("X", "S"):
        print("you tried that one already!")
    else:
        print("You missed the Ship!!!!\n")
        board[guess_row][guess_col] = "X"
        if turn == 9:
            print("Game Over .....")
