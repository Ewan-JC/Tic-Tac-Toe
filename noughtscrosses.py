import random

class NoughtsAndCrosses():
    def __init__(self,npcUser):
        self.board=self.generateBoard()
        self.againstAI=False
        self.players=self.getPlayers(npcUser)
        self.currentPlayer=True
        self.checkWin=False
        
        
    def generateBoard(self):
        board=[]
        for i in range(0,3):
            boardRow=[]
            for j in range(0,3):
                boardRow.append(None)

            board.append(boardRow)
    
        return board
    def getPlayers(self,NPC):

        if NPC=="yes":
            self.againstAI=True
            player1=User("O")
            player2=AI()
        else:
            player1=User("O")
            player2=User("X")
        return [player1,player2]

    def displayBoard(self):
        print(self.board)

    def checkTile(self,boardLocation):
        if self.board[boardLocation[0]][boardLocation[1]] != None:
            return False
        else:
            return True

    def makeMove(self,rowPos,colPos):   
        if self.checkTile([rowPos,colPos]) == True and self.players[1].getName()!="Computer":
            if self.currentPlayer==True:
                self.board[rowPos][colPos]=self.players[0].getToken()
            else:
                self.board[rowPos][colPos]=self.players[1].getToken()
            self.currentPlayer = not self.currentPlayer
            return True
        else:
            if self.players[1].getName()=="Computer":
                self.board[rowPos][colPos]=self.players[0].getToken()
                compMove=self.players[1].rngMoveChoice(self.board)
                self.board[compMove[0]][compMove[1]]=self.players[1].getToken()
                return True
            else:
        
                return False
            
    def checkIfWin(self):
        if self.board[0][0]==self.board[0][1]==self.board[0][2] !=None or self.board[1][0]==self.board[1][1]==self.board[1][2]!=None or self.board[2][0]==self.board[2][1]==self.board[2][2] !=None:
            return True
        if self.board[0][0]==self.board[1][0]==self.board[2][0] !=None or self.board[0][1]==self.board[1][1]==self.board[2][1] !=None or self.board[0][2]==self.board[1][2]==self.board[2][2] !=None:
            return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2] !=None or self.board[2][0]==self.board[1][1]==self.board[0][2] !=None:
            return True
      
        
        return False
        
class User():
    def __init__(self,tokenValue):
        self.name=self.setName()
        self.token=tokenValue


    def setName(self):
        name=input("please enter a player name")
        return name
    def getName(self):
        return self.name

    def getToken(self):
        return self.token


class AI(User):
    def __init__(self):
        self.name=self.setName()
        super().__init__("X")
        
    def setName(self):
        name="Computer"
        return name
    
    def rngMoveChoice(self,board):
        validBoardPos=[]
        for rowCount, row in enumerate(board):
            for colCount, value in enumerate(row):
                if value==None:
                    validBoardPos.append([rowCount,colCount])
        moveChoice=random.randint(0,len(validBoardPos)-1)
        return validBoardPos[moveChoice]
                






