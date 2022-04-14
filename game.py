class Game:
    def __init__(self,id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.Moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def getPlayerMove(self, p):
        return self.Moves[p]

    def player(self,player,move):
        self.Moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def Winner(self):
        p1 = self.Moves[0].upper()[0]
        p2 = self.Moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        else:
            winner = -1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
