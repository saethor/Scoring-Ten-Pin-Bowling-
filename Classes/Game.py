from Frame import Frame

class Game():
    def __init__(self):
        self.frames = []

    def addFrame(self, frame):
        """Adds a new frame to the game"""
        if not isinstance(frame, Frame):
            raise TypeError('Not a frame!')

        if len(self.frames) == 10:
            raise OverflowError('Game over!')

        self.frames.append(Frame)
        return True

    def getScore(self):
        """Return a total score for this game"""
        frames = []
        for frame in self.frames:
            frames.append(frame.score())     
        return frames 
