import numpy as np
import random as ra
def create():
    ttt = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
    return ttt

def dboard(ttt):
    print(ttt[0]+"|"+ttt[1]+"|"+ttt[2])
    print(ttt[3]+"|"+ttt[4]+"|"+ttt[5])
    print(ttt[6]+"|"+ttt[7]+"|"+ttt[8])
    return

def p1play(ttt):
    l = list()
    for i in range(2):
        for j in range(2):
            if (ttt[i][j]=="-"):
                l.append((i,j))
    
    print(l)
    x = input("Choose the indev of the location from the above options : ")
    ttt[l[x]] = "X"

def p2play(ttt):
    l = list()
    for i in range(2):
        for j in range(2):
            if (ttt[i][j]=="-"):
                l.append((i,j))
    
    ch = random.choice(l)
    ttt[ch] = "O"

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
# while(win!=1):
x1 = int(input("Player1 : Enter a number between 1 and 9 :"))
x2 = int(input("Player2 : Enter a number between 1 and 9 :"))


