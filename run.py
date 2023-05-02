#imports 
import os
from random import randint

# the board setup 
board = []

for i in range(0, 8):
    board.append(["O"] *8)

# Printing out the board 
def print_board(board):
    for row in board:
        print("  ".join(row))


# Gamme instructions and username prompt 

def print_logo():
    logo = """
    """
    print(logo)

print_logo()
print("\n")
print("Welcome to Battleship!\n")
