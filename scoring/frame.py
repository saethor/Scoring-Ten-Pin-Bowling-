class Frame():

    def __init__(self, lastFramePointer):
        """ 
            Runs a check if roll are a type of int
            if they are a object is assigned and no
            errors are thrown. 
        """
        self.lastFramePointer = lastFramePointer
        self.nextFramePointer = None
        self.firstRoll = None
        self.secondRoll = None
        self.thirdRoll = None
            
    def setScore(self, pines):
        """ 
            Sets the score for this frame. 

            Returns True if player is supposed to roll again. False if he is done
        """
        if self.firstRoll == None:
            return self.__firstRoll(pines)
        elif self.secondRoll == None:
            return self.__secondRoll(pines)

        return self.__thirdRoll(pines)

    def getScore(self):
        """
            Calls recoursive to get totalscore for all frames
        """
        if int(self.firstRoll) == 10:
            frameScore = self.getBonusPoints(2)
        elif int(self.firstRoll) + int(self.secondRoll) == 10:
            frameScore = self.getBonusPoints(1)
        else:
            frameScore = int(self.firstRoll) + int(self.secondRoll)

        if self.nextFramePointer == None:
            if self.firstRoll == 10 or self.secondRoll == 10 or int(self.firstRoll) + int(self.secondRoll) == 10:
                frameScore = int(self.firstRoll) + int(self.secondRoll) + int(self.thirdRoll)

        if self.lastFramePointer == None:
            return frameScore 
        
        return frameScore + self.lastFramePointer.getScore()

    def getBonusPoints(self, bonusRolls):
        """
            If player rolls a strike or a pare he gets a bone added to his score for the next frames. Total number of bonus frames are set to the bonusFrames parameter and the method calls it's self recoursive depending on how many times player should get a bonus (2 for strike 1 for spare)
        """
        frameScore = int(self.firstRoll) + int(self.secondRoll)
        if self.nextFramePointer == None or self.nextFramePointer.firstRoll == None:
            return frameScore

        if bonusRolls == 1:
            return frameScore + int(self.nextFramePointer.firstRoll)
        if bonusRolls == 2 and self.nextFramePointer.firstRoll != 10:
            return frameScore + int(self.nextFramePointer.firstRoll) + int(self.nextFramePointer.secondRoll)

        return int(self.nextFramePointer.firstRoll) + self.nextFramePointer.getBonusPoints(1)

    def isComplete(self):
        """
            Checks if the frame is completed and returns true or false
        """
        if self.nextFramePointer == None:
            if self.thirdRoll == None:
                return False
            return True
        if self.secondRoll == None:
            return False
        return True

    def __firstRoll(self, pines):
        """
            Wrapper for the first shot
        """
        if not self.__validate(pines):
            raise ValueError()
        
        self.firstRoll = pines
        if pines == 10:
            self.firstRoll = pines 
            "If last round player should roll three time"
            if self.nextFramePointer == None:
                return True
            self.secondRoll = 0
            return False
        return True

    def __secondRoll(self, pines):
        """
            Wrapper for the second shot
        """
        if self.nextFramePointer == None and self.firstRoll == 10:
            pinesLeft = 10
        else:
            pinesLeft = 10 - int(self.firstRoll)
        if not self.__validate(pines, pinesLeft):
            raise ValueError()

        self.secondRoll = pines
        
        "If last round player should roll three times"
        if self.nextFramePointer == None and int(self.firstRoll) + int(self.secondRoll) >= 10:
            return True

        "Player should not roll again"
        return False

    def __thirdRoll(self, pines):
        """
            Wrapper for the third (bonus) shot
        """
        if self.firstRoll == 10 and self.secondRoll != 10:
            pinesLeft = 10 - int(self.secondRoll)
        pinesLeft = 10

        if not self.__validate(pines, pinesLeft):
            raise ValueError()

        self.thirdRoll = pines
        
        return False

    def __validate(self, pines, pinesLeft = None):
        """
            Validate the roll so its a type of int
            and between 0 and 10
        """

        if not isinstance(pines, int):
            return False
        if pines < 0 or pines > 10:
            return False
        if pinesLeft != None and int(pines) > int(pinesLeft):
            return False
        return True

    def __getScoringLabel(self):
        if self.firstRoll == None and self.secondRoll == None:
            return "[   ]"
        elif self.nextFramePointer == None and self.thirdRoll != None:
            return "[{0}|{1}|{2}|{3}]".format(self.firstRoll, self.secondRoll, self.thirdRoll, self.getScore())
        elif self.nextFramePointer == None and self.secondRoll != None:
            return "[{0}|{1}| |{2}]".format(self.firstRoll, self.secondRoll, self.getScore())
        elif self.nextFramePointer == None and self.firstRoll != None:
            return "[{0}| | |{1}]".format(self.firstRoll, self.getScore())
        elif self.firstRoll == 10:
            return "[  X|{0}]".format(self.getScore())
        elif int(self.firstRoll) + int(self.secondRoll) == 10:
            return "[{0}|{1}|{2}]".format(self.firstRoll, "/", self.getScore())
        elif self.firstRoll == 0 and self.secondRoll != 0:
            return "[-|{0}|{1}]".format(self.secondRoll, self.getScore())
        elif self.firstRoll != 0 and self.secondRoll == 0:
            return "[{0}|-|{1}]".format(self.firstRoll, self.getScore())
        elif self.firstRoll == 0 and self.secondRoll == 0:
            return "[-|-|{0}]".format(self.getScore())
        else: 
            return "[{0}|{1}|{2}]".format(self.firstRoll, self.secondRoll, self.getScore())

    def __str__(self):
        return self.__getScoringLabel()
