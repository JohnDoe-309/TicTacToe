import copy
def create(): # this is to create a new emptty board
    ttt = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
    return ttt

scores = {'X':-1,'O':1,'tie':0}

def dboard(ttt): # this function displays the current state of the TTT board
    print(ttt[0][0]+"|"+ttt[0][1]+"|"+ttt[0][2])
    print(ttt[1][0]+"|"+ttt[1][1]+"|"+ttt[1][2])
    print(ttt[2][0]+"|"+ttt[2][1]+"|"+ttt[2][2])
    

def p1play(ttt): # this is the player 1s turn, he chooses from a set of indices available on the board
    l = list()
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                l.append([i,j])
    
    if not l:
        print("Tie")
        exit(1)

    print(l)
    x = int(input("Choose the index of the location from the above options : "))
    ttt[l[x][0]][l[x][1]] = "X"

def wonyet(ttt): # this is to check the winner of the board and allot scores to the winner
    for i in range(2):
        j = 0
        if (ttt[i][j]==ttt[i][j+1] and ttt[i][j+1]==ttt[i][j+2]):
            if (ttt[i][j]=="X"): 
                return "X" # if X wins
            if (ttt[i][j]=="O"):
                return "O" # if O wins

        elif (ttt[j][i]==ttt[j+1][i] and ttt[j+1][i]==ttt[j+2][i]):
            if (ttt[j][i]=="X"): 
                return "X"
            if (ttt[j][i]=="O"):
                return "O"
    i=0   
    if (ttt[i][i]==ttt[i+1][i+1] and ttt[i+1][i+1]==ttt[i+2][i+2]):
        if (ttt[i][i]=="X"): 
            return "X"
        if (ttt[i][i]=="O"):
            return "O"
    
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                return "continue" # if game not over yet
    
    return "tie" # tie

def wonfn(ttt): # this is the final win fn, checks the board to see if any player has won/tied the game
    for i in range(2):
        j = 0
        if (ttt[i][j]==ttt[i][j+1] and ttt[i][j+1]==ttt[i][j+2]):
            if (ttt[i][j]=="X" or ttt[i][j]=="O"):
                print(ttt[i][j]+" Wins")
                exit(1)

        elif (ttt[j][i]==ttt[j+1][i] and ttt[j+1][i]==ttt[j+2][i]):
            if (ttt[j][i]=="X" or ttt[j][i]=="O"):
                print(ttt[j][i]+" Wins")
                exit(1)
    i=0   
    if (ttt[i][i]==ttt[i+1][i+1] and ttt[i+1][i+1]==ttt[i+2][i+2]):
        if (ttt[i][i]=="X" or ttt[i][i]=="O"):
            print(ttt[i][i]+" Wins")
            exit(1)
    
    count = 0
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                continue
            else:
                count+=1
    if (count==9): print("Tie") # prints tie if all the squares of the board are filled


def bestmove(ttt): # to check the best possible move for the AI
    #Ais turn
    bestscore = -2 # any number less than -1
    x = -1 # initialising x to an out of bounds value
    y = -1 # initialising Y to an out of bounds value
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=='-'):
                ttt[i][j] = "O"
                score = minimax(ttt, False)
                ttt[i][j] = "-"
                if (score > bestscore):
                    bestscore = score
                    x = i
                    y = j
    ttt[x][y] = "O"

def minimax(ttt, aiturn):
    if (wonyet(ttt)!="continue"):
        return scores[wonyet(ttt)]

    if (aiturn):
        bestscore = -2 # any number less than -1
        for i in range(3):
            for j in range(3):
                if (ttt[i][j]=='-'):
                    ttt[i][j] = "O"
                    score = minimax(ttt, False) # shifts turn to p1
                    ttt[i][j] = "-"
                    bestscore = max(score, bestscore) # maximising the value of the ai player
        return bestscore
    else :
        bestscore = 2 # any number greater than 1
        for i in range(3):
            for j in range(3):
                if (ttt[i][j]=='-'):
                    ttt[i][j] = "X"
                    score = minimax(ttt, True) # shifts turn to ai
                    ttt[i][j] = "-"
                    bestscore = min(score, bestscore) # minimising the value of the ai player
        return bestscore

won = 0 
ttt = create() # creating board
while (won==0): 
    p1play(ttt)
    dboard(ttt)
    wonfn(ttt)
    print("\np2's turn\n")
    bestmove(ttt)
    dboard(ttt)
    wonfn(ttt)
    print("\np1's turn\n")
