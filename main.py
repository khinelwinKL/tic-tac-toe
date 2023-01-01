import os
import random


def display_board(board):
    os.system("cls")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])


def choose_marker():
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1: Choose your marker X or O: ").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))


def go_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position_choice = 0
    while position_choice not in range(1, 10) or not space_check(board, position_choice):
        position_choice = int(input("Choose a position from 1 to 9: "))
    return position_choice


def replay_game():
    replay = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if replay == "y":
        return True
    else:
        return False


print("Welcome to the TIC TAC TOE game!")

while True:
    the_board = [" "] * 10
    player1_marker, player2_marker = choose_marker()
    turn = go_first()
    print(f"{turn} will go first.")

    play_game = input("Ready to play? Type 'y' or 'n': ").lower()
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            mark_position = player_choice(the_board)
            place_marker(the_board, player1_marker, mark_position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            mark_position = player_choice(the_board)
            place_marker(the_board, player2_marker, mark_position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S A TIE!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay_game():
        break








