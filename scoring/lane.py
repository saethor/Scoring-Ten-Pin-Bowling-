from game import Game
from player import Player

class Lane():
    def __init__(self):
        self.games = []
        self.turn = 0 

    def next(self):
        """
            Returns the next player
        """
        game = self.games[self.turn]

        if len(self.games) > int(int(self.turn) + 1):
            self.turn += 1
        else:
            self.turn = 0

        return game

    def start(self):
        print 'Add player, hit enter twice to stop (Maximum 6 players)'
        while self.__addGame() == True and len(self.games) != 6:
            pass

    def __addGame(self):
        player = raw_input()
        if not player:
            return False
        self.games.append(Game(Player(player)))
        return True

    def __str__(self):
        string = ""

        for game in self.games:
            string += "Player: {0}\n{1}\n".format(str(game.player), str(game))

        return string
