from Frame import Frame
from Game import Game

class Player():
    def __init__(self, name):
        self.name = name
        self.Game = Game()

    def turn(self, firstRoll, secondRoll):
        """ 
        Adds a new move to the Game.frames 
        """
        try: 
            frame = Frame(firstRoll, secondRoll)
            self.Game.addFrame(frame)
        except TypeError as e:
            print 'Invalid move ({0})'.format(e)
        return True

    def score(self):
        return self.Game.getScore() 

