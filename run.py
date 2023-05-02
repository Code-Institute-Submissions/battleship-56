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




    