from frame import Frame
from player import Player
import random

class Game():
    def __init__(self, player):
        """ 
           Each game consist of 10 frames and one player. Each fram consist
           of 2 rolls with maximum of ten pines, each pine gives one point
        """

        if isinstance(player, Player):
            self.player = player
        else:
            self.player = "player{}".format(random.simple(range(100, 999),1))
        self.frames = [] 

        lastFrame = None
        nextFrame = None
        for i in range(0, 10):
            frame = Frame(lastFrame)
            if len(self.frames) > 0:
                self.frames[-1].nextFramePointer = frame
            self.frames.append(frame)
            lastFrame = frame

    def roll(self, pines):
        """
            Find the next frame that is not completed and set the score on that one.
        """
        frame = None 

        for f in self.frames:
            if not f.isComplete():
               frame = f 
               break

        return frame.setScore(pines)

    def __str__(self):
        string = ""
        for frame in self.frames:
            string += " {} ".format(str(frame))
        return string 
