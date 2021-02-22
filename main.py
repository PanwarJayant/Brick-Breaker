'''This main file will launch the game and handle the gaming session'''

from screen import screen
from bricks import bricks
from paddle import paddle
from ball import ball
from getch import _getChUnix
from alarmException import AlarmException
import signal
import time
from vars import vars


class mainObj(paddle, ball, bricks):
    def __init__(self):
        screen.__init__(self)
        paddle.__init__(self)
        ball.__init__(self)
        bricks.__init__(self)
        self.getchar = _getChUnix()
        self.releaseBall = False
        self.paddleContact = True
        self.restart = False
        self.welc = True
        self.game = True
        self.restartSignal = False

    def alarmHandler(self, signum, frame):
        raise AlarmException

    def inputTo(self, timeout=1):
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = self.getchar()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    def session(self):
        start = time.time()
        while(self.welc):
            if (not self.restart):
                self.welcomeFrame()
            ch1 = self.inputTo(0.04)
            if ch1 == ' ' or self.restart:
                # paddle
                self.setPaddle()
                if (not self.restart):
                    # bricks
                    self.setBrick()
                # ball
                self.setBall()
                self.game = True
                self.restart = False
                while(self.game):
                    inp = self.inputTo(0.14)
                    self.handleKeyboardInput(inp)
                    start_lives = self.LIVES_REMAINING
                    if (self.releaseBall):
                        self.moveBall()
                    self.printFrame()
                    if (self.LIVES_REMAINING == 0):
                        self.game = False
                        self.welc = False
                    elif (self.LIVES_REMAINING != start_lives):
                        # self.frame = []
                        self.removePaddle()
                        self.removeBall()
                        self.game = False
                        self.releaseBall = False
                        self.paddleContact = True
                        self.restart = True
                        self.restartSignal = True
                    end = time.time()
                    self.updateFrameText(
                        3, 92, "TIME: " + str(int(end-start)))

            elif ch1 == 'q':
                break

        self.gameOverFrame()

    def handleKeyboardInput(self, ch):
        if (ch == 'q'):
            self.game = False
            self.welc = False
        elif (ch == 'a' or ch == 'd'):
            mov = self.controlPaddle(ch, self.restartSignal)
            if (mov and self.paddleContact):
                self.controlBall(ch, self.restartSignal)
            if (self.restartSignal):
                self.restartSignal = False
        elif (ch == ' '):
            self.paddleContact = False
            self.releaseBall = True


m = mainObj()
m.session()
