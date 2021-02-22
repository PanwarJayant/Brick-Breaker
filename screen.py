'''This file deals with handling the terminal screen and spawning the objects on screen.'''

import os
from colorama import Fore, Back, Style
from vars import vars
import time


class screen(vars):

    # using constructor to utilize __init__ variables

    def __init__(self):
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = [
            int(x) for x in os.popen("stty size", "r").read().split()]
        self.SCREEN_HEIGHT -= 1
        # self.SCREEN_WIDTH -= 1
        self.__TEXT_COLOR = Fore.WHITE
        self.__BG_COLOR = Back.BLUE
        self.frame = []

    # function for clearing the screen

    def clearScreen(self):
        print(chr(27) + "[2J")
        print("\033[0;0H")

    # function for giving border layout to the grid

    def borderFrame(self):
        for y in range(self.SCREEN_HEIGHT):
            self.temp = []
            for x in range(self.SCREEN_WIDTH):
                if (y == 0 or x == 0 or y == self.SCREEN_HEIGHT-1 or x == self.SCREEN_WIDTH-1 or y == 1 or x == 1 or y == self.SCREEN_HEIGHT-2 or x == self.SCREEN_WIDTH-2 or x == self.SCREEN_WIDTH-3 or x == 2):
                    self.temp.append("@")
                else:
                    self.temp.append(" ")
            self.frame.append(self.temp)
        # self.printFrame()

    # function for defining layout of Welcome frame

    def welcomeFrame(self):
        self.borderFrame()

        self.updateFrameText(17, 72, "WELCOME TO BRICK BREAKER!")
        self.updateFrameText(19, 72, "You get 3 lives to destroy all bricks")
        self.updateFrameText(21, 72, "Press <SPACE> to release the ball")
        self.updateFrameText(23, 72, "Press <A> to move the paddle to left")
        self.updateFrameText(25, 72, "Press <D> to move the paddle to right")
        self.updateFrameText(27, 72, "Press <SPACE> to start the game!")

        self.printFrame()
        self.frame = []

    # function for defining layout of Game Over Frame

    def gameOverFrame(self):
        self.frame = []
        self.borderFrame()

        self.updateFrameText(17, 72, "GAME OVER!")
        self.updateFrameText(19, 72, "Your score was: " + str(self.SCORE))
        self.updateFrameText(21, 72, "See you soon ;)")

        self.printFrame()

    # function for defining layout of Gaming frame

    def gamingFrame(self):
        # self.frame = []
        self.borderFrame()

        for y in range(self.SCREEN_HEIGHT):
            self.tmp = []
            for x in range(self.SCREEN_WIDTH):
                if (y == 5):
                    self.frame[y][x] = "@"

        self.updateFrameText(3, 12, "SCORE: " + str(self.SCORE))
        self.updateFrameText(3, 46, "LIVES REMAINING: " +
                             str(self.LIVES_REMAINING))
        self.updateFrameText(3, 92, "TIME: " + str(self.TIME))

        # self.printFrame()

    # function for updating the text on frame

    def updateFrameText(self, y, x, txt):
        for i in range(0, len(txt)):
            self.frame[y][x+i] = txt[i]

    # function for printing any frame

    def printFrame(self):
        self.clearScreen()

        for y in range(0, self.SCREEN_HEIGHT):
            for x in range(0, self.SCREEN_WIDTH):

                if (self.frame[y][x] == "&"):
                    print(Fore.RED, Back.RED,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "*"):
                    print(Fore.LIGHTBLACK_EX, Back.LIGHTBLACK_EX,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "~"):
                    print(Fore.LIGHTYELLOW_EX, Back.LIGHTYELLOW_EX,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "$"):
                    print(Fore.GREEN, Back.GREEN,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "^"):
                    print(Fore.LIGHTRED_EX, Back.LIGHTRED_EX,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "#"):
                    print(Fore.BLACK, Back.BLACK,
                          self.frame[y][x], sep="", end="")

                elif (self.frame[y][x] == "Q"):
                    print(Fore.WHITE, Back.WHITE,
                          self.frame[y][x], sep="", end="")

                else:
                    print(self.__TEXT_COLOR, self.__BG_COLOR,
                          self.frame[y][x], sep="", end="")

            print()
        # print(Style.RESET_ALL)
