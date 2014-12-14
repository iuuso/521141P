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

def create_mine_board(horizontal, vertical):

    mine_board = []

    """

        Create the Mine board according to users
        selections

    """
    for x in range(vertical):
        board_row = []
        for y in range(horizontal):
            board_row.append(" ")
        mine_board.append(board_row)

    #if DEBUG:
    #    print "DEBUG_BOARD:", board

    return mine_board

def inject_mines_to_board(mine_board, amount_Of_Mines):

    i = 0

    while i < amount_Of_Mines:
        j = randrange(len(mine_board))
        k = randrange(len(mine_board[0]))

        # Check whether that spot already contains a mine
        if mine_board[j][k] != "X":
            mine_board[j][k] = "X"
            i = i + 1
            if DEBUG:
                print "DEBUG: MINE PLACED IN (%s,%s)" % (j,k)
            pass
        else:
            continue

    if DEBUG:
        print "DEBUG_MINE_COUNT: ", amount_Of_Mines
        print "DEBUG_MINES IN BOARD: ", mine_board
        check_mine_count(mine_board, amount_Of_Mines)

def numbers_to_mine_board(mine_board):
    for i in range(len(mine_board)):
        for j in range(len(mine_board[0])):
            if check_coordinates(i, j, len(mine_board[0]), len(mine_board)):
                if mine_board[i][j] != "X":
                    print "Täällä ollaan, miinoja laskentelemassa", i,j
                    mine_board[i][j] = calculate_number(mine_board, mine_board[i][j], i, j)
                    continue
                else:
                    if DEBUG:
                        print "Mine at [%i,%i], ohitetaan" % (i,j)
                    pass
            else:
                print "Nyt ollaan liian pitkällä"
                pass

    print mine_board
    return mine_board

def calculate_number(mine_board,cell, x, y):

    height = len(mine_board)
    width = len(mine_board[0])

    cell_x = x
    cell_y = y

    i = 0

    #print cell[0], type(cell[0])
    #cell_x = int(cell[0])
    #cell_y = int(cell[0][0])
    print cell_x, cell_y

    for z in range((cell_y - 1), (cell_y + 2)):
        for c in range((cell_x - 1),(cell_x + 2)):
            if check_coordinates(cell_y, cell_x, width, height):
                #print "Tilanne [%i, %i]: %s" % (z, c, mine_board[c][z])
                if mine_board[c][z] == "X":
                    i += 1
                    continue
                else:
                    pass
            else:
                print "TAas ollaan liian pitkälläS"
                pass
    print "Löydettiin", i
    return i

def check_coordinates(y, x, height, width):

    if (int(x) < 0 or int(y) < 0):
        return False
    elif (int(x) < int(width)) and (int(y) < int(height)):
        return True
    else:
        return False

def check_mine_count(mine_board, amount_Of_Mines):

    counter = sum(x.count('X') for x in mine_board)
    print "DEBUG_MINE COUNT CHECK: ", counter

def print_board(board):

    width = len(board)
    height = len(board[0])

    print "\n"

    # Print the Horizontal (x) numbers
    for i in range(width):
        if i == 0:
            print "      " + str(i + 1) + "",
        else:
            print "   " + str(i + 1) + " ",
    print "\n"

    # Print the Vertical (y)
    for z in range(height):

        if z != (height-1):
            print str(z+1) + "   ",
        else:
            print str(z+1) + "   ",

        for j in range(width):

            if board[j][z] == " ":
                print ' ',
            elif board[j][z] == "X":
                print "X",
            elif board[j][z] == "*":
                print "*",

            if j != (width-1):
                print " | ",

        if i != (height-1):
            print "\n    " + ((6 * "-") * width)
        else:
            print

    if DEBUG:
        print "DEBUG_BOARD WIDTH: ", width
        print "DEBUG_BOARD HEIGHT ", height


def choose_difficulty():

    print "\n --------DIFFICULTY-------------"
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

def create_game_board(vertical, horizontal):

    game_board = []

    """

        Create the Mine board according to users
        selections

    """
    for x in range(vertical):
        board_row = []
        for y in range(horizontal):
            board_row.append(" ")
        game_board.append(board_row)

    #if DEBUG:
    #    print "DEBUG_BOARD:", board

    return game_board

def populate_game_board(game_board):

    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == " ":
                game_board[i][j] = "*"
            else:
                print "Err: Something weird is going on man."

    return game_board

def is_hit(horizontal, vertical, mine_board):

    try:
        if mine_board[horizontal][vertical] == "X":
            return True
        else:
            return False
    except IndexError:
        return False


def main():
    # Main
    if DEBUG:
        x = 8
        y = 8
    else:
        x, y = define_board()

    mine_board = create_mine_board(x, y)
    game_board = create_game_board(x, y)
    game_board = populate_game_board(game_board)
    difficultyLevel = choose_difficulty()
    mine_Count = calculate_number_of_mines(difficultyLevel, mine_board)
    inject_mines_to_board(mine_board, mine_Count)
    numbers_to_mine_board(mine_board)

    loop_Counter = 0

    while True:

        print_board(mine_board)
        input = raw_input("\nEnter coordinates to check for mines (x,v): ")
        horizont = input.split(",")[0]
        vertical = input.split(",")[1]

        try:
            horizont = int(horizont)
            vertical = int(vertical)

            if (horizont > x) or (vertical > y):
                print "Err: The values you inserted are too big."
                continue
            elif (horizont < 0) or (vertical < 0):
                print "Err: You can not insert negative values."
                continue
            else:
                pass

        except ValueError:
            print "\nYour input was not a valid number. Insert numbers, please."
            continue

        if is_hit(horizont, vertical, mine_board):
            # Printtaa mineboard?
            print "Oh dang, you found a mine :("
            print "You survived for %i rounds! " % loop_Counter
            return loop_Counter
        else:
            # Printtaa game board
            print "You didn't hit any mine!"

        loop_Counter += 1

    # End While loop
    print "You survived for %i rounds! " % loop_Counter

if __name__ == "__main__":
    main()
