#https://github.com/shubhamhr07/tictactoe.git

def head():
    print("tic    1|2|3  ")
    print("tac    4|5|6  ")
    print("toe    7|8|9  ")

a=[""," "," "," "," "," "," "," "," "," "]

def game_board():
    print(a[1]+" | "+a[2]+" | "+a[3])
    print("---------")
    print(a[4]+" | "+a[5]+" | "+a[6])
    print("---------")
    print(a[7]+" | "+a[8]+" | "+a[9])

def winner():
    if a[1]==a[2]==a[3]!=" ":
        print(a[1] +"is winner")
        next = False
    elif a[4]==a[5]==a[6]!=" ":
        print(a[4] +"is winner")
        next = False
    elif a[7]==a[8]==a[9]!=" ":
        print(a[7] +"is winner")
        next = False
    elif a[1]==a[4]==a[7]!=" ":
        print(a[1] +"is winner")
        next = False
    elif a[2]==a[5]==a[8]!=" ":
        print(a[2] +"is winner")
        next = False
    elif a[3]==a[6]==a[9]!=" ":
        print(a[3] +"is winner")
        next = False
    elif a[1]==a[5]==a[9]!=" ":
        print(a[1] +"is winner")
        next = False
    elif a[3]==a[5]==a[7]!=" ":
        print(a[7] +"is winner")
        next = False
    else:
        next = True

head()
game_board()
    
x=int(input("Enter the position for '0'\n\t"))
a[x]="0"
    
winner()

head()
game_board()
    
y=int(input("Enter the position for 'x'\n\t"))
a[y]="x"
    
winner()   

print("Game Over")