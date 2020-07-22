import random as ra
def create():
    ttt = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
    return ttt

def dboard(ttt):
    print(ttt[0][0]+"|"+ttt[0][1]+"|"+ttt[0][2])
    print(ttt[1][0]+"|"+ttt[1][1]+"|"+ttt[1][2])
    print(ttt[2][0]+"|"+ttt[2][1]+"|"+ttt[2][2])

def p1play(ttt):
    l = list()
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                l.append([i,j])
    
    print(l)
    x = int(input("Choose the index of the location from the above options : "))
    ttt[l[x][0]][l[x][1]] = "X"

def p2play(ttt):
    l = list()
    for i in range(3):
        for j in range(3):
            if (ttt[i][j]=="-"):
                l.append([i,j])
    
    ch = ra.choice(l)
    ttt[ch[0]][ch[1]] = "O"

def wonyet(ttt):
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
    
win = 0
ttt = create()
while(win!=1):
    p1play(ttt)
    dboard(ttt)
    wonyet(ttt)
    print("\np2's turn\n")
    p2play(ttt)
    dboard(ttt)
    wonyet(ttt)
    print("\np1's turn\n")

