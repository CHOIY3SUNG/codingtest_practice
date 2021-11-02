import random

class Player:
    def __init__(self, name, pos=0):
        self.name = name
        self.pos = pos

    def getName(self):
        return self.name
        
    def getPos(self):
        return self.pos

    def move(self):
        self.pos += random.randrange(0, 6)

    def prtPlayer(self):
        print(self.name, " : ", self.pos)

class Board:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def prtBoard(self):
        pPos = self.player.getPos()
        cPos = self.computer.getPos()

        print("{:<10}".format(self.player.getName()), end="")
        for i in range(0, 30):
            if i == pPos:
                print("P", end="")
            else:
                print("●", end="")

        if pPos >= 30:
            print("P")
        else:
            print("Goal!")

        print("{:<10}".format(self.computer.getName()), end="")
        for i in range(0, 30):
            if i == cPos:
                print("C", end="")
            else:
                print("●", end="")

        if cPos >= 30:
            print("C")
        else:
            print("Goal!")

    def evaluate(self):

        if self.player.getPos() >= 30:
            self.prtBoard()
            print(self.player.getName() + "의 승리")
            return False
        elif self.computer.getPos() >= 30:
            self.prtBoard()
            print(self.computer.getName() + "의 승리")
            return False

        return True

input("주사위 게임을 시작합니다. Enter키를 눌러 진행해주세요!")

player = Player("최예성")
computer = Player("컴퓨터")
board = Board(player, computer)

while board.evaluate():
    board.prtBoard()
    input("Enter!!")
    player.move()
    if not board.evaluate():
        break
    board.prtBoard()
    input("컴퓨터가 말을 움직입니다.")
    computer.move()