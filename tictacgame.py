import random

Board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

Player = "X"
winner = None
gameRunning = True

# printing the game board

def gameBoard(Board):
    print(Board[0] +" | " + Board[1] +" | " + Board[2])
    print("--|---|----")
    print(Board[3] + " | " + Board[4] +" | " + Board[5])
    print("--|---|----")
    print(Board[6] +" | " + Board[7] +" | " + Board[8])

# taking player input     

def playerInput(Board):
    Input = int(input("Enter a number 1-9 :"))
    if(Input >= 1 and Input <= 9 and Board[Input-1] == "-"):
        Board[Input-1] = Player
    else:
        raise "Invalid move"   
    
# situations for win 

def checkrow(Board):
    global winner
    if Board[0] == Board[1] == Board[2] and Board[1] != "-":
        winner = Board[1]
        return True
    elif Board[3] == Board[4] == Board[5] and Board[4] != "-":  
        winner = Board[4]
        return True
    elif Board[6] == Board[7] == Board[8] and Board[7] != "-":  
        winner = Board[7]  
        return True
    
def checkcolumn(Board):
    global winner
    if Board[0] == Board[3] == Board[6] and Board[3] != "-": 
        winner = Board[3]
        return True
    elif Board[1] == Board[4] == Board[7] and Board[7] != "-":   
        winner = Board[4]
        return True
    elif Board[2] == Board[5] == Board[8] and Board[5] != "-":
        winner = Board[5]
        return True
    
def checkdiagonal(Board):
    global winner 
    if Board[0] == Board[4] == Board[8] and Board[4] != "-":   
        winner = Board[4]
        return True
    elif Board[2] == Board[4] == Board[6] and Board[4] != "-": 
        winner = Board[4]
        return True
    
# checking for tie 

def checktie(Board):
    global gameRunning
    if "-" not in Board:
        gameBoard(Board)
        print("Its a tie!")
        gameRunning = False

# switching player 

def switchPlayer():
    global Player
    if Player == "X":
        Player = "0"
    else:
        Player = "X" 

# bringing a computer

def computer(Board):
    while Player == "0":
        position = random.randint(0, 8)
        if Board[position] == "-":
            Board[position] = "0"
            switchPlayer()
            
        
# checking for win       

def checkwin(Board):
    global gameRunning
    if checkrow(Board) or checkcolumn(Board) or checkdiagonal(Board):
        gameBoard(Board)
        print(f"The winner is {winner}")
        gameRunning = False


# final execution 

while gameRunning:
    gameBoard(Board)
    playerInput(Board)
    switchPlayer()
    checkwin(Board)
    checktie(Board)
    computer(Board)
    checkwin(Board)
    checktie(Board)