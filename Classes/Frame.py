
class Frame():

    def __init__(self, firstRoll, secondRoll = None):
        """ Runs a check if roll are a type of int
            if they are a object is assigned and no
            errors are thrown. """

        if isinstance(firstRoll, int): 
            self.firstRoll = firstRoll
        else: 
            raise TypeError('Must be a type of int 1')
        if secondRoll != None and isinstance(secondRoll, int):
            self.secondRoll = secondRoll
        else: 
            raise TypeError('Must be a type of int 2')
    
    def score(self):
        """ Return a list with the all the scores 
            for this frame """

        if self.secondScore is not None:
            totalScore = self.firstRoll + self.secondRoll
        else:
            totalScore = firstRoll
        return [self.firstRoll, self.secondRoll, totalScore] 
