#https://github.com/shubhamhr07/tictactoe.git
import os

def head():
    print("tic    1|2|3    Enter 0 to exit ")
    print("tac    4|5|6  ")
    print("toe    7|8|9  ")

a=[""," "," "," "," "," "," "," "," "," "]

def game_board():
    print(a[1]+" | "+a[2]+" | "+a[3])
    print("---------")
    print(a[4]+" | "+a[5]+" | "+a[6])
    print("---------")
    print(a[7]+" | "+a[8]+" | "+a[9])

def win_msg():
    game_board()
    print("\t~~~~  "+turn+" WON  ~~~~")
    exit()

def winner():
    if (a[1]==a[2]==a[3]!=" "):
        win_msg()
    elif (a[4]==a[5]==a[6]!=" "):
        win_msg()
    elif (a[7]==a[8]==a[9]!=" "):
        win_msg()
    elif (a[1]==a[4]==a[7]!=" "):
        win_msg()
    elif (a[2]==a[5]==a[8]!=" "):
        win_msg()
    elif (a[3]==a[6]==a[9]!=" "):
        win_msg()
    elif (a[1]==a[5]==a[9]!=" "):
        win_msg()
    elif (a[3]==a[5]==a[7]!=" "):
        win_msg()
    else:
        os.system('clear')
        
def p_input():
    move=int(input("Enter the position for "+turn+" \n\t"))
    if move==0:
        print("\t~~~~~~GAME OVER~~~~~~")
        exit()
    if a[move]==" ":
        a[move]=turn
    else:
        print("Enter the empty position \n\t")
        p_input()
        
turn="0"

for i in range(10):
    head()
    game_board()
    p_input()
    winner()
    if turn == "0":
        turn="X"
    else:
        turn ="0"
    
    if i == 8:
        game_board()
        print("DRAW")
        exit()
