'''This file deals with all paddle functionalities'''
import random
from colorama import Fore, Back, Style
from screen import screen


class paddle(screen):

    # constructor

    def __init__(self):
        self.__startX = 78
        self.__startY = 38
        self.__x = self.__startX
        self.__y = self.__startY
        self.PADDLE_COLOR = Fore.BLACK
        self.PADDLE_BG_COLOR = Back.BLACK
        # invoking parent class constructor
        screen.__init__(self)

    # function for displaying the paddle

    def setPaddle(self):
        self.gamingFrame()
        self.updateFrameText(self.__startY, self.__startX, "##########")
        # self.printFrame()

    # function for controlling the paddle

    def controlPaddle(self, inp, res):

        if (res):
            self.__y = self.__startY
            self.__x = self.__startX

        if (inp == "a" and self.__x > 3):
            self.__x -= 1
            self.frame[self.__y][self.__x+10] = " "
            self.updateFrameText(self.__y, self.__x, "##########")
            return True

        elif (inp == "d" and self.__x + 10 < self.SCREEN_WIDTH - 3):
            self.__x += 1
            self.frame[self.__y][self.__x-1] = " "
            self.updateFrameText(self.__y, self.__x, "##########")
            return True

        else:
            return False

    def removePaddle(self):
        for i in range(0, 10):
            self.frame[self.__y][self.__x + i] = " "

    def getPaddle(self):
        return self.__x

    def getDiff(self):
        return self.__startX - self.__x
