import tkinter as tk
from tkinter import messagebox
from noughtscrosses import *



class GUI():
    def __init__(self):
        
        self.root=tk.Tk()
        self.root.winfo_toplevel().title("Noughts & Crosses")
        self.root.resizable(width=False,height=False)
        self.GUI=tk.Frame(self.root).grid()
        
        self.board=self.createBoard()
        self.moveHistory=tk.Label(self.GUI,height=14,width=20,background='#00ff00',anchor='n')
        self.currentPlayerDisp=tk.Label(self.GUI,height=3,width=20)
        self.moveHistoryString=""
        
        self.board.grid(row=0,column=0,rowspan=2,padx=5)
        self.currentPlayerDisp.grid(row=0,column=1,padx=(0,5))
        self.moveHistory.grid(row=1,column=1,padx=(0,5),pady=(0,5))
        self.displayPlayer('O')
        self.board.bind('<Button-1>',self.onButtonClick)

        npcUser=messagebox.askquestion(title="1P/2P?", message="Against AI?")
        self.game=NoughtsAndCrosses(npcUser)  

        if npcUser=="no":
            self.user1Name=tk.StringVar()
            self.user2Name=tk.StringVar()
            self.users=tk.Toplevel(self.root,height=50,width=200)
            user1NameLbl=tk.Label(self.users,text = "Player 1 Name: ").grid(row=0,column=0)
            user1NameEntry=tk.Entry(self.users,textvariable=self.user1Name).grid(row=0,column=1)
            user2NameLbl=tk.Label(self.users,text = "Player 2 Name: ").grid(row=1,column=0)
            user2NameEntry=tk.Entry(self.users,textvariable=self.user2Name).grid(row=1,column=1)
            submit=tk.Button(self.users,text="Submit",command=self.userNameSubmit).grid(row=2,columnspan=2)

               
        self.root.mainloop()


    def userNameSubmit(self):
        self.game.players[0].setName(self.user1Name.get())
        self.game.players[1].setName(self.user2Name.get())
        self.users.destroy()

    def updateMoveHistory(self):
        self.moveHistoryString+="\n"
        self.moveHistoryString+=("Last Move: {0},{1}").format(self.cursorX//100,self.cursorY//100)
        self.moveHistory.config(text=self.moveHistoryString)
    def displayPlayer(self,currPlayer):
        self.currentPlayerDisp.config(text="Current Player: {0}".format(currPlayer))
    
    def onButtonClick(self,event):
        self.cursorX,self.cursorY=event.x,event.y
        valid=self.game.makeMove(self.cursorX//100,self.cursorY//100)
        if valid==True:
            if self.game.currentPlayer==False:
                
                #self.placeToken('O')
                self.displayPlayer('X')
                self.updateMoveHistory()
            else:
              
                #self.placeToken('X')
                self.displayPlayer('O')
                self.updateMoveHistory()
        self.updateBoard()
        self.game.displayBoard()
        if self.game.checkWin==False and not any(None in i for i in self.game.board):
            self.generateTieBanner()
            self.root.destroy()
        if self.game.checkIfWin():
            self.generateWinBanner()
            self.root.destroy()
    def updateBoard(self):
        for i,row in enumerate(self.game.board):
            for j, token in enumerate(row):
                if token=="O":
                    canvasSymbol=self.board.create_oval(i*100+10,j*100+10,i*100+90,j*100+90,width=5)
                    
                elif token=="X":
                    
                    canvasSymbol=self.board.create_line(i*100+10,j*100+10,i*100+90,j*100+90,width=5)
                    canvasSymbol=self.board.create_line(i*100+10,j*100+90,i*100+90,j*100+10,width=5)
        #Look at the current board state and generate the tokens needed
        
  
    def placeToken(self,token):
        x,y=(self.cursorX//100)*100,(self.cursorY//100)*100
        if token=='O':
            
            canvasSymbol=self.board.create_oval(x+10,y+10,x+90,y+90,width=5)
            
        else:
            canvasSymbol=self.board.create_line(x+10,y+10,x+90,y+90,width=5)
            canvasSymbol=self.board.create_line(x+10,y+90,x+90,y+10,width=5)

    def createBoard(self):
        board=tk.Canvas(self.GUI,height=300,width=300,background='#fff')
        for i in range(0,2):
            vLine=board.create_line(0,(i+1)*100,300,(i+1)*100)
            hLine=board.create_line((i+1)*100,0,(i+1)*100,300)
        
        return board
    def generateTieBanner(self):
        messagebox.showinfo("Game Over!","It's a tie!")

    def generateWinBanner(self):
        if self.game.currentPlayer==False:
            messagebox.showinfo("Game Over!","Winner is {0}".format(self.game.players[0].getName()))
        else:
            messagebox.showinfo("Game Over!","Winner is {0}".format(self.game.players[1].getName()))



app=GUI()
