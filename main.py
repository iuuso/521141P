#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Minesweeper.
Written by Juuso Karlström in 2014

'''

# 1. Select size (freely selectable)
# 2. Select difficulty (easy,medium, difficult)
# 3. Print the layout and coordinates
# 4. Wait till the user

def draw_board(x, y):
    vertical = [x]
    horizontal = [y]
    print horizontal, vertical

    for i in x :
        print "| |"

def define_board():
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
    # Create a gaming board from the user inputted
    # values (x, y)
    board = []
    for x in range(horizontal):
        board.append([" "] * vertical)
    return board

def print_board(board):
    # Add mines later
    width = len(board)
    height = len(board[0])
    columnCount = width + width

    print "\n"

    # Print the Horizontal (y)
    for i in range(width):
        if i == 0:
            print "      " + str(i + 1) + "",
        else:
            print "   " + str(i + 1) + " ",
    print "\n"

    # Print the Vertical (x)
    for z in range(height):
        if z != (height -1):
            print " " + str(z + 1) + " "
            print "    " + ((6 * "-") * width)
        elif z == (height -1):
            print " " + str(z +1) + " "





def main():
    # Main
    x, y = define_board()
    board = create_board(x, y)
    print_board(board)

if __name__ == "__main__":
    main()
