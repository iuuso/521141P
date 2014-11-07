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

            if bool(size_validator(size)) == True:
                break
            else:
                continue

        except IndexError:
            print "Err: The size you inserted is not in the required format, for example 24 x 24\n"

def size_validator(size):
    try:
        x = int(size.split(" x ")[0])
        y = int(size.split(" x ")[1])
        print x
        print y
        return x, y
    except ValueError:
        print "Err: The characters you entered are not numbers. Try again."

if __name__ == "__main__":
    define_size()
