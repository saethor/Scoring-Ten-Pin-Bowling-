from scoring.lane import Lane
from scoring.frame import Frame
from scoring.player import Player
from scoring.game import Game
import os

class main():
    def __init__(self):
        self.__clear()
        self.lane = Lane()
        self.lane.start()
        self.game = self.lane.next()
        first = self.game

        for i in range(1, len(self.lane.games)*20):
            self.__clear()
            player = self.game.player
            print self.lane 
            print "{} turns.".format(player)
            self.game = self.__playerTurn(self.game, raw_input())
            if self.__gameOver(self.game):
                break
        self.__clear()
        print self.lane
        print 'Game Over!'
        raw_input()

    def __clear(self):
        """
            Wrapper that clears the console window
        """
        os.system('cls' if os.name=='nt' else 'clear')

    def __playerTurn(self, game, pines):
        try: 
            if game.roll(int(pines)):
                print 'Roll Again!'
                return self.__playerTurn(game, raw_input())
        except ValueError:
            print 'Try again!'
            return self.__playerTurn(game, raw_input())

        return self.lane.next()

    def __gameOver(self, game):
        for f in game.frames: 
            if not f.isComplete():
                return False
        return True
main()
