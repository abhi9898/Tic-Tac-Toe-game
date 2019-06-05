from IPython.display import clear_output

board = [" "] * 10

def display_board(board):
    clear_output()
    print(
        " " + board[7] + " | " + board[8] + " | " + board[9] + "\n" +
        "-----------\n" +
        " " + board[4] + " | " + board[5] + " | " + board[6] + "\n" +
        "-----------\n" +
        " " + board[1] + " | " + board[2] + " | " + board[3] + "\n"
    )

display_board(board)


def marker_input():
    marker = " "
    
    while not (marker == "X" or marker == "O"): ## Same as: while marker != "X" and marker != "O":
        marker = input("Player 1, select a marker (X or O): ").upper()
        
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return(
    board[7] == board[8] == board[9] == mark or
    board[4] == board[5] == board[6] == mark or
    board[1] == board[2] == board[3] == mark or
        
    board[1] == board[4] == board[7] == mark or
    board[2] == board[5] == board[8] == mark or
    board[3] == board[6] == board[9] == mark or
    
    board[1] == board[5] == board[9] == mark or
    board[3] == board[5] == board[7] == mark
    )


import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
        return board[position] == " "


def full_board_check(board):
    for n in range(1,10):
        if space_check(board, n):
            return False
    return True


full_board_check(board)


def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Choose your next position: "))
        
    return position

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")

