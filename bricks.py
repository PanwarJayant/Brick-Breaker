'''This file deals with all bricks functionalities'''

from colorama import Fore, Back, Style
from screen import screen


class bricks(screen):

    def __init__(self):
        self.__x = 30
        self.__y = 10
        # invoking parent class constructor
        screen.__init__(self)

    def setBrick(self):
        self.gamingFrame()
        # self.updateFrameText(self.__y, self.__x, "&&&&&&&&&&")
        col = self.__x
        row = self.__y

        while(col < 138):
            while(row < 25):
                if (row % 2 == 0):
                    self.updateFrameText(row, col, "&&&&&&&&&&")
                    self.updateFrameText(row, col+10, "**********")
                    self.updateFrameText(row, col+20, "$$$$$$$$$$")
                    self.updateFrameText(row, col+30, "^^^^^^^^^^")
                else:
                    self.updateFrameText(row, col, "$$$$$$$$$$")
                    self.updateFrameText(row, col+10, "^^^^^^^^^^")
                    self.updateFrameText(row, col+20, "&&&&&&&&&&")
                    self.updateFrameText(row, col+30, "**********")

                row += 1
            row = self.__y
            col += 40

        col2 = 30
        while(col2 < 150):
            self.updateFrameText(25, col2, "~~~~~~~~~~")
            col2 += 10
        # self.printFrame()
