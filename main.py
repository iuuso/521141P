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

class GameState:
    # Size, coordinates, amount of mines
    def __init__(size):
        self.size = 0

def define_size():

    while True:
        try:
            size = raw_input("Insert the size of the Minefield (number x number)\nSize: ")
            x = int(size.split(" x ")[0])
            y = int(size.split(" x ")[1])

            if x <= 0 or y <= 0:
                print "Err: Minefield too small, how about 24 x 24?\n"
                continue
            else:
                return x, y

        except ValueError:
            print "Err: The size you inserted is not in the required format, for example 24 x 24\n"

def draw_board(x, y):
    vertical = [x]
    horizontal = [y]
    print horizontal, vertical

    for i in x :
        print "| |"


if __name__ == "__main__":
    gameboardSize = define_size()
    draw_board(gameboardSize[0], gameboardSize[1])
