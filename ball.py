'''This file deals with all ball functionalities'''

from colorama import Fore, Back, Style
from screen import screen
import random
from paddle import paddle
import time


class ball(screen):

    # constructor

    def __init__(self):
        self.__startX = random.randrange(78, 87, 1)
        self.__startY = 37
        self.__x = self.__startX
        self.__y = self.__startY
        self.deviation = 0
        self.paddleX = 0
        self.paddleMid = 0
        self.deflection = 0
        # invoking parent class constructor
        screen.__init__(self)

    # function for displaying the ball

    def setBall(self):
        self.gamingFrame()
        self.updateFrameText(self.__startY, self.__startX, "Q")
        p = paddle()
        self.paddleX = p.getPaddle()
        self.paddleMid = self.paddleX + 5
        if (self.__startX < self.paddleMid):
            self.deviation = -1
        else:
            self.deviation = 1

        if (p.getDiff() < 0):
            self.deflection = -(p.getDiff()*self.getDiff())
        else:
            self.deflection = (p.getDiff()*self.getDiff())
        self.rev = False
        # self.printFrame()

    # function for handling ball movement

    def moveBall(self):

        # check if brick is nearby
        if (self.frame[self.__y-1][self.__x + self.deviation] == "$" or self.frame[self.__y+1][self.__x + self.deviation] == "$" or self.frame[self.__y-1][self.__x + self.deviation] == "^" or self.frame[self.__y+1][self.__x + self.deviation] == "^" or self.frame[self.__y-1][self.__x + self.deviation] == "&" or self.frame[self.__y+1][self.__x + self.deviation] == "&" or self.frame[self.__y-1][self.__x + self.deviation] == "*" or self.frame[self.__y+1][self.__x + self.deviation] == "*" or self.frame[self.__y-1][self.__x + self.deviation] == "~" or self.frame[self.__y+1][self.__x + self.deviation] == "~"):
            self.handleCollision()

        # going down after left wall collision
        elif (self.__x == 3 and self.rev and self.__y != 6):
            self.deviation = 1
            self.spawnBallbelow()

        # going up after left wall collision
        elif (self.__x == 3 and not self.rev and self.__y != 6):
            self.deviation = 1
            self.spawnBallabove()

        # going down after right wall collision
        elif (self.__x == self.SCREEN_WIDTH - 4 and self.rev and self.__y != 6):
            self.deviation = -1
            self.spawnBallbelow()

        # going up after right wall collision
        elif (self.__x == self.SCREEN_WIDTH - 4 and not self.rev and self.__y != 6):
            self.deviation = -1
            self.spawnBallabove()

        # collision with top right corner
        elif (self.__x == self.SCREEN_WIDTH - 4 and self.__y == 6):
            self.deviation = -1
            self.spawnBallbelow()

        # collision with top left corner
        elif (self.__x == 3 and self.__y == 6):
            self.deviation = 1
            self.spawnBallbelow()

        # collision with top wall
        elif (self.__y == 6 and (self.__x != 3 or self.__x != self.SCREEN_WIDTH-4)):
            self.rev = True
            self.spawnBallbelow()

        # general down movement
        elif (self.__y < 37 and self.rev):
            self.spawnBallbelow()

        # general up movement
        elif (self.__y > 6 and not self.rev):
            self.spawnBallabove()

        # reflection from paddle
        elif (self.frame[self.__y+1][self.__x+self.deviation] == "#"):
            self.rev = False

        # failing to catch the ball on paddle
        else:
            self.LIVES_REMAINING -= 1

    def controlBall(self, inp, res):

        if (res):
            self.__y = self.__startY
            self.__x = self.__startX

        if (inp == "a" and self.__x > 3 and self.__x < self.SCREEN_WIDTH - 3):
            self.__x -= 1
            self.frame[self.__y][self.__x+1] = " "
            self.updateFrameText(self.__y, self.__x, "Q")

        elif (inp == "d" and self.__x > 3 and self.__x < self.SCREEN_WIDTH - 3):
            self.__x += 1
            self.frame[self.__y][self.__x-1] = " "
            self.updateFrameText(self.__y, self.__x, "Q")

    def removeBall(self):
        self.frame[self.__y][self.__x] = " "

    def spawnBallabove(self):
        self.frame[self.__y][self.__x] = " "
        self.__y -= 1
        self.__x += self.deviation
        self.frame[self.__y][self.__x] = "Q"

    def spawnBallbelow(self):
        self.frame[self.__y][self.__x] = " "
        self.__y += 1
        self.__x += self.deviation
        self.frame[self.__y][self.__x] = "Q"

    def handleCollision(self):

        # collision with bottom of brick
        if(self.frame[self.__y-1][self.__x + self.deviation] == "&"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y-1][i] = "^"
            self.SCORE += 5
            self.rev = True
            self.spawnBallbelow()

        # collision with top of brick
        elif(self.frame[self.__y+1][self.__x + self.deviation] == "&"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y+1][i] = "^"
            self.SCORE += 5
            self.rev = False
            self.spawnBallabove()

        # collision with sides of bricks
        elif(self.frame[self.__y][self.__x + self.deviation] == "&"):
            if (self.deviation == 1):
                beg = self.__x + 1
            else:
                beg = self.__x - 10
            for i in range(beg, beg+10):
                self.frame[self.__y][i] = "^"
            self.SCORE += 5
            self.deviation = -self.deviation
            if (self.rev):
                self.spawnBallbelow()
            else:
                self.spawnBallabove()

        elif(self.frame[self.__y-1][self.__x + self.deviation] == "^"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y-1][i] = "$"
            self.SCORE += 5
            self.rev = True
            self.spawnBallbelow()

        elif(self.frame[self.__y+1][self.__x + self.deviation] == "^"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y+1][i] = "$"
            self.SCORE += 5
            self.rev = False
            self.spawnBallabove()

        elif(self.frame[self.__y][self.__x + self.deviation] == "^"):
            if (self.deviation == 1):
                beg = self.__x + 1
            else:
                beg = self.__x - 10
            for i in range(beg, beg+10):
                self.frame[self.__y][i] = "$"
            self.SCORE += 5
            self.deviation = -self.deviation
            if (self.rev):
                self.spawnBallbelow()
            else:
                self.spawnBallabove()

        elif(self.frame[self.__y-1][self.__x + self.deviation] == "$"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y-1][i] = " "
            self.SCORE += 5
            self.rev = True
            self.spawnBallbelow()

        elif(self.frame[self.__y+1][self.__x + self.deviation] == "$"):
            pos = self.__x + self.deviation
            point = pos % 10
            beg = pos - point
            for i in range(beg, beg+10):
                self.frame[self.__y+1][i] = " "
            self.SCORE += 5
            self.rev = False
            self.spawnBallabove()

        elif(self.frame[self.__y][self.__x + self.deviation] == "$"):
            if (self.deviation == 1):
                beg = self.__x + 1
            else:
                beg = self.__x - 10
            for i in range(beg, beg+10):
                self.frame[self.__y][i] = " "
            self.SCORE += 5
            self.deviation = -self.deviation
            if (self.rev):
                self.spawnBallbelow()
            else:
                self.spawnBallabove()

        # exploding bricks

        elif(self.frame[self.__y-1][self.__x + self.deviation] == "~"):
            for i in range(30, 151):
                self.frame[self.__y-1][i] = " "
                self.frame[self.__y-2][i] = " "
            self.SCORE += 180
            self.rev = True
            self.spawnBallbelow()

        elif(self.frame[self.__y+1][self.__x + self.deviation] == "~"):
            for i in range(30, 151):
                self.frame[self.__y+1][i] = " "
                self.frame[self.__y][i] = " "
            self.SCORE += 180
            self.rev = False
            self.spawnBallabove()

        elif(self.frame[self.__y][self.__x + self.deviation] == "~"):
            for i in range(30, 151):
                self.frame[self.__y][i] = " "
                self.frame[self.__y-1][i] = " "
            self.SCORE += 180
            self.deviation = -self.deviation
            if (self.rev):
                self.spawnBallbelow()
            else:
                self.spawnBallabove()

        elif(self.frame[self.__y-1][self.__x + self.deviation] == "*"):
            self.rev = True
            self.spawnBallbelow()

        elif(self.frame[self.__y+1][self.__x + self.deviation] == "*"):
            self.rev = False
            self.spawnBallabove()

        elif(self.frame[self.__y][self.__x + self.deviation] == "*"):
            self.deviation = -self.deviation
            if (self.rev):
                self.spawnBallbelow()
            else:
                self.spawnBallabove()

        self.updateFrameText(3, 12, "SCORE: " + str(self.SCORE))

    def getDiff(self):
        return self.__startX - self.__x
