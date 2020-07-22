import copy
def create():
    ttt = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
    return ttt

scores = {'X':1,'O':-1,'tie':0}

def dboard(ttt):
    print(ttt[0][0]+"|"+ttt[0][1]+"|"+ttt[0][2])
    print(ttt[1][0]+"|"+ttt[1][1]+"|"+ttt[1][2])
    print(ttt[2][0]+"|"+ttt[2][1]+"|"+ttt[2][2])
    return

def p1play(ttt):
    l = list()
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                l.append([i,j])
    
    print(l)
    x = int(input("Choose the index of the location from the above options : "))
    ttt[l[x][0]][l[x][1]] = "X"

def wonyet(ttt):
    for i in range(2):
        j = 0
        if (ttt[i][j]==ttt[i][j+1] and ttt[i][j+1]==ttt[i][j+2]):
            if (ttt[i][j]=="X"): 
                return "X"
            if (ttt[i][j]=="O"):
                return "O"

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
            return "continue" 
    
    return "tie" #tie

def wonfn(ttt):
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

def bestmove(ttt):
    #Ais turn
    bestscore = -20
    x = -1
    y = -1
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
        bestscore = -20
        for i in range(3):
            for j in range(3):
                if (ttt[i][j]=='-'):
                    ttt[i][j] = "O"
                    score = minimax(ttt, False)
                    ttt[i][j] = "-"
                    bestscore = max(score, bestscore)
        return bestscore
    else :
        bestscore = -20
        for i in range(3):
            for j in range(3):
                if (ttt[i][j]=='-'):
                    ttt[i][j] = "X"
                    score = minimax(ttt, True)
                    ttt[i][j] = "-"
                    bestscore = min(score, bestscore)
        return bestscore

won = 0
ttt = create()
while (won!=1 or won!=-1 or won!="tie"):
    p1play(ttt)
    dboard(ttt)
    wonfn(ttt)
    print("\np2's turn\n")
    bestmove(ttt)
    dboard(ttt)
    wonfn(ttt)
    print("\np1's turn\n")
