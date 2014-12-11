#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Minesweeper.
Written by Juuso Karlström in 2014

'''

from random import randrange

"""

    Set True for debugging mode, False on normal use

"""

DEBUG = True

"""

    Difficulty levels and mine
    ratio obtained from:
    http://www.minesweepers.org/playing.asp

"""

BEGINNER = 0.15625
INTERMEDIARY = 0.15625
EXPERT = 0.20625

"""

"""

def define_board():

    print " --------SIZE-------------"

    while True:
        try:
            size = raw_input("Insert the size of the Minefield (number x number)\nSize: ")
            x = int(size.split(" x ")[0])
            y = int(size.split(" x ")[1])

            if x <= 0 or y <= 0:
                print "Err: Minefield too small, how about 12 x 12?\n"
                continue

            elif x >= 20 or y >= 20:
                while True:
                    print "\nEhm, that size might be too big and not really playable."
                    choice = raw_input("You sure you wanna use that? (y,n): ")

                    if choice == "y":
                        print "\nOkay, you asked for it. Ye been warned!"
                        raw_input("\nPress ENTER to draw the gameboard...")
                        return (x, y)
                    elif choice == "n":
                        print "\nGood call! Let's try again. Maybe you wanna give 10 x 10 a go?"
                        break
                    else:
                        print "Give your answer in the form 'y' or 'n', please"
                        continue

            else:
                # Values good to go
                return (x, y)

        except ValueError:
            print "Err: The size you inserted is not in the required format, for example 12 x 12\n"
            continue

def create_board(horizontal, vertical):

    board = []

    """

        Create the Gaming board according to users
        selections

    """
    for x in range(vertical):
        board_row = []
        for y in range(horizontal):
            #board_row.append((x, y))
            board.append(board_row)

    if DEBUG:
        print "DEBUG_BOARD:", board

    return board

def inject_mines_to_board(board, amount_Of_Mines):

    i = 0

    while i <= amount_Of_Mines:
        j = randrange(len(board))
        k = randrange(len(board[0]))

        # Check whether that spot already contains a mine
        if board[j][k] == "X":
            continue
        else:
            board[j][k].append("X")
            pass

        i += i + 1

def print_board(board):

    width = len(board)
    height = len(board[0])

    if DEBUG:
        print "DEBUG_BOARD WIDTH: ", width
        print "DEBUG_BOARD HEIGHT ", height

    print "\n"

    # Print the Vertical (x)
    for i in range(height):
        if i == 0:
            print "      " + str(i + 1) + "",
        else:
            print "   " + str(i + 1) + " ",
    print "\n"

    # Print the Horizontal (y)
    for z in range(width):

        if z != (width -1):
            print " " + str(z + 1) + " "
            print "    " + ((6 * "-") * width)
        elif z == (width -1):
            print " " + str(z +1) + " "

        # for k in range(width):
        #     if k == 0:
        #         print sum(board[z][k])
        #     elif k == width:
        #         print sum(board[z][k])
        #     else:
        #         print sum(board[z][k]), " | ",
    # Print the values and cell dividers

def choose_difficulty():

    print " --------DIFFICULTY-------------"
    print " (b) BEGINNER"
    print " (i) INTERMEDIARY"
    print " (e) EXPERT"

    while True:
        choice = raw_input("\nPlease choose difficulty level (b, i, e): ")

        if choice == "b":
            return BEGINNER
        elif choice == "i":
            return INTERMEDIARY
        elif choice == "e":
            return EXPERT
        else:
            print "Err: Invalid value, please follow the instructions."
            continue

def calculate_number_of_mines(difficulty, board_Size):
    return int(difficulty * (len(board_Size) * len(board_Size[0])))

def main():
    # Main
    if DEBUG:
        x = 10
        y = 10
    else:
        x, y = define_board()

    board = create_board(x, y)
    difficultyLevel = choose_difficulty()
    mine_Count = calculate_number_of_mines(difficultyLevel, board)
    print_board(board)
    inject_mines_to_board(board, mine_Count)


if __name__ == "__main__":
    main()
