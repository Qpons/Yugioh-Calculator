from tkinter import *
from tkinter import messagebox
from random import randrange

root = Tk()
root.title('Yugioh Calculator')
root.geometry('325x350')

topFrame = Frame(root, width=240,height=20)
topFrame.grid(row=0,column=1)

bottomFrame = Frame(root, width=240, height=100)
bottomFrame.grid(row=1,column=1)

prevPlayer1HP = 8000
player1HP = 8000
player1HPVar = IntVar()
player1HPVar.set(player1HP)

prevPlayer2HP = 8000
player2HP = 8000
player2HPVar = IntVar()
player2HPVar.set(player2HP)

dice1Var = IntVar()
dice2Var = IntVar()
dice3Var = IntVar()

coin1Var = StringVar()
coin2Var = StringVar()
coin3Var = StringVar()

player1Name = Entry(topFrame, width=10)
player1Name.grid(row=0,column=0)
player1Name.insert(0, 'Player 1')

Label(topFrame, textvariable=player1HPVar).grid(row=1,column=0)
Button(topFrame, text='Damage', width=6, bg='red', fg='white', command=lambda i=1:playerDamaged(i)).grid(row=2,column=0)
Button(topFrame, text='Heal', width=6, bg='green', fg='white', command=lambda i=1:playerHeal(i)).grid(row=3,column=0)
Button(topFrame, text='Half', width=6,command=lambda i=1:playerHalf(i)).grid(row=2,column=1)
Button(topFrame, text='Undo', width=6,command=lambda i=1:playerUndo(i)).grid(row=3,column=1)

Button(topFrame, text='Restart', command=lambda:restartMatch()).grid(row=0,column=2)
Label(topFrame, text=' ').grid(row=4, column=2)

player2Name = Entry(topFrame, width= 10)
player2Name.grid(row=0,column=4)
player2Name.insert(0, 'Player 2')

Label(topFrame, textvariable=player2HPVar).grid(row=1,column=4)
Button(topFrame, text='Damage', width=6,bg='red', fg='white',command=lambda i=2:playerDamaged(i)).grid(row=2,column=3)
Button(topFrame, text='Heal', bg='green', fg='white',width=6,command=lambda i=2:playerHeal(i)).grid(row=3,column=3)
Button(topFrame, text='Half', width=6,command=lambda i=2:playerHalf(i)).grid(row=2,column=4)
Button(topFrame, text='Undo', width=6,command=lambda i=2:playerUndo(i)).grid(row=3,column=4)

damageVar = IntVar()
damageVar.set(0000)
damageStr = ''

currentDamageEntry = Entry(topFrame, width=15, textvariable=damageVar)
currentDamageEntry.grid(row=5,column=2)

Label(topFrame, text=' ').grid(row=6, column=2)

def restartMatch():
    global player1HP
    global player2HP
    global prevPlayer1HP
    global prevPlayer2HP
    damageVar.set(0000)
    damageStr = ''
    player1HP = 8000
    player2HP = 8000
    player1HPVar.set(player1HP)
    player2HPVar.set(player2HP)

def playerHalf(playernumber):
    global player1HP
    global player2HP
    global prevPlayer1HP
    global prevPlayer2HP
    if playernumber == 1:
        prevPlayer1HP = player1HP
        player1HP //= 2
        player1HPVar.set(player1HP)
    else:
        prevPlayer2HP = player2HP
        player2HP //= 2
        player2HPVar.set(player2HP)

def playerUndo(playernumber):
    global player1HP
    global player2HP
    if playernumber == 1:
        player1HP = prevPlayer1HP
        player1HPVar.set(player1HP)
    else:
        player2HP = prevPlayer2HP
        player2HPVar.set(player2HP)

numpad = [['7','8','9','Delete'],['4','5','6','Clear'],['1','2','3','Dice'],['0', '00', '000','Coin']]

for i,row in enumerate(numpad):
    for j,item in enumerate(row):
        Button(bottomFrame,text=item, width=5, height=2,command=lambda k=item:updateDamage(k)).grid(row=i+1,column=j, padx=2, pady=2)

def updateDamage(newChar):
    global damageStr
    if newChar == 'Dice':
        winDice = Toplevel()
        winDice.wm_title("Dice Roll!")
        winDice.geometry('150x170')
        dice1Var.set(0)
        dice2Var.set(0)
        dice3Var.set(0)
        Label(winDice, text='Dice Amount').grid(row=0, column=0, padx=5)
        Label(winDice, text='Result').grid(row=0, column=1, padx=5)
        Button(winDice, text="Single", width=6, command=lambda i=1:rollDice(i)).grid(row=1, column=0, padx=5, pady=5)
        Label(winDice, textvariable=dice1Var).grid(row=1, column=1)
        Button(winDice, text="Double", width=6, command=lambda i=2:rollDice(i)).grid(row=2, column=0, padx=5, pady=5)
        Label(winDice, textvariable=dice2Var).grid(row=2, column=1)
        Button(winDice, text="Triple", width=6, command=lambda i=3:rollDice(i)).grid(row=3, column=0, padx=5, pady=5)
        Label(winDice, textvariable=dice3Var).grid(row=3, column=1)
        Button(winDice, text='Clear', command=lambda i=0:rollDice(i)).grid(row=4,column=0)
    elif newChar == 'Coin':
        winCoin = Toplevel()
        winCoin.wm_title("Coin Toss!")
        winCoin.geometry('150x170')
        coin1Var.set(' ')
        coin2Var.set(' ')
        coin3Var.set(' ')
        Label(winCoin, text='Coin Amount').grid(row=0, column=0, padx=5)
        Label(winCoin, text='Result').grid(row=0, column=1, padx=5)
        Button(winCoin, text="Single", width=6, command=lambda i=1:flipCoin(i)).grid(row=1, column=0, padx=5, pady=5)
        Label(winCoin, textvariable=coin1Var).grid(row=1, column=1)
        Button(winCoin, text="Double", width=6, command=lambda i=2:flipCoin(i)).grid(row=2, column=0, padx=5, pady=5)
        Label(winCoin, textvariable=coin2Var).grid(row=2, column=1)
        Button(winCoin, text="Triple", width=6, command=lambda i=3:flipCoin(i)).grid(row=3, column=0, padx=5, pady=5)
        Label(winCoin, textvariable=coin3Var).grid(row=3, column=1)
        Button(winCoin, text='Clear', command=lambda i=0:flipCoin(i)).grid(row=4,column=0)
    elif newChar == 'Delete':
        if damageStr == '':
            damageVar.set(0)
        else:
            damageStr = damageStr[:-1]
            damageVar.set(int(damageStr))
    elif newChar == 'Clear':
        damageStr = ''
        damageVar.set(0)
    else:
        damageStr += newChar
        damageVar.set(int(damageStr))

def rollDice(diceAmount):
    if diceAmount == 0:
        dice1Var.set(0)
        dice2Var.set(0)
        dice3Var.set(0)
    else:
        dice1Var.set(randrange(1,7))
        if diceAmount >= 2:
            dice2Var.set(randrange(1,7))
            if diceAmount >= 3:
                dice3Var.set(randrange(1,7))

def flipCoin(coinAmount):
    if coinAmount == 0:
        coin1Var.set(' ')
        coin2Var.set(' ')
        coin3Var.set(' ')
    else:
        coin = randrange(1,3)
        if coin == 1:
            coin1Var.set('Heads')
        else:
            coin1Var.set('Tails')
        if coinAmount >= 2:
            coin = randrange(1,3)
            if coin == 1:
                coin2Var.set('Heads')
            else:
                coin2Var.set('Tails')
            if coinAmount >= 3:
                coin = randrange(1,3)
                if coin == 1:
                    coin3Var.set('Heads')
                else:
                    coin3Var.set('Tails')
            
def playerDamaged(playernumber):
    global player1HP
    global player2HP
    global prevPlayer1HP
    global prevPlayer2HP
    if playernumber == 1:
        prevPlayer1HP = player1HP
        player1HP -= damageVar.get()
        player1HPVar.set(player1HP)
    else:
        prevPlayer2HP = player2HP
        player2HP -= damageVar.get()
        player2HPVar.set(player2HP)

def playerHeal(playernumber):
    global player1HP
    global player2HP
    global prevPlayer1HP
    global prevPlayer2HP
    if playernumber == 1:
        prevPlayer1HP = player1HP
        player1HP += damageVar.get()
        player1HPVar.set(player1HP)
    else:
        prevPlayer2HP = player2HP
        player2HP += damageVar.get()
        player2HPVar.set(player2HP)


mainloop()