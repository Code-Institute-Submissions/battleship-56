from random import randint

# creates and clean board 
board = []

# adding the rows in board. 
for i in range(0, 8):
    board.append(["O"] *8)
    
# function to print the board rows.
def print_board(board):
    for row in board:
        print(" ".join(row))

# function to display to logo. 
def print_logo():
    logo = """
,-----.              ,--.     ,--.   ,--.          ,---.   ,--.      ,--.         
|  |) /_   ,--,--. ,-'  '-. ,-'  '-. |  |  ,---.  '   .-'  |  ,---.  `--'  ,---.  
|  .-.  \ ' ,-.  | '-.  .-' '-.  .-' |  | | .-. : `.  `-.  |  .-.  | ,--. | .-. | 
|  '--' / \ '-'  |   |  |     |  |   |  | \   --. .-'    | |  | |  | |  | | '-' ' 
`------'   `--`--'   `--'     `--'   `--'  `----' `-----'  `--' `--' `--' |  |-'  
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
ship_location = [(random_row(board),random_col(board)) for _ in range(num_ship)]

# Ships found. 
ships_found = 0

# main game loop 
turn = 0
while True:
    print("\nTurn", turn + 1)

    










    