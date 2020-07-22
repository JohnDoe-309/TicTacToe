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

def p2play(ttt):
    l = list()
    for i in range(2):
        for j in range(2):
            if (ttt[i][j]=="-"):
                l.append([i,j])
    
    ch = ra.choice(l)
    ttt[ch[0]][ch[1]] = "O"

def wonyet(ttt):
    for i in range(2):
        j = 0
        if (ttt[i][j]==ttt[i][j+1]==ttt[i][j+1]):
            win = 1
            return win

        elif (ttt[j][i]==ttt[j+1][i]==ttt[j+2][i]):
            win = 1
            return win
        
        elif (ttt[i][i]==ttt[i+1][i+1]==ttt[i+2][i+2]):
            win = 1
            return win  

def game(ttt):
    dboard(ttt)
    if (win==1): 
        print("Game Over")
        exit(1)
    if (win==2):
        print("Its a Tie")
        exit(1)

nums1 = list(range(9))
nums2 = list(range(9))
win = 0
ttt = create()
while(win!=1):
    p1play(ttt)
    p2play(ttt)
    game(ttt)
    wonyet(ttt)

